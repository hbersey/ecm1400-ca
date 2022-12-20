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

    @staticmethod
    def parse(json):
        return Species(
            code=json["@SpeciesCode"],
            name=json["@SpeciesName"],
            description=json["@Description"],
            health_effect=json["@HealthEffect"],
            info_link=json["@Link"],
        )

    @staticmethod
    def get_species() -> t.List["Species"]:
        res = requests.get(
            "http://api.erg.ic.ac.uk/AirQuality/Information/Species/Json")
        json = res.json()

        # Todo check for errors

        species: t.List[Species] = []

        for el in json["AirQualitySpecies"]["Species"]:
            species.append(Species.parse(el))

        return species