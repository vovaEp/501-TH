import numpy
import scipy.interpolate as spi 
import matplotlib.pyplot as plt

# Таблиця значень функції
x =  numpy.array([ 0.8, 2, 2.8, 4.1, 5, 5.9, 7.3, 8.1, 9.2, 10 ])
y = numpy.array([ 1.3, 2.6, 3.7, 4.5, 6.0, 7.2, 8.0, 9.2, 10.3, 11.8 ])

# Інтерполяційний поліном Лагранжа
p = spi.lagrange(x, y)
print(p)

# Формуємо точки для відображення полінома
z = numpy.linspace(-1, 7, 100)

# Відображаємо поліном та задані точки
plt.plot(z, p(z), '-')
plt.plot(x, y, 'o')
plt.legend(['L(x)', 'data'])
plt.xlabel('x') 
plt.ylabel('y') 
plt.show()