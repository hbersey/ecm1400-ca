from dashboard.panels._panel import DashboardPanel
from dashboard.monitoring_data import MonitoringData
import textwrap

def wrap(text, title, rh_size, rh_offset):
    lines = textwrap.fill(text, rh_size - len(title) - 3).splitlines()
    indent = rh_offset + len(title) + 1
    for i in range(len(lines)):
        if i == 0:
            continue
        lines[i] = f"\033[{indent}C {lines[i]}"
    return "\n".join(lines)

class AboutPanel(DashboardPanel):

    def _print(self, cols, lines, rh_size, rh_offset):
        n_cursor_up = (lines - 1)
        print(f"\033[{n_cursor_up}A")

        data = MonitoringData.instance()

        print(f"\033[{rh_offset}C Group: \033[1m\033[4m{data.group.name.upper()}\033[0m")
        print(f"\033[{rh_offset}C Description: {wrap(data.group.description, 'Description:', rh_size, rh_offset)}")
        print(f"\033[{rh_offset}C Learn More: \033[3;4m{data.group.website_url}\033[0m")

        print(f"\n\033[{rh_offset}C Site: \033[1m\033[4m{data.site.name.upper()}\033[0m ({data.site.code})")
        print(f"\033[{rh_offset}C Local Authority: {data.site.local_authority_name} ({data.site.local_authority_code})")
        print(f"\033[{rh_offset}C Type: {data.site.type_}")
        print(f"\033[{rh_offset}C Opened: {data.site.date_opened.strftime('%d/%m/%Y')}")
        print(f"\033[{rh_offset}C Closed: {data.site.date_closed.strftime('%d/%m/%Y')}")
        print(f"\033[{rh_offset}C Position: {data.site.latitude:.5f}, {data.site.longitude:.5f}")
        print(f"\033[{rh_offset}C Learn More: \033[3;4m{data.site.link}\033[0m")

        print(f"\n\033[{rh_offset}C Speicies: \033[1m\033[4m{data.species.name}\033[0m ({data.species.code})")
        print(f"\033[{rh_offset}C Description: {wrap(data.species.description, 'Description:', rh_size, rh_offset)}")
        print(f"\033[{rh_offset}C Health Effect: {wrap(data.species.health_effect, 'Health Effect:', rh_size, rh_offset)}")
        print(f"\033[{rh_offset}C Learn More: \033[3;4m{data.species.info_link}\033[0m")