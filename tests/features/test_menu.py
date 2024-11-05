from unittest.mock import patch, call
from src.features.menu import Menu


class TestMenu:
    def test_should_print_menu(self):
        with patch("builtins.print") as mock_print:
            Menu.show()
            expected_calls = [
                call(),
                call("   ==== MENU ====   "),
                call("1. Encrypt message"),
                call("2. Decrypt message"),
                call("3. Show message"),
                call("4. Save to the file"),
                call("5. Read from file"),
                call("6. End the program\n"),
            ]
            mock_print.assert_has_calls(expected_calls)
            assert mock_print.call_count == len(expected_calls)

    def test_get_choice_return_correct_number_when_is_in_range(self):
        with patch("builtins.input", return_value=1):
            choice = Menu.get_choice("Choose an option: ", start=1, end=2)
            assert choice == 1

    def test_get_choice_return_correct_number_when_is_not_in_range(self):
        with patch("builtins.input", side_effect=["7", "3"]), patch(
            "builtins.print"
        ) as mock_print:
            result = Menu.get_choice("Choose an option: ", start=1, end=5)
            mock_print.assert_called_once_with("Please enter a number between 1 and 5.")
            assert result == 3

    def test_get_choice_should_print_invalid_error_when_invalid_data(self):
        with patch("builtins.input", side_effect=["abc", "2"]), patch(
            "builtins.print"
        ) as mock_print:
            result = Menu.get_choice("Choose an option: ", start=1, end=5)
            mock_print.assert_any_call("Invalid input. Please enter a valid number.")
            assert result == 2

    def test_get_cipher_type_when_choice_is_in_range(self, mocker):
        mocker.patch("src.features.menu.Menu.get_choice", side_effect=[1, 2])
        assert Menu.get_cipher_type() == "rot_13"
        assert Menu.get_cipher_type() == "rot_47"

    def test_get_cipher_type_when_choice_is_not_in_range(self, mocker):
        mocker.patch("src.features.menu.Menu.get_choice", return_value=3)
        with patch("builtins.print") as mock_print:
            Menu.get_cipher_type()
            mock_print.assert_any_call("Invalid value. Please try again!")
