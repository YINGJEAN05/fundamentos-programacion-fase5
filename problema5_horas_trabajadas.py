# Universidad Nacional Abierta y a Distancia - UNAD
# Escuela de Ciencias Básicas, Tecnología e Ingeniería - ECBTI
# Programa: Ingeniería de Sistemas
# Curso: Fundamentos de Programación
# Código: 213022
# Fase 5 - Evaluación Final POA
# Estudiante: Jean Paul Cabrera Narváez
# Grupo: 213022_727
# Problema 5: Horas trabajadas semanalmente

def calcular_jornada(horas):
    """
    Función que calcula el total de horas semanales de un recurso
    y clasifica su jornada laboral.
    """
    total_horas = sum(horas)

    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return total_horas, clasificacion


# Matriz de datos:
# [Nombre del Recurso, Lunes, Martes, Miércoles, Jueves, Viernes]
recursos = [
    ["Andrés", 8, 8, 8, 8, 8],
    ["Camila", 9, 8, 9, 8, 9],
    ["Sofía", 7, 8, 7, 8, 7],
    ["Daniel", 10, 9, 8, 9, 8]
]


print("INFORME DE HORAS TRABAJADAS SEMANALMENTE")
print("-" * 55)
print("Recurso\t\tTotal Horas\tClasificación")
print("-" * 55)

for recurso in recursos:
    nombre = recurso[0]
    horas_semana = recurso[1:6]

    total, clasificacion = calcular_jornada(horas_semana)

    print(f"{nombre:<15}{total:<15}{clasificacion}")

print("-" * 55)
print("Proceso finalizado correctamente.")