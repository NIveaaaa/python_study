def mean(num_list):
	try:
		return sum(num_list)/len(num_list)
	except ZeroDivisionError:
		return 0
	except TypeError:
		raise TypeError("The algebraic mean of an empty list is undefined. "
                       "Please provide a list of numbers")
		