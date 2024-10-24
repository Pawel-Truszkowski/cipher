from typing import Optional


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
        print("6. End the program\n")

    @staticmethod
    def get_choice(message: str, start: int, end: int) -> Optional[int]:
        choice: Optional[int] = None
        try:
            choice: int = int(input(message))
            if not start <= choice <= end:
                raise ValueError
        except ValueError:
            print("You didn't choose the right option. Try again.")
        finally:
            return choice

    @staticmethod
    def get_message() -> str:
        message: str = input("Type the message: ")
        return message

    @staticmethod
    def get_rot_method() -> tuple[str, str]:
        message: str = input("Type the message: ")
        print("1. ROT13")
        print("2. ROT47")
        choice = Menu.get_choice("Choose the method [1-2]: ", start=1, end=2)
        if choice == 1:
            choice = 'rot_13'
        elif choice == 2:
            choice = 'rot_47'
        else:
            print('invalid value. Please try again!')
        return message, choice
