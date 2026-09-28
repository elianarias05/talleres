# trabajo10.py - Support Vector Machine (SVM) (Consola)
import numpy as np
from sklearn.svm import SVC

def taller_analitico_svm():
    print("\n" + "="*60)
    print("   TALLER ANALÍTICO: DIBUJANDO EL MARGEN (SVM)")
    print("="*60)
    print("Dataset Evaluado en Plano Cartesiano:")
    print(" - Clase A (0): (2,2), (3,3), (4,2)")
    print(" - Clase B (1): (6,6), (7,8), (8,7)\n")

    X = np.array([[2, 2], [3, 3], [4, 2], [6, 6], [7, 8], [8, 7]])
    Y = np.array([0, 0, 0, 1, 1, 1])

    modelo_svm = SVC(kernel='linear')
    modelo_svm.fit(X, Y)

    vectores = modelo_svm.support_vectors_

    print("[DESARROLLO Y VECTORES DE SOPORTE]")
    print("1. Línea Óptima y Espacio de 'Calle':")
    print("   -> El hiperplano de separación pasa de forma totalmente equidistante")
    print("      entre la frontera de ambas clases (entre x+y=6 y x+y=12).")
    print("2. Vectores de Soporte Identificados por la IA:")
    for v in vectores:
        print(f"   * Punto: ({v[0]:.0f}, {v[1]:.0f})")

    print("\n3. Inclusión de nuevo punto en (1,1) [Clase A]:")
    print("   -> ¿Cambia la línea de separación? NO.")
    print("   -> Justificación Teórica: El punto (1,1) está alejado de la frontera")
    print("      y dentro de la zona de confort de la Clase A. El hiperplano de SVM")
    print("      depende ÚNICAMENTE de los Vectores de Soporte que están al borde")
    print("      del margen, por lo que los puntos lejanos no alteran la frontera.")


def taller_laboratorio_svm():
    print("\n" + "="*60)
    print("   TALLER DE LABORATORIO: FRONTERAS NO LINEALES Y KERNEL TRICK")
    print("="*60)

    # 1. Dataset Original
    X_base = [[2, 2], [3, 3], [4, 2], [6, 6], [7, 8], [8, 7]]
    Y_base = [0, 0, 0, 1, 1, 1]

    print("--- 1. Pruebas con Kernel Lineal Original ---")
    modelo_lin = SVC(kernel='linear')
    modelo_lin.fit(X_base, Y_base)
    print("Vectores de Soporte (Lineal):")
    print(modelo_lin.support_vectors_)

    punto_eval = np.array([[5, 4]])
    pred_lin = modelo_lin.predict(punto_eval)[0]
    print(f"Predicción para el punto [5, 4]: Clase {pred_lin}\n")

    # 2. Agregar el punto conflictivo [5, 5] con etiqueta 0
    print("--- 2. Alteración del Dataset (Agregando [5, 5] de Clase A) ---")
    X_mod = np.array(X_base + [[5, 5]])
    Y_mod = np.array(Y_base + [0])

    print("Entrenando modelo con Kernel Lineal en datos complejos...")
    modelo_lin_mod = SVC(kernel='linear')
    modelo_lin_mod.fit(X_mod, Y_mod)
    print(f"Predicción para [5, 4] (Lineal Modificado): Clase {modelo_lin_mod.predict(punto_eval)[0]}")

    print("\nEntrenando modelo con Kernel RBF (Radial Basis Function)...")
    modelo_rbf = SVC(kernel='rbf')
    modelo_rbf.fit(X_mod, Y_mod)
    print(f"Predicción para [5, 4] (RBF Kernel Trick): Clase {modelo_rbf.predict(punto_eval)[0]}\n")

    print("-" * 60)
    print("[REFLEXIÓN: APLICACIONES EN EL MUNDO REAL]")
    print(" - Escenario Real: Diagnóstico médico (tumores cancerígenos rodeados")
    print("   de tejido sano) o Reconocimiento Facial (diferenciación de rasgos")
    print("   no lineales con iluminación/ángulos dinámicos).")
    print(" - Conclusión: El 'Kernel Trick' (RBF) proyecta los datos a dimensiones")
    print("   superiores para trazar fronteras de decisión curvas altamente complejas.")


def ejecutar_consola():
    """Punto de entrada principal llamado desde main.py"""
    while True:
        print("\n" + "*"*60)
        print("   SESIÓN 10: ALGORITMO SVM (SUPPORT VECTOR MACHINE)")
        print("*"*60)
        print("1. Taller Analítico (Dibujando el Margen y Vectores de Soporte)")
        print("2. Taller de Laboratorio (Fronteras No Lineales y Kernel RBF)")
        print("0. Volver al Menú Principal")

        opcion = input("\nSeleccione una opción (0-2): ").strip()

        if opcion == '1':
            taller_analitico_svm()
            input("\nPresione ENTER para continuar...")
        elif opcion == '2':
            taller_laboratorio_svm()
            input("\nPresione ENTER para continuar...")
        elif opcion == '0':
            break
        else:
            print("\nOpción inválida. Intente de nuevo.")


if __name__ == "__main__":
    ejecutar_consola()