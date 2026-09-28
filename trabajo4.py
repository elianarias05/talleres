# trabajo4.py - Inferencia Difusa Modelo Mamdani (Consola)

def taller_analitico_mamdani():
    print("\n" + "="*60)
    print("   TALLER ANALÍTICO: PROPAGACIÓN DE FUERZA (MAMDANI)")
    print("="*60)
    print("Regla R1: SI (Rentabilidad ALTA O Impacto_Social ALTO) Y (Riesgo BAJO)")
    print("          ENTONCES (Aprobación SEGURA)\n")
    
    grados = {
        "rentabilidad_alta": 0.6,
        "impacto_alto": 0.2,
        "riesgo_bajo": 0.4
    }
    
    # 1. Evaluación del OR entre Rentabilidad e Impacto
    fuerza_or = max(grados["rentabilidad_alta"], grados["impacto_alto"])
    
    # 2. Evaluación del AND con Riesgo Bajo
    fuerza_r1 = min(fuerza_or, grados["riesgo_bajo"])
    
    print("[DESARROLLO PASO A PASO]")
    print(f"1. Evaluación del OR: max({grados['rentabilidad_alta']}, {grados['impacto_alto']}) = {fuerza_or}")
    print(f"2. Evaluación del AND: min({fuerza_or}, {grados['riesgo_bajo']}) = {fuerza_r1}\n")
    
    print("[RESULTADOS]")
    print(f"-> Fuerza de activación de la premisa: {fuerza_r1}")
    print(f"-> Altura de truncamiento para 'Aprobación SEGURA' (Eje Y): {fuerza_r1}")


def taller_laboratorio_rrhh():
    print("\n" + "="*60)
    print("   TALLER DE LABORATORIO: MOTOR LÓGICO DE RECURSOS HUMANOS")
    print("="*60)
    
    # 1. Grados de membresía del empleado
    grados_empleado = {
        "desempeno_pobre": 0.1,
        "desempeno_promedio": 0.5,
        "desempeno_excelente": 0.85,
        "antiguedad_corta": 0.2,
        "antiguedad_larga": 0.6
    }
    
    print("Métricas de entrada (Fuzzificadas):")
    for k, v in grados_empleado.items():
        print(f" - {k}: {v}")
    print("\nReglas de Inferencia Aplicadas:")
    
    # R1: SI Desempeño es Pobre O Antigüedad es Corta -> Bono Bajo
    r1_bono_bajo = max(grados_empleado["desempeno_pobre"], grados_empleado["antiguedad_corta"])
    print(f" R1 (Bono Bajo)  = max(0.1, 0.2) -> {r1_bono_bajo:.2f}")
    
    # R2: SI Desempeño es Promedio -> Bono Medio
    r2_bono_medio = grados_empleado["desempeno_promedio"]
    print(f" R2 (Bono Medio) = {r2_bono_medio:.2f}")
    
    # R3: SI Desempeño es Excelente Y Antigüedad es Larga -> Bono Alto
    r3_bono_alto = min(grados_empleado["desempeno_excelente"], grados_empleado["antiguedad_larga"])
    print(f" R3 (Bono Alto)  = min(0.85, 0.6) -> {r3_bono_alto:.2f}")
    
    print("\n[RESULTADO DE ACTIVACIÓN POR CATEGORÍA]")
    activaciones = {
        "Bono Bajo": r1_bono_bajo,
        "Bono Medio": r2_bono_medio,
        "Bono Alto": r3_bono_alto
    }
    for bono, fuerza in activaciones.items():
        print(f" - {bono}: {fuerza:.2f} ({fuerza*100:.0f}%)")
        
    # 4. Demostración teórica de Agregación Mamdani (MAX T-Conorma)
    print("\n" + "-"*60)
    print("PREGUNTA TEÓRICA - AGREGACIÓN DE MAMDANI:")
    print("Si dos reglas concluyen 'Bono Alto' con fuerzas de 0.4 y 0.7:")
    
    fuerza_regla_a = 0.4
    fuerza_regla_b = 0.7
    fuerza_final_agregada = max(fuerza_regla_a, fuerza_regla_b)
    
    print("Código ejecutado: fuerza_final = max(0.4, 0.7)")
    print(f"Fuerza unificada final para 'Bono Alto': {fuerza_final_agregada}")


def ejecutar_consola():
    """Punto de entrada principal llamado desde main.py"""
    while True:
        print("\n" + "*"*60)
        print("   TRABAJO 4: INFERENCIA DIFUSA (MODELO MANDANI)")
        print("*"*60)
        print("1. Taller Analítico (Propagación de Fuerza)")
        print("2. Taller de Laboratorio (Motor Lógico de RRHH)")
        print("0. Volver al Menú Principal")

        opcion = input("\nSeleccione una opción (0-2): ").strip()

        if opcion == '1':
            taller_analitico_mamdani()
            input("\nPresione ENTER para continuar...")
        elif opcion == '2':
            taller_laboratorio_rrhh()
            input("\nPresione ENTER para continuar...")
        elif opcion == '0':
            break
        else:
            print("\nOpción inválida. Intente de nuevo.")


if __name__ == "__main__":
    ejecutar_consola()