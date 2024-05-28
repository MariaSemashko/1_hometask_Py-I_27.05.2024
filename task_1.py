'''Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны
с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.'''

a = float(input('Введите длину стороны a: '))
b = float(input('Введите длину стороны b: '))
c = float(input('Введите длину стороны c: '))

if a > b + c or b > a + c or c > a + b:
    print('Такого треугольника не существует')
elif a == b == c:
    print('Это равносторонний треугольник')
elif a == b or b == c or a == c:
    print('Это равнобедренный треугольник')
else:
    print('Это разносторонний треугольник')


