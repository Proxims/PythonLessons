# Lesson-17-Classes-part1

class Hero():
    """CLass to create Hero"""
    def __init__(self, name, lvl, race):
        """Initiate hero"""
        self.name = name
        self.lvl = lvl
        self.race = race
        self.health = 100

    def show_hero(self):
        """Show parameters of created hero"""
        discription = (self.name + " Lvl: " + str(self.lvl) + " Race: " + self.race + " Health % : " + str(self.health)).title()
        print(discription)

    def level_up(self):
        """Level Up"""
        self.lvl = int(self.lvl)
        self.lvl += 1

    def move(self):
        """Star moving"""
        print(" Hero " + self.name + " Started to move...")

    def get_hit(self, Enemy):
        """Get damage from enemy"""
        self.health = self.health - Enemy.damage
        print(self.name + " Was hit by: " + Enemy.name + " And get damage %: " + str(Enemy.damage) + " Current health % : " + str(self.health))

class Enemy():
    """Class to create enemy"""
    def __init__(self, name, lvl):
        """Initiate enemy"""
        self.name = name
        self.lvl = lvl
        self.health = 100
        self.damage = int(lvl) +10

    def show_enemy(self):
        """Show enemy"""
        discription = (self.name + " Lvl: " + str(self.lvl) + " Damage: " + str(self.damage))
        print(discription)

#----------------------------------------------------------------------------------------------

