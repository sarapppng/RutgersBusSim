# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define ee = Character("EE")
define rexb = Character("REXB")
define lx = Character("LX")
define h = Character("H")
define bhe = Character("B/He")
define w1 = Character("Weekend 1")
define w2 = Character("Weekend 2")
define c = Character("C")
define b = Character("B")
define pov = Character("[povname]")

define dave = ("Dave")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    label naming:

    povname = renpy.input("What's your name?", length = 32)
    povname = povname.strip()

    if not povname:
        povname = "Student-Chan"

    jump named

    label named:

    "So your name is [povname]?"

    menu:

        "Yes":

        "Welcome to the definitive Rutgers Bus Dating experience! We hope you enjoy ;)" 

        jump start

        "No":
        jump naming

    label start:
    "It’s a sunny day at the college avenue student center. You are a new transfer student at Rutgers who just transferred from Penn State."
    "Right now, you’re waiting for the bus to go to your first class! Expository Writing! So exciting!!"
    "Suddenly, someone runs up behind you, calling your name. You look behind you in confusion."
    "???" "Ah [povname], it’s your first day too?"
    "It’s your childhood friend, Dave! From high school! He looks worried."

    pov "Hey Dave, what’s up! Is something wrong?"

    dave "The buses! Dude, haven’t you been checking Reddit? All the buses have disappeared! Nobody can get to class!!!!!"

    

    e "Once you add a story, pictures, and music, you can release it to the world!"

    

    # This ends the game.

    return
