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
            print("Message saved to text file.")
        except Exception as e:
            print(f"An error occurred while saving to file: {e}")

    def read_all(self, file_name=None):
        file_name = file_name or self.FILE_NAME
        try:
            with open(file_name, "r") as file:
                lines = file.readlines()
                return lines
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return None

    def read(self, file_name=None):
        lines = self.read_all(file_name=file_name)
        if lines:
            print("Messages from file:")
            for line in lines:
                print(line)
        else:
            print("No messages to display.")


class JSONFileHandler(FileHandler):
    FILE_NAME = "files/messages.json"

    def save(self, data: dict[str, str]):
        try:
            existing_data = self.read_all() or []
            existing_data.append(data)
            with open(self.FILE_NAME, "w+") as outfile:
                json.dump(existing_data, outfile, indent=4)
                print("Message saved to json file.")
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")

    def read(self):
        data = self.read_all()
        if data:
            print("Messages from file:")
            for item in data:
                print(item)

    def read_all(self):
        try:
            with open(self.FILE_NAME, "r") as json_file:
                return json.load(json_file)
        except json.JSONDecodeError:
            print("No messages to display.")
            return []
        except FileNotFoundError:
            print("File not found, returning empty data.")
            return []
