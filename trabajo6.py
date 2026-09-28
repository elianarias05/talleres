# trabajo6.py - Árboles de Decisión y Machine Learning (Consola)
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_text

def taller_analitico_entropia():
    print("\n" + "="*60)
    print("   TALLER ANALÍTICO: EL ALGORITMO EN PAPEL")
    print("="*60)
    print("Dataset: 6 clientes (3 compraron seguro, 3 no compraron).\n")
    print("Evaluación de Preguntas Candidatas:")
    print(" - Pregunta A (¿Edad > 30?):")
    print("     * Izquierda: [2 compraron, 2 no] -> Entropía máxima (alta impureza)")
    print("     * Derecha:   [1 compró, 1 no]    -> Entropía máxima (alta impureza)")
    print(" - Pregunta B (¿Tiene Auto?):")
    print("     * Izquierda: [3 compraron, 0 no] -> Entropía 0 (grupo puro)")
    print("     * Derecha:   [0 compraron, 3 no] -> Entropía 0 (grupo puro)\n")

    print("[RESPUESTAS ANALÍTICAS]")
    print("1. Pregunta con mayor Ganancia de Información:")
    print("   -> La Pregunta B ('¿Tiene Auto?') proporciona la mayor Ganancia de")
    print("      Información, ya que separa el dataset en nodos totalmente puros")
    print("      (reduce la entropía a 0).\n")
    print("2. Regla Lógica Aprendida (SI... ENTONCES):")
    print("   -> SI Tiene_Auto == SI ENTONCES Compra_Seguro = SI")
    print("   -> SI Tiene_Auto == NO ENTONCES Compra_Seguro = NO")


def taller_laboratorio_marketing():
    print("\n" + "="*60)
    print("   TALLER DE LABORATORIO: EL EXPERTO AUTOMÁTICO (MARKETING)")
    print("="*60)

    # 1. Dataset de Entrenamiento (10 filas)
    # Columnas X: [Edad, Horas_Online, Compras_Previas]
    X = np.array([
        [19, 5, 0],
        [22, 8, 1],
        [45, 1, 0],
        [50, 2, 4],
        [25, 6, 2],
        [38, 7, 5],
        [60, 1, 1],
        [28, 4, 0],
        [31, 9, 3],
        [52, 2, 0]
    ])

    # Etiquetas Y: [1: Hizo clic en anuncio, 0: Lo ignoró]
    Y = np.array([1, 1, 0, 1, 1, 1, 0, 0, 1, 0])

    nombres_caracteristicas = ["Edad", "Horas_Online", "Compras_Previas"]

    # 2. Entrenamiento del Árbol de Decisión
    arbol = DecisionTreeClassifier(max_depth=3, random_state=42)
    arbol.fit(X, Y)

    # 3. Exportar las reglas en formato de texto
    reglas_texto = export_text(arbol, feature_names=nombres_caracteristicas)

    print("Base de Reglas generada automáticamente por el Árbol de Decisión:\n")
    print(reglas_texto)

    print("-" * 60)
    print("[DISCUSIÓN Y ANÁLISIS COMERCIAL]")
    print(" - Patrón detectado: Los usuarios más jóvenes o con más horas en línea y")
    print("   compras previas tienen una mayor probabilidad de hacer clic.")
    print(" - Conclusión: El Machine Learning permite automatizar la construcción")
    print("   de la Base de Conocimientos, superando la 'barrera de extracción' del")
    print("   experto humano mediante el análisis directo de datos históricos.")


def ejecutar_consola():
    """Punto de entrada principal llamado desde main.py"""
    while True:
        print("\n" + "*"*60)
        print("   TRABAJO 6: ÁRBOLES DE DECISIÓN Y MACHINE LEARNING")
        print("*"*60)
        print("1. Taller Analítico (Entropía y Ganancia de Información)")
        print("2. Taller de Laboratorio (Entrenamiento e Inferencia de Marketing)")
        print("0. Volver al Menú Principal")

        opcion = input("\nSeleccione una opción (0-2): ").strip()

        if opcion == '1':
            taller_analitico_entropia()
            input("\nPresione ENTER para continuar...")
        elif opcion == '2':
            taller_laboratorio_marketing()
            input("\nPresione ENTER para continuar...")
        elif opcion == '0':
            break
        else:
            print("\nOpción inválida. Intente de nuevo.")


if __name__ == "__main__":
    ejecutar_consola()