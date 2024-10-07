from abc import ABC, abstractmethod


class FileHandler(ABC):
    @abstractmethod
    def save(self):
        raise NotImplementedError

    @abstractmethod
    def read(self):
        raise NotImplementedError


class TextFileHandler(FileHandler):

    FILE_NAME = "messages.txt"

    def save(self, message: str) -> None:
        file_name = "messages.txt"
        try:
            with open(file_name, 'a') as file:
                file.write(f"{message}\n")
            print(f"Messages saved to {file_name}")
        except Exception as e:
            print(f"An error occurred while saving to file: {e}")

    def read(self):
        file_name = "messages.txt"
        try:
            with open(file_name, 'r') as file:
                lines = file.readlines()
        except Exception as e:
            print(f"An error occurred while saving to file: {e}")

        for line in lines:
            print(line)


class JSONFileHandler(FileHandler):
    def save(self):
        pass

    def read(self):
        pass

