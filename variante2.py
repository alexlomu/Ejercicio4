import matplotlib.pyplot as plt
import numpy as np
# Para esta variante, la solución óptima sería estudiar o divertirse durante el tiempo máximo posible
x_values = np.array([0, 4])
y_values = np.array([4, 0])

# Graficar el tiempo máximo de estudio y diversión
plt.plot(x_values, y_values, label='Estudiar o divertirse al máximo')

# Añadir etiquetas y leyenda
plt.xlabel('Horas de estudio')
plt.ylabel('Horas de diversión')
plt.legend()

# Mostrar el gráfico
plt.show()
