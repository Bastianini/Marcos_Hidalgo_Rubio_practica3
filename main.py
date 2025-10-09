from time_management import Time, mostrar_hora

from time_management import Time, mostrar_hora

def main():
    reloj = Time()

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Introducir nueva hora")
        print("2. Visualizar hora")
        print("3. Crear hora a partir de una cadena (HH:MM:SS FORMAT)")
        print("4. Mostrar cantidad de relojes creados")
        print("5. Terminar")

        opcion = input("Seleccione una opción: ").strip()

        # -----------------------------
        # Opción 1: introducir nueva hora
        # -----------------------------
        if opcion == "1":
            while True:
                try:
                    h = int(input("Horas: "))
                    m = int(input("Minutos: "))
                    s = int(input("Segundos: "))
                    f = input("Formato (AM/PM/24 HOURS): ").strip().upper()

                    # Validar formato antes de set_time()
                    if f not in ("AM", "PM", "24 HOURS"):
                        print("❌ Formato inválido. Usa AM, PM o 24 HOURS.\n")
                        continue

                    # Intentar asignar hora
                    if reloj.set_time(h, m, s, f):
                        print("✅ Hora actualizada correctamente.")
                        break
                    else:
                        print("❌ Error: hora fuera de rango. Inténtalo de nuevo.\n")

                except ValueError:
                    print("❌ Debes introducir números válidos para horas, minutos y segundos.\n")

        # -----------------------------
        # Opción 2: visualizar hora
        # -----------------------------
        elif opcion == "2":
            print("Hora actual:", mostrar_hora(reloj))

        # -----------------------------
        # Opción 3: crear hora desde cadena
        # -----------------------------
        elif opcion == "3":
            while True:
                cadena = input("Introduce la hora (ej. 02:30:00 PM o 14:45:00 24 HOURS): ").strip()
                nuevo = Time.from_string(cadena)
                if nuevo:
                    reloj = nuevo
                    print("✅ Hora creada correctamente.")
                    break
                else:
                    print("❌ Formato incorrecto. Inténtalo de nuevo.\n")

        # -----------------------------
        # Opción 4: mostrar número de relojes creados
        # -----------------------------
        elif opcion == "4":
            cantidad = Time.get_time_count()
            print(f"⏱️ Se han creado {cantidad} objeto(s) de la clase Time.")

        # -----------------------------
        # Opción 5: terminar
        # -----------------------------
        elif opcion == "5":
            print("👋 Programa terminado. ¡Hasta luego!")
            break

        # -----------------------------
        # Opción inválida
        # -----------------------------
        else:
            print("⚠️ Opción no válida. Introduzca un número del 1 al 5.")


if __name__ == "__main__":
    main()
