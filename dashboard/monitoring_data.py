from dashboard.sites import SiteGroup, Site
from dashboard.species import Species
import typing as t
from simplejson.errors import JSONDecodeError


class MonitoringData:
    _instance = None
    _groups: t.Dict[str, SiteGroup] = None
    _sites: t.Dict[str, t.List[Site]] = None  # one list per group
    _all_species: t.List[Species] = None
    _species: t.Dict[str, t.List[Species]] = None  # one list per site

    @property
    def groups(self) -> t.Dict[str, SiteGroup]:
        if self._groups == None:
            self._groups = {g.name: g for g in SiteGroup.get_all()}
        return self._groups

    def group_name(self, group_int: int) -> str:
        return list(self.groups.keys())[group_int]

    def sites(self, group_name: str) -> t.List[Site]:
        if self._sites == None:
            self._sites = {}

        if group_name not in self._sites:
            try:
                self._sites[group_name] = Site.get_sites(group_name)
            except JSONDecodeError:
                self._groups.pop(group_name)
                return []

        return self._sites[group_name]

    def species(self, site: Site) -> t.List[Species]:
        if self._all_species == None:
            self._all_species = Species.get_species()

        if self._species == None:
            self._species = {}

        if site.code not in self._species:
            self._species[site.code] = []
            for species in self._all_species:
                if species.code in site.specie_codes:
                    self._species[site.code].append(species)

        return self._species[site.code]

    def __init__(self) -> None:
        raise RuntimeError("This is a singleton, call instance() instead")

    @staticmethod
    def instance() -> "MonitoringData":
        if MonitoringData._instance is None:
            MonitoringData._instance = MonitoringData.__new__(MonitoringData)
        return MonitoringData._instance
