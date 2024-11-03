import tempfile
from ast import literal_eval
import pytest
import json
from src.features.file_handler import TextFileHandler, JSONFileHandler


class TestTextFileHandler:

    @pytest.fixture
    def file_handler(self):
        return TextFileHandler()

    def test_save_should_save_data_to_file(self, file_handler):
        data = {"original": "Hello", "encrypted": "Uryyb", "cipher": "rot13"}

        with tempfile.NamedTemporaryFile(mode="w+", delete=True) as temp_file:
            file_handler.save(data, file_name=temp_file.name)
            temp_file.seek(0)
            saved_content = temp_file.read().strip()
            assert literal_eval(saved_content) == data

    def test_read_all_should_return_data_from_file_when_file_is_not_empty(
        self, file_handler
    ):
        data = {"original": "Hello", "encrypted": "Uryyb", "cipher": "rot13"}

        with tempfile.NamedTemporaryFile(mode="w+", delete=True) as temp_file:
            file_handler.save(data, file_name=temp_file.name)

            read_content = file_handler.read_all(file_name=temp_file.name)

            saved_data = literal_eval(read_content[0].strip())
            assert saved_data == data

    def test_should_read_all_data_from_file_when_file_is_empty(self, file_handler):
        with tempfile.NamedTemporaryFile(mode="r", delete=True) as temp_file:
            read_content = file_handler.read_all(file_name=temp_file.name)
            assert read_content == []

    def test_read_should_print_all_data_when_file_is_not_empty(
        self, file_handler, mocker
    ):
        data = {"original": "Hello", "encrypted": "Uryyb", "cipher": "rot13"}
        with tempfile.NamedTemporaryFile(mode="w+", delete=True) as temp_file:
            file_handler.save(data, file_name=temp_file.name)
            mock_print = mocker.patch("builtins.print")
            file_handler.read(file_name=temp_file.name)
            mock_print.assert_any_call("Messages from file:")
            mock_print.assert_any_call(
                "{'original': 'Hello', 'encrypted': 'Uryyb', 'cipher': 'rot13'}\n"
            )

    def test_read_should_print_that_file_is_epmpty_when_file_is_epmty(
        self, file_handler, mocker
    ):
        with tempfile.NamedTemporaryFile(mode="w+", delete=True) as temp_file:
            mock_print = mocker.patch("builtins.print")
            file_handler.read(file_name=temp_file.name)
            mock_print.assert_any_call("No messages to display.")


class TestJSONFileHandler:
    @pytest.fixture
    def file_handler(self):
        return JSONFileHandler()

    def test_save_should_save_data_to_json_file(self, file_handler):
        data = {"original": "Hello", "encrypted": "Uryyb", "cipher": "rot13"}

        with tempfile.NamedTemporaryFile(mode="w+", delete=True) as temp_file:
            file_handler.FILE_NAME = temp_file.name
            file_handler.save(data)
            temp_file.seek(0)
            saved_content = json.load(temp_file)
            assert saved_content == [data]

    def test_read_all_should_return_data_when_file_is_not_empty(self, file_handler):
        data1 = {"original": "Hello", "encrypted": "Uryyb", "cipher": "rot13"}
        data2 = {"original": "World", "encrypted": "Jbeyq", "cipher": "rot13"}

        with tempfile.NamedTemporaryFile(mode="w+", delete=True) as temp_file:
            file_handler.FILE_NAME = temp_file.name
            file_handler.save(data1)
            file_handler.save(data2)

            read_content = file_handler.read_all()
            assert read_content == [data1, data2]

    def test_read_all_should_return_empty_list_when_file_is_empty(self, file_handler):
        with tempfile.NamedTemporaryFile(mode="w+", delete=True) as temp_file:
            file_handler.FILE_NAME = temp_file.name
            read_content = file_handler.read_all()
            assert read_content == []

    def test_read_should_print_all_data_when_file_is_not_empty(
        self, file_handler, mocker
    ):
        data1 = {"original": "Hello", "encrypted": "Uryyb", "cipher": "rot13"}
        data2 = {"original": "World", "encrypted": "Jbeyq", "cipher": "rot13"}

        with tempfile.NamedTemporaryFile(mode="w+", delete=True) as temp_file:
            file_handler.FILE_NAME = temp_file.name
            file_handler.save(data1)
            file_handler.save(data2)

            mock_print = mocker.patch("builtins.print")
            file_handler.read()

            mock_print.assert_any_call("Messages from file:")
            mock_print.assert_any_call(data1)
            mock_print.assert_any_call(data2)

    def test_read_should_print_message_when_file_is_empty(self, file_handler, mocker):
        with tempfile.NamedTemporaryFile(mode="w+", delete=True) as temp_file:
            file_handler.FILE_NAME = temp_file.name
            mock_print = mocker.patch("builtins.print")
            file_handler.read()
            mock_print.assert_any_call("No messages to display.")
