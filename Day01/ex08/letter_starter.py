# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    letter_starter.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmago <mmago@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/18 23:11:47 by mmago             #+#    #+#              #
#    Updated: 2022/09/18 23:11:48 by mmago            ###   ########.fr        #
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
		
def get_letter_start(email: str, emails_tsv_data: list) -> str:
	found = False
	for tsv_line in emails_tsv_data[1:]:
		tsv_line = tsv_line.replace('\n', '')
		fields = tsv_line.split('\t')
		print(fields[2])
		if fields[2] == f'"{email}"':
			found = True
			break

	if found == False:
		raise RuntimeError("Email was not found")
		
	return f"Dear {fields[0][1:-1]}, welcome to our team. " + \
			"We are sure that it will be a pleasure to work with you. " + \
			"That's a precondition for the professionals that our company hires."

def main():
	if len(sys.argv) == 2:
		data = get_letter_start(sys.argv[1], read_file('employees.tsv'))
		print(data)

if __name__ == '__main__':
	main()