# trabajo11.py - Redes Neuronales: El Perceptrón (Consola)
import numpy as np

def funcion_escalon(z):
    """Función de activación escalón (Step function)"""
    return 1 if z >= 0 else 0

def perceptron(X, W, b):
    """Cálculo Forward: combinación lineal Z y activación"""
    Z = np.dot(X, W) + b
    return funcion_escalon(Z)

def taller_analitico_perceptron():
    print("\n" + "="*60)
    print("   TALLER ANALÍTICO: CALCULANDO EL DISPARO DE LA NEURONA")
    print("="*60)
    print("Estructura de la Neurona:")
    print(" - Entradas X: Ingresos (X1) = 50, Deudas (X2) = 20")
    print(" - Pesos W   : W1 = 0.8, W2 = -0.5")
    print(" - Sesgo b   : b = -10\n")

    X = np.array([50, 20])
    W = np.array([0.8, -0.5])
    b = -10

    # 1. Combinación lineal Z
    Z = (X[0] * W[0]) + (X[1] * W[1]) + b
    salida = funcion_escalon(Z)

    print("[DESARROLLO PASO A PASO]")
    print(f"1. Combinación lineal Z = (50 * 0.8) + (20 * -0.5) + (-10)")
    print(f"   Z = 40 - 10 - 10 = {Z:.2f}")
    print(f"2. Paso por Función Escalón: salida = f({Z:.2f})")
    print(f"   Resultado final: {salida} ({'Aprobado' if salida == 1 else 'Rechazado'})\n")

    print("[ANÁLISIS DE PESOS EN EL ÁMBITO FINANCIERO]")
    print(" 3. ¿Por qué W2 (-0.5) es negativo?")
    print("    -> Las deudas representan un riesgo financiero. Un peso negativo")
    print("       penaliza el valor de Z a medida que las deudas aumentan,")
    print("       reduciendo la probabilidad de que la neurona apruebe el crédito.")


def taller_laboratorio_perceptron():
    print("\n" + "="*60)
    print("   TALLER DE LABORATORIO: COMPUERTAS LÓGICAS (AND Y OR)")
    print("="*60)

    casos = [
        np.array([0, 0]),
        np.array([0, 1]),
        np.array([1, 0]),
        np.array([1, 1])
    ]

    # 1. Compuerta AND (Demostración)
    W_and = np.array([0.5, 0.5])
    b_and = -0.8

    print("--- 1. Evaluación Compuerta Lógica AND (W=[0.5, 0.5], b=-0.8) ---")
    for x in casos:
        res = perceptron(x, W_and, b_and)
        print(f" Entradas {x} -> Salida: {res}")

    # 2. Compuerta OR (Ajuste manual de pesos)
    W_or = np.array([0.5, 0.5])
    b_or = -0.3

    print("\n--- 2. Solución a la Compuerta Lógica OR (W=[0.5, 0.5], b=-0.3) ---")
    for x in casos:
        res = perceptron(x, W_or, b_or)
        print(f" Entradas {x} -> Salida: {res}")

    print("\n" + "-"*60)
    print("[CONCLUSIÓN DEL RETO]")
    print(" Pesos configurados para la compuerta OR:")
    print(f"  * Vector W = {W_or}")
    print(f"  * Sesgo b  = {b_or}")
    print(" Con este ajuste, cualquier entrada que contenga al menos un 1")
    print(" genera un Z >= 0, logrando que el perceptrón dispare 1.")


def ejecutar_consola():
    """Punto de entrada principal llamado desde main.py"""
    while True:
        print("\n" + "*"*60)
        print("   SESIÓN 11: REDES NEURONALES - EL PERCEPTRÓN")
        print("*"*60)
        print("1. Taller Analítico (Combinación Lineal y Análisis de Pesos)")
        print("2. Taller de Laboratorio (Compuertas Lógicas AND / OR)")
        print("0. Volver al Menú Principal")

        opcion = input("\nSeleccione una opción (0-2): ").strip()

        if opcion == '1':
            taller_analitico_perceptron()
            input("\nPresione ENTER para continuar...")
        elif opcion == '2':
            taller_laboratorio_perceptron()
            input("\nPresione ENTER para continuar...")
        elif opcion == '0':
            break
        else:
            print("\nOpción inválida. Intente de nuevo.")


if __name__ == "__main__":
    ejecutar_consola()