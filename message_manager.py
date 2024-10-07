from file_handler import FileHandler


class MessageManager:
    def __init__(self, file_handler: FileHandler):
        self.buffer = []
        self.file_handler = file_handler

    def add_message(self, message: str) -> None:
        self.buffer.append(message)

    def show_messages(self) -> None:
        print("\nActual encrypted messages:")
        if not self.buffer:
            print("Empty")
        for index, elem in enumerate(self.buffer, 1):
            print(f"{index}. {elem}")

    def save_message(self) -> None:
        if self.buffer:
            for message in self.buffer:
                self.file_handler.save(message)
        else:
            print("Nothing to save.")

    def read_message(self) -> None:
        self.file_handler.read()