# trabajo9.py - KNN: K-Vecinos Más Cercanos (Consola)
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def taller_analitico_knn():
    print("\n" + "="*60)
    print("   TALLER ANALÍTICO: LA VOTACIÓN ESPACIAL (KNN)")
    print("="*60)
    print("Dataset de Entrenamiento:")
    print(" - Cliente 1 (A): (20, 30) -> NO COMPRA (0)")
    print(" - Cliente 2 (B): (40, 50) -> COMPRA (1)")
    print(" - Cliente 3 (C): (35, 45) -> COMPRA (1)")
    print("\nPunto Nuevo a evaluar: (30, 40)\n")

    p_nuevo = np.array([30, 40])
    a = np.array([20, 30])
    b = np.array([40, 50])
    c = np.array([35, 45])

    # 1. Cálculo de Distancias Euclidianas
    d_a = np.sqrt(np.sum((p_nuevo - a)**2))
    d_b = np.sqrt(np.sum((p_nuevo - b)**2))
    d_c = np.sqrt(np.sum((p_nuevo - c)**2))

    print("[DESARROLLO PASO A PASO]")
    print(f"1. Distancia a Cliente A (20, 30): sqrt((30-20)^2 + (40-30)^2) = sqrt(200) ≈ {d_a:.2f}")
    print(f"2. Distancia a Cliente B (40, 50): sqrt((30-40)^2 + (40-50)^2) = sqrt(200) ≈ {d_b:.2f}")
    print(f"3. Distancia a Cliente C (35, 45): sqrt((30-35)^2 + (40-45)^2) = sqrt(50)  ≈ {d_c:.2f}\n")

    print("[RESULTADOS Y CLASIFICACIÓN]")
    print("Vecino más cercano: Cliente C (Distancia ≈ 7.07)")
    print("2. Para K = 1:")
    print("   -> El vecino más cercano es C (COMPRA). Clasificación: COMPRA (1)")
    print("3. Para K = 3:")
    print("   -> Los 3 vecinos son [C: COMPRA, A: NO COMPRA, B: NO COMPRA/COMPRA (empate en dist. A y B)]")
    print("   -> Por mayoría (2 votos COMPRA de B y C vs 1 NO COMPRA de A). Clasificación: COMPRA (1)")
    print("   -> La decisión final se mantiene en COMPRA.")


def taller_laboratorio_knn():
    print("\n" + "="*60)
    print("   TALLER DE LABORATORIO: CLASIFICADOR UNIVERSAL KNN")
    print("="*60)

    # 1. Dataset Ampliado (10 puntos, 3 características: [Edad, Salario_Miles, Num_Hijos])
    X_entrenamiento = np.array([
        [20, 30, 0],
        [40, 50, 2],
        [35, 45, 1],
        [22, 25, 0],
        [48, 80, 3],
        [50, 70, 2],
        [25, 35, 0],
        [30, 40, 1],
        [55, 90, 2],
        [23, 28, 0]
    ])

    # Etiquetas: 0 = NO COMPRA, 1 = COMPRA
    Y_entrenamiento = np.array([0, 1, 1, 0, 1, 1, 0, 0, 1, 0])

    nuevo_cliente = np.array([[32, 42, 1]])
    print(f"Nuevo cliente evaluado: {nuevo_cliente[0]} ([Edad, Salario, Hijos])\n")

    # 2. Experimento con K=1
    knn1 = KNeighborsClassifier(n_neighbors=1)
    knn1.fit(X_entrenamiento, Y_entrenamiento)
    pred_k1 = knn1.predict(nuevo_cliente)[0]
    clase_k1 = "COMPRA" if pred_k1 == 1 else "NO COMPRA"
    print(f" -> Predicción con K=1: {pred_k1} ({clase_k1})")

    # 3. Experimento con K=5
    knn5 = KNeighborsClassifier(n_neighbors=5)
    knn5.fit(X_entrenamiento, Y_entrenamiento)
    pred_k5 = knn5.predict(nuevo_cliente)[0]
    clase_k5 = "COMPRA" if pred_k5 == 1 else "NO COMPRA"
    print(f" -> Predicción con K=5: {pred_k5} ({clase_k5})\n")

    print("-" * 60)
    print("[DISCUSIÓN: LA MALDICIÓN DE LA DIMENSIONALIDAD]")
    print("Si pasamos de 3 a 1,000 columnas (ej. píxeles de una imagen):")
    print(" 1. Los puntos se vuelven extremadamente equidistantes en espacios")
    print("    de alta dimensión (la diferencia entre el vecino más cercano")
    print("    y el más lejano tiende a cero).")
    print(" 2. El costo computacional crece drásticamente al calcular raíces")
    print("    cuadradas en 1,000 dimensiones para cada punto memorizado.")


def ejecutar_consola():
    """Punto de entrada principal llamado desde main.py"""
    while True:
        print("\n" + "*"*60)
        print("   SESIÓN 9: ALGORITMO KNN (K-NEAREST NEIGHBORS)")
        print("*"*60)
        print("1. Taller Analítico (Votación Espacial y Distancia Euclidiana)")
        print("2. Taller de Laboratorio (Clasificador Universal 3D)")
        print("0. Volver al Menú Principal")

        opcion = input("\nSeleccione una opción (0-2): ").strip()

        if opcion == '1':
            taller_analitico_knn()
            input("\nPresione ENTER para continuar...")
        elif opcion == '2':
            taller_laboratorio_knn()
            input("\nPresione ENTER para continuar...")
        elif opcion == '0':
            break
        else:
            print("\nOpción inválida. Intente de nuevo.")


if __name__ == "__main__":
    ejecutar_consola()