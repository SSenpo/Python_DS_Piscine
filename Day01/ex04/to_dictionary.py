# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    to_dictionary.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmago <mmago@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/18 23:12:05 by mmago             #+#    #+#              #
#    Updated: 2022/09/18 23:12:06 by mmago            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/Library/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python

def init_tuple() -> tuple:
	list_of_tuples = [
	('Russia', '25'),
	('France', '132'),
	('Germany', '132'),
	('Spain', '178'),
	('Italy', '162'),
	('Portugal', '17'),
	('Finland', '3'),
	('Hungary', '2'),
	('The Netherlands', '28'),
	('The USA', '610'),
	('The United Kingdom', '95'),
	('China', '83'),
	('Iran', '76'),
	('Turkey', '65'),
	('Belgium', '34'),
	('Canada', '28'),
	('Switzerland', '26'),
	('Brazil', '25'),
	('Austria', '14'),
	('Israel', '12')
	]
	return list_of_tuples

def	main():
	tuple = init_tuple()
	result = dict((y,x) for x, y in tuple)
	for key, value in result.items():
		print ('\'{}\' : \'{}\''.format(key, value))

if __name__ == '__main__':
	main()