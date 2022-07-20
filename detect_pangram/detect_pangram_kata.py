import string


def is_pangram(s: str):
    for char_num in range(97, 123):
        if s.lower().count(chr(char_num)) == 0:
            return False
    return True


print (string.ascii_lowercase)