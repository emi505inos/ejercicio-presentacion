# #Que locura Tinky-Uinky
nombre = str(input("¡Hola!, Soy Eduardo. ¿Como es tu nombre?: "))
print(f"¡Hola, {nombre}!")
pregunta = int(input("¿Cuantos años tienes?: "))
edadAdulto = 18
if pregunta > edadAdulto:
    print(f"¡{pregunta}! estas muy grande")
else:
    print(f"¡{pregunta}! todavia eres muy chico")

pregunta1 = str(input(f"{nombre}, ¿Qué estudias?: "))
print(f"¡{pregunta1}!")
sociologia = "Sociologia"
if pregunta1 == sociologia:
    print("¡Lo sabia! estudias lo mismo que mi hermano ☺")
else:
    print("Pense que estudiabas lo mismo que mi hermano")

pregunta2 = int(input(f"{nombre} ¿En que año de {pregunta1} te encuentras?: "))
añosCarreraMaximo = 5
añosCarreraMitad = 3
comienzo = 2

if pregunta2 == añosCarreraMaximo or pregunta2 == 4:
    print("¡Ah, mira! estas por finalizar tus estudios")

if pregunta2 == añosCarreraMitad:
     print("Vas por la mitad de la carrera" )

if pregunta2 <= comienzo:
    print("Recien comienzas la carrera")

pregunta3 = str(input("Dime, ¿Es verdad que piensas hacer un doctorado? (Si/No): "))

if pregunta3 == "Si":
    print(f"¡{pregunta3}, lo sabia!")

    pregunta4 = input('¿Piensas estudiar en el extranjero o en el pais?: ')

    if pregunta4 == "en el extranjero":
        print(f"¡{pregunta4}, que genial, buen viaje!")
    elif pregunta4 == 'En el pais':
        universidad = input(f"¿En que universidad?: ")
        print(f'{universidad}, es una buena universidad')
        print(f'Ha sido un placer conocerte {nombre}. Espero que te valla bien la {universidad}')

else:
    print(f"{pregunta3} lo puedo creer, me han engañado")
    print(f'Ha sido un placer conocerte {nombre}. Espero que te valla bien en {pregunta1}')


