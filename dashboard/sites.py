from dataclasses import dataclass
import typing as t
import requests
from dashboard.species import Species
from datetime import datetime
from utils import parse_or_none, or_none


@dataclass
class SiteGroup:
    name: str
    description: str
    website_url: str

    @staticmethod
    def get_all() -> t.List["SiteGroup"]:
        res = requests.get(
            "http://api.erg.ic.ac.uk/AirQuality/Information/Groups/Json")
        json = res.json()

        # Todo check for errors

        groups: t.List[SiteGroup] = []

        for el in json["Groups"]["Group"]:
            desc = el["@Description"]
            if desc == "Demo group for tender":
                continue

            groups.append(SiteGroup(
                name=el["@GroupName"],
                description=desc,
                website_url=el["@WebsiteURL"],
            ))

        return groups


def parse_date(s):
    return datetime.strptime(s, "%Y-%m-%d %H:%M:%S")


@dataclass
class Site:
    local_authority_code: int
    local_authority_name: str
    code: str
    name: str
    type_: str
    date_closed: datetime
    date_opened: datetime
    latitude: float
    longitude: float
    latitude_wgs84: float
    longitude_wgs84: float
    data_owner: str
    data_manager: str
    link: str
    specie_codes: t.List[str]

    @staticmethod
    def get_sites(group_name: str) -> t.List["Site"]:
        res = requests.get(
            f"https://api.erg.ic.ac.uk/AirQuality/Information/MonitoringSiteSpecies/GroupName={group_name}/Json")

        json = res.json()

        # Todo check for errors

        sites: t.List[Site] = []

        json_sites = json["Sites"]["Site"]
        if type(json_sites) != list:
            json_sites = [json_sites]

        for el in json_sites:
            if type(el["Species"]) == dict:
                specie_codes = [el["Species"]["@SpeciesCode"]]
            else:
                specie_codes = [s["@SpeciesCode"] for s in el["Species"]]

            sites.append(Site(
                local_authority_code=parse_or_none(
                    int, el["@LocalAuthorityCode"]),
                local_authority_name=parse_or_none(
                    str, el["@LocalAuthorityName"]),

                code=or_none(el["@SiteCode"]),
                name=or_none(el["@SiteName"]),
                type_=or_none(el["@SiteType"]),

                date_closed=parse_or_none(parse_date, el["@DateClosed"]),
                date_opened=parse_or_none(parse_date, el["@DateOpened"]),

                latitude=parse_or_none(float, el["@Latitude"]),
                longitude=parse_or_none(float, el["@Longitude"]),
                latitude_wgs84=parse_or_none(float, el["@LatitudeWGS84"]),
                longitude_wgs84=parse_or_none(float, el["@LongitudeWGS84"]),

                data_owner=or_none(el["@DataOwner"]),
                data_manager=or_none(el["@DataManager"]),

                link=or_none(el["@SiteLink"]),

                specie_codes=specie_codes
            ))
        return sites
