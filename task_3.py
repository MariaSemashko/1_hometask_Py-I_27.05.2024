''' Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
 Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
 Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)'''

from random import randint
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
attempt = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)
print(num)

while attempt > 0:
    user_version = int(input('Попробуйте угадать число: '))

    if user_version == num:
        print('Поздравляю, вы угадали!')
        break
    elif user_version > num:
        print('Меньше')
    else:
        print('Больше')

    attempt -= 1
    print(f'Осталось попыток {attempt}')

print(f'Правильным числом было {num}.')