import timeit


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


def main():
	IT_NUMBER = 90000000
	email_cl = Email_list()

	result = timeit.timeit(lambda: email_cl._iteration_loop(), number=IT_NUMBER)
	result_comp = timeit.timeit(lambda: email_cl._iteration_comprehensions(), number=IT_NUMBER)
	result_map = timeit.timeit(lambda: email_cl._iteration_map(), number=IT_NUMBER)
	all_res = sorted([result, result_comp, result_map])

	if (result_comp < result and result_comp < result_map):
		print("it is better to use a list comprehension")

	if (result < result_comp and result < result_map):
		print("it is better to use a loop\n")

	if (result_map < result and result_map < result_comp):
		print("it is better to use a map\n")
	print(f'{all_res[0]} vs {all_res[1]} vs {all_res[2]}')

	return

if __name__ == '__main__':
	try:
		main()
	except RuntimeError as err:
		print('Runtime error:', err.args[0])