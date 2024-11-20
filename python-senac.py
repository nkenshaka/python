import random

print('Bem vindo ao Gerador de senhas!')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+[]|;:,.<>?/0123456789'

number = input('Quantas senhas precisa?: ')
number = int(number)

length = input('Qual o comprimento da senha: ')
length = int(length)

if number > 1:
    print('\nAqui estão suas senhas: ')
else:
    print('\nAqui está sua senha: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
