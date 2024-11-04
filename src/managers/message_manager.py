from src.features.file_handler import FileHandler, JSONFileHandler


class MessageManager:
    """Manager for handling messages and their storage.

    Attributes:
        file_handler (FileHandler): The file handler used for saving and reading messages.
        json (JSONFileHandler): JSON-specific file handler for saving and reading JSON-formatted messages.
        buffer (dict): In-memory storage of messages and their converted versions.
    """

    def __init__(self, file_handler: FileHandler) -> None:
        """Initializes MessageManager with a specified file handler.

        Args:
            file_handler (FileHandler): A file handler instance for managing file operations.
        """
        self.file_handler = file_handler
        self.json = JSONFileHandler()
        self.buffer = {}

    def add_message(
        self, original_message: str, converted_message: str, rot_type: str
    ) -> None:
        """Adds a message and its converted version to the in-memory buffer.

        Args:
            original_message (str): The original message before conversion.
            converted_message (str): The message after applying the cipher.
            rot_type (str): The type of cipher used (e.g., "rot_13" or "rot_47").
        """
        self.buffer[original_message] = [converted_message, rot_type]

    def show_messages(self) -> None:
        """Displays all messages and their converted versions stored in the buffer."""
        print("\nActual converted messages:")
        if not self.buffer:
            print("Empty")
        else:
            for i, (key, value) in enumerate(self.buffer.items(), start=1):
                print(
                    f"{i}. Message: '{key}', Converted: '{value[0]}', Cipher type: '{value[1]}'"
                )

    def save_message(self) -> None:
        """Saves all messages from the buffer to both text and JSON files.

        If the buffer is empty, displays a message indicating there is nothing to save.
        """
        if not self.buffer:
            print("Nothing to save.")
        else:
            self.file_handler.save(self.buffer)
            self.json.save(self.buffer)

    def read_message(self) -> None:
        """Reads and displays messages from both the text and JSON files."""
        self.file_handler.read()
        self.json.read()
