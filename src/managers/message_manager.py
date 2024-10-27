from src.features.file_handler import FileHandler, TextFileHandler, JSONFileHandler


class MessageManager:
    def __init__(self, file_handler: FileHandler) -> None:
        self.file_handler = file_handler
        self.json = JSONFileHandler()
        self.buffer = {}

    def add_message(self, original_message: str, converted_message: str, rot_type: str) -> None:
        self.buffer[original_message] = [converted_message, rot_type]

    def show_messages(self) -> None:
        print("\nActual converted messages:")
        if not self.buffer:
            print("Empty")
        else:
            for i, (key, value) in enumerate(self.buffer.items(), start=1):
                print(f"{i}. Message: '{key}', Converted: '{value[0]}', Cipher type: '{value[1]}'")

    def save_message(self) -> None:
        if not self.buffer:
            print("Nothing to save.")
        else:
            self.file_handler.save(self.buffer)
            self.json.save(self.buffer)

    def read_message(self) -> None:
        self.file_handler.read()
        self.json.read()
