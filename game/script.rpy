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
define b = DynamicCharacter("b")
define pov = Character("[povname]")
<<<<<<< Updated upstream
define dave = ("Dave")
=======
define dave = Character("[Dave]")

# This sets all names to "???", so they can be revealed later
$ EE = REXB = LX = H = B/He = Wknd 1 = Wknd 2 = C = B = Dave = "???"
>>>>>>> Stashed changes

# The game starts here.

label start:
    scene bg uni #placeholder bg
    python:
        povname = renpy.input("What is your name?", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Student-Chan"

    jump named

label named: 

    "So your name is [povname]?"

    menu:

        "Yes":
            "Welcome to the definitive Rutgers Bus Dating experience! We hope you enjoy ;)" 
            jump intro

        "No":
            jump start

label intro:

    scene bg meadow #placeholder bg

    "It’s a sunny day at the college avenue student center. You are a new transfer student at Rutgers who just transferred from Penn State."
    "Right now, you’re waiting for the bus to go to your first class! Expository Writing! So exciting!!"
    "Suddenly, someone runs up behind you, calling your name. You look behind you in confusion."
    "???" "Ah [povname], it’s your first day too?"
    "It’s your childhood friend, Dave! From high school! He looks worried."

    show sylvie blue normal #placeholder sprite name

    pov "Hey Dave, what’s up! Is something wrong?"

    dave "The buses! Dude, haven’t you been checking Reddit? All the buses have disappeared! Nobody can get to class!!!!!"

    pov "On the first day? That’s horrible!"

    dave "I know! I’m gonna go grab a scooter and try heading to Cook/Douglass! I’ll catch you later bro, stay safe!"

    hide sylvie 
    
    "Dave died later that day :("

    "You think to yourself, maybe you shouldn’t take the scooter. It might just be a better idea to wait and see if a bus comes."
    "There’s no way a bus COULDN’T come, right?"
    $ b = "???"

    b "Oh my, how dreadful! No buses!"

    "A smooth, sultry voice calls out behind you. You whirl around in surprise, and immediately your face slowly starts burning."

    show sylvie green giggle

    "A man about twenty-two? years old wearing a navy blazer, black slacks and shoes, a rolex, and a light blue shirt with a tie that matched the blazer. Your eyes move up to his face and you feel your ears start burning."
    "A face that was sculpted from marble, with hazel eyes, thin gold framed glasses accentuating the deep hazel eyes. With high cheekbones and a californian tan? And black hair shaped and trimmed upwards with faded sides, you find yourself standing unable to even think coherently."

    pov "uhhhhhh...y-y-yes.."
    "you meekly say as your mind slowly resets."

    b "Oh my, how terrible, where are you trying to go?" 
    "He says as his voice continues to be as smooth as velvet."

    pov "Cook/douglass, I have a class called intro to expository writing there."
    "You manage to stammer out coherently as you slowly pull yourself together."

    b "Ah how interesting. Oh of course how rude of me now to introduce myself, you can call me B."
    "He says with a blinding smile."

    $ b = "B"

    pov "B, as in the letter ‘B’?"

    b "Exactly so, its sort of a nickname you could say"
    "He replies as smooth as before" #idk if this will be weird w/ the vn flow

    pov "I see, thats an interesting name. My name is [povname]"

    "You look at your watch and start to panic. You hastily bid B goodbye and start walking toward Cook/Douglass and hope that you dont get shot." 
    "As you leave, you realize your face is still burning from the man you had just met five minutes ago."
    

    # This ends the game.

    return
