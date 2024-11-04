from src.features.menu import Menu
from .message_manager import MessageManager
from .cipher_manager import CipherManager


class Manager:
    """Main manager class that coordinates menu display, message handling, and encryption/decryption operations.

    Attributes:
        menu (Menu): Instance of the Menu class for displaying options and getting user choices.
        message_manager (MessageManager): Manages message storage and file operations.
        cipher_manager (CipherManager): Manages encryption and decryption with various ciphers.
        active (bool): Indicates whether the application is currently running.
    """

    def __init__(
        self, menu: Menu, message_manager: MessageManager, cipher_manager: CipherManager
    ):
        """Initializes the Manager with menu, message manager, and cipher manager instances.

        Args:
            menu (Menu): Menu instance for handling user interaction.
            message_manager (MessageManager): Instance managing message storage and file operations.
            cipher_manager (CipherManager): Instance managing encryption and decryption processes.
        """
        self.menu = menu
        self.message_manager = message_manager
        self.cipher_manager = cipher_manager
        self.active = True

    def start(self) -> None:
        """Starts the main application loop, showing the menu and executing user commands until termination."""
        while self.active:
            self.menu.show()
            self.execute()

    def execute(self) -> None:
        """Gets the user's choice and executes the corresponding operation."""
        choice = self.menu.get_choice("Choose the option [1-6]: ", 1, 6)
        match choice:
            case 1:
                self._encrypt()
            case 2:
                self._decrypt()
            case 3:
                self._show_messages()
            case 4:
                self._save()
            case 5:
                self._read()
            case 6:
                self.active = False
                print("\nGood bye!")

    def _encrypt(self) -> None:
        """Handles the process of encrypting a message."""
        original_message = self.get_message()
        cipher_type = self.menu.get_cipher_type()
        encrypted_message = self.cipher_manager.encrypt(original_message, cipher_type)
        self.message_manager.add_message(
            original_message, encrypted_message, cipher_type
        )
        print(f"Encrypted message is: {encrypted_message}")

    def _decrypt(self) -> None:
        """Handles the process of decrypting a message."""
        original_message = self.get_message()
        cipher_type = self.menu.get_cipher_type()
        decrypted_message = self.cipher_manager.decrypt(original_message, cipher_type)
        self.message_manager.add_message(
            original_message, decrypted_message, cipher_type
        )
        print(f"Decrypted message is: {decrypted_message}")

    def _show_messages(self) -> None:
        """Displays all messages currently stored in the message manager."""
        self.message_manager.show_messages()

    def _save(self) -> None:
        """Saves all stored messages to a file."""
        self.message_manager.save_message()

    def _read(self) -> None:
        """Reads and displays messages from a file."""
        self.message_manager.read_message()

    @staticmethod
    def get_message() -> str:
        """Prompts the user to enter a message.

        Returns:
            str: The message entered by the user.
        """
        message: str = input("Type the message: ")
        return message
