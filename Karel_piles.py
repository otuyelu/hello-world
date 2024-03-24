from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.
def main():
    """
    Karel picks up all beeper in a row
    """
    while front_is_clear(): # check if obstable exist
        while beepers_present(): #check if beeper exist
            pick_beeper()
        move()
    # your code here
   
   
   
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
