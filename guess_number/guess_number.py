from random import randint

# Получаем случайное число в диапазоне от 1 до 100.
number = randint(1, 100)
print('Угадайте число от 1 до 100')

while True:
    guess = int(input('Введите число: '))

    if guess < number:
        print('Ваше число меньше того, что загадано.')
    if guess > number:
        print('Ваше число больше того, что загадано.')    
    if guess == number:
        print('Вы угадали!')


