"""
 Karel should place a zig zag pattern of beepers
 such that all odd columns have beepers in row 1 
 and all even columns have beepers in row 2
 """

from karel.stanfordkarel import *

def main():
    """
    Places beepers in a zig zag pattern.
    """
    while front_is_clear():
        diagonal_beepers()
        step_down()
        
def diagonal_beepers():  
    """
    Karel drops two beepers in a diagonal
    """
    put_beeper()
    turn_left()
    move()
    turn_right()
    if front_is_clear():#check for obstacle
        move()
        put_beeper()
        
def step_down():
    """
    karel steps down
    """
    turn_right()
    move()
    turn_left()
    if front_is_clear():#check for obstacle
        move()
        
def turn_right():
    """
    make three left turns to simulate a right turn
    """
    for i in range(3):
        turn_left() 

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
