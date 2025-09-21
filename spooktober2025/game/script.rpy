# Define characters here.

define i = Character(("Inigo Montoya"), color="#f8ee97")


# The game starts here.

label start:

    scene black

    "This is a story about murder....."
    
    scene bg gandalf

    "Gandalf was taking a peaceful stroll until suddenly..."

    show inigo happy
    with moveinright

    #anything that isn't dialogue should have a # at the front like these notes do
    #to make writing faster, just indicate who is speaking with the lowercase first letter of their name before the quote like this:

    i "My name is Inigo Montoya. You killed my father. Prepare to die."
    
    #if the narrator is speaking, leave out name letter like this:

    "He proceeded to stab Gandalf 37 times in the chest."
    "You are a Goblin, Skeleton, or other low level mob working for a BBEG. The tale is a pick your own story as adventurers come in the dungeon, slaughter you, and you get resurrected by BBEG. You can talk to other monster NPC's and change the outcome of the game. One ending you manage to find your way out and escape the dungeon, one ending you start a labor union and work to get the minions health care and dental, one ending you overthrow the BBEG and take their place, one ending you work your standard 9-5 in the dungeon and climb up the corporate ladder til you get too old that the BBEG stops resurrecting you."

    scene black

    "THE END"

    # This ends the game.

    return
