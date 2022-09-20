#!/usr/bin/env python3
#!/Users/mmago/PythonDS/Day03/ex00/mmago

import time
import sys
from bs4 import BeautifulSoup
import requests

class YahooFinanceScrapper:

    def __init__(self, ticker_symbol: str) -> None:
        self.ticker_symbol = ticker_symbol
        self.base_url = 'http://finance.yahoo.com/quote/{}/financials'
        self.page = None

    def set_ticker(self, ticker_symbol: str) -> None:

        self.ticker_symbol = ticker_symbol

    def request_page(self) -> int:

        self.page = requests.get(self.base_url.format(self.ticker_symbol),
                                 headers={'User-Agent': 'Custom'})
        return self.page.status_code

    def get_row(self, row_name: str, update_request=False) -> tuple:
        ## get page and check
        if self.page is None or update_request:
            self.request_page()
        if self.page.status_code != 200:
            raise RuntimeError(f'Request was failed with status code {self.page.status_code})')

        ## parse
        # prepare
        soup = BeautifulSoup(self.page.text, features='html.parser')
        if soup.find('section', attrs={'id': 'lookup-page'}) is not None:
            raise RuntimeError('Such page does not exist')

        # find
        values_row = []
        all_rows = soup.findAll('div', attrs={'data-test': 'fin-row'})
        for row in all_rows:
            if row.find('span', text=row_name, attrs={'class': 'Va(m)'}) is not None:
                all_cols = row.findAll('div', attrs={'data-test': 'fin-col'})
                for col in all_cols:
                    values_row.append(col.text)

        # check result
        if len(values_row) == 0:
            raise RuntimeError(f'Such field ({row_name}) does not exist')

        ## return
        return (row_name, *values_row)



def main(ticker_symbol: str, row_name: str):
    scrapper = YahooFinanceScrapper(ticker_symbol)

    try:
        print(scrapper.get_row(row_name))
    except RuntimeError as err:
        print('Runtime error:', err.args[0])

if __name__ == '__main__':
	if len(sys.argv) == 3:
		main(sys.argv[1], sys.argv[2])
		time.sleep(5)
	else:
		print('Invalid number of arguments')
		sys.exit(1)
