import random

random_number = random.randint(1, 5)
user_number = input("Угадай число( от 1 до 5): ")

if int(user_number) == random_number:
    print(f"Вы угадали! Число и правда было {random_number}")

elif random_number != int(user_number):
    print(f"К сожалению, вы не угадали. Число было {random_number}")
input()