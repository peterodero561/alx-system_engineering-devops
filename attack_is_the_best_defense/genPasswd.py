#!/usr/bin/python3
'''Generates password dictionary of length 11 and saves them in passwords.txt'''

import itertools

# characters used in password generaion
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?'

# generate all possible commbinations of characters fo length 11
passwords = itertools.product(chars, repeat=11)

# write genarated passwords to a file
with open('passwords.txt', 'w') as f:
    for passwd in passwords:
        f.write(''.join(passwd) + '\n')

print("Password dictionary created successfully")
