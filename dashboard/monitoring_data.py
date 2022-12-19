from dashboard.sites import SiteGroup, Site
import typing as t


class MonitoringData:
    _instance = None
    _groups: t.List[SiteGroup] = None
    _sites: t.Dict[int, t.List[Site]] = None  # one list per group

    @property
    def groups(self) -> t.List[SiteGroup]:
        if self._groups == None:
            self._groups = SiteGroup.get_all()
        return self._groups

    def sites(self, group_index: int) -> t.List[Site]:
        if self._sites == None:
            self._sites = {}

        if group_index not in self._sites:
            self._sites[group_index] = Site.get_sites(self.groups[group_index].name)

        return self._sites[group_index]

    def __init__(self) -> None:
        raise RuntimeError("This is a singleton, call instance() instead")

    @staticmethod
    def instance() -> "MonitoringData":
        if MonitoringData._instance is None:
            MonitoringData._instance = MonitoringData.__new__(MonitoringData)
        return MonitoringData._instance
