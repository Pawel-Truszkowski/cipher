# Cipher Encryption Application

## General Info
This project is a command-line application that allows users to encrypt and decrypt messages using ROT13 and ROT47 ciphers.
The program provides options for saving encrypted/decrypted messages to text or JSON files and reading saved messages from these files.
The application is organized following SOLID principles, with modular classes for managing ciphers, message handling, file operations, and user interactions.

## Technologies & Tools
- **Python 3.12**: The application is written in Python, utilizing its standard library for file handling, JSON serialization, and basic encoding functions.
- **pytest**: Unit testing is done with `pytest` package to ensure reliability of encryption and decryption functionality as well as other functionalities.
- **pre-commit**:
- **Github Actions**:

## Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Pawel-Truszkowski/cipher.git

2. **Run application**:
   ```bash
   python3 src/main.py

## Dev Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Pawel-Truszkowski/cipher.git

2. **Create virtual environment**
   ```bash
   python3 -m venv .venv
   ```

3. **Activate virtual environment**
   ```bash
   source ./venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

5. **Run application**:
   ```bash
   python3 src/main.py
   ```

6. **Run tests (Optional)**
   ```bash
   pytest
   ```
## Application View
<img width="242" alt="Zrzut ekranu 2024-11-5 o 18 04 34" src="https://github.com/user-attachments/assets/38db0147-138c-429b-9c12-18ac85137c80">
