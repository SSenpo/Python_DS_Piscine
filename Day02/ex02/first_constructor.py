
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

    def file_reader(self) -> str:
        if not os.access(self.file_path, os.R_OK):
            raise OSError("Can't read the file")

        with open(self.file_path, 'r', encoding='utf-8') as file:
            file_data = file.read()

        if self.check_correct_csv(file_data) is True:
            return file_data

    def check_correct_csv(self, file_data: str) -> bool:
        line_list = list(file_data.split('\n'))
        header_line = line_list[0].split(self.sep)
        if len(header_line) != self.headers:
            raise ValueError("Incorrectly value's.")

        for string in line_list[1:]:
            string = string.split(self.sep)
            if string not in self.correct_values:
                raise ValueError("Incorrectly data's.")

        return True


def main():
    research = Research(sys.argv[1])
    try:
        print(research.file_reader())
    except Exception as e:
        print(type(e).__name__, e, sep=': ')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main()
    else:
        print('Incorrect input.\nFor example: python3 <scrip_name.py> <filename.csv>')
