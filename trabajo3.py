# trabajo3.py - Sistemas Expertos y Lógica Difusa (Consola)

def membresia_triangular(x, a, b, c):
    """
    Calcula el grado de membresía mu(x) para una función triangular.
    Parámetros:
      a: Límite inferior (mu = 0)
      b: Pico máximo (mu = 1)
      c: Límite superior (mu = 0)
    """
    if x <= a or x >= c:
        return 0.0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x < c:
        return (c - x) / (c - b)
    return 0.0


def taller_analitico_temperatura():
    print("\n" + "="*60)
    print("   TALLER ANALÍTICO 1: EVALUACIÓN DE TEMPERATURA AGRADABLE")
    print("="*60)
    print("Conjunto Difuso: 'Temperatura Agradable'")
    print("Vértices: a = 18°C, b = 22°C, c = 26°C\n")

    a, b, c = 18.0, 22.0, 26.0

    # 1. Evaluación para x = 20°C
    mu_20 = membresia_triangular(20, a, b, c)
    print(f"1. Para x = 20°C:")
    print(f"   Fórmula aplicada: (20 - 18) / (22 - 18) = 2 / 4")
    print(f"   Grado de membresía μ(20) = {mu_20:.2f} ({mu_20 * 100:.0f}%)\n")

    # 2. Evaluación para x = 25°C
    mu_25 = membresia_triangular(25, a, b, c)
    print(f"2. Para x = 25°C:")
    print(f"   Fórmula aplicada: (26 - 25) / (26 - 22) = 1 / 4")
    print(f"   Grado de membresía μ(25) = {mu_25:.2f} ({mu_25 * 100:.0f}%)\n")

    # 3. Interpretación
    print("3. Interpretación de los resultados:")
    print("   - A 20°C, el ambiente está en un 50% dentro del rango 'Agradable',")
    print("     en camino a su punto óptimo (22°C).")
    print("   - A 25°C, el ambiente está a solo un 25% de ser 'Agradable',")
    print("     acercándose al límite superior (26°C) donde deja de serlo.")


def taller_laboratorio_conductores():
    print("\n" + "="*60)
    print("   TALLER DE LABORATORIO: EVALUACIÓN DIFUSA DE CONDUCTORES")
    print("="*60)

    # Definición de los conjuntos difusos (a, b, c)
    conjuntos = {
        "Novato": (0, 0, 5),
        "Intermedio": (2, 5, 8),
        "Experto": (5, 10, 20)
    }

    conductores = [3, 6, 12]
    print(f"Conductores a evaluar (años de experiencia): {conductores}\n")

    for i, exp in enumerate(conductores, 1):
        print(f"--- Conductor #{i} ({exp} años de experiencia) ---")
        
        grados = {}
        for categoria, (a, b, c) in conjuntos.items():
            # Caso especial para vértices iniciales como Novato (0,0,5)
            if a == b and exp == a:
                mu = 1.0
            else:
                mu = membresia_triangular(exp, a, b, c)
            
            grados[categoria] = mu
            print(f" - Membresía a {categoria}: {mu:.2f} ({mu * 100:.1f}%)")
        
        # Clasificación con el mayor grado de verdad
        mejor_categoria = max(grados, key=grados.get)
        max_grado = grados[mejor_categoria]
        
        print(f" >> Categoría predominante: {mejor_categoria.upper()} "
              f"con un grado de {max_grado:.2f}\n")


def ejecutar_consola():
    """Punto de entrada principal llamado desde main.py"""
    while True:
        print("\n" + "*"*60)
        print("   TRABAJO 3: INCERTIDUMBRE Y LÓGICA DIFUSA")
        print("*"*60)
        print("1. Taller Analítico 1 (Cálculo de Grados de Verdad - Temperatura)")
        print("2. Taller de Laboratorio (Evaluación de Conductores)")
        print("0. Volver al Menú Principal")

        opcion = input("\nSeleccione una opción (0-2): ").strip()

        if opcion == '1':
            taller_analitico_temperatura()
            input("\nPresione ENTER para continuar...")
        elif opcion == '2':
            taller_laboratorio_conductores()
            input("\nPresione ENTER para continuar...")
        elif opcion == '0':
            break
        else:
            print("\nOpción inválida. Intente de nuevo.")


if __name__ == "__main__":
    ejecutar_consola()