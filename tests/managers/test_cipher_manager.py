import pytest
from unittest.mock import Mock
from src.managers.cipher_manager import CipherManager
from src.features.cipher import Cipher


class TestCipherManager:

    @pytest.fixture
    def mock_rot_13_cipher(self):
        mock_cipher = Mock(spec=Cipher)
        mock_cipher.encrypt.return_value = "Encrypted ROT13 message"
        mock_cipher.decrypt.return_value = "Decrypted ROT13 message"
        return mock_cipher

    @pytest.fixture
    def mock_rot_47_cipher(self):
        mock_cipher = Mock(spec=Cipher)
        mock_cipher.encrypt.return_value = "Encrypted ROT47 message"
        mock_cipher.decrypt.return_value = "Decrypted ROT47 message"
        return mock_cipher

    @pytest.fixture
    def mock_cipher_manager(self, mock_rot_13_cipher, mock_rot_47_cipher):
        cipher_map = {'rot_13': mock_rot_13_cipher,
                      'rot_47': mock_rot_47_cipher}
        return CipherManager(cipher_map)

    def test_encrypt_should_return_encrypted_message_when_supported_cipher_type(self, mock_cipher_manager, mock_rot_13_cipher, mock_rot_47_cipher):
        assert mock_cipher_manager.encrypt('message', 'rot_13') == mock_rot_13_cipher.encrypt()
        assert mock_cipher_manager.encrypt('message', 'rot_47') == mock_rot_47_cipher.encrypt()

    def test_encrypt_should_raise_value_error_when_unsupported_cipher_type(self, mock_cipher_manager):
        with pytest.raises(ValueError, match=f"Unsupported cipher type: rot_11"):
            mock_cipher_manager.encrypt("message", 'rot_11')

    def test_decrypt_should_return_decrypted_message_when_supported_cipher_type(self, mock_cipher_manager, mock_rot_13_cipher, mock_rot_47_cipher):
        assert mock_cipher_manager.decrypt('message', 'rot_13') == mock_rot_13_cipher.decrypt()
        assert mock_cipher_manager.decrypt('message', 'rot_47') == mock_rot_47_cipher.decrypt()

    def test_decrypt_should_raise_value_error_when_unsupported_cipher_type(self, mock_cipher_manager):
        with pytest.raises(ValueError, match=f"Unsupported cipher type: rot_11"):
            mock_cipher_manager.decrypt("message", 'rot_11')