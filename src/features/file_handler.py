import json
from abc import ABC, abstractmethod


class FileHandler(ABC):
    @abstractmethod
    def save(self, message: str):
        raise NotImplementedError

    @abstractmethod
    def read(self):
        raise NotImplementedError


class TextFileHandler(FileHandler):
    FILE_NAME = "files/messages.txt"

    def save(self, message: str) -> None:
        try:
            with open(self.FILE_NAME, 'a') as file:
                file.write(f"{message}\n")
            print(f"Messages saved to {self.FILE_NAME}")
        except Exception as e:
            print(f"An error occurred while saving to file: {e}")

    def read(self):
        try:
            with open(self.FILE_NAME, 'r') as file:
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
    def save(self, message: dict[str, str]):
        try:
            with open('json_data', w) as outfile:
                json.dump(message)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise

    def read(self):
        try:
            with open('json_data.json') as json_file:
                data = json.load(json_file)
                print(data)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise
