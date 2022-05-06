from kata_vigenere_cipher_helper import VigenereCipher


def main():
    c = VigenereCipher("password","abcdefghijklmnopqrstuvwxyz")
    print(c.encode('codewars'))


main()