'''Ejercicio: Adivina mi número
Decides que quieres jugar un juego en el que estás ocultando 
un número de alguien. Almacene este número en una variable 
llamada 'respuesta'. 
Otro usuario proporciona un número llamado 'adivinar'.
Al comparar adivinar a respuesta, usted informa al 
usuario si su suposición es demasiado alta o baja.
Rellene los condicionales a continuación para informar
al usuario sobre cómo se compara su suposición con la respuesta.

respuesta = 10
adivinar = 10 
'''
respuesta = 100
adivinar = 10

if respuesta > adivinar:
    result = "Oops!  Tu respuesta es muy baja."
elif respuesta < adivinar:
    result = "Oops!  Tu respuesta es muy alta."
elif respuesta == adivinar:
    result = "Has adivinado la resuesta!"

print(result)