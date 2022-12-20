import typing as t
from monitoring_.dashboard import Dashboard
import reporting as pr
import intelligence as mi
from utils import menu
import sys


def main_menu() -> None:
    """Displays the main menu and opens the menu for the selected module."""

    menu("Main Menu", [
        ("R", "Access the PR module", reporting_menu),
        ("I", "Access the MI module", intelligence_menu),
        ("M", "Access the RM module", monitoring_menu),
        ("A", "Print the About text", about),
        ("Q", "Quit the application", quit)
    ])


def reporting_menu() -> None:
    """Takes input for a monitoring station and pollutant, then opens the reporting menu and runs the selected function. """

    ms = menu("Monitoring Station", [
        ("HRL", "Harlington"),
        ("MY1", "Marylebone Road"),
        ("KC1", "North Kensington"),
    ])

    p = menu("Pollutant", [
        ("NO", "Nitrogen Oxide"),
        ("PM10", "Particulate Matter 10"),
        ("PM25", "Particulate Matter 2.5"),
    ]).lower()

    print()
    menu("Polution Monitoring", [
        ("D", "Daily Average", lambda: pr.daily_average_interface(ms, p)),
        ("E", "Daily Median", lambda: pr.daily_median_interface(ms, p)),
        ("H", "Hourly Average", lambda: pr.hourly_average_interface(ms, p)),
        ("M", "Monthly Average", lambda: pr.monthly_average_interface(ms, p)),
        ("P", "Peak Hour Date", lambda: pr.peak_hour_date_interface(ms, p)),
        ("C", "Count Missing Data", lambda: pr.count_missing_data_interface(ms, p)),
        ("F", "Fill Missing Data", lambda: pr.fill_missing_data_interface(ms, p)),
    ])


def monitoring_menu() -> None:
    """Allows the user to enter full screen mode and then opens the monitoring monitoring_."""
    print("Monitoring Dashboard Opening Now.\nYou may want to enter full screen mode.")
    menu("Are you ready?", [
        ("Y", "Yes!"),
    ])

    d = Dashboard()
    d.run()


def intelligence_menu() -> None:
    """Displays the intelligence menu and runs the selected function."""

    menu("Mobility Intelligence", [
        ("R", "Find Red Pixels", lambda: mi.find_red_pixels_interface()),
        ("C", "Find Cyan Pixels", lambda: mi.find_cyan_pixels_interface()),
        ("D", "Detect Connected Components", lambda: mi.detect_connected_components_interface()), ])


def about() -> None:
    """Displays the about text, including the module code, ECM1400 and my six-digit candidate number, 228258."""
    print("ECM1400 Programming Continuous Assessment\nModule Code: ECM1400\nCandidate Number: 228258")


def quit() -> None:
    """Quits the program."""
    sys.exit(0)


if __name__ == '__main__':
    cont = True
    while cont:
        sel = main_menu()
        if sel == "Q":
            break

        sel = menu("Do you want to continue?", [
            ("Y", "Yes"),
            ("N", "No")
        ])
        cont = sel == "Y"
