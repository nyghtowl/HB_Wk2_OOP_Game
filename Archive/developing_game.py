#handlers
def keyboard_handler():
    if KEYBOARD[key.UP]:
        GAME_BOARD.draw_msg("You pressed up")
        next_y = PLAYER.y - 1 # sets var to decrease y by 1 in order to move up
        GAME_BOARD.del_el(PLAYER.x, PLAYER.y) # deletes the existing character
        GAME_BOARD.set_el(PLAYER.x, next_y, PLAYER) # places the character in the new place
    elif KEYBOARD[key.SPACE]:
        GAME_BOARD.erase_msg()
    elif KEYBOARD[key.DOWN]:
        GAME_BOARD.draw_msg("You pressed down")
        next_y = PLAYER.y + 1
        GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
        GAME_BOARD.set_el(PLAYER.x, next_y, PLAYER)
    elif KEYBOARD[key.RIGHT]:
        GAME_BOARD.draw_msg("You pressed right")
        next_x = PLAYER.x + 1
        GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
        GAME_BOARD.set_el(next_x, PLAYER.y, PLAYER)
    elif KEYBOARD[key.LEFT]:
        GAME_BOARD.draw_msg("You pressed left")
        next_x = PLAYER.x - 1
        GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
        GAME_BOARD.set_el(next_x, PLAYER.y, PLAYER)
    else:
        GAME_BOARD.draw_msg("What direction do you want to move?")    

