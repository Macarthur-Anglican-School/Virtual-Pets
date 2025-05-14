import random

genders = ["male", "female"]

class Pet():
    BABY = r""" v___v
(o)_(o)
`ʋ---ʋ`
"""
    CHILD = r""" V_____V
(O) w (O)
/| ___ |\
  U   U"""
    ADULT = r"""  W_______W
ᗧ(〇) W (〇)ᗤ
ᒪ/         \ᒧ
 \_________/
  ᗜ      ᗜ"""

    def __init__(self, name, age=0, gender=None, hunger=5, boredom=3, sleepiness=3):
        self.name = name
        self.age = age
        self.hunger = hunger
        self.boredom = boredom
        self.sleepiness = sleepiness
        self.__dead = self.check_death()

        if gender:
            self.gender = gender
        else:
            self.gender = random.choice(genders)
    
    def __str__(self):
        return f"""Name: {self.name}
Hunger: {'●' * self.hunger}
Boredom: {'●' * self.boredom}
Sleepiness: {'●' * self.sleepiness}"""
    
    def feed(self):
        if self.hunger > 2 and not self.__dead:
            self.hunger -= 3
    
    def play(self):
        if self.boredom > 2 and not self.__dead:
            self.boredom -= 3
    
    def sleep(self):
        if self.sleepiness > 4 and not self.__dead:
            self.sleepiness -= 5
    
    def wait(self):
        if not self.__dead:
            self.age += 1
            self.hunger += 1
            self.boredom += 1
            self.sleepiness += 1
    
    def kill(self):
        self.age = 15
        self.hunger = 10
        self.boredom = 10
        self.sleepiness = 10

    def check_death(self):
        return self.boredom >= 10 and self.sleepiness >= 10 and self.hunger >= 10 and self.age >= 15

def reproduce(pet1: Pet, pet2: Pet, name, **kwargs):
    if pet1.gender != pet2.gender:
        return Pet(name, **kwargs)
    else:
        raise Exception("Homosexual Alert")

bobby = Pet("Bobby")