# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    all_stocks.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmago <mmago@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/18 23:12:01 by mmago             #+#    #+#              #
#    Updated: 2022/09/18 23:12:02 by mmago            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/Library/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python

import sys

def	init_tuple() -> list:
	COMPANIES = {
	'Apple': 'AAPL',
	'Microsoft': 'MSFT',
	'Netflix': 'NFLX',
	'Tesla': 'TSLA',
	'Nokia': 'NOK'
	}
	STOCKS = {
    'AAPL': 287.73,
	'MSFT': 173.79,
	'NFLX': 416.90,
	'TSLA': 724.88,
	'NOK': 3.37
	}
	return COMPANIES,STOCKS

def delete_whitespaces(string: str) -> str:
	output_result = ''

	for symb in string:
		if not str.isspace(symb):
			output_result += symb
	
	return output_result


def parse_arguments(arg: str, sep=',') -> list:
	arg = delete_whitespaces(arg)
	
	parsed_values = []
	begin_index = 0
	while begin_index < len(arg):
		end_index = arg.find(sep, begin_index)
		if end_index + 1 >= len(arg):
			return []

		if end_index == -1:
			end_index = len(arg)

		if end_index - begin_index < 1:
			return []

		parsed_values.append(arg[begin_index:end_index])
		begin_index = end_index + 1

	return parsed_values

def is_key(value: str, dictionary: dict) -> tuple:
    lower_value = value.lower()

    for company_name in dictionary:
        if lower_value == company_name.lower():
            return (True, company_name)

    return (False, '')


def process_stocks_request(requests: list) -> None:
	companies, stocks = init_tuple()
	
	if len(requests) == 0:
		print()
		return
		
	for value in requests:
		result = is_key(value, companies)
		if result[0]:
			print(f'{ result[1] } stock price is { stocks[companies[result[1]]] }')
			continue
		
		result = is_key(value, stocks)
		if result[0]:
			print(f'{result[1]} is a ticker symbol' +
				f'for { list(companies.keys())[list(companies.values()).index(result[1])] }')
			continue
		
		print(f'{value} is an unknown company or an unknown ticker symbol')
		
	return
	
def main():
	if len(sys.argv) == 2:
		requests = parse_arguments(sys.argv[1])
		process_stocks_request(requests)
		
if __name__ == '__main__':
	main()