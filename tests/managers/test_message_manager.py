from unittest.mock import Mock, patch
import pytest
from src.managers.message_manager import MessageManager
from src.features.file_handler import FileHandler, JSONFileHandler


class TestMessageManager:

    @pytest.fixture
    def mock_file_handler(self):
        return Mock(spec=FileHandler)

    @pytest.fixture
    def mock_json(self):
        return Mock(spec=JSONFileHandler)

    @pytest.fixture
    def message_manager(self, mock_file_handler):
        return MessageManager(file_handler=mock_file_handler)

    def test_add_message_adds_correctly_when_buffer_is_not_empty(self, message_manager):
        message_manager.add_message("hello", "uryyb", "rot_13")
        assert "hello" in message_manager.buffer
        assert message_manager.buffer["hello"] == ["uryyb", "rot_13"]

    def test_show_message_should_print_when_buffer_is_not_empty(self, message_manager):
        message_manager.add_message("hello", "uryyb", "rot_13")
        with patch("builtins.print") as mock_print:
            message_manager.show_messages()
            mock_print.assert_any_call(
                "1. Message: 'hello', Converted: 'uryyb', Cipher type: 'rot_13'"
            )

    def test_show_message_should_print_empty_when_buffer_is_empty(
        self, message_manager
    ):
        with patch("builtins.print") as mock_print:
            message_manager.show_messages()
            mock_print.assert_any_call("\nActual converted messages:")
            mock_print.assert_any_call("Empty")

    def test_save_message_saves_when_buffer_is_not_empty(
        self, message_manager, mock_file_handler, mock_json
    ):
        with patch.object(message_manager, "json", mock_json):
            message_manager.add_message("hello", "uryyb", "rot_13")
            message_manager.save_message()

            mock_file_handler.save.assert_called_once_with(message_manager.buffer)
            mock_json.save.assert_called_once_with(message_manager.buffer)

    def test_save_message_does_not_save_when_buffer_is_empty(self, message_manager):
        with patch("builtins.print") as mock_print:
            message_manager.save_message()
            mock_print.assert_any_call("Nothing to save.")

    def test_read_message(self, message_manager, mock_file_handler, mock_json):
        message_manager.file_handler = mock_file_handler
        message_manager.json = mock_json
        message_manager.read_message()
        mock_file_handler.read.assert_called_once()
        mock_json.read.assert_called_once()
