# trabajo12.py - Redes Neuronales Densas o Multicapa (MLP) (Consola)
import numpy as np

def sigmoide(x):
    """Función de activación Sigmoide"""
    return 1 / (1 + np.exp(-x))

def taller_analitico_mlp():
    print("\n" + "="*60)
    print("   TALLER ANALÍTICO: CONTANDO PARÁMETROS (MLP)")
    print("="*60)
    print("Arquitectura de la Red:")
    print(" - Capa de Entrada: 3 características (Edad, Ingresos, Deuda)")
    print(" - Capa Oculta   : 1 capa con 4 neuronas")
    print(" - Capa de Salida  : 1 neurona (Aprobado/Rechazado)\n")

    # Cálculos analíticos
    pesos_capa1 = 3 * 4
    sesgos_capa1 = 4
    pesos_capa2 = 4 * 1
    sesgos_capa2 = 1
    total_parametros = pesos_capa1 + sesgos_capa1 + pesos_capa2 + sesgos_capa2

    print("[DESARROLLO Y CÁLCULO DE PARÁMETROS]")
    print(f"1. Pesos (W1) entre Entrada (3) y Capa Oculta (4): 3 x 4 = {pesos_capa1}")
    print(f"2. Sesgos (b1) en Capa Oculta: 1 por neurona = {sesgos_capa1}")
    print(f"3. Pesos (W2) entre Capa Oculta (4) y Salida (1): 4 x 1 = {pesos_capa2}")
    print(f"   Sesgo (b2) en Capa de Salida: 1 por neurona = {sesgos_capa2}")
    print("-" * 60)
    print(f"TOTAL DE PARÁMETROS ENTRENABLES: {total_parametros}\n")

    print("[CONCEPTO TEÓRICO]")
    print("El límite del Perceptrón simple (1969 - Minsky) radicaba en resolver")
    print("problemas no lineales. Agregar capas ocultas permite a la red 'plegar'")
    print("el espacio vectorial para clasificar patrones complejos (Teorema de")
    print("Aproximación Universal).")


def taller_laboratorio_mlp():
    print("\n" + "="*60)
    print("   TALLER DE LABORATORIO: CÁLCULO TENSORIAL Y PROCESAMIENTO EN LOTE")
    print("="*60)

    # Definición de pesos y sesgos
    W1 = np.array([
        [0.1, 0.2, 0.3, 0.4],
        [-0.5, 0.6, 0.7, -0.8],
        [0.9, -0.1, 0.2, 0.3]
    ])
    b1 = np.array([0.1, 0.2, 0.3, 0.4])

    W2 = np.array([0.5, 0.6, 0.7, 0.8])
    b2 = np.array([-0.1])

    # 1. Caso 1 Cliente
    X_un_cliente = np.array([0.5, 0.8, 0.2])
    
    Z1_single = np.dot(X_un_cliente, W1) + b1
    A1_single = sigmoide(Z1_single)
    Z2_single = np.dot(A1_single, W2) + b2
    salida_single = sigmoide(Z2_single)

    print("--- 1. Evaluación de 1 Solo Cliente ---")
    print(f" Val. Lineales Z1 (Sin activar): {Z1_single}")
    print(f" Activación A1 (Sigmoide en 0-1): {A1_single}")
    print(f" Predicción Final (Probabilidad): {np.round(salida_single[0], 4)}\n")

    # 2. Reto: Procesamiento en Lote (2 Clientes simultáneos Matrix 2x3)
    X_batch = np.array([
        [0.5, 0.8, 0.2],
        [0.1, 0.9, 0.9]
    ])

    Z1_batch = np.dot(X_batch, W1) + b1
    A1_batch = sigmoide(Z1_batch)
    Z2_batch = np.dot(A1_batch, W2) + b2
    salida_batch = sigmoide(Z2_batch)

    print("--- 2. Procesamiento en Lote (Batch de 2 Clientes Matrix 2x3) ---")
    print("Entradas (X):")
    print(X_batch)
    print("\nSalida Capa Oculta A1 (2x4):")
    print(np.round(A1_batch, 4))
    print("\nPredicciones Finales (Probabilidades por Cliente):")
    for i, pred in enumerate(salida_batch):
        print(f" * Cliente {i+1}: {np.round(pred, 4)}")

    print("\n" + "-"*60)
    print("[CONCLUSIÓN TENSORIAL]")
    print("Gracias a la multiplicación de matrices de NumPy (np.dot),")
    print("se evalúan miles de registros en paralelo reutilizando la misma")
    print("estructura de pesos sin necesidad de bucles for.")


def ejecutar_consola():
    """Punto de entrada principal llamado desde main.py"""
    while True:
        print("\n" + "*"*60)
        print("   SESIÓN 12: REDES NEURONALES DENSAS (MLP)")
        print("*"*60)
        print("1. Taller Analítico (Conteo de Parámetros y Arquitectura)")
        print("2. Taller de Laboratorio (Feedforward y Procesamiento Batch)")
        print("0. Volver al Menú Principal")

        opcion = input("\nSeleccione una opción (0-2): ").strip()

        if opcion == '1':
            taller_analitico_mlp()
            input("\nPresione ENTER para continuar...")
        elif opcion == '2':
            taller_laboratorio_mlp()
            input("\nPresione ENTER para continuar...")
        elif opcion == '0':
            break
        else:
            print("\nOpción inválida. Intente de nuevo.")


if __name__ == "__main__":
    ejecutar_consola()