import typing


def __menu(items: typing.List[typing.Tuple[str, str, typing.Callable]]):
    fns = {}

    for (option, description, fn) in items:
        print(f"{option}) {description}")
        fns[option] = fn

    while True:
        sel = input("\nYour selection: ").strip()
        if sel in fns.keys():
            fns[sel]()
            break


def main_menu():
    """Your documentation goes here"""

    __menu([
        ("R", "Access the PR module", reporting_menu),
        ("I", "Access the MI module", monitoring_menu),
        ("M", "Access the RM module", intelligence_menu),
        ("A", "Print the About text", about),
        ("Q", "Quit the application", quit)
    ])


def reporting_menu():
    """Your documentation goes here"""
    # Your code goes here

def monitoring_menu():
    """Your documentation goes here"""
    # Your code goes here


def intelligence_menu():
    """Your documentation goes here"""
    # Your code goes here

def about():
    """Your documentation goes here"""
    # Your code goes here


def quit():
    """Your documentation goes here"""
    # Your code goes here


if __name__ == '__main__':
    main_menu()
