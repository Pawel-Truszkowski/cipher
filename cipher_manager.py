from cipher import Cipher
from  typing import List


class CipherManager:
    def __init__(self, ciphers: List[Cipher]):
        self.ciphers = ciphers

    def encrypt(self, message: str, cipher_type: str) -> str:
        for cipher in self.ciphers:
            if cipher_type == cipher.rot_type:
                cipher.text = message
                return cipher.encrypt()

    def decrypt(self, message: str, cipher_type: int) -> str:
        for cipher in self.ciphers:
            if cipher_type == cipher.rot_type:
                cipher.text = message
                return cipher.decrypt()



