x = float(input('Введіть найближче значення величини Х:'))
delta_x = float(input('Введіть абсолютну похибку вимірювання величини Х:'))

y = float(input('Введіть найближче значення величини Y:'))
delta_y = float(input('Введіть абсолютну похибку вимірювання величини Y:'))

omega_x = delta_x / x
omega_y = delta_y / y

print('Відносна похибка значення величини Х:', omega_x)
print('Відносна похибка значення величини Y:', omega_y)

# Абсолютна похибка додавання:
def delta_sum(delta_x, delta_y):
    return delta_x + delta_y
print('Абсолютна похибка X+Y= ', delta_sum(delta_x, delta_y))

# Абсолютна похибка віднімання:
def delta_sub(delta_x, delta_y):
    return delta_x - delta_y
print('Абсолютна похибка X-Y= ', delta_sub(delta_x, delta_y))

# Абсолютна похибка множення:
def delta_multi(x,y, delta_x, delta_y):
    return delta_x * delta_y + delta_x * y +x*delta_y 
print('Абсолютна похибка X*Y= ', delta_multi(x,y,delta_x, delta_y))

# Абсолютна похибка ділення:
def delta_div(x,y, delta_x, delta_y):
    return ((delta_x + x)/(delta_y + y)) - (x/y)
print('Абсолютна похибка X/Y= ', delta_div(x,y,delta_x, delta_y))

# Відносна похибка додавання:
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