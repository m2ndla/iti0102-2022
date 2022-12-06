"""EX15 - Santa's workshop."""
import urllib.parse
import requests

"""
idee:
class lists:
    - initis annad nice, wish ja naughty listi kaasa
    - loeb sisse kõik listid ja loob listi, kus iga element on dict:
        - [
            {"nimi": "abc", "riik": "def", "wishlist": "str", "nice": True/False}
            jne
        - ]
 
class Kids():
    listide klassi inputi põhjal luuakse kid objekt, kus kogu info olemas

class Present():
    iga kingi kohta on oma objekt, kus on antud kingi nimetus, hind, tootmise aeg ja kaal

"""
kids_list = []
presents_list = []


class Lists:
    """Lists class."""

    def __init__(self, wish_list: str, nice_list: str, naughty_list: str):
        """Initialize Lists class."""
        self.wish_list = wish_list
        self.nice_list = nice_list
        self.naughty_list = naughty_list
        self.kids = []

    def read_wish_list(self):
        """Read wishlist and compile the info."""
        with open(self.wish_list, "r") as f:
            for line in f:
                item = line.split(",", 1)
                name = item[0]
                presents = item[1][:-1].split(",")
                lst = []
                for present in presents:
                    lst.append(present[1::])
                for kid in self.kids:
                    if kid["name"] == name:
                        kid["wishlist"] = lst
                        break

    def read_nice_list(self):
        """Read nice list and compile the info."""
        with open(self.nice_list, "r") as f:
            for line in f:
                item = line.split(",")
                name = item[0]
                country = item[1][1:-1:]
                self.kids.append({"name": name, "country": country, "nice": True})

    def read_naughty_list(self):
        """Read naughty list and compile the info."""
        with open(self.naughty_list, "r") as f:
            for line in f:
                item = line.split(",")
                name = item[0]
                country = item[1][1:-1:]
                self.kids.append({"name": name, "country": country, "nice": False})

    def read_lists(self):
        """Read all the lists."""
        self.read_nice_list()
        self.read_naughty_list()
        self.read_wish_list()

    def get_presents(self):
        """Make Present objects."""
        for kid in self.kids:
            for present in kid["wishlist"]:
                present_name_urllib = urllib.parse.quote(present)
                url_response = requests.get("https://cs.ttu.ee/services/xmas/gift?name=" + present_name_urllib)
                param = url_response.json()
                if "message" in param:
                    break
                presents_list.append(
                    Present(param["gift"], param["material_cost"], param["production_time"], param["weight_in_grams"])
                )

    def kids_into_list(self):
        """Add Kid objects into a list."""
        for kid in self.kids:
            for param in kid.values():
                kids_list.append(Kid(param[0], param[1], param[2], param[3]))

    def main_func(self):
        """Exec all functions needed."""
        self.read_lists()
        self.get_presents()
        self.kids_into_list()


class Kid:
    """Kid class."""

    def __init__(self, name: str, country: str, wishlist: list, nice: bool):
        """Initialize the kid class."""
        self.name = name
        self.country = country
        self.wishlist = wishlist
        self.nice = nice

    def __repr__(self):
        """Representation."""
        return f"Name: {self.name}, Country: {self.country}, Nice: {self.nice}, Wishlist items: {self.wishlist}."


class Present:
    """Present class."""

    def __init__(self, name: str, cost: int, production_time: int, weight_in_grams: int):
        """Initialize the present class."""
        self.name = name
        self.cost = cost
        self.production_time = production_time
        self.weight_in_grams = weight_in_grams

    def __repr__(self):
        """Representation."""
        return f"Present name: {self.name}, Cost: {self.cost}, Production time: {self.production_time}, Weight: " \
               f"{self.weight_in_grams}."


if __name__ == "__main__":
    lst = Lists("ex15_wish_list.csv", "ex15_nice_list.csv", "ex15_naughty_list.csv")
    lst.main_func()
    print(kids_list)
    print(presents_list)
