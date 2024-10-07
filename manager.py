from menu import Menu
from message_manager import MessageManager
from cipher_manager import CipherManager


class Manager:
    def __init__(self, menu: Menu, message_manager: MessageManager, cipher_manager: CipherManager):
        self.active = True
        self.menu = menu
        self.message_manager = message_manager
        self.cipher_manager = cipher_manager

    def start(self) -> None:
        while self.active:
            self.menu.show()
            self.execute()

    def execute(self) -> None:
        choice = self.menu.get_choice("Choose the option [1-6]: ")
        match choice:
            case 1:
                self.encrypt()
            case 2:
                self.decrypt()
            case 3:
                self.show_messages()
            case 4:
                self.save()
            case 5:
                self.read()
            case 6:
                self.active = False
                print("\nGood bye!")

    def encrypt(self) -> None:
        message, cipher_type = self.menu.get_rot_method()
        encrypted_message = self.cipher_manager.encrypt(message, cipher_type)
        self.message_manager.add_message(encrypted_message)
        print(f"Encrypted message is: {encrypted_message}")

    def decrypt(self) -> None:
        message, cipher_type = Menu.get_rot_method()
        decrypted_message = self.cipher_manager.decrypt(message, cipher_type)
        self.message_manager.add_message(decrypted_message)
        print(f"Decrypted message is: {decrypted_message}")

    def show_messages(self) -> None:
        self.message_manager.show_messages()

    def save(self) -> None:
        self.message_manager.save_message()

    def read(self) -> None:
        self.message_manager.read_message()

