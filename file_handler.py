from abc import ABC, abstractmethod


class FileHandler(ABC):
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def read(self):
        pass


class TextFormatFile(FileHandler):

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


class JSONFormatFile(FileHandler):
    def save(self):
        pass

    def read(self):
        pass

