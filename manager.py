
from menu import Menu
from cipher import ROT13


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
                self.decrypt()
            case 3:
                self.save()
            case 4:
                self.show_messages()
            case 5:
                self.active = False
                print("Zakończenie porgramu")
            case _:
                print("Nie wybrałeś odpowiedniej opcji.")

    def encrypt(self):
        result = self.rot13.encrypt()
        self.buffer.append(result)

    def decrypt(self):
        pass

    def save(self):
        pass

    def show_messages(self):
        for message in self.buffer:
            print(message)
