import random

password = ''
password_length = int(input('Enter password length: '))

for i in range(password_length):
    password = password + random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz')

print(f'Your password is {password}')

