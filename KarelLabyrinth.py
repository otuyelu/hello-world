"""
Karel moves forwards through a labyrinth
"""

from karel.stanfordkarel import *

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one!
    """
    while front_is_clear():
        move_to_wall()
        find_direction()
        
def find_direction():
    """
    check left and right in order to get Karel to face whichever 
    direction which isn't blocked off by a wall
    """
    if left_is_clear():
        turn_left()
    else:
        if right_is_clear():
            turn_right()
            
def turn_right():
    """
    make three left turns to simulate a right turn
    """
    for i in range(3):
        turn_left()   
def move_to_wall():
    """
    Move until Karel encounters an obstacle
    """
    while front_is_clear():
        move()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
