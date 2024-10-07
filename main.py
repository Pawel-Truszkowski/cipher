from cipher import Cipher, ROT13, ROT47
from file_handler import FileHandler, TextFileHandler
from cipher_manager import CipherManager
from message_manager import MessageManager
from manager import Manager
from menu import Menu


def main():
    text_file_handler = TextFileHandler()
    rot_13 = ROT13()
    rot_47 = ROT47()

    menu = Menu()
    cipher_manager = CipherManager(ciphers=[rot_13, rot_47])
    message_manager = MessageManager(file_handler=text_file_handler)
    manager = Manager(menu=menu, cipher_manager=cipher_manager, message_manager=message_manager)
    manager.start()


if __name__ == '__main__':
    main()