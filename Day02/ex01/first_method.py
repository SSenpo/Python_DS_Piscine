# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    first_class.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmago <mmago@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/19 11:09:13 by mmago             #+#    #+#              #
#    Updated: 2022/09/19 11:28:45 by mmago            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

##!/Library/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python

class Research:
    def file_reader(self) -> str:
        with open('data.csv', 'r', encoding='utf-8') as file:
            return file.read()


def main():
    research = Research()
    print(research.file_reader())


if __name__ == '__main__':
    main()
