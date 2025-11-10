import toml
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url


    def get_project(self):
        # Lataa TOML-tiedoston sisältö merkkijonona
        content = request.urlopen(self._url).read().decode("utf-8")
        print("TOML-tiedoston sisältö:\n", content)

        # Muunna TOML-data Pythonin tietorakenteeksi
        data = toml.loads(content)
        print("\nDeserialisoitu data:\n", data)

        # Haetaan tarvittavat tiedot
        tool_data = data["tool"]["poetry"]

        name = tool_data.get("name", "N/A")
        description = tool_data.get("description", "N/A")
        license = tool_data.get("license", "N/A")
        authors = tool_data.get("authors", [])
        dependencies = list(tool_data.get("dependencies", {}).keys())
        dev_dependencies = list(tool_data.get("group", {}).get("dev", {}).get("dependencies", {}).keys())

        # Palautetaan Project-olio
        return Project(name, description, license, authors, dependencies, dev_dependencies)