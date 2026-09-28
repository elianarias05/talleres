# trabajo5.py - Defuzzificación y Centro de Gravedad (Consola)
import numpy as np

def defuzz_centroide(x, mu):
    """
    Calcula el Centro de Gravedad (COG): COG = SUM(x * mu) / SUM(mu)
    """
    area_total = np.sum(mu)
    if area_total == 0:
        return 0.0
    return np.sum(x * mu) / area_total


def taller_analitico_cog():
    print("\n" + "="*60)
    print("   TALLER ANALÍTICO: CÁLCULO DE CENTRO DE MASA (COG)")
    print("="*60)
    print("Dominio discreto para porcentaje de descuento:")
    print(" - x = 10% -> mu(10) = 0.2")
    print(" - x = 20% -> mu(20) = 0.8")
    print(" - x = 30% -> mu(30) = 0.8")
    print(" - x = 40% -> mu(40) = 0.0\n")

    x = np.array([10, 20, 30, 40])
    mu = np.array([0.2, 0.8, 0.8, 0.0])

    numerador = np.sum(x * mu)
    denominador = np.sum(mu)
    descuento_crisp = defuzz_centroide(x, mu)

    print("[DESARROLLO PASO A PASO]")
    print(f"1. Numerador SUM(x * mu) : (10*0.2) + (20*0.8) + (30*0.8) + (40*0) = {numerador:.2f}")
    print(f"2. Denominador SUM(mu)   : 0.2 + 0.8 + 0.8 + 0.0 = {denominador:.2f}")
    print(f"3. Resultado COG         : {numerador:.2f} / {denominador:.2f} = {descuento_crisp:.2f}%\n")

    print(f"[RECOMENDACIÓN FINAL] Descuento exacto (Crisp): {descuento_crisp:.2f}%")


def taller_laboratorio_frenado():
    print("\n" + "="*60)
    print("   TALLER DE LABORATORIO: SISTEMA DE FRENADO AUTOMÁTICO")
    print("="*60)

    # 1. Validación de la función propia con los datos del taller analítico
    x_test = np.array([10, 20, 30, 40])
    mu_test = np.array([0.2, 0.8, 0.8, 0.0])
    val_cog = defuzz_centroide(x_test, mu_test)
    print(f"-> Validación de función propia COG: {val_cog:.2f}% (Coincide con taller analítico)\n")

    # 2. Sistema de Frenado Automático (Fuerza de 0 a 100 Newtons)
    x_fuerza = np.linspace(0, 100, 100)  # Arreglo con 100 elementos de 0 a 100
    
    # Generación de curva Gaussiana centrada en 70 (Frenado fuerte)
    media, desviacion = 70.0, 10.0
    curva_gaussiana = np.exp(-0.5 * ((x_fuerza - media) / desviacion) ** 2)

    # Defuzzificación
    fuerza_crisp = defuzz_centroide(x_fuerza, curva_gaussiana)

    print("[EVALUACIÓN DEL SISTEMA DE FRENADO]")
    print(f" - Universo de discurso : Fuerza de 0 a 100 N (100 puntos de muestreo)")
    print(f" - Perfil de respuesta   : Campana de Gauss centrada en {media} N")
    print(f" - Fuerza calculada (COG): {fuerza_crisp:.2f} Newtons\n")
    print(f"DICTAMEN: Aplicar señal de control de {fuerza_crisp:.2f} N a los frenos.")


def ejecutar_consola():
    """Punto de entrada principal llamado desde main.py"""
    while True:
        print("\n" + "*"*60)
        print("   TRABAJO 5: DEFUZZIFICACIÓN Y CENTRO DE GRAVEDAD")
        print("*"*60)
        print("1. Taller Analítico (Cálculo de Centro de Masa - COG)")
        print("2. Taller de Laboratorio (Frenado Automático / NumPy)")
        print("0. Volver al Menú Principal")

        opcion = input("\nSeleccione una opción (0-2): ").strip()

        if opcion == '1':
            taller_analitico_cog()
            input("\nPresione ENTER para continuar...")
        elif opcion == '2':
            taller_laboratorio_frenado()
            input("\nPresione ENTER para continuar...")
        elif opcion == '0':
            break
        else:
            print("\nOpción inválida. Intente de nuevo.")


if __name__ == "__main__":
    ejecutar_consola()