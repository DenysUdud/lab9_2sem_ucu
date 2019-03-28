def square_preceding(values):

	""" (list of number) -> NoneType

	Replace each item in the list with square the value of the

	preceding item, and replace the first item with 0.

	>>> L = [1, 2, 3]

	>>> square_preceding(L)

	>>> L

	[0, 1, 4]

	"""

	if values != [] and isinstance(values, list):

		temp_1 = values[0]

		values[0] = 0

		for i in range(1, len(values)):
			temp_2 = values[i]
			values[i] = temp_1 ** 2
			temp_1 = temp_2


l = [1, 2, 3]
square_preceding(l)
