from abc import ABC, abstractmethod
from codecs import encode, decode


ROT13 = 'rot_13'
ROT47 = 'rot_47'
ROTS = (ROT13, ROT47)


class Cipher(ABC):
    STATUS__DECRYPTED = 'decrypted'
    STATUS__ENCRYPTED = 'encrypted'

    def __init__(self, text: str = '', status: str = ''):
        self.text = text
        self.status = status
        self._set_rot_type()

    @property
    @abstractmethod
    def rot_type(self):
        raise NotImplementedError

    @abstractmethod
    def _set_rot_type(self):
        raise NotImplementedError

    @abstractmethod
    def encrypt(self):
        raise NotImplementedError

    @abstractmethod
    def decrypt(self):
        raise NotImplementedError


class ROT13(Cipher):
    def __init__(self, text: str = '', status: str = ''):
        super().__init__(text, status)

    @property
    def rot_type(self):
        return self._rot_type

    def _set_rot_type(self):
        self._rot_type = ROT13

    def encrypt(self) -> str:
        encrypted_text = encode(self.text, 'rot_13')
        self.status = "encrypted"
        return encrypted_text

    def decrypt(self) -> str:
        decrypted_text = decode(self.text, 'rot_13')
        self.status = "decrypted"
        return decrypted_text


class ROT47(Cipher):
    def __init__(self, text: str = '', status: str = ''):
        super().__init__(text, status)

    @property
    def rot_type(self):
        return self._rot_type

    def _set_rot_type(self):
        self._rot_type = ROT47

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
