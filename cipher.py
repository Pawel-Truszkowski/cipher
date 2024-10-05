from abc import ABC, abstractmethod
from dataclasses import dataclass
from codecs import encode, decode
from typing import List


@dataclass
class Cipher(ABC):
    text: str = ""
    rot_type: str = None
    status: bool = False

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
        self.status = True
        return encrypted_text

    def decrypt(self) -> str:
        decrypted_text = decode(self.text, 'rot_13')
        self.status = False
        return decrypted_text


class ROT47(Cipher):
    def __init__(self):
        super().__init__()
        self.rot_type = 'rot_47'

    def encrypt(self):
        x = []
        for i in range(len(self.text)):
            j = ord(self.text[i])
            if 33 <= j <= 126:
                x.append(chr(33 + ((j + 14) % 94)))
            else:
                x.append(self.text[i])

        return ''.join(x)

    def decrypt(self):
        return self.encrypt()