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