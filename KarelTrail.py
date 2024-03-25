"""
Karel follow the trail of beepers (picking up beepers as she goes)
until the end!
"""

from karel.stanfordkarel import *

def main():
    """
    Karel follow the trail of beepers 
    (picking up beepers as she goes) until the end!
    """
    while beepers_present():
        follow_straight_trail()
        step_backwards()
        # Check left
        turn_left()
        move()
        if no_beepers_present():
            # Trail doesn't continue to the left;
            # Go right
            step_backwards()
            turn_around()
            move()
        
def follow_straight_trail():
        while beepers_present():
            pick_beeper()
            move()
"""
def find_trail():
    turn_left()
    move()
    if beepers_present():
        follow_straight_trail()
    else:
        step_backwards()
        turn_right()
        move()
        if beepers_present():
            follow_straight_trail()
        else:
            step_backwards()
"""
def turn_right():
    for i in range(3):
        turn_left()
        
def turn_around():
    for i in range(2):
        turn_left()

def step_backwards():
        turn_around()
        move()
        turn_around()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
