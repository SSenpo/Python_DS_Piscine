# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    caesar.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmago <mmago@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/18 23:11:37 by mmago             #+#    #+#              #
#    Updated: 2022/09/18 23:11:39 by mmago            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/Library/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python
import sys

def ascii_shift_char(char: str, shift: int) -> str:
    ALPHABET_SIZE=26
    CLETTER_CODE_BEGIN = 65 # A
    CLETTER_CODE_END = 90   # Z
    SLETTER_CODE_BEGIN = 97 # a
    SLETTER_CODE_END = 122  # z
    ASCII_CODE_MIN=0
    ASCII_CODE_MAX=127

    code = ord(char)
    if (code < ASCII_CODE_MIN) or (code > ASCII_CODE_MAX):
        raise ValueError('The script does not support your language yet')

    if CLETTER_CODE_BEGIN <= code <= CLETTER_CODE_END:
        code += shift
        if code < CLETTER_CODE_BEGIN:
            code = CLETTER_CODE_END - (CLETTER_CODE_BEGIN - code - 1) % ALPHABET_SIZE
        elif code > CLETTER_CODE_END:
            code = CLETTER_CODE_BEGIN + (code - CLETTER_CODE_END - 1) % ALPHABET_SIZE
    elif SLETTER_CODE_BEGIN <= code <= SLETTER_CODE_END:
        code += shift 
        if code < SLETTER_CODE_BEGIN:
            code = SLETTER_CODE_END - (SLETTER_CODE_BEGIN - code - 1) % ALPHABET_SIZE
        elif code > SLETTER_CODE_END:
            code = SLETTER_CODE_BEGIN + (code - SLETTER_CODE_END - 1) % ALPHABET_SIZE

    return chr(code)


def caesar_encode(data: str, caesar_shift: int) -> str:
    encoded_string = ''

    for char in data:
        encoded_string += ascii_shift_char(char, caesar_shift)

    return encoded_string


def caesar_decode(data: str, caesar_shift: int) -> str:
    dencoded_string = ''

    for char in data:
        dencoded_string += ascii_shift_char(char, -caesar_shift)

    return dencoded_string


def caesar_cipher(task: str, data: str, caesar_shift=3) -> str:
    if task == 'encode':
        return caesar_encode(data, caesar_shift)
    if task == 'decode':
        return caesar_decode(data, caesar_shift)
    raise ValueError("Unknown task for Caesar cipher")

def main():
    if len(sys.argv) == 4:
        print(caesar_cipher(sys.argv[1], sys.argv[2], int(sys.argv[3])))
    else:
        raise RuntimeError('''Invalid number of agruments:
        Please provide next parametrs:
        ./caesar.py  <encode/decode>  <string_to_process>  <shift>''')


if __name__ == '__main__':
    main()