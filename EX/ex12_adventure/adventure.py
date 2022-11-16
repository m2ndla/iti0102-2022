"""EX12: Adventure."""


class Adventurer:
    """Adventurer class."""

    def __init__(self, name: str, class_type: str, power: int, experience: int = 0):
        """Initialize the Adventurer class."""
        self.name = name
        self.class_type = class_type
        self.power = power
        self.experience = experience
        possible_classes = ["Fighter", "Druid", "Wizard", "Paladin", "Fighter"]
        if class_type not in possible_classes:
            print(f"Ei, {self.name}, sa ei saa olla {class_type}, nüüd sa pead fighter olema.")
            self.class_type = "Fighter"
        if power > 99:
            print("Ei maksa ennast liiga tugevaks ka alguses teha!")
            self.power = 10
        if 0 > experience:
            self.experience = 0

    def __repr__(self):
        """
        Adventurer representation.

        Format: [name], the [class_type], Power: [power], Experience: [experience].
        """
        return f"{self.name}, the {self.class_type}, Power: {self.power}, Experience: {self.experience}."

    def add_power(self, power: int):
        """Adding power to adventurer."""
        self.power += power

    def add_experience(self, exp: int):
        """Adding experience to adventurer."""
        if exp > 0:
            self.experience += exp
        if self.experience > 99:
            self.power += (self.experience // 10)
            self.experience = 0


class Monster:
    """Monster class."""

    def __init__(self, name: str, type: str, power: int):
        """Initialize the Monster class."""
        self.name = name
        self.type = type
        self.power = power
        if "Zombie" in self.type:
            self.name = f"Undead {self.name}"

    def __repr__(self):
        """
        Monster representation.

        Format: [name] of type [type], Power: [power].
        """
        return f"{self.name} of type {self.type}, Power: {self.power}."


class World:
    """World-class. (pun intended)."""

    def __init__(self, master_name: str):
        """Initialize the class world."""
        self.master_name = master_name
        self.adventurer_list = []
        self.monster_list = []
        self.graveyard = []
        self.necromancers = False
        self.active_adventurers = []
        self.active_monsters = []

    def get_python_master(self):
        """Return python master's name."""
        return self.master_name

    def get_adventurer_list(self):
        """Return adventurer list."""
        return self.adventurer_list

    def get_monster_list(self):
        """Return monster list."""
        return self.monster_list

    def add_adventurer(self, adventurer: Adventurer):
        """Add adventurer to adventurer list."""
        if isinstance(adventurer, Adventurer):
            self.adventurer_list.append(adventurer)
        else:
            print(f"{adventurer.name}, peremees, sina küll seikleja olla ei saa.")

    def add_monster(self, monster: Monster):
        """Add monster to monster list."""
        if isinstance(monster, Monster):
            self.monster_list.append(monster)
        else:
            print(f"Ei, {monster.name}, sa ei saa olla vaenlane.")

    def get_graveyard(self):
        """Return graveyard list."""
        return self.graveyard

    def remove_character(self, name):
        """Remove character from list."""
        for character in self.adventurer_list:
            if character.name == name:
                self.graveyard.append(character)
                self.adventurer_list.remove(character)
                break
        for character in self.monster_list:
            if character.name == name:
                self.graveyard.append(character)
                self.monster_list.remove(character)
                break
        for character in self.graveyard:
            if character.name == name:
                self.graveyard.remove(character)
                break

    def necromancers_active(self, active: bool):
        """Change status of necromancers."""
        if active:
            self.necromancers = True
        else:
            self.necromancers = False

    def revive_graveyard(self):
        """Revive players in the graveyard."""
        if self.necromancers:
            for character in self.graveyard:
                if isinstance(character, Monster):
                    character.type = "Zombie"
                    character.name = f"Undead {character.name}"
                    self.monster_list.append(character)
                if isinstance(character, Adventurer):
                    self.monster_list.append(Monster(f"Undead {character.name}", f"Zombie {character.class_type}", character.power))
            del self.graveyard[:]
            self.necromancers = False

    def get_active_adventurers(self):
        """Return active adventurers sorted by experience."""
        sorted_active = sorted(self.active_adventurers, key=lambda x: x.experience, reverse=True)
        return sorted_active

    def add_strongest_adventurer(self, class_type: str):
        """Add the strongest adventurer who is not yet active."""
        lst = []
        for adventurer in self.adventurer_list:
            if adventurer.class_type == class_type:
                lst.append(adventurer)
        strongest = sorted(lst, key=lambda x: x.power, reverse=True)
        self.active_adventurers.append(strongest[0])
        self.adventurer_list.remove(strongest[0])

    def add_weakest_adventurer(self, class_type: str):
        """Add the weakest adventurer who is not yet active."""
        lst = []
        for adventurer in self.adventurer_list:
            if adventurer.class_type == class_type:
                lst.append(adventurer)
        weakest = sorted(lst, key=lambda x: x.power)
        self.active_adventurers.append(weakest[0])
        self.adventurer_list.remove(weakest[0])

    def add_most_experienced_adventurer(self, class_type: str):
        """Add the most experienced adventurer who is not yet active."""
        lst = []
        for adventurer in self.adventurer_list:
            if adventurer.class_type == class_type:
                lst.append(adventurer)
        most_xp = sorted(lst, key=lambda x: x.experience, reverse=True)
        self.active_adventurers.append(most_xp[0])
        self.adventurer_list.remove(most_xp[0])

    def add_least_experienced_adventurer(self, class_type: str):
        """Add the least experienced adventurer who is not yet active."""
        lst = []
        for adventurer in self.adventurer_list:
            if adventurer.class_type == class_type:
                lst.append(adventurer)
        least_xp = sorted(lst, key=lambda x: x.experience)
        self.active_adventurers.append(least_xp[0])
        self.adventurer_list.remove(least_xp[0])

    def add_adventurer_by_name(self, name: str):
        """Add an adventurer by name."""
        lst = []
        for adventurer in self.adventurer_list:
            if adventurer.name == name:
                lst.append(adventurer)
        for adventurer in lst:
            self.active_adventurers.append(adventurer)
            self.adventurer_list.remove(adventurer)

    def add_all_adventurers_of_class_type(self, class_type: str):
        """Add all adventurers of given class type, who are not yet active."""
        lst = []
        for adventurer in self.adventurer_list:
            if adventurer.class_type == class_type:
                lst.append(adventurer)
        for adventurer in lst:
            self.active_adventurers.append(adventurer)
            self.adventurer_list.remove(adventurer)

    def add_all_adventurers(self):
        """Add all adventurers who are not yet active."""
        for adventurer in self.adventurer_list:
            self.active_adventurers.append(adventurer)
        del self.adventurer_list[:]

    def get_active_monsters(self):
        """Return all the active monsters."""
        sorted_monsters = sorted(self.active_monsters, key=lambda x: x.power, reverse=True)
        return sorted_monsters

    def add_monster_by_name(self, name: str):
        """Add a monster by its name if they're not yet active."""
        lst = []
        for monster in self.monster_list:
            if monster.name == name:
                lst.append(monster)
        for monster in lst:
            self.active_monsters.append(monster)
            self.monster_list.remove(monster)

    def add_strongest_monster(self):
        """Add the strongest monster, who is not yet active."""
        sorted_monsters = sorted(self.monster_list, key=lambda x: x.power, reverse=True)
        self.active_monsters.append(sorted_monsters[0])
        self.monster_list.remove(sorted_monsters[0])

    def add_weakest_monster(self):
        """Add the weakest monster, who is not yet active."""
        sorted_monsters = sorted(self.monster_list, key=lambda x: x.power)
        self.active_monsters.append(sorted_monsters[0])
        self.monster_list.remove(sorted_monsters[0])

    def add_all_monsters_of_type(self, type: str):
        """Add all monsters of given type, who are not yet active."""
        lst = []
        for monster in self.monster_list:
            if monster.type == type:
                lst.append(monster)
        for monster in lst:
            self.active_monsters.append(monster)
            self.monster_list.remove(monster)

    def add_all_monsters(self):
        """Add all monsters who are not yet active."""
        for monster in self.monster_list:
            self.active_monsters.append(monster)
        del self.monster_list[:]

    def are_druids(self):
        """Check if there are druids."""
        for adventurer in self.active_adventurers:
            if "Druid" in adventurer.class_type:
                return True
        return False

    def are_animals_or_ents(self):
        """Check if there are Animal or Ent type of monsters."""
        for monster in self.active_monsters:
            if "Animal" in monster.type or "Ent" in monster.type:
                return True
        return False

    def are_zombies(self):
        """Check if there are zombies."""
        for monster in self.active_monsters:
            if "Zombie" in monster.type:
                return True
        return False

    def get_powers(self):
        """Return the winner of the fight."""
        advent_power = 0
        monster_power = 0
        remove_lst = []
        for monster in self.active_monsters:
            if self.are_druids() and self.are_animals_or_ents():
                remove_lst.append(monster)
            else:
                monster_power += monster.power
        if remove_lst:
            for monster in remove_lst:
                self.active_monsters.remove(monster)
                self.monster_list.append(monster)
        for adventurer in self.active_adventurers:
            if self.are_zombies() and adventurer.class_type == "Paladin":
                adventurer.power = adventurer.power * 2
            advent_power += adventurer.power
        if advent_power > monster_power:
            return True
        elif monster_power > advent_power:
            return False
        elif monster_power == advent_power:
            return None

    def remove_paladins_power(self):
        """Remove the power of Paladin class adventurers after fight."""
        if self.are_zombies():
            for adventurer in self.active_adventurers:
                if adventurer.class_type == "Paladin":
                    adventurer.power = adventurer.power // 2

    def xp_from_adventure(self, draw: bool, deadly: bool):
        """Calculate the xp given to adventurers."""
        pwr = 0
        for monster in self.active_monsters:
            pwr += monster.power
        exp_per_adventurer = pwr // len(self.active_adventurers)
        if draw:
            self.give_xp(exp_per_adventurer // 2)
        if deadly:
            self.give_xp(exp_per_adventurer * 2)
        else:
            self.give_xp(exp_per_adventurer)

    def give_xp(self, exp: int):
        """Give xp to adventurers."""
        for adventurer in self.active_adventurers:
            adventurer.add_experience(exp)

    def make_adventurers_inactive(self):
        """Remove adventurers from active list."""
        for adventurer in self.active_adventurers:
            self.adventurer_list.append(adventurer)
        del self.active_adventurers[:]

    def make_monsters_inactive(self):
        """Remove monsters from active list."""
        for monster in self.active_monsters:
            self.monster_list.append(monster)
        del self.active_monsters[:]

    def adventurers_win(self, deadly: bool):
        """Do what is needed when adventurers win."""
        self.xp_from_adventure(False, deadly)
        self.remove_paladins_power()
        self.make_adventurers_inactive()
        if deadly:
            for monster in self.active_monsters:
                self.get_graveyard().append(monster)
            del self.active_monsters[:]
        else:
            self.make_monsters_inactive()

    def monsters_win(self, deadly: bool):
        """Do what is needed when monsters win."""
        self.remove_paladins_power()
        self.make_monsters_inactive()
        if deadly:
            for adventurer in self.active_adventurers:
                self.get_graveyard().append(adventurer)
            del self.active_adventurers[:]
        else:
            self.make_adventurers_inactive()

    def draw(self, deadly: bool):
        """Do what is needed when the adventurers and monsters are in a stalemate."""
        self.xp_from_adventure(True, deadly)
        self.remove_paladins_power()
        self.make_adventurers_inactive()
        self.make_monsters_inactive()

    def go_adventure(self, deadly: bool = False):
        """Go on an adventure. Finally."""
        if self.get_powers() is True:
            self.adventurers_win(deadly)
        elif self.get_powers() is False:
            self.monsters_win(deadly)
        elif self.get_powers() is None:
            self.draw(deadly)

# if get powers == :
#   True: advent võitis, anna xp, remove paladins power ja if deadly, siis monsterid graveyardi, muidu tagasi listi
#   False: monsterid võitsid, no xp, remove paladins power ja if deadly, siis advent graveyardi, muidu tagasi listi
#   None: viik, anna xp, remove paladins power ja kõik mongolid tagasi listi


if __name__ == "__main__":
    print("Kord oli maailm.")
    world = World("Sõber")
    print(world.get_python_master())  # -> "Sõber"
    print(world.get_graveyard())  # -> []
    print()
    print("Tutvustame tegelasi.")
    hero = Adventurer("Sander", "Paladin", 50)
    friend = Adventurer("Peep", "Druid", 25)
    another_friend = Adventurer("Toots", "Wizard", 40)
    annoying_friend = Adventurer("XxX_Eepiline_Sõdalane_XxX", "Tulevikurändaja ja ninja", 999999)
    print(hero)  # -> "Sander, the Paladin, Power: 50, Experience: 0."
    # Ei, tüütu sõber, sa ei saa olla tulevikurändaja ja ninja, nüüd sa pead fighter olema.
    # Ei maksa liiga tugevaks ka ennast alguses teha!
    print(annoying_friend)  # -> "XxX_Eepiline_Sõdalane_XxX, the Fighter, Power: 10, Experience: 0."
    print(friend)  # -> "Peep, the Druid, Power: 25, Experience: 0."
    print(another_friend)  # -> "Toots, the Wizard, Power: 40, Experience: 0."
    print()

    print("Peep, sa tundud kuidagi nõrk, ma lisasin sulle natukene tugevust.")
    friend.add_power(20)
    print(friend)  # -> "Peep, the Druid, Power: 45, Experience: 0."
    print()

    world.add_adventurer(hero)
    world.add_adventurer(friend)
    world.add_adventurer(another_friend)
    print(world.get_adventurer_list())  # -> Sander, Peep ja Toots

    world.add_monster(annoying_friend)
    # Ei, tüütu sõber, sa ei saa olla vaenlane.
    print(world.get_monster_list())  # -> []
    world.add_adventurer(annoying_friend)
    print()

    print("Oodake veidikene, ma tekitan natukene kolle.")
    zombie = Monster("Rat", "Zombie", 10)
    goblin_spear = Monster("Goblin Spearman", "Goblin", 10)
    goblin_archer = Monster("Goblin Archer", "Goblin", 5)
    big_ogre = Monster("Big Ogre", "Ogre", 120)
    gargantuan_badger = Monster("Massive Badger", "Animal", 1590)

    print(big_ogre)  # -> "Big Ogre of type Ogre, Power: 120."
    print(zombie)  # -> "Undead Rat of type Zombie, Power: 10."

    world.add_monster(goblin_spear)

    print()
    print("Mängime esimese seikluse läbi!")
    world.add_strongest_adventurer("Druid")
    world.add_strongest_monster()
    print(world.get_active_adventurers())  # -> Peep
    print(world.get_active_monsters())  # -> [Goblin Spearman of type Goblin, Power: 10.]
    print()

    world.go_adventure(True)

    world.add_strongest_adventurer("Druid")
    print(world.get_active_adventurers())  # -> [Peep, the Druid, Power: 45, Experience: 20.]
    print("Surnuaias peaks üks goblin olema.")
    print(world.get_graveyard())  # ->[Goblin Spearman of type Goblin, Power: 10.]
    print()

    world.add_monster(gargantuan_badger)
    world.add_strongest_monster()

    world.go_adventure(True)
    # Druid on loomade sõber ja ajab massiivse mägra ära.
    print(world.get_adventurer_list())  # -> Kõik 4 mängijat.
    print(world.get_monster_list())  # -> [Massive Badger of type Animal, Power: 1590.]

    world.remove_character("Massive Badger")
    print(world.get_monster_list())  # -> []
    print()

    print(
        "Su sõber ütleb: \"Kui kõik need testid andsid sinu koodiga sama tulemuse mille ma siin ette kirjutasin, peaks "
        "kõik okei olema, proovi testerisse pushida! \" ")
