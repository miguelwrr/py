import csv
from typing import NamedTuple

class Atleta(NamedTuple):
    nombre: str
    edad: int
    pais: str
    peso: float


def leer_olimpiadas(ruta: str) -> list[Atleta]:
    registros = []

    with open(ruta, "r", encoding="utf-8") as f:

        reader = csv.reader(f)
        next(reader)

        for row in reader:
            nombre = row[0]
            edad = int(row[1])
            pais = row[2]
            peso = float(row[3])

            registros.append(Atleta(nombre, edad, pais, peso))

    return registros



def edad_media(registros: list[Atleta]) -> float:

    suma_edades = 0

    for registro in registros:
        suma_edades += registro.edad

    return float(suma_edades)/len(registros)



def num_atletas_por_pais(registros: list[Atleta]) -> dict[str, int]:

    res = dict()

    for registro in registros:
        if registro.pais not in res.keys():
            res[registro.pais] = 1
        else:
            res[registro.pais]+=1

    return res


def nombre_Atletas_por_pais(registros: list[Atleta]) -> dict[str, list[str]]:

    res = {}

    for registro in registros:
        if registro.pais not in res.keys():
            res[registro.pais] = []

        res[registro.pais].append(registro.nombre)

    return res


def atleta_mayor_peso(registros: list[Atleta]) -> str:
    registros = sorted(registros, key = lambda x:x.peso, reverse = True)

    return registros[0].nombre


def pais_mayor_peso_medio(registros: list[Atleta]) -> str:
    paises_peso = {}

    for registro in registros:
        if registro.pais not in paises_peso.keys():
            paises_peso[registro.pais] = []

        paises_peso[registro.pais].append(registro.peso)

    for k in paises_peso.keys():
        paises_peso[k] = sum(paises_peso[k])/len(paises_peso[k])
    return sorted(paises_peso.items(), key=lambda x:x[1], reverse=True)[0][0]


def metodozip(registros: list[Atleta]) -> int:
    registros = sorted(registros, key=lambda x:x.edad)
    edades_registros = [row.edad for row in registros]
    edades = zip(edades_registros, edades_registros[1:])
    diferencia_maxima = 0

    for elem in edades:
        diferencia = elem[1] - elem[0]
        diferencia_maxima = diferencia if diferencia > diferencia_maxima else diferencia_maxima

    return diferencia_maxima