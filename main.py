class Pet():
    def __init__(self, name, age=0, hunger=5, boredom=3, sleepiness=3):
        self.name = name
        self.age = age
        self.hunger = hunger
        self.boredom = boredom
        self.sleepiness = sleepiness
        self.dead = self.check_death()
    
    def feed(self):
        if self.hunger > 2 and not self.dead:
            self.hunger -= 3
    
    def play(self):
        if self.boredom > 2 and not self.dead:
            self.boredom -= 3
    
    def sleep(self):
        if self.sleepiness > 4 and not self.dead:
            self.sleepiness -= 5
    
    def wait(self):
        if not self.dead:
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

bobby = Pet()

####----Task 1----####
#Set up your pet with the following attributes:
#name (make this mandatory), age (default:0), hunger (default: 5), boredom (default:3), sleepiness(default:3)

####----Task 2----####
#instantiate your pet object with the name of your choice

####----Task 3----#### 
# We need to add the following methods to our Virtual Pet:
# 1. Feed - which will reduce hunger by 3
# use a selection to make sure if hunger goes below zero it gets reset to 0 (we don’t want any negative numbers.)
# 2. Play - which will reduce boredom by 3
# 3. Sleep - which will reduce sleepiness by 5
# 4. Wait - which will increase age, and increase hunger, boredom and sleepiness
# 5. Is_dead - which will check to see if the Pet has hit the thresholds we have set as the
# maximum possible hunger, boredom and sleepiness

###----Task 4----####
# Make a new method called check_death() that checks when a pet dies.
# These are the conditions I have chosen to use to determine if the pet should be dead.
# (Note: you can change these to make your pet harder or easier to keep alive)
    # ● Boredom is at 10
    # ● Sleepiness is at 10
    # ● Hunger is at 10
    # ● Age is at a random age between 15 and 20 or more


####---Task 5----####
#make it so that the feed, sleep, play and wait will check if the pet
#is dead before you upadate those properties.

#Go to page 9 of the tutorial to learn how to make the mainline (https://classroom.google.com/w/NzE2NTQ0NzA2MTYx/t/all)