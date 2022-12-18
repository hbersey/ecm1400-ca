class MonitoringData:
    _instance = None

    def __init__(self) -> None:
        raise RuntimeError("This is a singleton, call instance() instead")

    @staticmethod
    def isntance() -> "MonitoringData":
        if MonitoringData._instance is None:
            MonitoringData._instance = MonitoringData.__new__(MonitoringData)
        return MonitoringData._instance
