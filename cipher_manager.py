from cipher import Cipher
from typing import List, Dict


class CipherManager:
    def __init__(self, cipher_map: Dict[str, Cipher]):
        self.cipher_map = cipher_map

    def encrypt(self, message: str, cipher_type: str) -> str:
        if cipher_type not in self.cipher_map:
            raise ValueError(f"Unsupported cipher type: {cipher_type}")

        cipher = self.cipher_map[cipher_type]
        cipher.text = message
        return cipher.encrypt()


    def decrypt(self, message: str, cipher_type: str) -> str:
        if cipher_type not in self.cipher_map:
            raise ValueError(f"Unsupported cipher type: {cipher_type}")

        cipher = self.cipher_map[cipher_type]
        cipher.text = message
        return cipher.decrypt()


