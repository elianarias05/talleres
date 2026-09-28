# trabajo2.py - Motor de Inferencia, Categorización de Vehículos y Detección de Fraude (Consola)

def motor_inferencia_adelante():
    print("\n" + "="*55)
    print("   MOTOR DE INFERENCIA: ENCADENAMIENTO HACIA ADELANTE")
    print("="*55)
    print("Indique con 's' (sí) o 'n' (no) las condiciones observadas:\n")
    
    fiebre = input("¿El paciente presenta fiebre? (s/n): ").strip().lower() == 's'
    tos = input("¿El paciente presenta tos seca? (s/n): ").strip().lower() == 's'
    fatiga = input("¿El paciente reporta fatiga/cansancio? (s/n): ").strip().lower() == 's'
    dificultad_respirar = input("¿Presenta dificultad para respirar? (s/n): ").strip().lower() == 's'
    
    hechos = set()
    if fiebre: hechos.add("fiebre")
    if tos: hechos.add("tos")
    if fatiga: hechos.add("fatiga")
    if dificultad_respirar: hechos.add("dificultad_respirar")
    
    # Base de reglas para inferencia
    inferencias = []
    
    # Regla 1: Fiebre + Tos -> Infección Respiratoria Básica
    if "fiebre" in hechos and "tos" in hechos:
        hechos.add("infeccion_respiratoria")
        inferencias.append("Infección respiratoria primaria")
        
    # Regla 2: Infección Respiratoria + Fatiga -> Cuadro Gripal Severo
    if "infeccion_respiratoria" in hechos and "fatiga" in hechos:
        hechos.add("cuadro_gripal_severo")
        inferencias.append("Cuadro gripal de nivel severo")
        
    # Regla 3: Cuadro Gripal Severo + Dificultad para respirar -> Neumonía / Caso Crítico
    if "cuadro_gripal_severo" in hechos and "dificultad_respirar" in hechos:
        hechos.add("posible_neumonia")
        inferencias.append("Alerta médica: Posible Neumonía o Síndrome Respiratorio Agudo")

    print("\n[RESULTADOS DEL PROCESAMIENTO]")
    print(f"Hechos iniciales detectados: {len(hechos)}")
    if inferencias:
        print("Deducciones generadas por el motor:")
        for idx, inf in enumerate(inferencias, 1):
            print(f" {idx}. {inf}")
    else:
        print("No se generaron deducciones de alto riesgo con los síntomas reportados.")


def categorizacion_vehiculos():
    print("\n" + "="*55)
    print("   CATEGORIZACIÓN Y PEAJE DE VEHÍCULOS")
    print("="*55)
    
    try:
        ejes = int(input("Ingrese el número de ejes del vehículo: "))
        peso_toneladas = float(input("Ingrese el peso bruto del vehículo (Toneladas): "))
        tipo_uso = input("¿El uso es Particular, Comercial o Pasajeros? (p/c/b): ").strip().lower()
        
        print("\n[CLASIFICACIÓN DEL VEHÍCULO]")
        if ejes == 2 and peso_toneladas <= 3.5:
            categoria = "Categoría I - Vehículos Livianos / Automóviles"
            tarifa = 10500
        elif ejes == 2 and peso_toneladas > 3.5:
            categoria = "Categoría II - Camiones Pequeños / Busetas"
            tarifa = 18000
        elif ejes == 3 or ejes == 4:
            categoria = f"Categoría III - Camiones/Buses de {ejes} ejes"
            tarifa = 29000
        elif ejes > 4:
            categoria = f"Categoría IV - Transporte Pesado de Carga Multi-eje ({ejes} ejes)"
            tarifa = 38000 + ((ejes - 4) * 5000)
        else:
            categoria = "Categoría Especial / Indeterminada"
            tarifa = 0
            
        print(f"Clasificación: {categoria}")
        print(f"Tarifa de Peaje Calculada: ${tarifa:,.0f} COP")
        
    except ValueError:
        print("\n[ERROR] Ingrese valores numéricos válidos para ejes y tonelaje.")


def deteccion_fraude():
    print("\n" + "="*55)
    print("   SISTEMA DE DETECCIÓN DE FRAUDE EN TRANSACCIONES")
    print("="*55)
    
    try:
        monto = float(input("Monto de la transacción ($): "))
        hora = int(input("Hora de la transacción (0 - 23): "))
        ub_habitual = input("¿La transacción es en la ciudad habitual? (s/n): ").strip().lower() == 's'
        ip_frecuente = input("¿La dirección IP / Dispositivo es frecuente? (s/n): ").strip().lower() == 's'
        
        score_riesgo = 0
        factores = []
        
        if monto > 5000000:
            score_riesgo += 40
            factores.append("Monto atípicamente alto (> $5'000.000)")
        elif monto > 2000000:
            score_riesgo += 20
            factores.append("Monto moderadamente alto")
            
        if hora >= 0 and hora <= 4:
            score_riesgo += 25
            factores.append("Horario de madrugada no habitual")
            
        if not ub_habitual:
            score_riesgo += 30
            factores.append("Ubicación geográfica inusual")
            
        if not ip_frecuente:
            score_riesgo += 20
            factores.append("Dispositivo o IP no reconocida")
            
        print("\n[EVALUACIÓN DE SEGURIDAD]")
        print(f"Puntaje total de riesgo: {score_riesgo} / 100")
        
        if score_riesgo >= 70:
            print("DICTAMEN: TRANSACCIÓN BLOQUEADA (Riesgo Alto de Fraude)")
        elif score_riesgo >= 40:
            print("DICTAMEN: REQUIERE VERIFICACIÓN OTP / SMS (Riesgo Medio)")
        else:
            print("DICTAMEN: TRANSACCIÓN APROBADA (Riesgo Bajo)")
            
        if factores:
            print("\nFactores de riesgo identificados:")
            for f in factores:
                print(f" - {f}")
                
    except ValueError:
        print("\n[ERROR] Ingrese datos numéricos válidos.")


def ejecutar_consola():
    """Punto de entrada principal llamado desde main.py"""
    while True:
        print("\n" + "*"*55)
        print("   TRABAJO 2: MOTOR DE INFERENCIA, VEHÍCULOS Y FRAUDE")
        print("*"*55)
        print("1. Motor de Inferencia (Encadenamiento Hacia Adelante)")
        print("2. Categorización y Peaje de Vehículos")
        print("3. Evaluación de Riesgo de Fraude")
        print("0. Volver al Menú Principal")
        
        opcion = input("\nSeleccione una opción (0-3): ").strip()
        
        if opcion == '1':
            motor_inferencia_adelante()
            input("\nPresione ENTER para continuar...")
        elif opcion == '2':
            categorizacion_vehiculos()
            input("\nPresione ENTER para continuar...")
        elif opcion == '3':
            deteccion_fraude()
            input("\nPresione ENTER para continuar...")
        elif opcion == '0':
            break
        else:
            print("\nOpción inválida. Intente de nuevo.")

if __name__ == "__main__":
    ejecutar_consola()