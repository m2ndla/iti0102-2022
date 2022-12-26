"""EX15 - Santa's workshop."""
import urllib.parse
import requests
import os.path

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

class warehouse(ladu):
    valmis kinkide ladu

class factory:
    kinkide tootmine vastavalt vajadusele, initis kaasas olemasolev $$$ ja aeg

class world????
    võiks kombineerida asju ja kõik funktsioonid sinna toppida? või lists teha ümber worldiks vms

"""


class World:
    """World, lists and database class."""

    def __init__(self, wish_list: str, nice_list: str, naughty_list: str):
        """Initialize Lists class."""
        self.wish_list = wish_list
        self.nice_list = nice_list
        self.naughty_list = naughty_list
        self.kids = []  # algne list lastest dicti kujul
        self.children = []  # lõplik list lastest objektidena, kus on kogu info (k.a. wishlist) kaasa antud

    def read_wish_list(self):
        """Read wishlist and compile the info."""
        with open(self.wish_list, "r") as f:
            for line in f:
                item = line.split(",", 1)
                if len(item) == 1:
                    break
                name = item[0]
                presents = item[1][:-1].split(",")
                itemlist = []
                for present in presents:
                    itemlist.append(present[1::])
                for kid in self.kids:
                    if kid["name"] == name:
                        kid["wishlist"] = itemlist
                        break

    def read_nice_list(self):
        """Read nice list and compile the info."""
        with open(self.nice_list, "r") as f:
            for line in f:
                item = line.split(",")
                if len(item) == 1:
                    break
                name = item[0]
                country = item[1][1:-1:]
                self.kids.append({"name": name, "country": country, "nice": True})

    def read_naughty_list(self):
        """Read naughty list and compile the info."""
        with open(self.naughty_list, "r") as f:
            for line in f:
                item = line.split(",")
                if len(item) == 1:
                    break
                name = item[0]
                country = item[1][1:-1:]
                self.kids.append({"name": name, "country": country, "nice": False})

    def files_exist(self):
        """Check if given filenames exist."""
        if os.path.exists(self.wish_list) and os.path.exists(self.nice_list) and os.path.exists(self.naughty_list):
            return True
        else:
            return False

    def read_lists(self):
        """Read all the lists."""
        self.read_nice_list()
        self.read_naughty_list()
        self.read_wish_list()

    def add_kids_to_list(self):
        """Parse kids into list as objects."""
        for kid in self.kids:
            wishlist = []
            for present in kid["wishlist"]:
                present_name_urllib = urllib.parse.quote(present)
                url_response = requests.get("https://cs.ttu.ee/services/xmas/gift?name=" + present_name_urllib)
                param = url_response.json()
                wishlist.append(
                    Present(param["gift"], param["material_cost"], param["production_time"], param["weight_in_grams"])
                )
            self.children.append(Kid(kid["name"], kid["country"], kid["nice"], wishlist))

    def main(self):
        """Execute all functions."""
        if self.files_exist():
            self.read_lists()
            self.add_kids_to_list()
        else:
            return "One or more files do not exist!"


class Kid:
    """Kid class."""

    def __init__(self, name: str, country: str, nice: bool, wishlist: list):
        """Initialize the kid class."""
        self.name = name
        self.country = country
        self.wishlist = wishlist
        self.nice = nice

    def __repr__(self):
        """Representation."""
        return f"\n\nName: {self.name}\nCountry: {self.country}\nNice: {self.nice}\nWishlist items: {self.wishlist}."


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
        return f"\n\nPresent name: {self.name}\nCost: {self.cost}\nProduction time: {self.production_time}\nWeight: " \
               f"{self.weight_in_grams}."


class Warehouse:
    """Warehouse class."""

    def __init__(self):
        """Initialize the Warehouse class."""
        self.gifts = []

    def is_gift_in_warehouse(self, gift_name: str):
        """Find gift by name."""
        for gift in self.gifts:
            if gift.name == gift_name:
                return True
        return False


class Factory:
    """Factory class."""

    def __init__(self, available_money: int, available_time: int):
        """Initialize the factory class."""
        self.available_money = available_money
        self.available_time = available_time
        self.assembled_presents = []

    def add_or_remove_money(self, amount: int):
        """Add or remove available money."""
        self.available_money = self.available_money + amount

    def add_or_remove_time(self, amount: int):
        """Add or remove available time."""
        self.available_time = self.available_time + amount

    def assemble(self, present: Present):
        """Assemble present."""
        if self.available_time >= present.production_time and self.available_money >= present.cost:
            self.assembled_presents.append(present)
            self.available_time = self.available_time - present.production_time
            self.available_money = self.available_money - present.cost
        else:
            return False

    def move_to_warehouse(self, warehouse_object: Warehouse):
        """Move gifts to warehouse object."""
        warehouse_object.gifts.extend(self.assembled_presents)
        self.assembled_presents = []
