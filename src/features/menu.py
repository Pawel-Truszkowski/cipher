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
        while True:
            try:
                choice = int(input(message))
                if start <= choice <= end:
                    return choice
                print(f"Please enter a number between {start} and {end}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    @staticmethod
    def get_cipher_type() -> str:
        print("1. ROT13")
        print("2. ROT47")
        choice = Menu.get_choice("Choose the cipher type [1-2]: ", start=1, end=2)
        rot_type = None
        if choice == 1:
            rot_type = 'rot_13'
        elif choice == 2:
            rot_type = 'rot_47'
        else:
            print('invalid value. Please try again!')
        return rot_type
