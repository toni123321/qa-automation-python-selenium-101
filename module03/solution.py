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
    str_lower = str.lower()
    vowels = 'aeiouyAEIOUY'
    return sum(str_lower.count(v) for v in vowels)
    
def count_consonants(str):
    str_lower = str.lower()
    consonants = 'bcdfghjklmnpqrstvwxz'
    return sum(str_lower.count(c) for c in consonants)

def prime_number(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True        
    
def fact_digits(n):
    result_sum = 0
    for number in to_digits(n):
        result_sum += fact(number)
        
    return result_sum
    
def fact(n):
    if (n == 0) or (n == 1):
        return 1
    return n * fact(n - 1)
                
def fibonacci(n):
    if n == 1:
        return [1]
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib
        
 
def fib_number(n):
    fib = fibonacci(n)
    result = ""
 
    for i in fib:
        result += str(i)
 
    return int(result)
    

def palindrome(n):
    string = str(n)
 
    first_half = 0
 
    while first_half < (len(string) / 2 +1):
        if string[first_half] != string[len(string) - 1 - first_half]:
            return False
        first_half += 1
 
    return True

def char_histogram(string):
    keys = []
    dict = {}
 
    for ch in string:
        keys.append(ch)
 
    for ch in string:
        dict[ch] = keys.count(ch)
 
    return dict
