## Object-Oriented Practice

# MODULES
import time, os, pickle
import tkinter as tk
from random import randint
from scripts.browse_for_path import browse_for_path
        
# GAME OBJECT
class Game(object):

    # INITIALIZER
    def __init__(self):   
        # Stores player objects along with their IDs
        self.players = dict()

    # METHODS    
    
    # Creates a new player object
    def create_player(self):
        identification = len(self.players)
        name = input("What is the player's name?: ")
        classification = int(input("Are they a Warrior [0], Mage [1], or Archer[2]?: "))
        new_player = Player(identification, name, classification)
        self.players[new_player.identification] = new_player

    # Saves the game object
    def save(self):
        if not os.path.exists("saves/"):
            os.makedirs("saves/")
        pickle.dump(self, open("saves/Game_%s" % time.strftime("%Y-%m-%d"), "wb"))
        print()
        print("Game saved!")
        print()

    # Load data from a saved game object
    def load(self):
        self.players = pickle.load(open(browse_for_path(), "rb")).players
        print()
        print("Game loaded!")
        print()

# PLAYER OBJECT
class Player(object):

    # Class Defaults
    level = 1
    in_combat = False
    
    # INITIALIZER
    def __init__(self, identification, name, classID):

        # Initializer Constants (not needed outside of this scope)
        # TODO: Create Player creation UI
        # TODO: Break classifications down as subclasses of Player
        CLASSIFICATIONS = ["Warrior",
                           "Mage",
                           "Archer"]
        STARTING_HP = {"Warrior" : 30,
                       "Mage" : 10,
                       "Archer" : 15}

        # Attributes
        self.identification = identification
        self.name = name
        self.classification = CLASSIFICATIONS[classID]
        self.max_health = STARTING_HP[self.classification]
        self.current_health = self.max_health

    # METHODS

    # Calculates the damage done to a target
    def calc_damage(self, target):
        damage = randint(0, round(self.level * 2))
        return damage

    # Updates current health based on damage taken
    def take_damage(self, damage):
        self.current_health -= damage

    # Updates current health based on amount healed
    def heal_damage(self, heal):
        self.current_health += heal
        
    # Performs a level up
    def level_up(self):
        self.max_health += int((self.level * self.max_health) * 0.1)
        self.current_health = self.max_health
        self.level += 1
        print()
        print("%s leveled up!" % self.name)
        print()
        self.stats()
        print()

    # Gets player stats
    def stats(self):
        print()
        print(self.name)
        print("Level: %i" % self.level)
        print("Class: %s" % self.classification)
        print("Health: %i/%i" % (self.current_health, self.max_health))
        print()

    # Performs an attack
    # TODO: Make this more classification specific
    def attack(self, target):
        damage = self.calc_damage(target)
        target.take_damage(damage)
        print()
        print("%s attacks %s for %i damage!" % (self.name, target.name, damage))
        print()

    def fight(self, target):
        Fight(self, target) # Store this???


# FIGHT OBJECT (game state)
class Fight(object):

    # Class Defaults
    TURN = 1

    # INITIALIZER
    def __init__(self, initiator, target):
        # Set attributes
        self.initiator = initiator # Player object
        self.target = target # Player object

        # Set combat states
        self.initiator.in_combat = True
        self.target.in_combat = True

        # Run scene
        self.fight_scene()

        # Reset combat states
        self.initiator.in_combat = False
        self.target.in_combat = False

    # METHODS

    # Fight scene
    def fight_scene(self):
        fighting = True
        while fighting:
            # TODO: Create a turn-based fight
            print("Fight scene takes place between %s and %s."
                  % (self.initiator.name, self.target.name))

            # TODO: Check if fight is still going
            # Otherwise end fight
            fighting = False


# MAIN ENTRY POINT

if __name__ == "__main__":
    game = Game()
