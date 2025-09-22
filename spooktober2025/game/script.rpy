# Define characters here.

define s = Character(("Stella"), color="#f89797")
define p = Character(("Penelope"), color="#eaf897")

# The game starts here.

label start:

    play music title if_changed
    
    scene bg library

    "Curious to what treasures awaited in this little lost library, Penelope pulled at the knob screwed onto the little door, but it didn't budge. She furrowed her brow and tugged harder. The rusted metal hinges creaked ominously, greeting her entry."

    "A cloud of dust puffed in her face and she coughed, waving it away. Inside were two rows of weathered books, stacked neatly end to end, each one looking as old as the last. She brushed away some grime, tilting her head to get a better look at the titles along the edges."

    "Penelope's dismay grew as she recognized many of the titles, yet had very little interest in reading them. Classics, mostly, but nothing that seemed to excite her."

    p "Seriously, is it that hard to add one lousy Percy Jackson?"

    "She was about to close the door and trudge back down the hill when one small book, pressed against the edge by a large dictionary, caught her eye. She pulled it out to examine it, but found the gold lettering on the mahogany red cover seemed to be etched away." 

    "Mov- -era, By Stella Jac-."

    "Turning it over, Penelope's curiosity got the better of her as she flipped to the title page."
        
    "*Flash*"
        
    "Penelope screamed and dropped the book as if it were made of red-hot metal. Pages flipped furiously between the covers, some ripping out entirely and swirling above as if caught in a wild tornado. Pale blue light flashed in bursts like a firecracker." 

    "Penelope watched in horror as the long, slender form of delicate fingers rose from the book. An entire person seemed to rise out of the book, hovering gingerly in the air and stretching their arms, yawning loudly." 

    s "Well, I'llll be."

    show stella happy
    with fade

    "Penelope opened her mouth to scream again, but no sound came out. Her eyes filled with the image of the floating translucent lady smiling cheerfully down at her."


    #"Gandalf was taking a peaceful stroll until suddenly..."

    #show inigo happy
    #with moveinright

    #anything that isn't dialogue should have a # at the front like these notes do
    #to make writing faster, just indicate who is speaking with the lowercase first letter of their name before the quote like this:

    #voice "erin/name.MP3"
    #i "My name is Inigo Montoya. You killed my father. Prepare to die."
    
    #if the narrator is speaking, leave out name letter like this:

    #"He proceeded to stab Gandalf 37 times in the chest."
    #"You are a Goblin, Skeleton, or other low level mob working for a BBEG. The tale is a pick your own story as adventurers come in the dungeon, slaughter you, and you get resurrected by BBEG. You can talk to other monster NPC's and change the outcome of the game. One ending you manage to find your way out and escape the dungeon, one ending you start a labor union and work to get the minions health care and dental, one ending you overthrow the BBEG and take their place, one ending you work your standard 9-5 in the dungeon and climb up the corporate ladder til you get too old that the BBEG stops resurrecting you."

    scene black

    "THE END"

    # This ends the game.

    return
