"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    """
     Karel has been asked to make Zebra crossings. In the world of 
     Karel, a Zebra crossing is defined as a pattern beginning with 
     a 2-square wide column of beepers, followed by repeating pairs 
     of a 3-square wide gap and a 2-square wide column of beepers. 
    """
    while front_is_clear():
        paint()
        if front_is_clear():    # check if Karel has space to paint
            for i in range(4):
                move()
def paint():
    """
    Paint two line of beepers to make a zebra stripe
    paint_up()
    paint_down()
    
def paint_up(): 
    """
    Paint a line of beepers going up
    """
    turn_left()
    while front_is_clear():
        put_beeper()
        move()
    turn_right()
    put_beeper()
    move() 
    
def paint_down():
    """
    Paint a line of beepers going down
    """
    turn_right()
    while front_is_clear():
        put_beeper()
        move()
    turn_left()
    put_beeper()
    
def turn_right():
    """
    make three left turns to simulate a right turn
    """
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
