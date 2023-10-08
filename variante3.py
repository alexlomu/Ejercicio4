import matplotlib.pyplot as plt
import numpy as np
# Si el objetivo es convertirse en un "trol", la solución óptima sería pasar las 10 horas disponibles en diversión.
y_values = np.linspace(0, 10, 400)

# Graficar el tiempo máximo de diversión
plt.plot(np.zeros_like(y_values), y_values, label='Diversión al máximo')

# Añadir etiquetas y leyenda
plt.xlabel('Horas de estudio')
plt.ylabel('Horas de diversión')
plt.legend()

# Mostrar el gráfico
plt.show()
