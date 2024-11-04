import json
from typing import List, Optional
from abc import ABC, abstractmethod


class FileHandler(ABC):
    """Abstract base class for handling file operations."""

    @abstractmethod
    def save(self, data: dict):
        """Abstract method to save data to a file.

        Args:
            data (dict): The data to be saved.
        """
        raise NotImplementedError

    @abstractmethod
    def read(self):
        """Abstract method to read data from a file."""
        raise NotImplementedError


class TextFileHandler(FileHandler):
    """Handles saving and reading of messages to and from a text file."""

    FILE_NAME = "files/messages.txt"

    def save(self, data: dict[str, str], file_name: Optional[str] = None) -> None:
        """Saves data to a text file as a single line.

        Args:
            data (dict[str, str]): The data to be saved.
            file_name (str, optional): Optional custom file name. Defaults to FILE_NAME.
        """
        file_name = file_name or self.FILE_NAME
        try:
            with open(file_name, "w+") as file:
                file.write(f"{data}\n")
            print("Message saved to text file.")
        except Exception as e:
            print(f"An error occurred while saving to file: {e}")

    def read_all(self, file_name: Optional[str] = None) -> list[str]:
        """Reads all lines from the text file.

        Args:
            file_name (str, optional): Optional custom file name. Defaults to FILE_NAME.

        Returns:
            list[str]: List of all lines in the file, or None if an error occurs.
        """
        file_name = file_name or self.FILE_NAME
        try:
            with open(file_name, "r") as file:
                lines = file.readlines()
                return lines
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return None

    def read(self, file_name: Optional[str] = None) -> None:
        """Reads and displays all lines from the text file.

        Args:
            file_name (str, optional): Optional custom file name. Defaults to FILE_NAME.
        """
        lines = self.read_all(file_name=file_name)
        if lines:
            print("Messages from file:")
            for line in lines:
                print(line)
        else:
            print("No messages to display.")


class JSONFileHandler(FileHandler):
    """Handles saving and reading of messages to and from a JSON file."""

    FILE_NAME = "files/messages.json"

    def save(self, data: dict[str, str]):
        """Saves data to a JSON file. Appends new data to an existing list in the JSON file.

        Args:
            data (dict[str, str]): The data to be saved.
        """
        try:
            existing_data = self.read_all() or []
            existing_data.append(data)
            with open(self.FILE_NAME, "w+") as outfile:
                json.dump(existing_data, outfile, indent=4)
                print("Message saved to JSON file.")
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")

    def read(self):
        """Reads and displays all JSON objects from the JSON file."""
        data = self.read_all()
        if data:
            print("Messages from file:")
            for item in data:
                print(item)

    def read_all(self) -> List[dict[str, str]]:
        """Reads all JSON data from the file.

        Returns:
            list[dict[str, str]]: List of messages from the JSON file,
            or an empty list if the file is empty or not found.
        """
        try:
            with open(self.FILE_NAME, "r") as json_file:
                return json.load(json_file)
        except json.JSONDecodeError:
            print("No messages to display.")
            return []
        except FileNotFoundError:
            print("File not found, returning empty data.")
            return []
