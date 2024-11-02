import pytest
from src.features.cipher import ROT13, ROT47


class TestRot13:

    @pytest.fixture
    def rot13(self):
        rot13 = ROT13()
        return rot13

    def test_rot13_create_correct_object(self, rot13):
        assert rot13.rot_type == ROT13
        assert isinstance(rot13, ROT13)
        assert rot13.text == ''
        assert rot13.status == ''

    def test_encrypt_return_correct_encrypted_message(self, rot13):
        rot13.text = 'message'
        expected_encrypted_text = 'zrffntr'
        encrypt_text = rot13.encrypt()
        assert encrypt_text == expected_encrypted_text
        assert rot13.status == 'encrypted'

    def test_decrypt_return_correct_decrypted_message(self, rot13):
        rot13.text = 'zrffntr'
        expected_decrypted_text = 'message'
        decrypt_text = rot13.decrypt()
        assert decrypt_text == expected_decrypted_text
        assert rot13.status == 'decrypted'

    def test_multiple_encrypt_decrypt_calls(self, rot13):
        rot13.text = 'message'
        encrypted = rot13.encrypt()
        decrypted = rot13.decrypt()
        assert encrypted == 'zrffntr'
        assert decrypted == 'message'

    def test_invalid_input_type(self, rot13):
        with pytest.raises(TypeError):
            rot13.text = 123
            rot13.encrypt()


class TestRot47:

    @pytest.fixture
    def rot47(self):
        rot47 = ROT47()
        return rot47

    def test_rot47_create_correct_object(self, rot47):
        assert rot47.rot_type == ROT47
        assert isinstance(rot47, ROT47)
        assert rot47.text == ''
        assert  rot47.status == ''

    def test_encrypt_return_correct_encrypted_message(self, rot47):
        rot47.text = 'message'
        expected_encrypted_text = '>6DD286'
        encrypt_text = rot47.encrypt()
        assert encrypt_text == expected_encrypted_text
        assert rot47.status == 'encrypted'

    def test_decrypt_return_correct_decrypted_message(self, rot47):
        rot47.text = '>6DD286'
        expected_decrypted_text = 'message'
        decrypt_text = rot47.decrypt()
        assert decrypt_text == expected_decrypted_text
        assert rot47.status == 'decrypted'

    def test_multiple_encrypt_decrypt_calls(self, rot47):
        rot47.text = 'message'
        encrypted = rot47.encrypt()
        decrypted = rot47.decrypt()
        assert encrypted == '>6DD286'
        assert decrypted == 'message'

    def test_invalid_input_type(self, rot47):
        with pytest.raises(TypeError):
            rot47.text = 123
            rot47.encrypt()
#
# from unittest.mock import patch
# ######################################
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