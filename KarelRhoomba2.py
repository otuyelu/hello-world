"""
Karel is so good at cleaning up beepers that they decided to not just clean up 
one spot, but all of the spots! Lots of beepers have been spread across the world 
and Karel wants to clean them all up
"""

from karel.stanfordkarel import *

def main():
    # If we aren't at the top row (we use a while loop because we don't know how many rows there are)
    while left_is_clear():
        ### Pick up a row of beepers ###
        clear_beepers()
            
        if beepers_present():
            pick_beeper()
        
        ### Move back to the first column ###
        turn_around()
        move_to_wall()
        
        ### Move up to the next row ###
        turn_right()
        move()
        
        ### Reset Karel for loop pre-conditions by turning right to face East ###
        turn_right()
    
    ### Pick up the final row of beepers ###
    clear_beepers()
    
    if beepers_present():
        pick_beeper()
        
def clear_beepers():
    while front_is_clear():
        # Pick up a beeper if present
        if beepers_present():
            pick_beeper()
        move()
        
def turn_right():
    """
    make three left turns to simulate a right turn
    """
    for i in range(3):
        turn_left() 

def turn_around():
    """
    Make two left turns to turn around
    """
    for i in range(2):
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
