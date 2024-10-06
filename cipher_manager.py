from cipher import ROT13, ROT47


class CipherManager:
    def __init__(self):
        self.rot13 = ROT13()
        self.rot47 = ROT47()

    def encrypt(self, message: str, cipher_type: int) -> str:
        if cipher_type == 1:
            self.rot13.text = message
            return self.rot13.encrypt()
        elif cipher_type == 2:
            self.rot47.text = message
            return self.rot47.encrypt()
        else:
            raise ValueError("Invalid cipher type selected.")

    def decrypt(self, message: str, cipher_type: int) -> str:
        if cipher_type == 1:
            self.rot13.text = message
            return self.rot13.decrypt()
        elif cipher_type == 2:
            self.rot47.text = message
            return self.rot47.decrypt()
        else:
            raise ValueError("Invalid cipher type selected.")
