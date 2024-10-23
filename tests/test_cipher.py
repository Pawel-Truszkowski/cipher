import pytest
from src.features.cipher import ROT13, ROT47


class TestRot13:
    # TODO parametrize

    @pytest.fixture
    def rot13(self):
        rot13 = ROT13()
        return rot13

    def test_rot_13_create_correct_object(self, rot13):
        assert rot13.rot_type == ROT13
        assert isinstance(rot13, ROT13)
        assert rot13.text == ''
        assert rot13.status == ''

    def test_encrypt_return_correct_encrypted_message(self, rot13):
        rot13.text = 'message'
        expected_encrypted_text = 'zrffntr'
        encrypt_text = rot13.encrypt()
        assert encrypt_text == expected_encrypted_text

    def test_decrypt_return_correct_decrypted_message(self, rot13):

        pass




#
# from unittest.mock import patch
# ######################################
#
#
#
#
#
# def get_choice(message: str, start, end):
#     choice = None
#     try:
#         choice: int = int(input(message))
#         if not start <= choice <= end:
#             raise ValueError
#     except ValueError:
#         print("You didn't choose the right option. Try again.")
#     finally:
#         return choice
#
# def get_rot_method() -> tuple[str, str]:
#     message: str = input("Type the message: ")
#     print("1. ROT13")
#     print("2. ROT47")
#     choice = get_choice("Choose the method [1-2]: ", start=1, end=2)
#     if choice == 1:
#         choice = 'rot_13'
#     elif choice == 2:
#         choice = 'rot_47'
#     else:
#         print('invalid value. Please try again!')
#     return message, choice
# def func():
#     print('Hi')
#
# def test_should_print_message():
#     with patch('builtins.print') as mock_print:
#         func()
#         mock_print.assert_called_once_with('Hi')
#
# def test_get_choice_return_correct_number_when_is_in_range():
#     with patch('builtins.input', return_value=1):
#         assert get_choice('Daj mi proszę liczbę') == 1
#
# def test_get_choice_return_correct_number_when_is_not_in_range():
#     with patch('builtins.input', return_value=7):
#         with patch('builtins.print') as mock_print:
#             get_choice('Hi daj mi liczbe.')
#             mock_print.assert_called_once_with("You didn't choose the right option. Try again.")
#
# def test_get_rot_return_correct_number_when_is_in_range():
#     with patch('builtins.input', side_effect=['Pies', 1]):
#         assert get_rot_method() == ('Pies', 'rot_13')