import numpy as np
import matplotlib.pyplot as plt
#import statistics as stats

# Constante de permeabilidad del vacío
mu_0 = 4 * np.pi * 1e-7  # en T·m/A

# Parámetros del solenoide para el calculo teorico cuando x varia
L = 0.162  # Longitud
N = 300  # Número de vueltas
a = 0.02  # Radio
I = 1 # Corriente

# Parámetros del solenoide para el calculo teorico cuando I varia
L = 0.162 # Longitud
N = 300 # Número de vueltas
a = 0.02 # Radio
x = 0 # Posición en el centro de la bobina

# Función para calcular Bx teórico para un valor de I
def calcular_Bx(mu_0, N, I, L, a, x):
    term1 = mu_0 * N * I / (2 * L)
    term2 = L / 2 - x
    term3 = np.sqrt((L / 2 - x) ** 2 + a ** 2)
    term4 = np.sqrt((L / 2 + x) ** 2 + a ** 2)
    term5 = L / 2 + x
    
    Bx = term1 * (term2 / term3 + term5 / term4)
    return Bx * 1000  # Convertir a miliTeslas (mT)

# Valores de corriente (en amperios)
I_vals = np.array([0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])

# Valores de x (en metros)
x_vals = np.linspace(-L/2, L/2, 9)


# Calcular valores de Bx teórico con x variando
Bx_vals = calcular_Bx(mu_0, N, I, L, a, x_vals)

Bx_vals2 = calcular_Bx(mu_0, N, I_vals, L, a, x)

# Datos experimentales para x variando
Bx_exp1 = np.array([1.07, 1.9, 2.11, 2.15, 2.17, 2.15, 2.09, 1.9, 1.2])

# Datos experimentales para I variando
Bx_exp2 = np.array([0.42, 0.67, 0.87, 1.1, 1.34, 1.53, 1.8, 2.0])


# GRAFICA PARA X VARIANDO
# ------------------------------------------------------------------------
# # Crear la gráfica para x variando
# plt.plot(x_vals, Bx_vals, label='Teórico', color='blue', marker='o')
# plt.scatter(x_vals, Bx_exp1, color='green', label='Experimental 1')
# pendiente1 = np.polyfit(x_vals, Bx_exp1, 1)
# print(pendiente1)

# # Configurar la gráfica
# plt.xlabel('Longitud(m)')
# plt.ylabel('B_x (mT)')
# plt.title('Campo magnético B_x en función de x (Teórico y Experimental)')
# plt.legend()
# plt.grid(True)

# Mostrar la gráfica

# ------------------------------------------------------------------------


# GRAFICA PARA I VARIANDO
# ------------------------------------------------------------------------
# Crear la gráfica para I variando
# plt.plot(I_vals, Bx_vals2, label='Teórico', color='blue', marker='o')
# plt.scatter(I_vals, Bx_exp2, color='green', label='Experimental 2')
# pendiente2 = np.polyfit(I_vals, Bx_exp2, 1)
# print(pendiente2)

# # Configurar la gráfica
# plt.xlabel('Corriente I (A)')
# plt.ylabel('B_x (mT)')
# plt.title('Campo magnético B_x en función de I (Teórico y Experimental)')
# plt.legend()
# plt.grid(True)


plt.show()
