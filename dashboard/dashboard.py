import interface as intf


class Dashboard:
    rh_state: int
    lh_state: any
    is_rh: bool

    def __init__(self):
        self.rh_state = 0
        self.lh_state = None
        self.is_rh = False

    def __run(self):
        while True:
            intf.layout()

    @staticmethod
    def run():
        dashboard = Dashboard()
        dashboard.__run()


if __name__ == "__main__":
    Dashboard.run()