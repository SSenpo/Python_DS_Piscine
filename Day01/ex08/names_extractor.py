# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    names_extractor.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmago <mmago@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/18 23:11:51 by mmago             #+#    #+#              #
#    Updated: 2022/09/18 23:11:52 by mmago            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/Library/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python
import sys

def	read_file(file_name: str) -> list:
	with open(file_name, 'r', encoding='utf-8') as file:
		str = file.readlines()
	return str

def	write_file(file_name: str, write_str: list) -> None:
	with open(file_name, 'w', encoding="utf-8") as file:
		file.writelines(write_str)

def extract_sur_name(email: str) -> tuple:
	first_dot_index = email.find('.')
	sobaka_index = email.find('@')

	name = email[:first_dot_index]
	name = str.upper(name[0]) + name[1:]

	surname = email[first_dot_index + 1:sobaka_index]
	surname = str.upper(surname[0]) + surname[1:]

	return (name, surname)

def extract_names_csv(emails: list) -> list:
	result_tsv = ['"Name"\t"Surname"\t"E-mail"\n']

	for email in emails:
		email = email.replace('\n', '')
		extract_data = extract_sur_name(email)
		result_tsv.append(f'"{extract_data[0]}"\t"{extract_data[1]}"\t"{email}"\n')

	return result_tsv


def	main():
	if len(sys.argv) == 2:
		data = extract_names_csv(read_file(sys.argv[1]))
		write_file('employees.tsv', data)

if __name__ == '__main__':
	main()