
class Menu:
    @staticmethod
    def show():
        print()
        print("   ==== MENU ====   ")
        print("1. Szyfruj wiadomość")
        print("2. Deszyfruj wiadomość")
        print("3. Zapisz wiadomość do pliku")
        print("4. Pokaż wiadomości")
        print("5. Zakończ program")

    @staticmethod
    def get_choice():
        choice = 0
        try:
            choice = int(input("Wybierz opcję [1-5]: "))
        except ValueError:
            print("Nie wybrałeś odpowiedniej opcji. Spróbuj jeszcze raz.")
        finally:
            return choice

