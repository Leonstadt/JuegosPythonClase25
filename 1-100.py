import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido al juego de adivina el número!")
    print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")

    while True:
        intento = int(input("Introduce tu número: "))
        intentos += 1
        distancia=abs(numero_secreto - intento)
    

        if intento < numero_secreto:
            print("Demasiado bajo, intenta de nuevo.")
        elif intento > numero_secreto:
            print("Demasiado alto, intenta de nuevo.")            
        
        if distancia == 0:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break
        elif distancia <=10:
            print("¡Estas muy cerca!")
        elif distancia <=20:
            print("Estas cerca")
        else: 
            print("Estas muy lejos")

adivina_el_numero()