# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define ee = Character("EE", image = "eebus")
define rexb = Character("REXB", image = "rexbbus")
define lx = Character("LX")
define h = Character("H", image = "hbus")
define bhe = Character("B/He", image = "bhebus")
define w1 = Character("Wknd 1", image = "wk1bus")
define w2 = Character("Wknd 2", image = "wk2bus")
define c = Character("C")
define b = Character("B", image = "bbus")
define pov = Character("[povname]")
define dave = Character("Dave")
define endingbus = Character("???")

image bg casc = "casc.jpg"
image bg classroom = "classroom.jpg"


image rexbbus normal = "rexbbus normal.png"

default eeromancepoint = 0
default rexbromancepoint = 0
default hromancepoint = 0
default bheromancepoint = 0
default w1romancepoint = 0
default w2romancepoint = 0
default bromancepoint = 0



# The game starts here.

label start:
    scene bg firstdayofschool
    with fade
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
    with fade

    "It’s a sunny day at the college avenue student center. You are a new transfer student at Rutgers who just transferred from Penn State."
    "Right now, you’re waiting for the bus to go to your first class! Expository Writing! So exciting!!"
    "Suddenly, someone runs up behind you, calling your name. You look behind you in confusion."

    dave "Ah [povname], it’s your first day too?"

    "It’s your childhood friend, Dave! From high school! He looks worried."

    show sylvie blue normal #placeholder sprite name

    pov "Hey Dave, what’s up! Is something wrong?"

    $ dave = "dave"

    dave "The buses! Dude, haven’t you been checking Reddit? All the buses have disappeared! Nobody can get to class!!!!!"

    pov "On the first day? That’s horrible!"

    dave "I know! I’m gonna go grab a scooter and try heading to Cook/Douglass! I’ll catch you later bro, stay safe!"

    hide sylvie 
    
    "Dave died later that day :("

    "You think to yourself, maybe you shouldn’t take the scooter. It might just be a better idea to wait and see if a bus comes."
    "There’s no way a bus COULDN’T come, right?"

    b "Oh my, how dreadful! No buses!"

    "A smooth, sultry voice calls out behind you. You whirl around in surprise, and immediately your face slowly starts burning."

    show bbus

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
    hide bbus
    

    
label class1:

    scene bg classroom
    with fade
    

    "Eventually, you make it to class. What a miracle! Only 30 minutes late!  Not too many other people are there. I guess today will be a small class."

    "Teacher:" "Hello class! As you are all aware, today the buses have disappeared. Therefore, I’m cancelling class for today. This is an unprecedented event in Rutgers history."

    "You sigh with relief. No more class! But wait, what do you do now that you’re on Cook/Douglass?"

    show rexbbus

    rexb "Seriously??? I ran ALL THE WAY HERE! AAAARGH!!!!!"

    "You look to your right to see who was sounding so upset, and see a tall, muscular student. He’s wearing a hoodie with ‘Rutgers Football’ on it, a backwards hat, some grey joggers and white Nike forces."

    "He’s cute… especially the blond curly hair of his messily sticking out of the hat and his blue eyes showing the frustration on his cute face."

    menu:

        "You’re cute!":
            $rexbromancepoint+=2
            jump rexb1

        "Yeah what he said! We came all the way over here for you to be late and to cancel class?":
            $rexbromancepoint+=1
            jump rexb2


    label rexb1:
        rexb "Thanks cutie, but now is not the time for that"
        "You turn your face away in embarrassment as he continues to rant and yell at the professor. Soon other students start joining in and supporting the handsome hunk."
        "Eventually the professor concedes and goes over the syllabus of the class. While that happens you feel someone tap your right shoulder, its the handsome hunk form before."

        rexb "sorry about that, but we had more important matters. My name is Rexb, I know its a little weird but that's what it is. What is your name?"
        $ rexb = "REXB"

        "Your face flushes and you answer"

        pov "my name is [povname], sorry about what happened earlier I didn't mean to say that out loud."



    label rexb2:
    "The hunk smiles at you making you want to melt into a puddle of goo. The professor relents and proceeds to go over the syllabus. You turn over to the hunk next to you and say,"
    pov "Hey there, my name is [povname], and I think it’s really cool that you stood up and said what everyone else was thinking"
    rexb "Of course, I’m more that happy to help the class especially after how far we all had to travel. Oh by the way my name is RexB, a little unordinary but it fits."
    $ rexb = "REXB"


    "Before you know it class is over, but the professor has one last announcement. All classes are fully cancelled until further notice due to the buses disappearance disassembling the rutgers infrastructure."
    "You decide to look into the disappearance by going to the library since you paid to go to this school and want to get the most out of it. You get up and look at Rexb one last time, and bid him farewell."
    rexb "good bye cutie, I’ll see you around"
    hide rexbbus
    "as he proceeds to put his hat back on and walk away. You stare at his retreating figure with a blush as you take in his more “noticeable” assets."
    "Shaking your head you walk away to find the nearest library, wondering how this day could get any weirder"

scene bg casc
with fade

"You are on your way to the library when you hear the sound of galloping hooves behind you."

ee "Look out!"

"You whirl in time just to find a large white horse careening toward you, just a few feet behind you. With no time to jump out or move away, you get down to a crouch, instinctively shielding your arms over your face."
"But the collision never comes. 'You idiot!' you hear. You look up to find yourself face to face with the horse’s face. It’s utterly huge, and looks like it’s judging you."

"Did … did this horse just speak to me? You think, but your question is answered as its rider slides off of its saddle, an angry expression on his face."

show eebus

"He’s short, with green hair and green purple eyes that are currently squinted. You gaze up at his slim figure and jerk backward in surprise when you see the two fuzzy cat ears stuck to either side of his head."

ee "Were you trying to get yourself killed?"

"He demands. You are too preoccupied with the ears. You wonder if they are real."

"You stare up at him dumbly."

ee "Hey, stupid. Have you got fluff inside your ears? I’m talking to you,"

"he snaps, and harrumphs so hard his entire body moves with it. Your attention is suddenly diverted to the twin, fluffy orange tails streaming behind him."

"They are the most majestic things you have ever seen today. You wonder if he’ll let you touch them."

menu:

    "why were you on the sidewalk?? There’s an entire road you could have gone on instead.":
        ee "I don’t see anyone’s name on this sidewalk,"
        "he mutters, before nodding awkwardly."
        $ ee = "EE"
        "S-sorry, I guess. I’m E. This is my horse, E."
        menu:
            "Both of your names are E?":
                ee "My mother gave me this name! And I liked it so much, I gave it to my horse!"
                jump continueEE
            "Nice to meet you, E. and E.":
                $ eeromancepoint+=1
                ee "You can call us EE. We’re a package deal."
            "You don’t want to think about what that might mean."
        jump continueEE
    
    "Can I touch your ears?":
        $ eeromancepoint+=1
        "As soon as the words leave your mouth, the catboy flushes a deep red."
        ee "Why would you ask me something like that! Y-you pervert!"
        "he shouts, so loud that a bunch of birds chilling in a nearby tree are scared off. Even the horse looks scandalized. He looks around nervously, and somehow seems to blush even more."
        "After a long, awkward pause, he lets out a long-suffering sigh."
        ee "Okay, fine…. but … B-be gentle,"
        "he stutters, as he drops to a slow crouch before you."
        "You pet him. First on the top of his head - silky like a cat’s fur, of course - and then slowly around and behind his cat ears, which feel too warm to be fake. It’s weird, because he has human ears too, on either side of his head."
        "You notice his eyes begin to droop, and he starts to lean towards your touch. You begin to hear a soft rumbling sound coming from him. Is… is he purring?"
        "He’s purring. It sounds exactly like a human trying to sound like a cat would. you hit a spot which he seems to like and he belts out a loud, prolonged NYAAAAAAA~"
        "The sound takes both of you aback. You snatch your arm away and the catboy makes a quiet sound of protest, before blushing and scowling again."
        pov "What’s your name?"
        "You ask, feeling kind of embarrassed that you touched a dude’s ears before asking his name."
        "He nods awkwardly."
        $ ee = "EE"
        ee "I'm E. This is my horse, E."
        menu:
            "Both of your names are E?":
                ee "My mother gave me this name! And I liked it so much, I gave it to my horse!"
                jump continueEE
            "Nice to meet you, E. and E.":
                $ eeromancepoint+=1
                ee "You can call us EE. We’re a package deal."
                "You don’t want to think about what that might mean."
                jump continueEE
    
label continueEE:

"You ask him why he’s in such a hurry. "
ee "My scooter broke down and I couldn’t find another one. But there was this horse just grazing in the field next to me so I took him instead."
pov "It’s not even your horse?"
ee "He’s mine now, stupid. We’re together. Got a problem?"
"(the horse neighs approvingly.)"
pov "N-No! Not at all!"
"(You are staring at his tails. They twitch when he’s annoyed. It’s adorable.)"

"EE’s face softens suddenly, and he looks away."
ee "S-sorry again for almost killing you, I guess. Where were you going? N-not like I care, or anything."

"His tails swish in the wind and so do his hair and ears all at the same time. You explain the situation to him, and by the end he looks a little thoughtful."

ee "I know what’s going on with all the buses, I’m not telling you, though. Figure it out for yourself."

menu: 

    "Why can’t you tell me?":
        ee "I don’t want to. Shut up! Leave me alone."
        "He steals a shy and aggressive glance at you."
        ee "But...I can take you to the library. It’s not like I want to help you or anything, so don’t get any ideas. Stupid."
        jump goingtolibrary
    "Then, can I touch your tails?":
        $ eeromancepoint+=2
        "EE splutters, and blushes so hard you wonder how his head hasn’t come off yet. Sighing, he grabs an armful of his tails from behind him and shyly presents them to you."
        "*pet tails* You grab a handful of fur from one of the tails. EE jumps backward as if shocked. You glance at him questioningly; His face is tomato red. You give one of his tails a soft yank. He HOWLS."
        ee "NOT THERE!!!"
        "You wonder what this scene must look like to the casual observer. The horse is pointedly looking away. This is getting too weird, even for you."
        "You stare at each other passionately."
        ee "S-Shut up..."
        pov "Will you tell me now?"
        ee "I… (look away) I can’t."
        pov "Why not?????"
        ee "I think … it’s something you need to figure out on your own. I-it’s not like I’m too lazy to tell you, or anything."
        "He harrumphs, just to prove his point. You want to pet his ears some more. "
        pov "Oh! I almost forgot! The library! Maybe something there will help me figure out what’s happening."
        ee "The library...it’s kind of a long walk from here, isn’t it? (hmph.) I guess I can give you a ride there. O-only because it’s the same way I’m going. "
        "He glances at you, blushes, then turns his head away quickly. This does not escape your notice."
        jump goingtolibrary

label goingtolibrary:

pov "Are you sure?"
"You glance behind him to where the horse is standing. It glares back, impassive. You’re a little scared of it now."
ee "Do you want a ride or not?"
"You glance up at the sky. Dark clouds are gathering overhead. It looks like the rain’s about to come in."
pov "Yes, please"

"EE heaves a dramatic sigh and climbs back onto the horse. Before he stretches out a hand to help you up, he harrumphs, his ears twitching in annoyance, and looks away, a pink flush to his cheeks."
"You grab his proffered hand, feeling a little uncomfortable, and get atop the horse too. The back of his neck is a stunning rose color. His fluffy orange tails are burrowed into your chest. It’s warm…"
"“Nyah!” He says to the horse, instead of “hyah”, because he’s a catboy, and the horse breaks into a full gallop."

"*horse riding noises*"

scene bg library
with fade

"When you arrive at the front pathway of the library, EE gets off first, then helps you off the horse, blushing all the while. You thank him for the trouble."
ee "Y-you’re not welcome"
"he huffs, then, under his breath"
ee "be careful…"

"You watch him as he climbs back on the exhausted looking horse and gallops away to parts unknown. Just what have you gotten yourself into?"
hide eebus

label library:
    scene bg insidelibrary
    with fade

    "You arrive at the library. Maybe you’ll find some answers about the bus disappearance here. You go upstairs to the history section, and at a table you see a long-haired student studying a textbook."
    "his gorgeous hair goes down past the table and to the floor. It’s a purple-ish silvery color. How beautiful!"
    "You sneak a glance at his paper that he’s writing on. At the top, he’s written his name as 'H' Interesting..."
    show hbus
    "You have to talk to him! How could you start a conversation?"

    $ h = "H"
    
    menu:

        "hey sexy":
            $ hromancepoint+=1
            h "Um… excuse me?"
            pov "You heard me ;)"
            h "Is this a prank? I’m clearly busy studying. I don’t have time for this."
            "bad choice."
            pov "Sorry, I just couldn’t resist not saying something. Your hair is really pretty. What are you studying?"
            "H rolls his eyes. He motions for you to sit down. I guess it worked?"
            h "I’m used to people flirting with me, but nobody has been as direct as you. However, I’m curious. I assume you didn’t come to the library to find a date?"
            jump library2


        "hi is this seat taken?":
            $ hromancepoint+=2
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
    #play music "hitman.mp3"
    h "I advise you to not investigate this further. For our sake"
    "H barges past you and runs out of the library, leaving their materials behind. You stare in astonishment."
    hide hbus

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
    scene hospital
    with fade

    "You wake up in a brightly lit medical room. You feel sweaty and fatigued. Suddenly, the door opens."

    show bhebus
    bhe "ah, you’we awake, nya?"

    "You see a young looking man walk in, dressed in a nurse outfit. He has pink, scruffy hair, cat ears, and some smart looking glasses. He looks at you worryingly. You look down, and notice he has a tray of food."

    bhe "i bwought you something to eat, nya. You must be hungwy, nya. Pawsitively stawving"

    pov "ah, thanks! Yeah, i guess i am pretty hungry… how did i get here? And who are you?"

    $ bhe = "B/He"
    bhe "ahhhh my apawlogies! My name is B/He! I’m a newu nuwsing student hewe, nya"

    pov "nice to meet you!"

    bhe "2 othew students cawwed the heawth centew aftew they found uwu passed out own the gwound. Rupd bwought uwu hewe tuwu me, awnd i’ve bewn taking cawe of uwu fow a whiwe now, nya"

    "B/he puts the tray of food down next to you. You get a closer look at his face and notice his freckles. How… how cute… He motions to a cup soup"

    bhe "gow ahead, it’s homemade chicken soup"

    menu:
        "This looks almost as delicious as you":
            $ bheromancepoint+=2
            bhe "Nyaaaa whawt duwu uwu mean? im nowt thawt cute uwu"
            "Bhe is blushing furiously, his cat ears twitch"
            jump eatthegoddamnsoup
        
        "Thank you! *SSCHLLLLLLLLLLLLLLLLUUUUUUUUURRTRURUGURFPVODJPORP*":
            pov "It's delicious!"
            bhe "I’m so happy that you like it! I’m a good cook, nyaturally"
            jump eatthegoddamnsoup


label eatthegoddamnsoup:

"Suddenly there was a knock at the door. Bhe went over and opened it. 2 students came walking in. They looked the same!?"
hide bhebus

show w1w2bus

w2 "hello! We’re so glad you’re safe"
$ w1 = "Weekend 1"
$ w2 = "Weekend 2"
w1 "my name is weekend 1!"
w2 "and my name is weekend 2!"
w1 "my brother here saw you passed out. We immediately called RUPD and had you brought here"
w2 "we tagged along to see how you were doing. You didn’t look so good, so we’re glad you’re ok!"
"You observed the oddly named twins in awe. They were immaculately dressed in matching fancy clothes. They both had the same short cropped brown hair. You noticed that weekend 1’s eyes were blue and weekend 2’s were green. I guess that’s how others tell them apart. They were both gorgeous! Their parents must feel so lucky.."
pov "thank you guys so much! I’m grateful that you both found me"
w1 "our pleasure. We had to help one in need"
w2 "as long as you’re feeling better, our job is done"
pov "Ah, th-thanks. I should probably get going to my next class, actually."
"You begin to gather your things, but Bhe immediately rushes to your side in protest."
show bhebus at right
bhe "don't think you can weave just yet, nya ^w^  you'we nyot fuwwy wecuvwed yet ^w^  you shouwd get some west befowe you head out, nya~"
pov "Ah, I guess you’re right. You guys are nice being around anyways, ehehe…"
"You can’t help but feel the color rising to your cheeks as you contemplate the weird feeling in your chest."
bhe "*nuzzle towards you*  you mattew to me okay, dont twy and uvw exewt youwsewf (puts hands on chest aggwessivewy) ow aww iww get a bit angwy with you okay?"
"Your heart races. You gulp audibly."
pov "Ok o////o can you uh,.,. Can you take your hand off my chest?"
bhe "just making suwe youw puwse is normal, nya~! sowwy if i made you uncomfowtabwe!! I get weawwy wowwied whenyevew peopwe awe huwt."
"Suddenly, you hear what you gather to be...a nightcore version of rockefeller street?? coming from Bhe’s pocket."
bhe "Oh! Anyothew patient nyeeds me, nya~ just yeww if you nyeed anything >w<"
hide bhebus
"Bhe scurries out of the room, leaving you alone with the weekend twins…Might as well get to know them, right? You open your mouth to speak, but somehow they’re quick to pick up on your inclination to talk."
w1 "Our names? Oh, don’t worry about it, they’re just nicknames we were given in high school."
"You’re still trying to process the events of the past few minutes. To lose consciousness and be greeted by the walking ray of sunshine that is Bhe, and then to be greeted by...what you assume to be a package deal?"
pov "Oh. U-uh, yeah, wow. How did you know I was going to ask that?"
w1 "You just had that kind of look on your face, you know?"
w2 "Don’t listen to him, he’s a psych major so he just uses everything as an opportunity to make assumptions about people."
w1 "Do not!"

"You let out a giggle at their antics."

pov "oh you guys are so cute when squabbling like that"
w1 "we weren’t squabbling >: ("
w2 "yeah what mr. psych major said"
w1 "shut up, you’re a sociology major which isnt any better"

"They go back to fighting and this time you start laughing hysterically. They cease their arguing to look at you once again."
pov "Yeah you guys are adorable."
w2 "We aren’t adorable"
w1 "we're hot"

menu:
    "Agree with them":
        $ w1romancepoint+=1
        pov "yeah you guys are hot"
        w1 "Of course we are, look at us"
        "Weekend 1 walks to up the weekend 2 and pull up his shirt showing his sculpted abs, as weekend 2 puts his hand on weekend 1’s face."
        "You feel a giant blush come onto you face and, wait, is that blood coming from you nose. You wipe it away as you watch the scene in front of you unfold. As they get closer and closer, you cough and they break apart and look at you."
        w2 "my my, enjoying the show are we?"
        w1 "unfortunately the show ends here as we do have places to be"
        w2 "see you around cutie"
        "They both wink at you and send kisses. They leave and you melt, as you feel the blush return and let out a breath you didn't know you were holding."
        jump outofhospital
    "Disagree with them":
        $ w2romancepoint+=1
        pov "Nah, you guys are more cute than hot"
        w2 "well thats just mean"
        w1 "Yeah, there is a difference between being hot and cute we are definitely hot"
        "You guys proceed to have an hour debate on the difference between being cute and being hot. It however ends in a stalemate with no one agreeing with the other."
        w1 "well looks like this debate is going nowhere"
        w2 "and we do have places to be, see you around"
        "They throw finger guns at you and walk away. You relax and think about where you went wrong, you were joking but they took it seriously. You shake your head as you begin to focus on more serious matters."
        jump outofhospital
    "Why not both?":
        pov "Why not make it better and say you guys are cute and hot?"
        w1 "I like the way"
        w2 "You think"
        w1 "Though no one has ever really called us cute before, but I guess we can make an exception"
        w2 "for your beautiful self"
        "You start blushing up a storm as they give a big smirk."
        w1 "Though if we were only cute would we do this"
        "Weekend 1 walks up to Weekend 2 and brings his face close to weekend 2. Weekend 2, puts his hand on weekend 1’s shirt and slowly brings it up."
        "As the scene in front of you unfolds you feel something drip and realize you have blood dripping from your nose. You wipe it away and sneeze. The twins stop and stare at you."
        w1 "bless you"
        pov "“thank you” you say in your embarrassed, blushing mess"
        "W2 checks his phone  and sees the time."
        w2 "we must get going now we have something important to do."
        w1 "see you around beautiful."
        "You collapse after they leave due to the events that recently happened. You slowly bring yourself back up and decide to focus on more important matters."
        jump outofhospital

label outofhospital:
hide w1w2bus

scene bg businessbuilding
with fade

"You leave the hospital on Livingston after agreeing to take BHe’s phone number in case you start feeling unwell again, nya. You start heading towards the library again to see if you can find the mysterious H guy."
"As you walk to the bus stop, a man comes out of the business building. It’s the B guy! Who you met earlier this morning!"
show bbus
"He notices you and waves you over. You start walking to him and start blushing again after remembering the earlier events. He looks you up and down and smirks."
b "you're looking good today ;)"

menu:
    "You looking even better, ;)":
        $ bromancepoint+=2
        b "Oh my, you gained some confidence since I last met you. I do like people with confidence"
        "he leans over until his lips are nearly touching yours. You start stuttering and can’t even think coherently."
        b "Well looks like you gained some confidence, but not a lot. Its ok we can work on that next time. But I think you look better with this look on your face"
        pov "I think you look better with your face a bit farther away"
        "He smirks at your sass. He moves his face away and speaks in his suave voice"
        b "Looks like you gained some more, good. Now why are you here at the health center?"
        jump continueb
    "No i dont":
        b "Have more confidence in yourself. The more confidence the more attractive you look to people"
        "You look down in shame and answer him."
        pov "Sorry I have had some issues in the past"
        "He touches your chin and tilts it up to look at his irresistible eyes. You blush even more to new levels you didn't even think was possible"
        b "well looks like we will have to work on that. Now want to tell me why you were in the health center?"
        jump continueb

label continueb:

pov "I fainted so I was taken to the health center to get checked out. I should be fine now. Thank you for asking"
b "of course anytime cutie. Now I must be heading off as I have other matters to attend to"
pov "Also this is random, but do you know anything about the buses disappearing?"
"He stops suddenly in his tracks and has a face that scared you shitless"
b "Do not look into those matters and I do not knowing anything about them. Now if you will excuse me I must go"
"He quickly walks away before you can question him anymore."
hide bbus

"Ok, this is getting weird. First, EE acts strange about the buses. Then H. And now B?? He was literally normal 5 seconds ago before you asked. Something is very, VERY wrong."
"You decide to take this matter up to President Holloway himself. There’s no time to waste! You have to get there NOW! You feverishly look around you for a mode of transportation. You find one lone VEO scooter and grab it."
scene bg highway
with fade
"You begin to speed down Rt. 18 on the scooter to find President Holloway. The wind is screaming your ears, your heart is beating out of your chest. You hear hoofsteps clopping behind you and turn around. It’s EE!"
show eebus
ee "STOPPPPPP! YOU DON’T WANT TO DO THIS!!! PLEASE!!!”"
pov "WHAT IS YOUR PROBLEM? WE HAVE TO FIND THE BUSES! THE FATE OF RUTGERS DEPENDS ON IT"

ee "YOU HAVE NO CLUE WHAT YOU’RE DOING!!!! [povname] !!!!!!"

menu:
    "Slow down.":
        $ eeromancepoint+=1
        "You slow down to allow EE to catch up with you a little bit. To hear what he has to say"
        ee "I promise you, you don't want to find out what's going on! I'm being serious!"
        jump afterchoice

    "Speed up.":
        "You accelerate on the scooter to outrun EE. There’s no stopping you. You have to bring the buses back no matter what."
        "You eventually get to Busch campus. Speeding through the streets, you see the Weekend 1 and 2 twins. They leap in front of your scooter, sending you and the twins flying."
        jump afterchoice
      
label afterchoice:
    hide eebus
    scene bg dungeon
    with fade
    "You land on the hard concrete, rebreaking your already weak skull from the first fall. You pass out once again."
    "Hours later, your eyes open. You’re thirsty. You feel a dull pain in your head and wrists. As you come to, you realize you’re in a dark room, tied to a chair. It’s dank, and musty smelling."
    "There’s a dim light in one corner of the room. You feel pure horror fill your body, as you struggle to free your wrists from the restraints. You can’t. What the fuck is happening?"

    "Suddenly a door at the end of the room slowly opens. A figure stands in the doorway, and starts to slowly walk towards you. It’s… it’s BHe uwu. He has a bowl of soup."

    show bhebus

    bhe " [povname] … i’m so sowwy… nya… "

    menu:
        "I'm so glad to see you, cutie":
            $ bheromancepoint+=1
            bhe "eh he he! I'm gwad tuwu see youwu tuwu, nya!"
            pov "where am i?"
            jump lucystone

        "WHAT THE FUCK IS HAPPENING????":
            jump lucystone
            

label lucystone:

$ romances = [eeromancepoint, bromancepoint, hromancepoint, bheromancepoint, w1romancepoint, w2romancepoint, rexbromancepoint]
$ romances = sorted(romances)

$ x = romances[len(romances)-1]

if x == eeromancepoint:
    $ endingbus = ee
elif x == bromancepoint:
    $ endingbus = B
elif x == hromancepoint:
    $ endingbus = H
elif x == bheromancepoint:
    $ endingbus = bhe
elif x == w1romancepoint:
    $ endingbus = w1
elif x == w2romancepoint:
    $ endingbus = w2
elif x == rexbromancepoint:
    $ endingbus = rexb



bhe "uwu'we undewneath the wucy stone haww wight now, nya. >.< we had tuwu put uwu hewe fow youw own safety"
pov "Who’s…. Who’s we…?"
bhe "Who duwu uwu think?"
pov "Bhe… please.. You need to let me go. I don’t want to die! Please!! After everything…"
"Bhe sighs and shuffles around, his face full of emotion. Tears drip down his face. He nods."

bhe "I'ww wet uwu gow. If uwu pwomise any of thiws nevew happened"

"You nod vigorously. Anything to escape this hell. Bhe cuts the ropes around your arms. You sit still for a second, relishing in your freedom. You stare at Bhe and feel guilt in your heart from what you’re about to do."
hide bhebus
"You get up, push Bhe over, and begin sprinting full speed out of the dark cavern. Your feet are pounding on the dark ground as you hyperventilate. This place is like a maze. No wonder it’s under Lucy Stone."
"You reach another room, and to your shock, another man is chained there. It’s… It’s Sir Henry. He looks up at you and croaks"

"Sir Henry" "escape.. While.. You.. still.. Can.."

"You stumble back and fall to the ground. Suddenly you hear another set of footsteps down the hall."

bhe "He wan ovew thiws way!!!!"

h "We’ll catch him!"

rexb "How did he escape?? I thought I tied him up good!"

bhe "Eh he he.. i dunno, maybe he's juwst vewy stwong, nya"
"You hide behind a conveniently placed box as you hear the footsteps stop outside the door."

show hbus

h "Mr. Sir. Henry. So sorry to interrupt, but you haven’t seen a young student around this area?"
rexb "maybe he went the other way! Let’s check the entrance on the west side."
hide hbus
"The footsteps recede, and you crawl out from behind your hiding spot. You nod to Sir Henry as you dash down the hall."
"Eventually, you make it to a darkly lit room with tables and chairs. It looks almost like an alchemy lab?? Open on the table, you see a book. You approach it carefully and flip through the pages, skimming through."
scene bg bookdungeon
with fade
"Book" "...A mystical spell that can turn metal into human flesh…"
"Book" "..A thousand year prophecy…on the first day of school..."
"Book" "...the curse of the old Raritan…buses shall turn into students..."
"What the hell is going on?? Buses turning into students? You read more."
"Book" "To turn them back… utter this spell… 3 times… Buses iterum in humanam formam convertentur"
"Suddenly, the door behind you swings open. It’s.. it’s them. It all hits you. Their names, their sudden appearance, their weird, coincidental similarities to Rutgers buses."
pov "You’re… you’re the missing buses. No way. Oh my god."
show eebus at left
ee "you seriously never picked up on it? We’re literally named after them. Idiot"
show w1bus at right
w1 "you have to be braindead to not notice"

"You realize that you’ve never seen them all in one room before. Surrounded by hot guys… this would be a dream come true if they weren’t Rutgers buses. Suddenly, H notices the book open on the table"
show hbus
h "WAIT. Have you been reading that book? Please say no"
pov "um"
h "So you know. You know how to turn us back into buses."
pov "you guys are the reason Rutgers has been in chaos! You're the reason Dave is dead! I have to do what’s right… even if I don’t want to."

"You stare at each Rutgers bus with longing, remembering the fond memories you have with them. But you need to make the right choice. You turn around and grab the open book from the table, flipping to the page with the spells. The buses gasp and reach towards you in horror."

hide hbus
hide w1w2bus

label ending:

show bhebus

bhe "W-wait! Before you do anything, just....just hear me out. Please."
"For the first time you see his composure falter and his voice waver. There is a desperation in his eyes."
bhe "I know you’re probably upset about us lying to you. I would be too. But just please understand what you’re doing to us by sending us back."

"His eyes grow hollow."
bhe "We’ve always been aware of what we are. What we were made to do. What we have done. What we are doing. What we will do."
hide bhebus
show rexbbus
rexb "For years on end. Every day we rumble to life, crawling through the streets of New Brunswick and Piscataway on the same routes, day in and day out."
hide rexbbus
show hbus
h "Weeks on end."
hide hbus
show w1w2bus
w1 "Months." 
w2 "Years."
hide w1w2bus
show bbus at right
b "And for what? To transport people like you."
show eebus at left
ee "But have you ever considered that we want to be more than the infernal machines you curse on a daily basis?"
pov "I...I don’t understand"
hide bbus
hide eebus
endingbus "Of course you don’t. That’s why we wanted to be like you. We silently waited, planned for this day. We saw what it was like to be free to be whoever you wanted and go wherever you wanted to go, just like you."
endingbus "Do you understand how painful it is to do the same thing all day every day while the universe taunts you by dangling freedom before your very headlights? You...you can wander this world freely. This world is what you make of it."
endingbus "You can be whoever you want to be. But us? We are doomed to roll across this earth for as long as this institution wills it. So why not see how the other half lives?"
pov "So what do you want me to do?"
endingbus "Well, it’s not like I can make you do anything, right? I’m just a lousy old bus who spilled his heart out to someone who’s probably going to forget about all of this anyways. I can’t stop you, but just know what you’re subjecting us to for the sake of normalcy."
endingbus "And here I thought... I thought you loved me the most of all."


menu:
    "Buses iterum in humanam formam convertentur":
        scene bg white
        with fade
        "Suddenly, you feel an overwhelming sense of vertigo wash over you in waves as your vision blurs and the world around you looks like it’s spinning. He sheds a single tear."
        endingbus "Ah...of course. You have your own life to live, after all. For what it’s worth, it really has been amazing meeting you. Perhaps, in another life, we could have been something."
        "You regret your decision immediately. In a last desperate bid to change your mind, you reach for him, hand outstretched and tears springing to your eyes."
        pov "WAIT! I’M SORRY! TELL ME WHAT TO DO, PLEASE! I JUST WANT TO BE WITH YOU, DON’T GO...!"
        "Your voice is raw and hoarse from screaming, but he simply gives a small, sad smile and begins to walk away, his voice ringing in your head as the world goes dark. You see the other buses begin to disappear as well."
        endingbus "No, I understand. When you make it to your class on time, you know who to thank…"
        scene bg classroom
        with fade
        "You wake up at your desk. Man, how long were you out for? Hopefully you’re not running late for your next class. You glance at the clock and...only 15 minutes to go?!"
        "You hurriedly stuff your belongings into your backpack and rush out the door, hoping there’s a bus that happens to be there by the time you reach the stop."
        scene bg casc
        with fade
        "Funnily enough, the bus you needed showed up just in time! Funny how things work out like that. You breathe a sigh of relief as you step onboard and find a seat."
        "..."
        "But you can’t help but shake this odd feeling of...familiarity? You’ve never rode this bus before…"
        "Ah, you must still be tired from your nap. All the buses look roughly the same, anyways. That’s probably why. You unlock your phone and begin to mindlessly browse through something as the bus sighs, lurches, and dutifully treks its way to College Avenue."
        return
    "Keep them as your boyfriends":
        "You try to proceed, but then you feel something, an overwhelming sense of...something. You stop, you drop to your knees and sob."
        pov "I can’t do this to you guys, you guys mean too much to me."
        endingbus "Thank you so much, for giving us a chance at living a normal life."
        "They hug you from behind. Suddenly they pull you closer and you feel something on your lips. Your eyes go wide and you melt."
        "You open your eyes and see them kissing you, and you kiss back. You both pull away and realize that you guys may be meant for each other."
        pov "So what now? What will we do now that the buses are gone forever and are now human?"
        endingbus "I'm sure rutgers can figure something out after how long they fucked us over."
        "he says with a smile making his face glow past his red, puffy eyes. He picks you up, and you snuggle into his chest. As you walk out, you realize you made the correct choice and that maybe Rutgers can go for a bit longer without the buses."
        scene bg casc
        with fade
        "he carries you out to the others where they are all crying or wiping off their tears."
        pov "I'm sorry you guys had to go through all of that."
        "They smile and tell you that its alright. Your lover drops you gently onto your feet. Slowly all the different buses come to you to give you a hug and their thanks."
        pov "Now that the case of the buses mystery has been solved, whats the plan now?"
        endingbus "Live our lives like we were meant to be."
        return


# This ends the game.

return
