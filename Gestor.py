# Lista para almacenar las calificaciones
calificaciones = []

# Función para registrar calificaciones
def registrar_calificacion():
    print("=== Registro de Calificaciones ===")
    
    # Solicitar datos al usuario
    nombre_estudiante = input("Nombre del estudiante: ")
    materia = input("Materia: ")
    
    # Validar la calificación
    while True:
        try:
            calificacion = float(input("Calificación (0-10): "))
            if 0 <= calificacion <= 10:
                break
            else:
                print("La calificación debe estar entre 0 y 10. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Introduce un número.")
    
    observaciones = input("Observaciones (opcional): ")
    
    # Guardar la calificación en la lista
    calificaciones.append({
        "estudiante": nombre_estudiante,
        "materia": materia,
        "calificacion": calificacion,
        "observaciones": observaciones
    })
    
    print("¡Calificación registrada exitosamente!\n")

# Función para mostrar las calificaciones registradas
def mostrar_calificaciones():
    print("=== Calificaciones Registradas ===")
    if not calificaciones:
        print("No hay calificaciones registradas.")
    else:
        for i, calificacion in enumerate(calificaciones, 1):
            print(f"{i}. Estudiante: {calificacion['estudiante']}")
            print(f"   Materia: {calificacion['materia']}")
            print(f"   Calificación: {calificacion['calificacion']}")
            print(f"   Observaciones: {calificacion['observaciones']}\n")

# Menú principal
def menu():
    while True:
        print("=== Menú Principal ===")
        print("1. Registrar Calificación")
        print("2. Mostrar Calificaciones")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            registrar_calificacion()
        elif opcion == "2":
            mostrar_calificaciones()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.\n")

# Ejecutar el menú
if __name__ == "__main__":
    menu()


    # Daniem


    asdfasfdasdfafadfasfdasdfasfdas
    Falsedfasfdasdfas
    defdf
    assertdfa
    FileNotFoundErroras
    