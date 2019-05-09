import os
import math
from re import findall

def sum_of_digits(n):
	num = abs(n)
	res = 0
	while num:
		res += num % 10
		num //= 10
	return res

def to_digits(n):
	num = abs(n)
	digits = [int(x) for x in str(n)]
	return digits
	
def to_number(digits):
	res = int("".join(map(str, digits)))
	return res
	
def count_vowels(str):
	vowels='aeiouyAEIOUY'
	count = 0
	for s in str:
		if s in vowels: count=count+1
	return count
def count_consonants(str):
	str2 = str.lower()
	consonants = 'bcdfghjklmnpqrstvwxz'
	return sum(str2.count(c) for c in consonants)

def prime_number(n):
	pass
	
def fact_digits(n):
	pass 
	
def fibonacci(n):
	pass

def fib_number(n):
	pass

def palindrome(n):
	pass

def char_histogram(string):
	pass
	
	
