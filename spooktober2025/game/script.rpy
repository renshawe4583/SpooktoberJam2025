# Define characters here.

define s = Character(("Stella"), color="#97b9f8")
define p = Character(("Penelope"), color="#97f8e0")
define a = Character(("Attendant"), color="#9e97f8")
# custom screen transition - quickly fades to white, then back to the scene.
define flash = Fade(0.1, 0.5, 0.5, color="#fff")
# custom character fade out
transform slowdissolve:
    alpha 1.00
    easein 15.0 alpha 0.00

# The game starts here.

label start:

    #play music main_theme if_changed
    
    scene bg library

   
    "Curious to what treasures awaited in this little lost library, Penelope pulled at the knob screwed onto the little door, but it didn't budge. She furrowed her brow and tugged harder. The rusted metal hinges creaked ominously, greeting her entry."

    "A cloud of dust puffed in her face and she coughed, waving it away. Inside were two rows of weathered books, stacked neatly end to end, each one looking as old as the last. She brushed away some grime, tilting her head to get a better look at the titles along the edges."

    "Penelope's dismay grew as she recognized many of the titles, yet had very little interest in reading them. Classics, mostly, but nothing that seemed to excite her."

    p "Seriously, is it that hard to add one lousy Percy Jackson?"

    "She was about to close the door and trudge back down the hill when one small book, pressed against the edge by a large dictionary, caught her eye."

    "She pulled it out to examine it, but found the gold lettering on the mahogany red cover to be etched away." 

    '{i}"Mov- -era, By Stella Jac-."'

    "Turning it over, Penelope's curiosity got the better of her as she flipped to the title page."
        
    scene bg library
    with flash
        
    "Penelope screamed and dropped the book as if it were made of red-hot metal. Pages flipped furiously between the covers, some ripping out entirely and swirling above as if caught in a wild tornado. Pale blue light flashed in bursts like a firecracker." 

    "Penelope watched in horror as the long, slender form of delicate fingers rose from the book. An entire person seemed to rise out of the book, hovering gingerly in the air and stretching their arms, yawning loudly." 
    
    voice "Stella/Stella001.MP3"
    s "Well, I'llll be."

    show stella happy
    with dissolve

    "Penelope opened her mouth to scream again, but no sound came out. Her eyes filled with the image of the floating translucent lady smiling cheerfully down at her."
    voice "Stella/Stella002.MP3"
    s "Aren't you just the cutest little thing?"

    p "A-bah...ah ga ga..."
    voice "Stella/Stella003.MP3"
    s "Oh, mercy me! You must be mortified. I'm sorry for the little scare. Here, let me help you up."

    "She gracefully bent down and extended a hand towards Penelope. Penelope took it without thinking, still awestruck. As she reached out, the woman's hand felt smooth and cold to the touch."
    voice "Stella/Stella004.MP3"
    s "Much better."

    p "Who-, or what are you even?"
    voice "Stella/Stella005.MP3"
    s "Where are my manners? Why, I'm the great Stella Jackson."

    "A flash of hesitation seemed to cross her eyes as she looked down at her translucent form."
    voice "Stella/Stella006.MP3"
    s "As for what, it appears that I am some apparition of sorts."

    p "You mean you don't know?"
    voice "Stella/Stella007.MP3"
    s "I guess I don't. Last thing I remember was rolling around in my grave, eternal beauty rest and all, when some strange figure appeared."
    voice "Stella/Stella008.MP3"    
    s "Large fellow, I reckon, he seemed to reach down and scoop me up right up. Carried me for a while, and plopped on this here shelf. That's when you came along."

    p "That doesn't answer a ton of questions. Why were you even in a book to begin with?"

    "Stella looked down and carefully picked up the novel, turning it over in her hands curiously."
    voice "Stella/Stella009.MP3"
    s "Well, if it ain't my old autobiography. I remember writing this between takes on Up and Away."

    "Stella thumbed through the now still pages before pressing the book close to her chest."
    voice "Stella/Stella010.MP3"
    s "My, what gorgeous days those were. Bright lights, caviar, flip tops, the BOYS!"

    p "Flip-tops?"
    voice "Stella/Stella011.MP3"
    s "Oh, to be swept up on the stage again. To see the pictures come alive. Sigh"
        
    p "Like, a movie?"
    voice "Stella/Stella012.MP3"
    s "Why yes. It was a miracle to be a part of."

    p "Wait, you were, like, a movie star?"
    voice "Stella/Stella013.MP3"
    s "One of the very best, dear. You couldn't walk down Hollywood Boulevard without seeing my name in lights."

    p "Sooo, what happened?"

    "The actress's expression dropped."
    voice "Stella/Stella014.MP3"
    s "I was...on the way to a premiere. It was shaping up to be my biggest night yet. The cameras were flashing, the crowd was cheering, I guess with all the commotion, I didn't notice the two headlights coming my way."

    "Stella shook her head, as if to shake the painful memories loose."
    voice "Stella/Stella015.MP3"
    s "But that's all in the past now. Boy, I sure wish I could have seen that show."

    p "Why don't you? Go see a show, I mean. You have all eternity, don't you?"
    voice "Stella/StellaLaugh.MP3"       
    "Stella laughed."
    voice "Stella/Stella016.MP3"        
    s "Oh, would if I could, darlin. But it don' work like that. My soul is where I was put to rest, and since I'm in this here cemetery, this cemetery is where I stay."
        
    "Penelope paused, waiting for the moment to catch up with her new airhead friend. Moments passed before she spoke."

    p "Buuut, you're not in the cemetery."

    "Stella blinked, unsure of what she had just heard, before turning to notice the two of them standing before the library outside of the wrought iron gate."
    voice "Stella/Stella017.MP3"
    s "Mercy me, it would appear so."

    "Her eyes widened and shone like stars."
    voice "Stella/Stella018.MP3"
    s "Do you know what this means?"

    p "You're no longer under house arrest?"
    voice "Stella/Stella019.MP3"
    s "Why, we can go have the night of our lives, silly!"

    "She bounced in the air, clapping her hands, getting excitedly close to Penelope."
    voice "Stella/Stella020.MP3"
    s "Ooo, we can go to the supermarket, or dress shoppin', or dance to the jukebox, or-"

    p "Woah whoa whoa, won't that freak everyone out to see a ghost wandering around town?"

    "Stella paused to think."
    voice "Stella/Stella021.MP3"        
    s "You got over it rather quickly, wouldn't cha say?"

    p "Touche."
    voice "Stella/Stella022.MP3"        
    s "This is gonna be so much fun! What should we do first?"

    "Penelope glanced down at her half-dead watch, ticking away at her curfew."

    p "Nothing too crazy, I need to be back by nine."
    voice "Stella/Stella023.MP3"        
    s "Oh, of course, dear. We'll have a night on the town and be back in a jiffy."

    "Penelope walked down the hill toward the small town at the bottom, Stella hovering gleefully behind her, chatting away."
    voice "Stella/Stella024.MP3"
    s "{i}Gasp,{/i} I remember when that was the local sock hop bowlin' alley. Over there, they used to sell everything from vacuums to washers, everything an average housewife would need."
    voice "Stella/Stella025.MP3"
    s "I can't believe they still have the old mill. Don't even get me started on how it used to smell."
    hide stella happy
    with dissolve
    "Penelope rolled her eyes. It was like talking to her grandma. She kept searching for people's reaction to her disembodied friend, but no one seemed to pay them any mind. It was just an average evening in Greensville."

    "As she breathed a sigh of relief, she noticed the only thing she could hear was her sneakers on the cold pavement. The night had gone uncharacteristically quiet."

    "Glancing around, Stella was nowhere to be seen. Panic started to creep up Penelope's throat as she doubled back, checking across the road and looking into alleyways."

    "Finally, she turned around the corner store and found Stella staring sorrowfully into an outcropped storefront."
    show stella happy
    with dissolve
    p "What happened? I thought I lost you."

    "Penelope followed her eyes, connecting the dots to a flashing movie poster."

    '"{i}Tonight only: Tim Cruise stars in Objective Improbable 8."'

    "Penelope smiled. Without a word, she marched through the door and up to the ticket counter."

    scene bg theater
    with dissolve

    p "Two for Objective Improbable, please."

    "The bored-looking attendant sized her up and down before glancing behind her."

    a "You got a friend coming late? Show starts in seven minutes."

    p "Oh -erm, I guess one for Objective Improbable, actually."

    "The clerk shrugged, accepting Penelope's outstretched allowance and traded her a ticket stub before returning to his game of staring off into space, oblivious to Stella squealing behind Penelope."
   
    show stella happy
    with dissolve

    voice "Stella/Stella026.MP3"
    s "Eeeee, thankyouthankyouthankyou, my gracious, I can't believe I get to wake up and see an honest to god twenty first century movie for the first time in 70 years. Oh, what should I wear? Is my hair ok? Do you think I need a touch-up? Hey, where ya going?"

    "Penelope reappeared holding some popcorn bought with the rest of her weekly allowance, and they stepped into the theater together."

    scene black
    with dissolve

    "She helped Stella find their seats. The theater was sparse with guests, with plenty of vacant rows in between."
    voice "Stella/Stella027.MP3"
    s "Ain't this just swell? Best chairs in the house, I say. You mind if I try some of that there popped corn?"

    "The screen blared with an endless stream of advertisements. Stella bounced in her seat, gasping at every movie trailer, pointing out similarities to her old film days, and rating every male actor based on their hotness."

    "Penelope was just starting to worry that the ghost would end up yapping through the whole movie when the lights dimmed and the curtain unfurled."

    "Actors flashed into view, running across the top of a train in a dramatic chase." 
    
    "Penelope got a gnawing feeling in her stomach. What if the actress didn't like action movies? She probably preferred romance, drama, and musicals." 
    
    "Shifting in her seat, she glanced over at Stella."

    "Her mouth was agape, eyes wide, utterly enchanted with the scene on screen."

    scene bg theater
    show stella happy
    with dissolve

    voice "Stella/Stella028.MP3"
    s "That was INCREDIBLE! Can you believe they flew those aeroplanes upside down? I nearly jumped out of my skin. Why, that must have taken decades' worth of production. And the music was so thrilling, I can still feel it rattling my bones. If I had bones, that is."

    "Stella snorted at her own joke."
    scene black
    with dissolve
    "The pair compared their favorite moments, walking on air as they climbed the hill at the edge of town. A small box nailed to a sturdy wooden post crept into their view."
    
    scene bg library
    show stella happy
    with dissolve
    "The conversation began to trail away as the end of their walk neared. Penelope could feel the energy drain from Stella's voice with every step."

    p "What is it, what's wrong?"

    "Stella opened her mouth to say something, but no words came out. She took another breath and tried again."
    voice "Stella/Stella029.MP3"
    s "I get the feeling, this might have been a one-time thing. Something's tellin' me that it's going to be a very long time before we see each other again."

    "Penelope's throat became tight, not wanting to acknowledge the end to their story. Stella turned to face her, grinning from ear to ear."
    voice "Stella/Stella030.MP3"
    s "Thank you, sweetheart. This has been the best evening a girl could ask for."

    p "But-why? I don't understand. Why do you have to go?"

    "Stella drifted closer to Penelope, gently folding the book into her hands."
    voice "Stella/Stella031.MP3"
    s "When I was…asleep, I always felt like I had been cheated out of the night that I passed. While I had come to accept my circumstances, it always bothered me."
    voice "Stella/Stella032.MP3"
    s "All I wanted was one more night. One night at the movies, where I could be myself, and not a character I play on screen."

    "Stella's gentle and icy hand brushed the hair out of Penelope's view as her own pearly eyes welled up with tears."
    voice "Stella/Stella033.MP3"
    s "And darlin', you did exactly that. And I can't thank you enough. For being you, n' all."

    p "Please-"

    "Penelope caught her breath when the pale moonlight shone more clearly through Stella's increasingly translucent form."

    show stella happy at slowdissolve
   
    "As if evaporating into a cloud of mist, the ends of her pointed dress, the tips of her delicately manicured fingers, all began to lose their shape and drift away in the breeze."
    voice "Stella/Stella034.MP3"
    s "You hold onto that there story, hon. It feels…special. At least to me."

    "Stella's gentle smile began fading into the cold autumn night."

    "Penelope clutched the book and hugged it tightly to her chest."

    p "Then, it's special to me too."



    
    scene black
    with fade

    jump harley

label harley:

    "The next night..."
    scene bg library
    with dissolve

    "As the leaves crunch beneath Penelope's feet, the familiar little box of stories beckoned her from the other side of the road." 
    "Excited at the prospects of today's adventure, she raced over to flip the latch and open the small makeshift library posted on the curb. The usual books were still right where she left them, untouched, unmoving, but filled with potential."
    "Penelope scanned the small wooden shelves for new stories. Moby Dick, The Great Gatsby, War and Peace. Nothing looked out of place this time. Surely, there has to be one."
    "She furrowed her brow at the books again, taking a second, even a third look at each of them."
    "Romeo and Juliet, To Kill a Mockingbird, Harley and Me, Game of Thrones, Bli...wait, Harley? That one misplaced letter almost ruined her day."
    "Penelope rolled her eyes, already guessing at the next colorful character to this lonely graveyard."
    p "Probably some unfunny prankster who needs me to write jokes for them, ha." 
    "She slid the book out, finding it surprisingly thin, nothing more than a simple picture book. The ink was bright red against a white backdrop.  A picture on the front depicted two figures in a tight but gentle embrace."
    "Penelope flipped open the book, looking up to greet her next friend."
    "A moment passes."
    "Then another. She looked around the empty field, worried she had chosen wrong. Maybe it was just a printing error."
    show harley happy at offscreenright
    show harley happy:
        xalign 2.0
        linear 1 xpos 0

    "Suddenly, something barreled past her legs! It almost knocks Penelope to the ground, racing somewhere behind her vision."
    "She turned her head and caught a glimpse, not of something ghostly pale or blue, but a blur of something much brighter, standing out against the misty, chilly morning."
    show harley happy at offscreenright
    show harley happy:
        xalign 2.0
        linear .5 xpos 0
    
    "It raced around her again, circling, but oddly, not threatening. She paused, excited with anticipation."
    "In one quick movement, Penelope snapped around the other direction, determined to catch it off guard. The light jerked off course and crashed straight into her, sending the two of them tumbling."
    "Worried from the impact of the rogue fireball, Penelope winced, struggling to find her breath. It felt like an elephant was lying on her chest."
    "A very furry elephant...panting heavily from its recent burst of zoomies."
    hide harley
    show harley happy

    "She opened her eyes to the large grinning dog, sitting proudly on her chest, his face only an inch or two from hers."
    p "Oh my god, don't do that."
    "The dog sank further into her chest as her body relaxed, now relieved of the unsure danger."
    "Penelope reached up to scratch the dog's head as he leaned heavily into her hand, his collar jingling with every bob of his head. On the end, in nice printed letters is the name: Harley."
    p "Of course." 
    "Pushing off the dew-soaked grass, Penelope tried to sit up. To Harley's reluctance, he shifted to lie awkwardly in the crook between her chest and knees, oblivious to her attempts at escape."
    "She ran her hand down his back as he stared off at something in between the trees, his tail thumping happily on the ground, spraying her already soaked tee shirt with more dew."
    p "Ok, Harley."
    "His head turns at the recognition of his name, finally stepping back and giving her his full attention. Without him suffocating her, she could hardly tell he's a ghost at all."
    "Instead of a slightly translucent pale color, Harley's golden retriever form seemed to be a warm tinted yellow."
    "From a distance, he'd look just like any other dog...but in reality...Penelope pushed the harrowing thoughts away, knowing full well what they'd lead to."
    "Harley started sniffing around Penelope's feet, curious about a new discovery he had made. As she stooped down to take a closer look, Penelope heard a loud crunch as Harley's jaws clamped together."
    "Without hesitation, he took off, putting 10 feet between him and Penelope before checking back to make sure she was following."
    p "Whatever it is, that can't be good." 
    "Penelope took off, tearing after the mischievous pup, clearly proud of the prize trapped between his jaws."
    "Penelope's shoes pounded against the twigs and high brush in hot pursuit of four bounding paws."
    "Harley raced around a tall gravestone, poking his head out to check if she had seen him before taking off again, following the low brick wall in a fast-paced trot."
    "Eager to cut him off, Penelope followed close behind, but with enough distance to quickly adjust once he reached the corner."
    "Before she realized it, Harley had slipped behind a large bush and disappeared through the wrought iron fence."
    "Penelope pushed the neglected, pointed twigs aside to reveal a small hole in the fence, barely big enough for her to squeeze through."
    "Harley sat patiently on the other side, watching her, slowly gnawing on an estranged pine cone between his teeth."
    "{i}Sigh{/i}. Penelope crawled on all fours, not looking forward to explaining the new mud stains on her jeans to her parents."
    "Brushing off the dirt, she glanced around the large open field situated next to the cemetery. Clearly there wasn't a lot of interest in dead smelling real estate."
    "Harley's tail thumped against the ground, congratulating her on her journey. His head approached low, gently placing the slobber-soaked pine cone at her feet."
    "Leaping back, he braced for the chase, dropping his front legs and staring intently at the unmoving tree seed."
    "Penelope gingerly plucked the pinecone from the ground, careful to avoid the areas that were clearly more damp than others."
    "Harley's happy grin turned into brainless determination, the sides of his face relaxing into a droop as his eyes followed the makeshift ball."
    "At least the summer softball season Penelope's parents signed her up for wouldn't go to waste."
    "Winding up, she shifted her balance and launched the cone with all her might. Harley barreled after the toy, sprinting at top speed for the first time in decades."
    "Penelope soaked in the simplicity of it all, as Harley triumphantly bounced back to her with his prize, his hurried golden form circling her legs, clearly looking for good boy pets with every pass."
    p "Good job buddy, hehe. Now drop it."
    "The dog hesitated, his glazed eyes staring up at her. She tried again, a little sterner-"
    p "...Drop it." 
    "Bowing his head, Harley pretended to relinquish his toy before pulling his head back at the last minute."
    "Penelope gave him her best mom stare." 
    p "Drop…it."
    "Reluctantly, he complied, straining every muscle in his body with anticipation of the next throw."
    "Hours seemed to fly by as Penelope and Harley tossed the pinecone, chased, and lay together in the grass, enjoying each other's company until the sun started to dip beneath the tall pine treeline."
    "Penelope looked down at the happy little dog sprawled awkwardly across the lawn, head lying heavily in her lap, snoring away."
    "She could see that his ghostly form was already fading, signaling the little time they had left. Penelope ran her finger beneath his slender chin, causing his back leg to twitch and kick."
    p "Ah, Harley, you just wanted one more day of fun, didn't you?" 
    "Her voice quivered. She wasn't sure if he understood what she was saying, or knew what an impact he had had, giving her a simple afternoon just to exist with him."
    "And that was enough. She was enough."
    p "Cmon, Harley." 
    "The words caught in her throat as she tried to wipe away the guilt she felt, unsure if she'd see him again."
    p "Time for a good long nap."
    "She sat up, causing him to stir, roll in the dirt, and leap to his feet, happy to accompany her where she pleased."
    "They walked together through the park and around the fenced graveyard toward the entrance. Each step felt like a weight being placed on Penelope's heart."
    "When they reached the little library, Harley stuck his nose to the post, sniffing around for any sign of dog friends or rogue squirrels. Once he checked that it was safe, he turned back to her, proud and grinning, goofy as ever."
    "Penelope knelt down next to him and pressed her forehead against his."
    p "I know you have to go, and we probably won't see each other again, but I want you to know what a good boy you are. How much everyone must have loved you, and-" 
    "Her words were cut off by a big sloppy kiss from Harley. His tongue flicked in and out of his mouth as he barraged her face with slobber."
    "Harley looked up with knowing eyes, as if he already knew what she was going to say. She smiled, wishing she could have a few more minutes with him, but the sky was already shifting from pink to violet."
    
    show harley happy at slowdissolve

    p "Good night, Harley. Sleep tight, I love you."
    "As the last of the light vanished, so did Harley, his happy tail thumping in the grass, thanking her for the time she spent with him."


    scene black
    with dissolve

    "THE END"

    return