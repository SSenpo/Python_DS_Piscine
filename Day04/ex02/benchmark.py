import timeit
import sys
from tokenize import Double


class Email_list:
	def __init__(self) -> None:
		self.emails = []
		mycop = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
		for i in range(5):
			self.emails.extend(mycop)
		del mycop

	def	_iteration_loop(self) -> list:
		list_mail = []

		for e in self.emails:
			if "@gmail" in e:
				list_mail.append(e)
		
		return list_mail


	def	_iteration_comprehensions(self) -> list:
		list_mail = [mail for mail in self.emails if "@gmail" in mail]

		return list_mail

	def	_iteration_map(self) -> list:
		list_mail = []
		def search_gmail(_: str):
			if _.find("@gmail") != -1:
				return _
		list_mail = list(map(search_gmail, self.emails))

		return list_mail
	
	def	_iteration_filter(self) -> list:
		list_mail = []
		def search_gmail(_: str):
			if _.find("@gmail") != -1:
				return _
		list_mail = list(filter(search_gmail, self.emails))

		return list_mail


def main(method: str, it_num: str) -> None:
	try:
		it_num = int(it_num)
	except:
		print("Can't parse number of iterations")
		return
	
	IT_NUMBER = it_num
	email_cl = Email_list()

	if (method == "loop"):
		result = timeit.timeit(lambda: email_cl._iteration_loop(), number=IT_NUMBER)
	if (method == "list_comprehension"):
		result = timeit.timeit(lambda: email_cl._iteration_comprehensions(), number=IT_NUMBER)
	if (method == "map"):
		result = timeit.timeit(lambda: email_cl._iteration_map(), number=IT_NUMBER)
	if (method == "filter"):
		result = timeit.timeit(lambda: email_cl._iteration_filter(), number=IT_NUMBER)

	print(f'{result}')

	return

if __name__ == '__main__':
	if len(sys.argv) == 3:
		try:
			main(sys.argv[1], sys.argv[2])
		except RuntimeError as err:
			print('Runtime error:', err.args[0])
	else:
		print('Incorrect input.')