
##!/Library/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python

import os
import sys


class Research:
    sep = ','
    headers = 2
    correct_values = [['0', '1'],
                      ['1', '0']]

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def __check_correct_csv(self, file_data: str) -> bool:
        line_list = list(file_data.split('\n'))
        header_line = line_list[0].split(self.sep)
        if len(header_line) != self.headers:
            raise ValueError("Incorrectly value's.")

        for string in line_list[1:]:
            string = string.split(self.sep)
            if string not in self.correct_values:
                raise ValueError("Incorrectly data's.")

        return True

    def __check_first_string(self, first_s: str, has_header: bool) -> bool:
        check_list = [first_s[:-1].split(self.sep)]
        if check_list[0] not in self.correct_values:
            has_header = True
            return has_header
        else:
            has_header = False
            return has_header

    def __convert_to_list(self, file_data: list, has_header: bool) -> list:
        result = []

        for index in range(int(has_header), len(file_data)):
            values = file_data[index].split(self.sep)
            result.append(values)

        return result

    def file_reader(self, has_header=True) -> list:
        if not os.access(self.file_path, os.R_OK):
            raise OSError("Can't read the file")

        with open(self.file_path, 'r', encoding='utf-8') as file:
            first_string = file.readline()
            has_header = self.__check_first_string(first_string, has_header)
            file_data = first_string + file.read()

        if self.__check_correct_csv(file_data):
            data = list(file_data.split('\n'))
            return self.__convert_to_list(data, has_header)

    class Calculations:

        def counts(self, data: list) -> tuple:
            heads = 0
            tails = 0

            for values in data:
                if values[0] == '1':
                    heads += 1
                else:
                    tails += 1

            return heads, tails

        def fractions(self, heads_and_tails: tuple) -> tuple:
            total = sum(heads_and_tails)

            return tuple(value / total * 100 for value in heads_and_tails)


def main():
    research = Research(sys.argv[1])
    try:
        res = research.file_reader()
    except Exception as e:
        print(type(e).__name__, e, sep=': ')
        return

    calc = research.Calculations()
    count = calc.counts(res)
    fraction = calc.fractions(count)

    print(f'{res}\n{count[0]} {count[1]}\n{fraction[0]} {fraction[1]}')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main()
    else:
        print('Incorrect input.\nFor example: python3 <scrip_name.py> <filename.csv>')