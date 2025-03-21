#Como estudiante, quiero ver mis calificaciones para saber cómo voy en cada materia.

# Diccionario para guardar las calificaciones de los estudiantes
calificaciones_estudiantes = {}

# Función para registrar calificaciones
def registrar_calificacion():
    estudiante = input("Nombre del estudiante: ")
    
    while True:
        materia = input("Materia (o escribe 'fin' para terminar): ")
        if materia.lower() == "fin":
            break
        nota = float(input(f"Calificación en {materia}: "))
        
        if estudiante not in calificaciones_estudiantes:
            calificaciones_estudiantes[estudiante] = {}
        
        calificaciones_estudiantes[estudiante][materia] = nota
        print(f"Calificación registrada: {estudiante} - {materia}: {nota}")

# Función para consultar calificaciones
def consultar_calificaciones():
    estudiante = input("Nombre del estudiante: ")
    
    if estudiante in calificaciones_estudiantes:
        print(f"\nCalificaciones de {estudiante}:")
        for materia, nota in calificaciones_estudiantes[estudiante].items():
            print(f"{materia}: {nota}")
    else:
        print("Estudiante no encontrado.")

# Menú para interactuar con el sistema
def menu():
    while True:
        print("\n--- Menú de Calificaciones ---")
        print("1. Registrar calificaciones")
        print("2. Consultar calificaciones")
        print("3. Salir")
        opcion = input("Selecciona una opción (1-3): ")

        if opcion == "1":
            registrar_calificacion()
        elif opcion == "2":
            consultar_calificaciones()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()


#DVR ESTA HU CUMPLE YA QUE SE PUEDE REGISTRAR Y CONSULTAR LAS CALIFICACIONES DE LOS ESTUDIANTES.    