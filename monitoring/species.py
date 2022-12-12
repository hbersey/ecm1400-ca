from dataclasses import dataclass
import typing as t
import requests


@dataclass
class Species:
    code: str
    name: str
    description: str
    health_effect: str
    info_link: str


def get_species() -> t.List[Species]:
    res = requests.get(
        "http://api.erg.ic.ac.uk/AirQuality/Information/Species/Json")
    json = res.json()

    # Todo check for errors

    species: t.List[Species] = []

    for el in json["AirQualitySpecies"]["Species"]:
        species.append(Species(
            code=el["@SpeciesCode"],
            name=el["@SpeciesName"],
            description=el["@Description"],
            health_effect=el["@HealthEffect"],
            info_link=el["@Link"],
        ))

    return species
