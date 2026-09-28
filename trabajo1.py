# trabajo1.py - Evaluación Crediticia y Diagnóstico de Servidores IT (Consola)

def evaluacion_crediticia():
    print("\n" + "="*50)
    print("      MÓDULO 1: EVALUACIÓN DE CRÉDITO")
    print("="*50)
    
    try:
        ingresos = float(input("Ingrese los ingresos mensuales ($): "))
        historial = input("¿Tiene buen historial crediticio? (s/n): ").strip().lower()
        monto_solicitado = float(input("Ingrese el monto del préstamo solicitado ($): "))
        
        # Lógica de evaluación crediticia
        if ingresos >= 3000000 and historial == 's':
            if monto_solicitado <= ingresos * 10:
                resultado = "CRÉDITO APROBADO: Cumple con los criterios financieros y de riesgo."
            else:
                resultado = "CRÉDITO RECHAZADO: El monto solicitado supera el límite de endeudamiento."
        elif ingresos >= 1500000 and historial == 's':
            if monto_solicitado <= ingresos * 5:
                resultado = "CRÉDITO APROBADO CON CONDICIONES: Requiere un fiador/garantía."
            else:
                resultado = "CRÉDITO RECHAZADO: Excede la capacidad de pago para este nivel de ingresos."
        else:
            resultado = "CRÉDITO RECHAZADO: Historial crediticio insatisfactorio o ingresos insuficientes."
            
        print("\n[RESULTADO EVALUACIÓN]")
        print(f"Status: {resultado}")
        
    except ValueError:
        print("\n[ERROR] Por favor, ingrese valores numéricos válidos para los montos.")

def diagnostico_servidores():
    print("\n" + "="*50)
    print("      MÓDULO 2: DIAGNÓSTICO DE SERVIDORES IT")
    print("="*50)
    
    try:
        cpu_usage = float(input("Ingrese el uso de CPU (%): "))
        ram_usage = float(input("Ingrese el uso de Memoria RAM (%): "))
        disco_usage = float(input("Ingrese el uso de Disco (%): "))
        
        print("\n[DIAGNÓSTICO DEL SISTEMA]")
        
        # Evaluación de métricas
        alertas = []
        if cpu_usage > 85:
            alertas.append("ALERTA CRÍTICA: Sobrecarga en la CPU. Considere finalizar procesos no esenciales.")
        if ram_usage > 90:
            alertas.append("ALERTA CRÍTICA: Memoria RAM casi agotada. Riesgo de cuelgue por swap.")
        if disco_usage > 95:
            alertas.append("ALERTA CRÍTICA: Espacio en disco insuficiente. Limpie archivos temporales.")
            
        if not alertas:
            print("ESTADO: Servidor Operativo en parámetros normales.")
        else:
            print("ESTADO: Se detectaron anomalías:")
            for alerta in alertas:
                print(f" - {alerta}")
                
    except ValueError:
        print("\n[ERROR] Ingrese valores porcentuales válidos (0 a 100).")

def ejecutar_consola():
    """Punto de entrada principal llamado desde main.py"""
    while True:
        print("\n" + "*"*50)
        print("      TRABAJO 1: EVALUACIÓN CREDITICIA Y DIAGNÓSTICO IT")
        print("*"*50)
        print("1. Ejecutar Evaluación Crediticia")
        print("2. Ejecutar Diagnóstico de Servidores IT")
        print("0. Volver al Menú Principal")
        
        opcion = input("\nSeleccione una opción (0-2): ").strip()
        
        if opcion == '1':
            evaluacion_crediticia()
            input("\nPresione ENTER para continuar...")
        elif opcion == '2':
            diagnostico_servidores()
            input("\nPresione ENTER para continuar...")
        elif opcion == '0':
            break
        else:
            print("\nOpción inválida. Intente de nuevo.")
    
if __name__ == "__main__":
    ejecutar_consola()