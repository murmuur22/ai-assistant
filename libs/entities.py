import math

class Entity:
    def __init__(self):

        # Description
        self.name = ""
        self.title = ""
        self.background = ""

        self.health = 20

        # XP
        self.level = 0
        self.xp = 0

        # Stats
        self.strength = 20       # -> Damage
        self.dexterity = 20      # -> Dodge chance
        self.endurance = 20      # -> Defense
        self.intelligence = 20   # -> Proficency
        self.wisdom = 20         # -> 
        self.charisma = 20       # -> Charisma

        # Skills for skill checks
        self.skills = {}

        # Inventory
        self.inventory = {}


    def fight(self, opponent):
        opponent.damage(self.attack)

    # Damage function with attack/defense formula 
    def damage(self, amount):
        self.health -= math.floor(amount*(100/(100+self.endurance)))
        if self.health <= 0:
            self.kill()

    # Function to add an item to the inventory
    def inv_add(self, key, item):
        self.inventory[key] = item
    
    # Function to add an item to the inventory
    def inv_remove(self, key):
        return self.inventory.pop(key)

    def kill(self):
        pass

class Player(Entity):
    def __init__(self):
        pass

    def level_up(self):
        pass