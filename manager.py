
from menu import Menu
from cipher import ROT13
from os import system


class Manager:
    def __init__(self):
        self.rot13 = ROT13()
        # self.rot47 = ROT47()
        self.active = True
        self.buffer = []

    def start(self):
        while self.active:
            Menu.show()
            self.execute()

    def execute(self):
        choice = Menu.get_choice()
        match choice:
            case 1:
                self.rot13.text = input("Podaj wiadomość do zaszyfrowania: ")
                self.encrypt()
            case 2:
                self.rot13.text = input("Podaj szyfr: ")
                self.decrypt()
            case 3:
                self.save()
            case 4:
                self.show_messages()
            case 5:
                self.active = False
                print("Zakończenie porgramu")

    def encrypt(self):
        encrypted_message = self.rot13.encrypt()
        self.buffer.append(encrypted_message)
        print(f"Zaszyfrowana wiadomość to: {encrypted_message}")

    def decrypt(self):
        decrypted_message = self.rot13.decrypt()
        self.buffer.append(decrypted_message)
        print(f"Odszyfrowana wiadomość to: {decrypted_message}")

    def save(self):
        pass

    def show_messages(self):
        print("\nActual encrypted messages:")
        for index, elem in enumerate(self.buffer, 1):
            print(index, elem)