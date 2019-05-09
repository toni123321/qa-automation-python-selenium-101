import os

def num_add(a, b):
	return a + b
	
def num_sub(a, b):
	return a - b

def num_mul(a, b):
	return a * b

def num_div(a, b):
	return float(a) / float(b)

def num_floor(a, b):
	return a // b

def num_rem(a, b):
	return a % b

IS_TRUE = True
IS_FALSE = False

PANCAKE_INGREDIENTS = {
	"flour": 2,
	"eggs": 4,
	"milk": 200,
	"butter": False,
	"salt": 0.001
}

def ingredient_exists(ingr, dict):
	if dict.has_key(ingr):
		return IS_TRUE
	else:
		return IS_FALSE

def fatten_pancakes(dict):
	dict_copy = dict.copy()	
	dict_copy['eggs'] = 6
	dict_copy['butter'] = True
	return dict_copy
	

def add_sugar(dict):
	dict_copy = dict.copy()
	dict_copy['sugar'] = 1
	return dict_copy	
	
def remove_salt(dict):
	dict_copy = dict.copy()
	dict_copy.pop("salt")
	return dict_copy

FIBONACCI_NUMBERS = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

def add_fibonacci(lst):
	f1 = lst[len(lst) - 1]
	f2 = lst[len(lst) - 2]
	fn = f1 + f2
	lst.append(fn)
	return lst
	
def fib_exists(lst, n):
	if(n in lst):
		return True
	else:
		return False

def which_fib(lst, n):
		index = lst.index(n)
		return index+1
