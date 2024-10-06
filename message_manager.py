class MessageManager:
    def __init__(self):
        self.buffer = []

    def add_message(self, message: str) -> None:
        self.buffer.append(message)

    def show_messages(self) -> None:
        print("\nActual encrypted messages:")
        if not self.buffer:
            print("Empty")
        for index, elem in enumerate(self.buffer, 1):
            print(f"{index}. {elem}")