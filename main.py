import random
import time

genders = ["male", "female"]

class Pet():
    CHILD = r""" v___v
(o)_(o)
`ʋ---ʋ`
"""
    TEEN = r""" V_____V
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
        self.health = 50
        self.__dead = self.check_death()

        if self.age > 2:
            self.health = 70
        if self.age > 5:
            self.health = 100

        if gender:
            self.gender = gender
        else:
            self.gender = random.choice(genders)
    
    def __str__(self):
        if self.age < 3:
            char = Pet.CHILD
        elif self.age < 6:
            char = Pet.TEEN
        else:
            char = Pet.ADULT

        return f"""Name: {self.name}
Age: {self.age}
Gender: {self.gender}
Hunger: {'●' * self.hunger}
Boredom: {'●' * self.boredom}
Sleepiness: {'●' * self.sleepiness}
{char}"""
    
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

            if self.age > 2:
                self.health = 70
            if self.age > 5:
                self.health = 100
    
    def kill(self):
        self.age = 15
        self.hunger = 10
        self.boredom = 10
        self.sleepiness = 10

    def check_death(self):
        return self.boredom >= 10 and self.sleepiness >= 10 and self.hunger >= 10 and self.age >= 15

    def reproduce(self, pet, name, **kwargs):
        if self.gender != pet.gender:
            return Pet(name, **kwargs)
        else:
            raise Exception("🚨 Gay Alert 🚨")

def fight(pet1: Pet, pet2: Pet):
    while True:
        attack1 = random.randint(5, 20)
        pet2.health -= attack1
        print(f"🥊 {pet1.name} deals {attack1} damage to {pet2.name}! 🥊")
        print(f"🏥 {pet2.name} is at {pet2.health} health. 🏥", end="\n\n")

        if pet2.health <= 0:
            print("-" * 30, end="\n\n")
            print(f"☠️ {pet2.name} has lost the fight! ☠️")
            print(f"🏆 {pet1.name} wins! 🏆")
            
            return pet1

        time.sleep(1)
        
        attack2 = random.randint(5, 20)
        pet1.health -= attack2
        print(f"🥊 {pet2.name} deals {attack2} damage to {pet1.name}! 🥊")
        print(f"🏥 {pet1.name} is at {pet1.health} health. 🏥", end="\n\n")

        if pet1.health <= 0:
            print("-" * 30, end="\n\n")
            print(f"☠️ {pet1.name} has lost the fight! ☠️")
            print(f"🏆 {pet2.name} wins! 🏆")
            
            return pet2

        print("-" * 30, end="\n\n")

        time.sleep(1.5)

bobby = Pet("Bobby", 5)
charlie = Pet("Charlie", 5)

winner = fight(bobby, charlie)