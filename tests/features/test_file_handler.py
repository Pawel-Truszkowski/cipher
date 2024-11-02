import tempfile

import pytest

from src.features.file_handler import TextFileHandler


class TestTextFileHandler:

    # @pytest.fixture
    # def temp_file(self):
    #     return tempfile.TemporaryFile()

    @pytest.fixture
    def file_handler(self):
        handler = TextFileHandler()
        # handler.FILE_NAME = temp_file.name
        return handler

    def test_save_should_save_data_to_file(self, file_handler):
        data = {"original": "Hello", "encrypted": "Uryyb", "cipher": "rot13"}

        with tempfile.NamedTemporaryFile(mode="w+", delete=True) as temp_file:

            file_handler.save(data, file_name=temp_file.name)

            temp_file.seek(0)
            saved_content = temp_file.read().strip()

            # assert eval(saved_content) == data

            from ast import literal_eval

            assert literal_eval(saved_content) == data


class TestJSONFileHandler:
    pass
