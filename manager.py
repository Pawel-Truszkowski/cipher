
from menu import Menu
from message_manager import MessageManager
from cipher_manager import CipherManager


class Manager:
    def __init__(self):
        self.active = True
        self.message_manager = MessageManager()
        self.cipher_manager = CipherManager()

    def start(self) -> None:
        while self.active:
            Menu.show()
            self.execute()

    def execute(self) -> None:
        choice = Menu.get_choice("Choose the option [1-5]: ")
        match choice:
            case 1:
                self.encrypt()
            case 2:
                self.decrypt()
            case 3:
                self.save()
            case 4:
                self.show_messages()
            case 5:
                self.active = False
                print("\nGood bye!")

    def encrypt(self) -> None:
        message, cipher_type = Menu.get_rot_method()
        encrypted_message = self.cipher_manager.encrypt(message, cipher_type)
        self.message_manager.add_message(encrypted_message)
        print(f"Encrypted message is: {encrypted_message}")

    def decrypt(self) -> None:
        message, cipher_type = Menu.get_rot_method()
        decrypted_message = self.cipher_manager.decrypt(message, cipher_type)
        self.message_manager.add_message(decrypted_message)
        print(f"Decrypted message is: {decrypted_message}")

    def save(self) -> None:
        self.message_manager.save()

    def show_messages(self) -> None:
        self.message_manager.show_messages()
