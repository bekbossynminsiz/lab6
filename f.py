# 1. Multiply all numbers in a list
from functools import reduce

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

numbers = [2, 3, 4, 5]
print(multiply_list(numbers))  

# 2. Count uppercase and lowercase letters in a string
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

s = "Hello World"
upper, lower = count_case(s)
print(f"Uppercase Letters: {upper}, Lowercase Letters: {lower}")

# 3. Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

s = "madam"
print(is_palindrome(s))  

# 4. Invoke square root function after specific milliseconds
import time
import math

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000) 
    return math.sqrt(number)

number = 25100
delay = 2123  
result = delayed_sqrt(number, delay)
print(f"Square root of {number} after {delay} milliseconds is {result}")

# 5. Check if all elements in a tuple are true
def all_true(t):
    return all(t)

t = (True, True, False)
print(all_true(t))  
