import json
import random
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests
from bs4 import BeautifulSoup


class VersionUpdater:
    def __init__(self):
        self.versionsPath = Path(__file__).parent / "browserVersions.json"
        self.versionsPath.touch()

    def updateFirefox(self):
        url = "https://en.wikipedia.org/wiki/Firefox"
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        version = (
            soup.find("table", class_="infobox-subbox")
            .find("td", class_="infobox-data")
            .text
        )
        version = version[: version.find("[")]
        self.firefox = version

    def updateChrome(self):
        url = "https://en.wikipedia.org/wiki/Google_Chrome"
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        infoBoxes = soup.find_all("td", class_="infobox-data")
        version = infoBoxes[7].text[: infoBoxes[7].text.find("/")]
        self.chrome = version

    def updateSafari(self):
        url = "https://en.wikipedia.org/wiki/Safari_(web_browser)"
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        infoBoxes = soup.find_all("td", class_="infobox-data")
        version = infoBoxes[2].text[: infoBoxes[2].text.find("[")]
        self.safari = version

    def updateEdge(self):
        url = "https://en.wikipedia.org/wiki/Microsoft_Edge"
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        infoBoxes = soup.find_all("td", class_="infobox-data")
        version = infoBoxes[3].text[: infoBoxes[3].text.find("[")]
        self.edge = version

    def updateVivaldi(self):
        url = "https://en.wikipedia.org/wiki/Vivaldi_(web_browser)"
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        infoBoxes = soup.find_all("td", class_="infobox-data")
        version = infoBoxes[5].text[: infoBoxes[5].text.find(" ")]
        self.vivaldi = version

    def updateOpera(self):
        url = "https://en.wikipedia.org/wiki/Opera_(web_browser)"
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        infoBoxes = soup.find_all("td", class_="infobox-data")
        version = infoBoxes[2].p.text[: infoBoxes[2].p.text.find(" ")]
        self.opera = version

    def updateAll(self):
        updaters = [
            self.updateFirefox,
            self.updateChrome,
            self.updateSafari,
            self.updateEdge,
            self.updateVivaldi,
            self.updateOpera,
        ]
        with ThreadPoolExecutor(6) as executor:
            for updater in updaters:
                executor.submit(updater)
        versions = {
            "Firefox": self.firefox,
            "Chrome": self.chrome,
            "Edg": self.edge,
            "Vivaldi": self.vivaldi,
            "OPR": self.opera,
            "Safari": self.safari,
        }
        self.versionsPath.write_text(json.dumps(versions))


platforms = [
    "(Windows NT 10.0; Win64; x64)",
    "(x11; Ubuntu; Linux x86_64)",
    "(Windows NT 11.0; Win64; x64)",
    "(Macintosh; Intel Mac OS X 13_0_0)",
]


def getAgent() -> str:
    """Build and return a user agent string."""
    browsers = json.loads((Path(__file__).parent / "browserVersions.json").read_text())
    browser = random.choice(list(browsers.keys()))
    if browser == "Safari":
        platform = platforms[-1]
        useragent = f'Mozilla/5.0 {platform} AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{browsers["Safari"]} Safari/605.1.15'
    else:
        platform = random.choice(platforms)
        if browser == "Firefox":
            platform = platform[: platform.rfind(")")] + f"; rv:{browsers[browser]})"
            useragent = (
                f"Mozilla/5.0 {platform} Gecko/20100101 Firefox/{browsers[browser]}"
            )
        else:
            useragent = f'Mozilla/5.0 {platform} AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{browsers["Chrome"]} Safari/537.36'
            if browser == "Edg":
                useragent += f' Edg/{browsers["Edg"]}'
            elif browser == "OPR":
                useragent += f' OPR/{browsers["OPR"]}'
            elif browser == "Vivaldi":
                useragent += f' Vivaldi/{browsers["Vivaldi"]}'
    return useragent
