from src.features.menu import Menu
from .message_manager import MessageManager
from .cipher_manager import CipherManager


class Manager:
    def __init__(
        self, menu: Menu, message_manager: MessageManager, cipher_manager: CipherManager
    ):
        self.menu = menu
        self.message_manager = message_manager
        self.cipher_manager = cipher_manager
        self.active = True

    def start(self) -> None:
        while self.active:
            self.menu.show()
            self.execute()

    def execute(self) -> None:
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
        original_message = self.get_message()
        cipher_type = self.menu.get_cipher_type()
        encrypted_message = self.cipher_manager.encrypt(original_message, cipher_type)
        self.message_manager.add_message(
            original_message, encrypted_message, cipher_type
        )
        print(f"Encrypted message is: {encrypted_message}")

    def _decrypt(self) -> None:
        original_message = self.get_message()
        cipher_type = self.menu.get_cipher_type()
        decrypted_message = self.cipher_manager.decrypt(original_message, cipher_type)
        self.message_manager.add_message(
            original_message, decrypted_message, cipher_type
        )
        print(f"Decrypted message is: {decrypted_message}")

    def _show_messages(self) -> None:
        self.message_manager.show_messages()

    def _save(self) -> None:
        self.message_manager.save_message()

    def _read(self) -> None:
        self.message_manager.read_message()

    @staticmethod
    def get_message() -> str:
        message: str = input("Type the message: ")
        return message
