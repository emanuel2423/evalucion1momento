import openpyxl

estudiantes = {}


for i in range(3):
    nombre = input("Ingrese el nombre del estudiante {}: ".format(i + 1))
    nota = float(input(f"Ingrese la nota de {nombre}: "))
   
    estudiantes[nombre] = nota


promedio = sum(estudiantes.values()) / len(estudiantes)


libro = openpyxl.Workbook()
hoja = libro.active

hoja['A1'] = "Nombres"
hoja['B1'] = "Promedio"

hoja['B2'] = promedio

fila = 2
for nombre in estudiantes.keys():
    fila += 1
    hoja[f'A{fila}'] = nombre

libro.save("ejercicio5.xlsx")

print("Ejercicio 5 guardado en ejercicio5.xlsx!")