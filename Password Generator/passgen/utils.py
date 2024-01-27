import random
from string import ascii_letters

def generate_password(count_of_letters, count_of_numbers, count_of_symbols):
    letters = [i for i in ascii_letters]
    numbers = [str(i) for i in range(10)]
    symbols = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

    password_list = []

    for i in range(1, count_of_letters+1):
        password_list += random.choice(letters)

    for i in range(1, count_of_numbers+1):
        password_list += random.choice(numbers)

    for i in range(1, count_of_symbols+1):
        password_list += random.choice(symbols)

    random.shuffle(password_list)

    password = ''

    for i in password_list:
        password += i

    return password