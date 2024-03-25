from karel.stanfordkarel import *

"""
Karel should paint the whole world with beepers.
"""


def main():
    """
    no matter the size of the world, Karel should
    fill it with beepers
    """
    while left_is_clear():
        paint_row()
        reset_to_next_row()
    paint_row()
    
def paint_row():
        while front_is_clear():
            put_beeper()
            move()
        put_beeper()
    
def reset_to_next_row():
    """
    Pre: Karel is at the end of a row, facing right (East)
    Post: Karel is at the start of the next row, facing right (East)
    """
    turn_around()
    move_to_wall()
    turn_right()
    move()
    turn_right()
    
def move_to_wall():
    while front_is_clear():
        move()
    
    
def turn_right():
    for i in range(3):
        turn_left()
        
        
def turn_around():
    turn_left()
    turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
