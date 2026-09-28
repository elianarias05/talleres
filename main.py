import os
import trabajo1
import trabajo2
import trabajo3
import trabajo4
import trabajo5
import trabajo6
import trabajo9
import trabajo10
import trabajo11
import trabajo12

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    while True:
        limpiar_pantalla()
        print("=" * 60)
        print("         PORTAFOLIO ACADÉMICO DE PROYECTOS         ")
        print("=" * 60)
        print(" 1. Trabajo 1: Evaluación Crediticia y Diagnóstico IT")
        print(" 2. Trabajo 2: Motor de Inferencia (Vehículos y Fraude)")
        print(" 3. Trabajo 3: Lógica Difusa y Funciones de Membresía")
        print(" 4. Trabajo 4: Inferencia Difusa (Modelo Mamdani)")
        print(" 5. Trabajo 5: Defuzzificación y Centro de Gravedad")
        print(" 6. Trabajo 6: Árboles de Decisión y Machine Learning")
        print(" 7. Trabajo 9: Algoritmo KNN (K-Vecinos Más Cercanos)")
        print(" 8. Trabajo 10: Support Vector Machine (SVM)")
        print(" 9. Trabajo 11: Redes Neuronales (El Perceptrón)")
        print("10. Trabajo 12: Redes Neuronales Densas (MLP)")
        print(" 0. Salir")
        print("=" * 60)
        
        opcion = input("Seleccione una opción (0-10): ").strip()
        
        if opcion == '1':
            limpiar_pantalla()
            trabajo1.ejecutar_consola()
            input("\nPresione ENTER para volver al menú principal...")
        elif opcion == '2':
            limpiar_pantalla()
            trabajo2.ejecutar_consola()
            input("\nPresione ENTER para volver al menú principal...")
        elif opcion == '3':
            limpiar_pantalla()
            trabajo3.ejecutar_consola()
            input("\nPresione ENTER para volver al menú principal...")
        elif opcion == '4':
            limpiar_pantalla()
            trabajo4.ejecutar_consola()
            input("\nPresione ENTER para volver al menú principal...")
        elif opcion == '5':
            limpiar_pantalla()
            trabajo5.ejecutar_consola()
            input("\nPresione ENTER para volver al menú principal...")
        elif opcion == '6':
            limpiar_pantalla()
            trabajo6.ejecutar_consola()
            input("\nPresione ENTER para volver al menú principal...")
        elif opcion == '7':
            limpiar_pantalla()
            trabajo9.ejecutar_consola()
            input("\nPresione ENTER para volver al menú principal...")
        elif opcion == '8':
            limpiar_pantalla()
            trabajo10.ejecutar_consola()
            input("\nPresione ENTER para volver al menú principal...")
        elif opcion == '9':
            limpiar_pantalla()
            trabajo11.ejecutar_consola()
            input("\nPresione ENTER para volver al menú principal...")
        elif opcion == '10':
            limpiar_pantalla()
            trabajo12.ejecutar_consola()
            input("\nPresione ENTER para volver al menú principal...")
        elif opcion == '0':
            print("\n¡Gracias por utilizar el sistema!")
            break
        else:
            print("\nOpción no válida. Intente de nuevo.")
            input("\nPresione ENTER para continuar...")

if __name__ == "__main__":
    mostrar_menu()