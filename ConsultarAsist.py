#Como estudiante, quiero ver mi asistencia para saber si tengo faltas.

# Datos de ejemplo: asistencia de un estudiante
asistencia = {
    "Matemáticas": ["2023-10-01: Presente", "2023-10-02: Ausente"],
    "Ciencias": ["2023-10-01: Presente", "2023-10-02: Presente"]
}

# Función para consultar asistencia
def consultar_asistencia():
    estudiante = input("Nombre del estudiante: ")
    print(f"\nAsistencia de {estudiante}:")
    for curso, registros in asistencia.items():
        print(f"{curso}:")
        for registro in registros:
            print(f"  - {registro}")

# Llamar a la función
consultar_asistencia()

#DVR ESTA HU CUMPLE YA QUE SE PUEDE CONSULTAR LA ASISTENCIA DE LOS ESTUDIANTES.