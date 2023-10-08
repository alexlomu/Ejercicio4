import matplotlib.pyplot as plt
import numpy as np
# Si el objetivo es divertirse al máximo, la solución óptima sería pasar el tiempo máximo permitido por sus padres en diversión, es decir, 4 horas.
y_values = np.array([0, 4])

# Graficar el tiempo máximo de diversión
plt.plot(np.zeros_like(y_values), y_values, label='Diversión al máximo')

# Añadir etiquetas y leyenda
plt.xlabel('Horas de estudio')
plt.ylabel('Horas de diversión')
plt.legend()

# Mostrar el gráfico
plt.show()
