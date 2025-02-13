import random
import time

def jugar_ruleta():
    # Inicializar el tambor con una bala en una posición aleatoria
    tambor = [0, 0, 0, 0, 0, 1]
    random.shuffle(tambor)  # Mezclar tambor

    print("BIENVENIDO AL JUEGO DE LA RULETA RUSA")
    nombre = input("Digita tu nombre para iniciar el juego: ")

    # Decidir quién empieza
    print("Se decidirá quién inicia el juego...")
    time.sleep(1)
    jugador_actual = random.choice([nombre, "COMPUTADORA"])
    print(f"El jugador seleccionado para iniciar es: {jugador_actual}")

    # Comienza el juego
    while True:
        input(f"\nPresiona ENTER para que {jugador_actual} dispare...")
        print(f"{jugador_actual} se prepara para disparar...")
        time.sleep(2)
        
        # Extraer la primera bala del tambor (simulando giro antes de disparar)
        bala = tambor.pop(0)

        if bala == 1:
            print(f"¡¡BANG!! {jugador_actual} perdió el juego.")
            break
        else:
            print("¡¡CLICK!!... La bala no estaba en la recámara.")
        
        # Cambiar de jugador
        jugador_actual = "COMPUTADORA" if jugador_actual == nombre else nombre

    # Preguntar si desea jugar de nuevo
    jugar_nuevamente = input("\n¿Quieres jugar de nuevo? (s/n): ").strip().lower()
    if jugar_nuevamente == 's':
        jugar_ruleta()
    else:
        print("Gracias por jugar. ¡Hasta la próxima!")

# Ejecutar el juego
jugar_ruleta()
