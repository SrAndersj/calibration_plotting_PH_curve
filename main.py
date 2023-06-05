import matplotlib.pyplot as plt
import numpy as np

def plot_curva_titulacion(Ve, pH):
    plt.plot(Ve, pH, marker='o', linestyle='-', color='b')
    plt.xlabel('Volumen agregado (mL)')
    plt.ylabel('pH')
    plt.title('Curva de titulación')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    # Datos de volumen agregado (Ve) y pH
    Ve = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
    pH = np.array([2.0, 2.3, 3.0, 3.5, 4.0, 6.5, 9.0, 11.0, 12.0, 12.3, 12.5])

    # Llamar a la función para graficar la curva de titulación
    plot_curva_titulacion(Ve, pH)

