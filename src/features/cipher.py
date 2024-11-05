from abc import ABC, abstractmethod
from codecs import encode, decode


ROT13 = "rot_13"
ROT47 = "rot_47"
ROTS = (ROT13, ROT47)


class Cipher(ABC):
    """
    Abstract base class for ciphers.

    Attributes:
        text (str): The message to be encrypted or decrypted.
        status (str): The current status of the text, either 'decrypted' or 'encrypted'.
    """

    STATUS__DECRYPTED = "decrypted"
    STATUS__ENCRYPTED = "encrypted"

    def __init__(self, text: str = "", status: str = ""):
        """
        Initialize the cipher with the given text and status.

        Args:
            text (str): The message to be encrypted or decrypted. Defaults to an empty string.
            status (str): The status of the text (either 'decrypted' or 'encrypted'). Defaults to an empty string.
        """
        self.text: str = text
        self.status: str = status
        self._set_rot_type()

    @property
    @abstractmethod
    def rot_type(self):
        """Abstract method to get the rotation type of the cipher (e.g., 'rot_13' or 'rot_47')."""
        raise NotImplementedError

    @abstractmethod
    def _set_rot_type(self):
        """Abstract method to set the rotation type. Must be implemented in subclasses."""
        raise NotImplementedError

    @abstractmethod
    def encrypt(self):
        """Encrypts the text attribute and updates the status to 'encrypted'.

        Returns:
            str: The encrypted text.
        """
        raise NotImplementedError

    @abstractmethod
    def decrypt(self):
        """Decrypts the text attribute and updates the status to 'decrypted'.

        Returns:
            str: The decrypted text.
        """
        raise NotImplementedError


class ROT13(Cipher):
    """Class for handling ROT13 encryption and decryption.

    ROT13 shifts each letter by 13 positions in the alphabet, preserving case.
    """

    def __init__(self, text: str = "", status: str = ""):
        """Initialize the ROT13 cipher with the given text and status.

        Args:
            text (str): The message to be encrypted or decrypted. Defaults to an empty string.
            status (str): The status of the text (either 'decrypted' or 'encrypted'). Defaults to an empty string.
        """
        super().__init__(text, status)

    @property
    def rot_type(self):
        """str: Returns the type of rotation as 'rot_13'."""
        return self._rot_type

    def _set_rot_type(self):
        """Sets the rotation type for the ROT13 cipher."""
        self._rot_type = ROT13

    def encrypt(self) -> str:
        """Encrypts the text using ROT13 and updates the status to 'encrypted'.

        Returns:
            str: The encrypted text.
        """
        self.text = encode(self.text, "rot_13")
        self.status = self.STATUS__ENCRYPTED
        return self.text

    def decrypt(self) -> str:
        """Decrypts the text using ROT13 and updates the status to 'decrypted'.

        Returns:
            str: The decrypted text.
        """
        self.text = decode(self.text, "rot_13")
        self.status = self.STATUS__DECRYPTED
        return self.text


class ROT47(Cipher):
    """Class for handling ROT47 encryption and decryption.

    ROT47 shifts characters in the ASCII range (33 to 126) by 47 positions.
    """

    def __init__(self, text: str = "", status: str = ""):
        """Initialize the ROT47 cipher with the given text and status.

        Args:
            text (str): The message to be encrypted or decrypted. Defaults to an empty string.
            status (str): The status of the text (either 'decrypted' or 'encrypted'). Defaults to an empty string.
        """
        super().__init__(text, status)

    @property
    def rot_type(self):
        """str: Returns the type of rotation as 'rot_47'."""
        return self._rot_type

    def _set_rot_type(self):
        """Sets the rotation type for the ROT47 cipher."""
        self._rot_type = ROT47

    def encrypt(self) -> str:
        """Encrypts the text using ROT47 and updates the status to 'encrypted'.

        Returns:
            str: The encrypted text.
        """
        x = []
        for i in range(len(self.text)):
            char = ord(self.text[i])
            if 33 <= char <= 126:
                x.append(chr(33 + ((char + 14) % 94)))
            else:
                x.append(self.text[i])
        self.status = self.STATUS__ENCRYPTED
        self.text = "".join(x)
        return self.text

    def decrypt(self) -> str:
        """Decrypts the text using ROT47 (same operation as encryption) and updates the status to 'decrypted'.

        Returns:
            str: The decrypted text.
        """
        self.text = self.encrypt()
        self.status = self.STATUS__DECRYPTED
        return self.text
