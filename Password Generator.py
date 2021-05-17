# This program generates a strong and random password for a given length.

import random

print('\tPassword Generator\n')

password = ''
setOfChar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ\
abcdefghijklmnopqrstuvwxyz\
!@#$%^&*(),.'

length = int(input('Enter password length:\t'))

for c in range(length):
    password += random.choice(setOfChar)

print('\nGenerated password is:\t' + password)