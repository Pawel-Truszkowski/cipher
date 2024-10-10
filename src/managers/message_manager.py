from src.features.file_handler import FileHandler


class MessageManager:
    def __init__(self, file_handler: FileHandler) -> None:
        self.file_handler = file_handler
        self.buffer: list[str] = []

    def add_message(self, message: str) -> None:
        self.buffer.append(message)

    def show_messages(self) -> None:
        print("\nActual encrypted messages:")
        if not self.buffer:
            print("Empty")
        else:
            for index, elem in enumerate(self.buffer, start=1):
                print(f"{index}. {elem}")

    def save_message(self) -> None:
        if not self.buffer:
            print("Nothing to save.")
        else:
            for message in self.buffer:
                self.file_handler.save(message)

    def read_message(self) -> None:
        self.file_handler.read()