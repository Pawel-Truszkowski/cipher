import json
from abc import ABC, abstractmethod


class FileHandler(ABC):
    @abstractmethod
    def save(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    def read(self):
        raise NotImplementedError


class TextFileHandler(FileHandler):
    FILE_NAME = "files/messages.txt"

    def save(self, data: dict[str, str], file_name=None) -> None:
        file_name = file_name or self.FILE_NAME
        try:
            with open(file_name, "w+") as file:
                file.write(f"{data}\n")
            print(f"Message saved to {file_name}")
        except Exception as e:
            print(f"An error occurred while saving to file: {e}")

    def read(self, file_name=None):
        file_name = file_name or self.FILE_NAME
        try:
            with open(file_name, "r") as file:
                lines = file.readlines()
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")

        if lines:
            print("Messages from file: \n")
            for line in lines:
                print(line)
        else:
            print("Can't read the file.")


class JSONFileHandler(FileHandler):
    FILE_NAME = "files/messages.json"

    def save(self, data: dict[str, str]):
        try:
            existing_data = self.read_all() or []
            existing_data.append(data)
            with open(self.FILE_NAME, "w") as outfile:
                json.dump(existing_data, outfile, indent=4)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")

    def read(self):
        data = self.read_all()
        if data:
            print("Messages from file:")
            for item in data:
                print(item)
        else:
            print("No messages to display.")

    def read_all(self):
        try:
            with open(self.FILE_NAME, "r") as json_file:
                return json.load(json_file)
        except json.JSONDecodeError as err:
            print(f"Error reading JSON: {err}")
            return []
        except FileNotFoundError:
            print("File not found, returning empty data.")
            return []
