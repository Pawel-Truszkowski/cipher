from src.features.cipher import Cipher
from typing import Dict


class CipherManager:
    """Manager for handling encryption and decryption with different cipher types.

    Attributes:
        cipher_map (Dict[str, Cipher]): A dictionary mapping cipher types to their respective cipher instances.
    """

    def __init__(self, cipher_map: Dict[str, Cipher]):
        """Initializes the CipherManager with a mapping of cipher types to cipher instances.

        Args:
            cipher_map (Dict[str, Cipher]): Dictionary where keys are cipher type names (e.g., "rot_13")
                                            and values are instances of Cipher subclasses.
        """
        self.cipher_map = cipher_map

    def encrypt(self, message: str, cipher_type: str) -> str:
        """Encrypts a message using the specified cipher type.

        Args:
            message (str): The message to be encrypted.
            cipher_type (str): The type of cipher to use for encryption (e.g., "rot_13" or "rot_47").

        Returns:
            str: The encrypted message.

        Raises:
            ValueError: If the specified cipher_type is not supported by the manager.
        """
        if cipher_type not in self.cipher_map:
            raise ValueError(f"Unsupported cipher type: {cipher_type}")

        cipher = self.cipher_map[cipher_type]
        cipher.text = message
        return cipher.encrypt()

    def decrypt(self, message: str, cipher_type: str) -> str:
        """Decrypts a message using the specified cipher type.

        Args:
            message (str): The message to be decrypted.
            cipher_type (str): The type of cipher to use for decryption (e.g., "rot_13" or "rot_47").

        Returns:
            str: The decrypted message.

        Raises:
            ValueError: If the specified cipher_type is not supported by the manager.
        """
        if cipher_type not in self.cipher_map:
            raise ValueError(f"Unsupported cipher type: {cipher_type}")

        cipher = self.cipher_map[cipher_type]
        cipher.text = message
        return cipher.decrypt()
