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


def main():
	IT_NUMBER = 90000000
	email_cl = Email_list()

	result = timeit.timeit(lambda: email_cl._iteration_loop(), number=IT_NUMBER)
	result_comp = timeit.timeit(lambda: email_cl._iteration_comprehensions(), number=IT_NUMBER)

	if (result > result_comp):
		print(f"it is better to use a list comprehension\n{result_comp} vs {result}")

	if (result < result_comp):
		print(f"it is better to use a loop\n \
			{result} vs {result_comp}")

	return

if __name__ == '__main__':
	try:
		main()
	except RuntimeError as err:
		print('Runtime error:', err.args[0])