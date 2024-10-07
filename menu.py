
class Menu:
    @staticmethod
    def show() -> None:
        print()
        print("   ==== MENU ====   ")
        print("1. Encrypt message")
        print("2. Decrypt message")
        print("3. Show message")
        print("4. Save to the file")
        print("5. Read from file")
        print("6. End the program")

    @staticmethod
    def get_choice(message: str) -> int:
        choice: int = 0
        try:
            choice: int = int(input(message))
        except ValueError:
            print("You didn't choose the right option. Try again.")
        finally:
            return choice

    @staticmethod
    def get_rot_method() -> tuple[str, int]:
        message: str = input("Type the message: ")
        print("1. ROT13")
        print("2. ROT47")
        choice = Menu.get_choice("Choose the method [1-2]: ")
        return message, choice
