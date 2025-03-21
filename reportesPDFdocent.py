#Como docente, quiero generar reportes en PDF para analizar el progreso de los estudiantes.

# Función para generar un reporte en PDF
def generar_reporte():
    estudiante = input("Nombre del estudiante: ")
    calificaciones = {
        "Matemáticas": 8.5,
        "Ciencias": 9.0,
        "Historia": 7.5
    }

    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas

    nombre_archivo = f"reporte_{estudiante}.pdf"
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.drawString(100, 750, f"Reporte de Calificaciones de {estudiante}")
    y = 700
    for materia, nota in calificaciones.items():
        c.drawString(100, y, f"{materia}: {nota}")
        y -= 20
    c.save()
    print(f"Reporte generado: {nombre_archivo}")

# Llamar a la función
generar_reporte()