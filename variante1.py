import matplotlib.pyplot as plt
import numpy as np

# Definir las restricciones
x = np.linspace(0, 10, 400)
y1 = 10 - x
y2 = x + 1
y3 = np.minimum(x, 4)

# Graficar las restricciones
plt.plot(x, y1, label='x + y ≤ 10')
plt.plot(x, y2, label='y - x ≤ 1')
plt.plot(x, y3, label='x, y ≤ 4')

# Encontrar el punto de intersección factible
x_opt = 1.5  # Valor de x en la solución óptima
y_opt = 1.5  # Valor de y en la solución óptima
plt.plot(x_opt, y_opt, 'ro')  # Marcar la solución óptima

# Añadir etiquetas y leyenda
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Mostrar el gráfico
plt.show()
