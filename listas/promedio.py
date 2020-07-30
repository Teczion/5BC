# promedio de notas
notas = input("Ingrese las notas separadas por comas: ")

# Se utiliza split para romper la cadena
separados = notas.split(",")
sumatoria = 0
for nota in separados:
    sumatoria += int(nota)

# Se utiliza len para obtener el numero de elementos
# de la lista separados
print("El resultados es: " + str(sumatoria/len(separados)))

# COMPLEMENTO Codigo que se puede implementar

# codigo Pablo Sabaj
'''
notas = []
n = int(input(" ¿Cuantas notas ingresara? "))
for i in range(n):
    nt = int(input("Calificacion: "))
    notas.append(nt)
print(notas)
'''
# Codigo Alexander Luis
'''
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lenguaje "]
scores = []
for subject in subjects:
    score = input("¿Qué nota has sacado en " + subject + "?")
    scores.append(score)
for i in range(len(subjects)):
    print("En " + subjects[i] + " has sacado " + scores[i])
'''
