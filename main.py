import random

password = ''
password_length = int(input('Enter length of the password: '))

for i in range(password_length):
    password = password + random.choice('QWERTYUIOPASDFGHJKLZXCVBNM1234567890qwertyuiopasdfghjklzxcvbnm')

print(f'Your password is {password}')

