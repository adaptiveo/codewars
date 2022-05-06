class VigenereCipher(object):


    __key = ''
    __alphabet = ''


    def __new__(cls, *args, **kwargs):
        cls.__key = args[0]
        cls.__alphabet = args[1]
        return super().__new__(cls)

    def __init__(self, key, alphabet):
        ...


    @classmethod
    def __generate_key_string(cls, input_string: str):
        return (cls.__key * (len(input_string) // len(cls.__key) + 1))[:len(input_string)]


    @classmethod
    def __generate_shifted_symbol(cls, natural_symbol, base_symbol):
        return cls.__alphabet[(cls.__alphabet.index(natural_symbol) + cls.__alphabet.index(base_symbol)) % len(cls.__alphabet)]


    @classmethod
    def __generate_unshifted_symbol(cls, encoded_symbol, base_symbol):
        return cls.__alphabet[
            abs((cls.__alphabet.index(encoded_symbol) + len(cls.__alphabet) - cls.__alphabet.index(base_symbol))) % len(cls.__alphabet)]


    def encode(self, input_string):
        result = ''
        key_string = self.__generate_key_string(input_string)
        for index in range(len(input_string)):
            if input_string[index] in self.__alphabet:
                result += self.__generate_shifted_symbol(input_string[index], key_string[index])
            else:
                result += input_string[index]
        return result


    def decode(self, encoded_string):
        result = ''
        key_string = self.__generate_key_string(encoded_string)
        for index in range(len(encoded_string)):
            if encoded_string[index] in self.__alphabet:
                result += self.__generate_unshifted_symbol(encoded_string[index], key_string[index])
            else:
                result += encoded_string[index]
        return result
