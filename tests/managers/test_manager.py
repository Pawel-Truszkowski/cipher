import pytest
from unittest.mock import Mock, patch
from src.managers.manager import Manager, MessageManager, CipherManager


class TestManager:
    @pytest.fixture
    def mock_menu(self):
        menu = Mock()
        menu.get_choice.return_value = 1
        menu.get_cipher_type.return_value = 'rot_13'
        return menu

    @pytest.fixture
    def mock_message_manager(self):
        message_manager = Mock(spec=MessageManager)
        return message_manager

    @pytest.fixture
    def mock_cipher_manager(self):
        mock_cipher_manager = Mock(spec=CipherManager)
        mock_cipher_manager.encrypt.return_value = 'Encrypted Message'
        mock_cipher_manager.decrypt.return_value = 'Decrypted Message'
        return mock_cipher_manager

    @pytest.fixture
    def manager(self, mock_menu, mock_message_manager, mock_cipher_manager):
        return Manager(mock_menu, mock_message_manager, mock_cipher_manager)

    def test_encrypt_should_print_encrypted_message_when_running_correct(self, manager, mock_message_manager, mock_cipher_manager):
        with patch('builtins.input', return_value='Hello World'):
            with patch('builtins.print') as mock_print:
                manager._encrypt()
                mock_cipher_manager.encrypt.assert_called_once_with('Hello World', 'rot_13')
                mock_message_manager.add_message.assert_called_once_with('Hello World', 'Encrypted Message', 'rot_13')
                mock_print.assert_called_once_with("Encrypted message is: Encrypted Message")

    def test_decrypt_should_print_decrypted_message_when_running_correct(self, manager, mock_message_manager, mock_cipher_manager):
        with patch('builtins.input', return_value='message'):
            with patch('builtins.print') as mock_print:
                manager._decrypt()
                mock_cipher_manager.decrypt.assert_called_once_with('message', 'rot_13')
                mock_message_manager.add_message.assert_called_once_with('message', 'Decrypted Message', 'rot_13')
                mock_print.assert_called_once_with("Decrypted message is: Decrypted Message")

    def test_show_messages(self, manager, mock_message_manager):
        manager._show_messages()
        mock_message_manager.show_messages.assert_called_once()

    def test_save(self, manager, mock_message_manager):
        manager._save()
        mock_message_manager.save_message.assert_called_once()

    def test_read(self, manager, mock_message_manager):
        manager._read()
        mock_message_manager.read_message.assert_called_once()

    def test_execute_calls_correct_method_based_on_choice(self, manager, mocker):
        mock_encrypt = mocker.patch.object(manager, '_encrypt')
        manager.execute()
        mock_encrypt.assert_called_once()

    def test_start_when_flag_active_is_true(self, manager, mock_menu, mocker):
        pass

