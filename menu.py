class Menu:
    @staticmethod
    def show():
        print("==== MENU ====")
        print("1. Szyfruj tekt")
        print("2. Deszyfruj tekst")
        print("3. Pokaż wiadomości")
        print("4. Zakończ program")

    @staticmethod
    def get_choice():
        choice = int(input("Wybierz opcję: "))
        return choice
