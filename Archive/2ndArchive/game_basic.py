import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

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

class Character(GameElement):
    IMAGE = "Horns" # attribute from GameElement

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

class Gem(GameElement):
    IMAGE = "BlueGem"
    SOLID = False

    # interact instance method (aka function)
    def interact(self, player):
        player.inventory.append(self)
        player.IMAGE = "Panda"
        GAME_BOARD.draw_msg("Hey you! You just acquired a gem! You have %d items!" % (len(player.inventory)))

####   End class definitions    ####

#handlers
def keyboard_handler():
    direction = None # local variable established

#    GAME_BOARD.draw_msg("What direction do you want to move?")    
    
    # keyboard commands that help define up, down, right and left
    if KEYBOARD[key.UP]:
        GAME_BOARD.draw_msg("You pressed up")
        direction = "up"
    if KEYBOARD[key.DOWN]:
        GAME_BOARD.draw_msg("You pressed down")
        direction = "down"
    if KEYBOARD[key.RIGHT]:
        GAME_BOARD.draw_msg("You pressed right")
        direction = "right"
    if KEYBOARD[key.LEFT]:
        GAME_BOARD.draw_msg("You pressed left")
        direction = "left"
    if KEYBOARD[key.SPACE]:
        GAME_BOARD.erase_msg()
    
    # loop that feeds direction to next_pos instance method under character
    # allows keyboard to tell where to move the player
    if direction:
        # var that takes the result next_pos which is a list of x,y
        next_location = PLAYER.next_pos(direction)
        # var that takes the position of x
        next_x = next_location[0]
        # var that takes the position of y
        next_y = next_location[1]

        # checks obejcts to determine if they exist (e.g. SOLID attirbute)
        existing_el = GAME_BOARD.get_el(next_x, next_y)

        # calls interact method if it exists and executes otherwise does nothing
        if existing_el:
            existing_el.interact(PLAYER)

        if existing_el is None or not existing_el.SOLID:
            # deletes the current player at position
            GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
            # places player at new position based on x,y received from next_pos
            GAME_BOARD.set_el(next_x, next_y, PLAYER)


#initialize    
def initialize():
    """Put game initialization code here"""
    rock_positions = [
            (5, 1),
            (3, 2),
            (3, 2),
            (4, 3),
            (5, 8),
            (7, 7)
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
    rocks[-1].SOLID = False

    GAME_BOARD.draw_msg("Find the fake rock.")

    # creates a gem on the board that is not solid as noted in its class above
    gem = Gem()
    GAME_BOARD.register(gem)
    GAME_BOARD.set_el(3, 1, gem)

    for rock in rocks:
        print rock
    
    # initialize player
    global PLAYER
    PLAYER = Character()
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(2,2, PLAYER)
    print PLAYER




