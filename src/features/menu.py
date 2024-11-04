from typing import Optional


class Menu:
    """Class for displaying the menu and handling user inputs for a cipher application."""

    @staticmethod
    def show() -> None:
        """Displays the main menu options to the user."""
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
        """Prompts the user to enter a choice within a specified range.

        Args:
            message (str): The prompt message displayed to the user.
            start (int): The minimum valid integer choice.
            end (int): The maximum valid integer choice.

        Returns:
            Optional[int]: The user's choice if within the specified range, or None if an invalid input is given.
        """
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
        """Prompts the user to select a cipher type (ROT13 or ROT47).

        Returns:
            str: The selected cipher type ('rot_13' or 'rot_47').
        """
        print("1. ROT13")
        print("2. ROT47")
        choice = Menu.get_choice("Choose the cipher type [1-2]: ", start=1, end=2)
        rot_type = None
        if choice == 1:
            rot_type = "rot_13"
        elif choice == 2:
            rot_type = "rot_47"
        else:
            print("Invalid value. Please try again!")
        return rot_type
