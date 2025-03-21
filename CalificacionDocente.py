#Como docente, quiero registrar calificaciones para llevar un control del rendimiento de los estudiantes.

# Diccionario para almacenar calificaciones de estudiantes
calificaciones_estudiantes = {}

# Función para registrar calificaciones
def registrar_calificacion():
    estudiante = input("Nombre del estudiante: ")
    materia = input("Materia: ")
    nota = float(input("Calificación: "))
    
    if estudiante not in calificaciones_estudiantes:
        calificaciones_estudiantes[estudiante] = {}
    
    calificaciones_estudiantes[estudiante][materia] = nota
    print(f"Calificación registrada: {estudiante} - {materia}: {nota}")

# Llamar a la función
registrar_calificacion()

#DVR ESTA HU CUMPLE YA QUE SE PUEDE REGISTRAR LAS CALIFICACIONES DE LOS ESTUDIANTES.