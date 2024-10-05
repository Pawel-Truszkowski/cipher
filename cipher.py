from abc import ABC, abstractmethod
from dataclasses import dataclass
from codecs import encode, decode
from typing import List


@dataclass
class Cipher(ABC):
    text: str = ""
    rot_type: str = None
    status: str = ""

    @abstractmethod
    def encrypt(self):
        pass

    @abstractmethod
    def decrypt(self):
        pass


class ROT13(Cipher):
    def __init__(self):
        super().__init__()
        self.rot_type = 'rot_13'

    def encrypt(self) -> str:
        encrypted_text = encode(self.text, 'rot_13')
        self.status = "encrypted"
        return encrypted_text

    def decrypt(self) -> str:
        decrypted_text = decode(self.text, 'rot_13')
        self.status = "decrypted"
        return decrypted_text


class ROT47(Cipher):
    def __init__(self):
        super().__init__()
        self.rot_type = 'rot_47'

    def encrypt(self) -> str:
        x = []
        for i in range(len(self.text)):
            char = ord(self.text[i])
            if 33 <= char <= 126:
                x.append(chr(33 + ((char + 14) % 94)))
            else:
                x.append(self.text[i])
        self.status = "encrypted"
        return ''.join(x)

    def decrypt(self) -> str:
        self.status = "decrypted"
        return self.encrypt()
