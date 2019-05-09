def f_c(x):
	'''
	return value 4 for any input parameter
	'''
	return 4

def f_x(x, a, b):
	result = a * x + b
	return result

def sum(x):
	n1 = f_x(x, 1, 1)
	n2 = f_x(x, 2, 2)
	n3 = f_x(x, 3, 3)
	sum = n1 + n2 + n3
	return sum
