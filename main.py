from time_management import Time, mostrar_hora

def main():
    reloj = Time()

    while True:
        print("\n--- MENÚ ---")
        print("1. Introducir nueva hora")
        print("2. Visualizar hora")
        print("3. Crear hora a partir de una cadena (HH:MM:SS FORMAT)")
        print("4. Terminar")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            h = int(input("Horas: "))
            m = int(input("Minutos: "))
            s = int(input("Segundos: "))
            f = input("Formato (AM/PM/24 HOURS): ")
            if reloj.set_time(h, m, s, f):
                print("Hora actualizada correctamente.")
            else:
                print("Hora o formato inválido.")

        elif opcion == "2":
            print("Hora actual:", mostrar_hora(reloj))

        elif opcion == "3":
            cadena = input("Introduce la hora (ej. 02:30:00 PM): ")
            nuevo = Time.from_string(cadena)
            if nuevo:
                reloj = nuevo
                print("Hora creada correctamente.")
            else:
                print("Formato de cadena inválido.")

        elif opcion == "4":
            print("Programa terminado.")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
