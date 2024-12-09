#!/bin/python3

from random import randint
from string import ascii_letters, digits, punctuation
from itertools import product


nr_characters = int(input("How long should the password be? "))
possible_characters = ascii_letters + digits + punctuation

sum = 0

password = ""
for _ in range(nr_characters):
    curr_character = possible_characters[randint(0, len(possible_characters) - 1)]
    password += curr_character
    if curr_character in digits:
        sum += int(curr_character)

if sum != 25:
    while sum + 9 <= 25:
        password += '9'
        sum += 9

if sum != 25:
    password += str(25 - sum)


print(sum)
print(password)

#for print_com in product(digits, repeat=3):
#    print(print_com)
