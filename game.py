import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys
import random

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
KEYBOARD = None
PLAYER = None
######################

GAME_WIDTH = 9
GAME_HEIGHT = 9

#### Put class definitions here ####
class Rock(GameElement): # inheritence from GameElement class
    IMAGE = "Rock"
    SOLID = True # sets a class attibute of solid which is intrinsic property


class Panda(GameElement):
    IMAGE = "Panda"
    SOLID = False

    def interact(self, player):    
        GAME_BOARD.draw_msg("Welcome to your doom!")

class Tree(GameElement):
    IMAGE = "ShortTree"
    SOLID = True

    def interact(self, player):
        if player.IMAGE == "Princess":
            return
        else:
            Tree.SOLID = False
            player.inventory2.append(self)

class Character(GameElement):
    IMAGE = "Princess" # attribute from GameElement
    
    # instance method (like a function) that gives the class a character
    # returns a tuple
    def next_pos(self, direction):
        if direction == "up":
            return (self.x, self.y-1)
        elif direction == "down":
            return (self.x, self.y+1)
        elif direction == "left":
            return (self.x-1, self.y)
        elif direction == "right":
            return (self.x+1, self.y)
        return None
    # inventory is made as an instance attribute that can be reused
    # adds an initalizer (sets up object with inital values)
    # starts with an empty inventory
    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []

class Door(GameElement):
    IMAGE = "DoorOpen"
    SOLID = True

    def interact(self, player):
        #if key in player.inventory2:
        if player.IMAGE == "Princess":
            return
        elif 'key' in player.inventory2:
            GAME_BOARD.del_el(player.x, player.y)
            GAME_BOARD.set_el(1, 3, player)
        else: 
            return
#type(GAME_BOARD).__init__(GAME_BOARD, new_height, new_width)
#type(GAME_BOARD) => Class Board
#

# class Voodoo(object):
#     def method(self, x):
#         pass

# v = Voodoo()
# v.method(5) # Voodoo.method(v, 5)

class GrassBlock(GameElement):
    IMAGE = "GrassBlock"

class EndDoor(GameElement):
    IMAGE = "DoorOpen"
    SOLID = False

    def interact(self, player):
#        Board.__init__(GAME_BOARD, GAME_WIDTH, GAME_HEIGHT)        
        grass = GrassBlock()
        GAME_BOARD.register(grass)
        GAME_BOARD.set_el(4, 3, grass)

class Character2(GameElement):
    IMAGE = "Horns" # new character when choose gem

    # instance method (like a function) that gives the class a character
    # returns a tuple
    def next_pos(self, direction):
        if direction == "up":
            return (self.x, self.y-1)
        elif direction == "down":
            return (self.x, self.y+1)
        elif direction == "left":
            return (self.x-1, self.y)
        elif direction == "right":
            return (self.x+1, self.y)
        return Nonequit

    def __init__(self):
        GameElement.__init__(self)
        self.inventory2 = []

class Orangegem(GameElement):
    IMAGE = "OrangeGem"
    SOLID = True

class Greengem(GameElement):
    IMAGE = "GreenGem"
    SOLID = True


class Gem(GameElement):
    IMAGE = "BlueGem"
    SOLID = False

    # interact instance method (aka function)
    def interact(self, player):
        item = player.inventory.append(self)
        x_holder = player.x
        y_holder = player.y
        GAME_BOARD.del_el(player.x, player.y)

        global PLAYER
        PLAYER = Character2()
        GAME_BOARD.register(PLAYER)
        GAME_BOARD.set_el(x_holder, y_holder, PLAYER)
        print PLAYER
        PLAYER.inventory2.append(item)
        GAME_BOARD.draw_msg("Hey you! You just acquired a gem! You have %d items!" % (len(player.inventory)))
        
        door2 = EndDoor()   
        GAME_BOARD.register(door2)
        GAME_BOARD.set_el(2, 3, door2)

class Key(GameElement):
    IMAGE = "Key"
    SOLID = False

    def interact(self, player):
        if player.IMAGE == "Princess":
            Key.SOLID = True
        else:
            Key.SOLID = False
            player.inventory2.append('key')

####   End class definitions    ####

#handlers
def keyboard_handler():
    direction = None # local variable established

#    GAME_BOARD.draw_msg("What direction do you want to move?")    
    
    # keyboard commands that help define up, down, right and left
    if KEYBOARD[key.UP]:
#        GAME_BOARD.draw_msg("You pressed up")
        direction = "up"
    if KEYBOARD[key.DOWN]:
#        GAME_BOARD.draw_msg("You pressed down")
        direction = "down"
    if KEYBOARD[key.RIGHT]:
#        GAME_BOARD.draw_msg("You pressed right")
        direction = "right"
    if KEYBOARD[key.LEFT]:
#        GAME_BOARD.draw_msg("You pressed left")
        direction = "left"
    if KEYBOARD[key.SPACE]:
#        GAME_BOARD.erase_msg()
        pass
    
    # loop that feeds direction to next_pos instance method under character
    # allows keyboard to tell where to move the player
    
    if direction:
        # var that takes the result next_pos which is a list of x,y
        next_location = PLAYER.next_pos(direction)
        # var that takes the position of x
        next_x = next_location[0]
        # var that takes the position of y
        next_y = next_location[1]

      
       
        # make sure the game doesn't end if reach boundary of board
        if next_x >= GAME_WIDTH or next_x < 0:
            # GAME_BOARD.set_el(2, 2, PLAYER)
            return
        if next_y >= GAME_HEIGHT or next_y < 0:
            return
            # calls interact method if it exists and executes otherwise does nothing
      
        # checks obejcts to determine if they exist (e.g. SOLID attirbute) 
        existing_el = GAME_BOARD.get_el(next_x, next_y)
        print existing_el

        if existing_el:
            existing_el.interact(PLAYER)
            

        if existing_el is None or not existing_el.SOLID:
            # deletes the current player at position
            GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
            # places player at new position based on x,y received from next_pos
            GAME_BOARD.set_el(next_x, next_y, PLAYER)
        
        
def secondWorld():
    GAME_BOARD.draw_msg("Welcome to hell!")


#initialize    
def initialize():
    """Put game initialization code here"""
    GAME_BOARD.draw_msg("Shall we play a game?")

    rock_positions = [
            (0, 4),
            (1, 4),
            (2, 4),
            (3, 4),
            (3, 0),
            (3, 1),
            (3, 2),
            (3, 3),
            (6, 7),
            (6, 6),
            (7, 6),
            (6, 8),
            ]
    
    #rock list    
    rocks = []
    
    #loop to create rocks
    for pos in rock_positions: # pos it the list of rock positons
        rock = Rock()
        GAME_BOARD.register(rock) # register the rock on the board
        GAME_BOARD.set_el(pos[0], pos[1], rock) # set each rock in  one of the positions
        rocks.append(rock)

    # example of how you can change the attribute for an instance of an object
    # in this case for the last rock, we can change the SOLID attribute to false
#    x = random.randint(0, 6)
#    rocks[x].SOLID = False


 #   GAME_BOARD.draw_msg("Find the fake rock.")

    # creates a gem on the board that is not solid as noted in its class above
    gem = Gem()
    GAME_BOARD.register(gem)
    GAME_BOARD.set_el(6, 2, gem)

    gem2 = Orangegem()
    GAME_BOARD.register(gem2)
    GAME_BOARD.set_el(6, 3, gem2)

    gem3 = Greengem()
    GAME_BOARD.register(gem3)
    GAME_BOARD.set_el(5, 2, gem3)

    door = Door()
    GAME_BOARD.register(door)
    GAME_BOARD.set_el(7, 7, door)

    tree = Tree()
    GAME_BOARD.register(tree)
    for num in range(GAME_HEIGHT-1):
        GAME_BOARD.set_el(GAME_WIDTH-1, num, tree)

    key = Key()
    GAME_BOARD.register(key)
    GAME_BOARD.set_el(2, 6, key)

    for rock in rocks:
        print rock
    
    panda = Panda()
    GAME_BOARD.register(panda)
    GAME_BOARD.set_el(1,2, panda)
    print panda

    # initialize player
    global PLAYER
    PLAYER = Character()
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(5,7, PLAYER)
    print PLAYER


    