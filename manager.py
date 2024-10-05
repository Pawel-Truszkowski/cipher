
from menu import Menu
from cipher import ROT13, ROT47
from os import system


class Manager:
    def __init__(self):
        self.rot13 = ROT13()
        self.rot47 = ROT47()
        self.active = True
        self.buffer = []

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
                print("Good bye!")

    def encrypt(self) -> None:
        message, choice = Menu.get_rot_method()
        if choice == 1:
            self.rot13.text = message
            encrypted_message = self.rot13.encrypt()
            self.buffer.append(encrypted_message)
            print(f"Encrypted message is: {encrypted_message}")
        elif choice == 2:
            self.rot47.text = message
            encrypted_message = self.rot47.encrypt()
            self.buffer.append(encrypted_message)
            print(f"Encrypted message is: {encrypted_message}")

    def decrypt(self) -> None:
        message, choice = Menu.get_rot_method()
        if choice == 1:
            self.rot13.text = message
            decrypted_message = self.rot13.decrypt()
            self.buffer.append(decrypted_message)
            print(f"Decrypted message is: {decrypted_message}")
        elif choice == 2:
            self.rot47.text = message
            decrypted_message = self.rot47.encrypt()
            self.buffer.append(decrypted_message)
            print(f"Decrypted message is: {decrypted_message}")

    def save(self):
        pass

    def show_messages(self):
        print("\nActual encrypted messages:")
        if not self.buffer:
            print("Empty")
        for index, elem in enumerate(self.buffer, 1):
            print(index, elem)