from olimpiadas import *

if __name__ == "__main__":
    file = "ej1/data/atletas.txt"

    registros = leer_olimpiadas(file)



    print(f"\tLeidos {len(registros)} registros\n\tMostrando los 3 primeros")

    for r in registros[:3]:
        print(f"\t{r}")

    #print(edad_media(registros))
    # print(num_atletas_por_pais(registros))
    # print(nombre_atletas_por_pais(registros))

    #print(atleta_mayor_peso(registros))
    # print(pais_mayor_peso_medio(registros))
    #print(f"La diferencia máxima entre atletas consecutivos es de {metodozip(registros)}.")
    ordenar(registros)
    print(registros)