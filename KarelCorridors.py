from karel.stanfordkarel import *

def main():
    """
    Traverses variable length corridors and place beepers at the ends of them if there aren't already beepers there.
    """
    check_ceiling()
    
def check_ceiling():
    """
    Check if an obstacle exist to the north
    """
    turn_left()
    if front_is_clear():
        turn_right()
        drop_beeper()
    else:
        turn_right()
        move_to_wall()
        if no_beepers_present():
            put_beeper()
        turn_around()
        move_to_wall()
        turn_right()
    turn_right()
    

def drop_beeper():
    """
    drop beeper at the end of the corridor
    """
    move_to_wall()
    if no_beepers_present():
        put_beeper()
    turn_around()
    move_to_wall()
    turn_right()
    if front_is_clear():
        move()
    else:
        turn_right()
    turn_right()
    check_ceiling() # check if ceiling exist
    
def move_to_wall():
    """
    Move until Karel encounters an obstacle
    """
    while front_is_clear():
        move()
        
def turn_around():
    """
    Make two left turns to turn around
    """
    for i in range(2):
        turn_left()

def turn_right():
    """
    make three left turns to simulate a right turn
    """
    for i in range(3):
        turn_left()   


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
