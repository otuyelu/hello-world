from karel.stanfordkarel import *

"""
File: KarelColumns.py
--------------------
Karel repairs each of the columns in the temple
"""

def main():
    """
    Karel has been hired to build the columns in the Temple
    of Artemis in Efes. In particular, there are a set of 
    arches where the stones (represented by beepers, of course)
    are missing from the columns supporting the arches
    """
    while front_is_clear():
        build_column()
        next_column()
    build_column()
    
def next_column():
    
    for i in range(4):
        move()
    
def build_column():
    """
    Build a column of beepers and return to floor
    """
    turn_left()
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    turn_around()
    while front_is_clear():
        move()
    turn_left()

def turn_around():
    """
    make two left turns to turn Karel around
    """
    for i in range(2):
        turn_left()

def turn_right():
    """
    make three left turns to simulate a right turn
    """
    for i in range(3):
        turn_left()
if __name__ == '__main__':
    main()
