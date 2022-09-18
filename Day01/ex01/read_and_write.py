# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    read_and_write.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmago <mmago@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/18 23:12:13 by mmago             #+#    #+#              #
#    Updated: 2022/09/18 23:12:15 by mmago            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/Library/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python

def	read_file(file_name: str) -> list:
	with open(file_name, 'r', encoding='utf-8') as file:
		str = file.readlines()
	return str

def	write_file(file_name: str, write_str: list) -> None:
	with open(file_name, 'w', encoding="utf-8") as file:
		file.writelines(write_str)

def	format_string(o_file: list, item: str) -> list:
	item = item.replace('\",', '\"\t')
	item = item.replace('false,', 'false\t')
	item = item.replace('true,', 'true\t')
	o_file.append(item)
	return o_file


def	main():
	input_fiel = read_file("ds.csv")
	output_file = []

	for item in input_fiel:
		output_file = format_string(output_file, item)
	write_file("ds.tsv", output_file)



if __name__ == '__main__':
	main()