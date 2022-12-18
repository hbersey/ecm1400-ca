import typing as t
from dashboard.dashboard import Dashboard
import reporting as pr


def __menu(title: str, items: t.List[t.Tuple[str, str, t.Optional[t.Callable]]]):
    fns = {}

    print(f"\n{title}")
    print("-" * len(title), end="\n\n")

    for (option, description, *fn) in items:
        print(f"{option}) {description}")
        fns[option] = fn[0] if len(fn) == 1 else lambda: None

    print()

    while True:
        sel = input("Your selection: ").strip()
        if sel in fns.keys():
            fns[sel]()
            break
        print("\nInvalid selection. Please try again.")

    return sel


def main_menu():
    """Your documentation goes here"""

    __menu("Main Menu", [
        ("R", "Access the PR module", reporting_menu),
        ("I", "Access the MI module", monitoring_menu),
        ("M", "Access the RM module", intelligence_menu),
        ("A", "Print the About text", about),
        ("Q", "Quit the application", quit)
    ])


def reporting_menu():
    """Your documentation goes here"""

    ms = __menu("Monitoring Station", [
        ("HRL", "Harlington"),
        ("MY1", "Marylebone Road"),
        ("KC1", "North Kensington"),
    ])

    p = __menu("Pollutant", [
        ("NO", "Nitrogen Oxide"),
        ("PM10", "Particulate Matter 10"),
        ("PM25", "Particulate Matter 2.5"),
    ]).lower()

    print()
    __menu("Polution Monitoring", [
        ("D", "Daily Average", lambda: pr.daily_average_interface(ms, p)),
        ("E", "Daily Median", lambda: pr.daily_median_interface(ms, p)),
        ("H", "Hourly Average", lambda: pr.hourly_average_interface(ms, p)),
        ("M", "Monthly Average", lambda: pr.monthly_average_interface(ms, p)),
        ("P", "Peak Hour Date"),
        ("C", "Count Missing Data"),
        ("F", "Fill Missing Data"),
    ])


def monitoring_menu():
    """Your documentation goes here"""
    d = Dashboard()
    d.run()


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
