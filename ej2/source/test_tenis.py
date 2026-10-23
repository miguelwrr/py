from tenis import *


def main() -> None:
    route = "ej2/data/datos.txt"

    registries = leer_registros(route)

    print(f"Leidos {len(registries)} registros.")
    print("Mostrando los 3 primeros")
    for row in registries[:3]:
        print(row)
    print("\n\n")

    print(desviacion(registries, 20))


if __name__ == "__main__":
    main()