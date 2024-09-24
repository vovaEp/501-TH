# вхідні дані
x = 35.4
delta_x = 0.2

y = 0.3
delta_y = 0.003

omega_x = delta_x / x
omega_y = delta_y / y

print('Відносна похибка площі:', omega_x)
print('Відносна похибка розміру плитки:', omega_y)

# Абсолютна похибка додавання
def delta_sum(delta_x, delta_y):
    return delta_x + delta_y
print('Абсолютна похибка X+Y= ', delta_sum(delta_x, delta_y))

# Абсолютна похибка віднімання
def delta_sub(delta_x, delta_y):
    return delta_x - delta_y
print('Абсолютна похибка X-Y= ', delta_sub(delta_x, delta_y))

# Абсолютна похибка множення
def delta_multi(x,y, delta_x, delta_y):
    return delta_x * delta_y + delta_x * y +x*delta_y 
print('Абсолютна похибка X*Y= ', delta_multi(x,y,delta_x, delta_y))

# Абсолютна похибка ділення
def delta_div(x,y, delta_x, delta_y):
    return ((delta_x + x)/(delta_y + y)) - (x/y)
print('Абсолютна похибка X/Y= ', delta_div(x,y,delta_x, delta_y))

# Відносна похибка додавання
def omega_div(x,y, omega_x, omega_y):
    return x/(x+y)*omega_x + y/(x+y)*omega_y
print('Відносна похибка X+Y= ',omega_div(x,y, omega_x, omega_y))


# Відносна похибка віднімання
def omega_subtraction(x,y, omega_x, omega_y):
    return x/(x-y)*omega_x - y/(x-y)*omega_y
print('Відносна похибка X-Y= ',omega_subtraction(x,y, omega_x, omega_y))


# Відносна похибка множення
def omega_multi(omega_x, omega_y):
    return omega_x * omega_y + omega_x + omega_y
print('Відносна похибка X*Y= ',omega_multi(omega_x, omega_y))

# Відносна похибка ділення
def omega_div( omega_x, omega_y):
    return (omega_x - omega_y)/(omega_y +1)
print('Відносна похибка X/Y= ',omega_div(omega_x, omega_y))


# 1 Обчисліть площу кімнати на основі ваших вимірювань.
room_length = 5
delta_length = 0.05
room_width = 3
delta_width = 0.05

room_square = room_length * room_width
print('площа кімнати, м2', room_square)

# 2 Визначте абсолютну похибку обчислення площі, враховуючи похибки вимірювань довжини та ширини.
# відносна похибка довжини
omega_length =   delta_length / room_length
print('відносна похибка довжини', omega_length)

# відносна похибка ширини
omega_width = delta_width /room_width 
print('відносна похибка ширини', omega_width)
print('абсолютна похибка площі', delta_multi(room_length,room_width, delta_length,  delta_width))

# 3 Обчисліть відносну похибку обчислення площі.
room_square_err = omega_multi(omega_length, omega_width)
print('Відносна похибка площі', room_square_err)

# 4 Оберіть плитку в онлайн-магазині (посилання на товар), визначте її кількість (похибку на вимірювання плитки можна не враховувати, а можна і врахувати :-)
# https://epicentrk.ua/ua/shop/plytka-cersanit-bruno-lait-hrei-30x30.html
tile_square = 0.3 * 0.3
tile_number = room_square / tile_square
tile_delta = delta_div(room_square, room_square_err, tile_square,  0)
print('Абсолютна похибка при діленні: ', tile_delta)
print('Кількість плитки: ', tile_number , '±', round(tile_delta, 2))

# 5 Опишіть джерела похибок, які могли виникнути під час вимірювань, і дайте рекомендації щодо зменшення похибок при наступних вимірюваннях.
#Основні джерела похибок під час вимірювань:

#Нечіткість вимірювання: наприклад, невідповідність відліків на рулетці або неточності у вимірюванні через вигин рулетки.
#Нерівності підлоги: якщо підлога або стіни мають нерівності, це може вплинути на точність вимірювань.
#Зміна температури: лінійні розміри можуть трохи змінюватися під впливом температури, що призведе до незначних похибок.
#Товщина шву між плитками

#Рекомендації щодо зменшення похибок:
#Використовуйте точніші інструменти, наприклад, лазерний далекомір для точнішого вимірювання.
#Повторіть вимірювання кілька разів та використайте середнє значення для зменшення випадкових похибок.
#Звертайте увагу на кути приміщення: перевірте їх на прямокутність і врахуйте можливі викривлення.