
import numpy as np
import matplotlib.pyplot as plt

monto_inicial = 10000
años = 10
rendimiento_esperado = 0.10
volatilidad = 0.15
num_simulaciones = 10000

# 1. Creamos una matriz para almacenar los valores de cada año (años + 1 para incluir el año 0)
trayectorias = np.zeros((num_simulaciones, años + 1))
trayectorias[:, 0] = monto_inicial

# 2. Calculamos de forma acumulativa para cada uno de los 10 años
for t in range(1, años + 1):
    Z = np.random.standard_normal(num_simulaciones)
    trayectorias[:, t] = trayectorias[:, t-1] * np.exp(
        (rendimiento_esperado - 0.5 * volatilidad**2) * 1 +
        volatilidad * np.sqrt(1) * Z
    )
valores_finales = trayectorias[:, -1]

# 3. Extraer y calcular los Percentiles del año final
p10 = np.percentile(valores_finales, 10)
p50 = np.percentile(valores_finales, 50)
p90 = np.percentile(valores_finales, 90)

# 4. Mostrar resultados en pantalla
print(f"Monto inicial: ${monto_inicial:,.2f}")
print(f"Monto final más bajo (Percentil 10) tras 10 años: ${p10:,.2f}")
print(f"Monto final esperado (Percentil 50) tras 10 años: ${p50:,.2f}")
print(f"Monto final más alto (Percentil 90) tras 10 años: ${p90:,.2f}")

# 5. Graficar las trayectorias usando Matplotlib
plt.figure(figsize=(12, 6))

# Graficamos las primeras 10000 trayectorias individuales de forma tenue
tiempo = np.arange(años + 1)
for i in range(10000):
    plt.plot(tiempo, trayectorias[i, :], color='lightgray', alpha=0.5, label='Trayectorias' if i == 0 else "")

# Calculamos los percentiles históricos año tras año para graficarlos
percentil_10_hist = np.percentile(trayectorias, 10, axis=0)
percentil_50_hist = np.percentile(trayectorias, 50, axis=0)
percentil_90_hist = np.percentile(trayectorias, 90, axis=0)

# Graficar los percentiles como líneas de referencia destacadas
plt.plot(tiempo, percentil_10_hist, color='red', linestyle='--', linewidth=2, label='Percentil 10 (Escenario Bajo)')
plt.plot(tiempo, percentil_50_hist, color='blue', linestyle='-', linewidth=2, label='Percentil 50 (Mediana)')
plt.plot(tiempo, percentil_90_hist, color='green', linestyle='--', linewidth=2, label='Percentil 90 (Escenario Alto)')

# Detalles del gráfico
plt.title('Simulación de Monte Carlo - Proyección del Portafolio a 10 Años', fontsize=14)
plt.xlabel('Años', fontsize=12)
plt.ylabel('Valor del Portafolio ($)', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left')
plt.show()

