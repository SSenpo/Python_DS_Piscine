# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ticker_symbols.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmago <mmago@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/18 23:12:08 by mmago             #+#    #+#              #
#    Updated: 2022/09/18 23:12:09 by mmago            ###   ########.fr        #
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

def	search_value(name: str) -> None:
	company, stocks = init_tuple()
	
	for key, value in company.items():
		if name.lower() == value.lower():
			print("{} {}".format(value, stocks.get(company.get(key))))
			return
	print("Unknown company")
	

def	main():
	if (len(sys.argv) == 2):
		search_value(sys.argv[1])

if __name__ == '__main__':
	main()