from typing import NamedTuple
from datetime import datetime, date
import csv

class Partido(NamedTuple):
    fecha: date
    rival: str
    superficie: str
    duracion: int
    juegos_ganados: int
    juegos_perdidos: int
    ganado: bool


def leer_registros(ruta: str) -> list[Partido]:

    res = []

    with open(ruta, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            fecha = datetime.strptime(row[0], "%d/%m/%Y").date()
            res.append(Partido(fecha, row[1], row[2], int(row[3]), int(row[4]), int(row[5]), row[6] == "True"))

    return res


def desviacion(partidos: list[Partido], n: int) -> list[tuple[int, Partido]]:

    media = sum(row.duracion for row in partidos)/len(partidos)


    return [(abs(media-row.duracion), row) for row in partidos if abs(media-row.duracion)>=n]


def diccionario_diferencia_juegos_superficie(partidos: list[Partido], n: int = 3) -> dict[str, list[date]]:
    res = {}


    for p in partidos:
        if p.superficie not in res.keys():
            res[p.superficie] = []

        res[p.superficie].append((p.fecha, p.ganado))

    


def sort_dict_games_surface(games: dict[str, list[tuple[date, bool]]], n: int) -> dict[str, list[date]]:
    pass


