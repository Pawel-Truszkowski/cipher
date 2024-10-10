from cipher import ROT13, ROT47
from file_handler import TextFileHandler
from cipher_manager import CipherManager
from message_manager import MessageManager
from manager import Manager
from menu import Menu


def main():
    cipher_manager = CipherManager(cipher_map={'rot_13': ROT13(), 'rot_47': ROT47()})
    message_manager = MessageManager(file_handler=TextFileHandler())
    manager = Manager(menu=Menu(), cipher_manager=cipher_manager, message_manager=message_manager)
    manager.start()


if __name__ == '__main__':
    main()