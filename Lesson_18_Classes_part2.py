# Lesson-18-Classes-part2

from Lesson_17_Classes_part1 import *

class MageHero(Hero):
    """Class to create Mage Hero"""
    def __init__(self, name, lvl, race, magiclvl):
        """Initiate mage hero"""
        super().__init__(name, lvl, race)
        self.magiclvl = magiclvl
        self.mana = 100
        self.magicdmg = int(self.magiclvl) + int(self.lvl)/2

    def makemagic(self):
        """Use Magic"""
        self.mana = self.mana - self.magiclvl

    def show_hero(self):
        """Show parameters of created hero"""
        discription = (self.name + " Lvl: " + str(self.lvl) + " Race: " + self.race + " Health % : " + str(self.health)
                       + " Magic Lvl: " + str(self.magiclvl) + " Mana: " + str(self.mana)).title()
        print(discription)


newhero1 = Hero("Septic", "60", "Orc")
newenemy1 = Enemy("Elf", "20")
newhero2 = MageHero("Daenaer", "10", "Dark Elf", "5")


newhero1.show_hero()
newhero1.level_up()
newhero1.show_hero()
newhero1.move()
newhero2.show_hero()


newenemy1.show_enemy()