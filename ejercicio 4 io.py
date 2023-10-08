import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# Definir las variables
x1, x2 = sp.symbols('x1 x2')

# Definir las restricciones
eq1 = 2*x1 + x2 - 1200
eq2 = 3*x1 + 4*x2 - 2400
eq3 = x1 + x2 - 800
eq4 = x1 - x2 - 450

# Resolver las ecuaciones para x2 en términos de x1
x2_1 = sp.solve(eq1, x2)[0]
x2_2 = sp.solve(eq2, x2)[0]
x2_3 = sp.solve(eq3, x2)[0]
x2_4 = sp.solve(eq4, x2)[0]

# Crear un rango de valores de x1 para graficar
x1_values = np.linspace(0, 1000, 400)

# Calcular los correspondientes valores de x2 para cada ecuación
x2_values_1 = [x2_1.subs(x1, val) for val in x1_values]
x2_values_2 = [x2_2.subs(x1, val) for val in x1_values]
x2_values_3 = [x2_3.subs(x1, val) for val in x1_values]
x2_values_4 = [x2_4.subs(x1, val) for val in x1_values]

# Graficar las restricciones
plt.plot(x1_values, x2_values_1, label='2x1 + x2 <= 1200')
plt.plot(x1_values, x2_values_2, label='3x1 + 4x2 <= 2400')
plt.plot(x1_values, x2_values_3, label='x1 + x2 <= 800')
plt.plot(x1_values, x2_values_4, label='x1 - x2 <= 450')

# Añadir etiquetas y leyenda
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend()

# Calcular el valor de Z para el plan de producción actual
x1_actual = 550
x2_actual = 100
Z_actual = 8*x1_actual + 5*x2_actual
plt.title(f'Plan Actual - Z = {Z_actual}')

# Mostrar el gráfico
plt.show()

# Imprimir el valor de Z para el plan de producción actual
print(f'Para el plan de producción actual:')
print(f'Z = {Z_actual} €')
print(f'x1 = {x1_actual} docenas')
print(f'x2 = {x2_actual} docenas')
