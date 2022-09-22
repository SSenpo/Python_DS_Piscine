import timeit
import sys
from functools import reduce


class Math:
	def __init__(self, sum_squares: int) -> None:
		self.sum_squares = sum_squares

	def	_sum_loop(self) -> int:
		sum = 0
		for num in range(self.sum_squares):
			sum += num * num

		return sum
	
	def _sum_reduce(self) -> int:
		def sum2(prev: int, next: int):
			return prev + next**2
		return reduce(sum2, range(1, self.sum_squares + 1))  


def main(method: str, it_num: str, count_sum: str) -> None:
	try:
		it_num = int(it_num)
		count_sum = int(count_sum)
	except:
		print("Can't parse number of iterations")
		return
	
	IT_NUMBER = it_num
	math = Math(count_sum)

	if (method == "loop"):
		result = timeit.timeit(lambda: math._sum_loop(), number=IT_NUMBER)
	if (method == "reduce"):
		result = timeit.timeit(lambda: math._sum_reduce(), number=IT_NUMBER)

	print(f'{result}')

	return

if __name__ == '__main__':
	if len(sys.argv) == 4:
		try:
			main(sys.argv[1], sys.argv[2], sys.argv[3])
		except RuntimeError as err:
			print('Runtime error:', err.args[0])
	else:
		print('Incorrect input.')