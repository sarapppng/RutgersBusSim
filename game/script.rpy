# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define ee = Character("EE")
define rexb = Character("REXB")
define lx = Character("LX")
define h = Character("H")
define bhe = Character("B/He")
define w1 = Character("Wknd 1")
define w2 = Character("Wknd 2")
define c = Character("C")
define b = Character("B")
define pov = Character("[povname]")
define dave = Character("Dave")

image bg casc = "casc.jpg"
image bg classroom = "classroom.jpg"

# ok i think i fucked it up and this doesnt actually work loll?
#$ ee = rexb = lx = h = bhe = w1 = w2 = c = b = dave = "???"



# The game starts here.

label start:
    scene bg meadow #placeholder bg
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

    scene bg casc

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

    "???" "Oh my, how dreadful! No buses!"

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

    pov "B, as in the letter ‘B’?"

    b "Exactly so, its sort of a nickname you could say"
    "He replies as smooth as before" #idk if this will be weird w/ the vn flow

    pov "I see, thats an interesting name. My name is [povname]"

    "You look at your watch and start to panic. You hastily bid B goodbye and start walking toward Cook/Douglass and hope that you dont get shot." 
    "As you leave, you realize your face is still burning from the man you had just met five minutes ago."
    
    jump class1
    

    
label class1:

    scene bg classroom

    "Eventually, you make it to class. What a miracle! Only 30 minutes late!  Not too many other people are there. I guess today will be a small class."

    "Teacher:" "Hello class! As you are all aware, today the buses have disappeared. Therefore, I’m cancelling class for today. This is an unprecedented event in Rutgers history."

    "You sigh with relief. No more class! But wait, what do you do now that you’re on Cook/Douglass?"

    "???" "Seriously??? I ran ALL THE WAY HERE! AAAARGH!!!!!"

    "You look to your right to see who was sounding so upset, and see a tall, muscular student. He’s wearing a hoodie with ‘Rutgers Football’ on it, a backwards hat, some grey joggers and white Nike forces."

    "He’s cute… especially the blond curly hair of his messily sticking out of the hat and his blue eyes showing the frustration on his cute face."

    menu:

        "You’re cute!":
            jump rexb1

        "Yeah what he said! We came all the way over here for you to be late and to cancel class?":
            jump rexb2


    label rexb1:
        "???" "Thanks cutie, but now is not the time for that"
        "You turn your face away in embarrassment as he continues to rant and yell at the professor. Soon other students start joining in and supporting the handsome hunk."
        "Eventually the professor concedes and goes over the syllabus of the class. While that happens you feel someone tap your right shoulder, its the handsome hunk form before."

        rexb "sorry about that, but we had more important matters. My name is Rexb, I know its a little weird but that's what it is. What is your name?"

        "Your face flushes and you answer"

        pov "my name is [povname], sorry about what happened earlier I didn't mean to say that out loud."

        jump class1.2


    label rexb2:
        "The hunk smiles at you making you want to melt into a puddle of goo. The professor relents and proceeds to go over the syllabus. You turn over to the hunk next to you and say,"
        
        pov "Hey there, my name is [povname], and I think it’s really cool that you stood up and said what everyone else was thinking"

        "???" "Of course, I’m more that happy to help the class especially after how far we all had to travel. Oh by the way my name is RexB, a little unordinary but it fits."

        jump class1.2


label class1.2:
    "Before you know it class is over, but the professor has one last announcement. All classes are fully cancelled until further notice due to the buses disappearance disassembling the rutgers infrastructure."
    "You decide to look into the disappearance by going to the library since you paid to go to this school and want to get the most out of it. You get up and look at Rexb one last time, and bid him farewell."

    rexb "good bye cutie, I’ll see you around"
    "as he proceeds to put his hat back on and walk away. You stare at his retreating figure with a blush as you take in his more “noticeable” assets."
    "Shaking your head you walk away to find the nearest library, wondering how this day could get any weirder"

label library:
    scene bg library

    "You arrive at the library. Maybe you’ll find some answers about the bus disappearance here. You go upstairs to the history section, and at a table you see a long-haired student studying a textbook."
    "his gorgeous hair goes down past the table and to the floor. It’s a purple-ish silvery color. How beautiful!"
    "You sneak a glance at his paper that he’s writing on. At the top, he’s written his name as 'H' Interesting..."
    "You have to talk to him! How could you start a conversation?"
    
    menu:

        "hey sexy":
            h "Um… excuse me?"
            pov "You heard me ;)"
            h "Is this a prank? I’m clearly busy studying. I don’t have time for this."
            "bad choice."
            pov "Sorry, I just couldn’t resist not saying something. Your hair is really pretty. What are you studying?"
            "H rolls his eyes. He motions for you to sit down. I guess it worked?"
            h "I’m used to people flirting with me, but nobody has been as direct as you. However, I’m curious. I assume you didn’t come to the library to find a date?"
            jump library2


        "hi is this seat taken?":
            "H looks up at you, seeming slightly annoyed."
            h "no..."
            "You smile politely and take a seat, breaking out your laptop."
            pov "My name is [povname]! Nice to meet you! And you are?"
            h "My name is H. Just H. Did you come here to make new friends on the first day?"
            jump library2

label library2:

    pov "Actually no, I came to find a history book about the Rutgers buses"
    "Hearing this, H perks up. He seems surprised."
    h "Why the Rutgers buses?"
    pov "They’ve disappeared. I wanted to know if this has ever happened before in Rutgers history. I mean, buses don’t just disappear, right? I need to learn about buses."
    "H sits silently, pondering something. They meet your eyes"
    "He suddenly gets up and steps closer to your face. You can feel his warm breath on your skin as he whispers"
    h "I advise you to not investigate this further. For our sake"
    "H barges past you and runs out of the library, leaving their materials behind. You stare in astonishment."

    menu: 
        "Run after him":
            "You start running after H as fast as you can. He slides down the hand rail on the stairs and hits the floor running. This guy is insane!"
            "You attempt to jump down all the steps at once, but your ankle rolls. You fall to the floor, hit your head, and black out."
            jump hospital

        "Stay there":
            "You hear his footsteps slowly recede. Looking at the table, you decide to read his notes. What if he’s written his phone number on there somewhere?"
            "Reading them, you notice there’s a lot of fancy graphs and equations. They all seem to be about some sort of magical spell? Weird… "
            "All of a sudden you feel a bad headache coming on. Your stomach twists and a pain shoots up your spine. You black out."
            jump hospital

label hospital:
    "???" "ah, you'we awake, nya?"

    "You see a young looking man walk in, dressed in a nurse outfit. He has pink, scruffy hair, cat ears, and some smart looking glasses. He looks at you worryingly. You look down, and notice he has a tray of food."

    "???" "i bwought you something to eat, nya. you must be hungwy, nya. pawsitively stawving."

    pov "Ah, thanks! Yeah, I guess I am pretty hungry… how did I get here? And who are you?"

    bhe "ahhhh my apawlogies! My name is b/he! i’m a new nuwsing student hewe, nya."

    pov "Nice to meet you!"
    "B/he puts the tray of food down next to you. You get a closer look at his face and notice his freckles. How… how cute… "

    bhe " 2 othew students cawwed the heawth centew aftew they found uwu passed out own the gwound. rupd bwought uwu hewe tuwu me, awnd i’ve bewn taking cawe of uwu fow a whiwe now, nya"
    "He motions to a cup of soup"
    "You take a sip of the soup as bhe watches you expectantly. It’s delicious! Who knew this kind nurse was such a good cook, too!"

    bhe "NYAAAA WHAT DO YOU MEAN? Im not that cute uwu"

    pov "It's delicious!"

    "B/He giggles"
    bhe "i’m so happy that you wike it! i’m a good cook, nyaturally"

    "Suddenly there's a knock at the door. B/He goes over and opens it. 2 students come walking in. They look disappointed?"

    




















# This ends the game.
return
