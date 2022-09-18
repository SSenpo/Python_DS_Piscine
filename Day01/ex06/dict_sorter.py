# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    dict_sorter.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmago <mmago@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/18 23:11:58 by mmago             #+#    #+#              #
#    Updated: 2022/09/18 23:11:59 by mmago            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/Library/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python

def init_tuple() -> list:
	list_of_tuples = {
	'Russia': '25',
	'France': '132',
	'Germany': '132',
	'Spain': '178',
	'Italy': '162',
	'Portugal': '17',
	'Finland': '3',
	'Hungary': '2',
	'The Netherlands': '28',
	'The USA': '610',
	'The United Kingdom': '95',
	'China': '83',
	'Iran': '76',
	'Turkey': '65',
	'Belgium': '34',
	'Canada': '28',
	'Switzerland': '26',
	'Brazil': '25',
	'Austria': '14',
	'Israel': '12'
	}
	return list_of_tuples

def sort_dictionary(dictionary: dict) -> dict:
	return dict(sorted(dictionary.items(),
		key=lambda item: (-int(item[1]), item[0])))

def	main():
	dict = sort_dictionary(init_tuple())
	for country in dict.keys():
		print(country)

if __name__ == '__main__':
	main()