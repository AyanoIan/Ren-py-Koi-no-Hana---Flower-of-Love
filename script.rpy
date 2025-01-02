
default player_name = ""
default nao_known = 0  
default known_ren = 0

define mc = Character("[mc]")
define ai = Character("Aiko")
define n = Character("Nao")
define ren = Character("Ren")
define ry = Character("Ryan")

label start:

    $ persistent.gameplay == 0:

    if nao_known == 1:
        define n = Character("Nao")  
    elif nao_known == 0:
        define n = Character("???")
    if known_ren == 1:
        define ren = Character("Ren")
    elif known_ren == 0:
        define ren = Character("???")
    if known_ry == 1:
        define ry = Character("Ryan")
    elif known_ry == 0:
        define ry = Character("???")

    # Prompt for player name
    while player_name == "":
        "What is your name?"
        $ player_name = renpy.input("Enter your name:").strip()

        if player_name == "":
            "Please enter a valid name!"

    "Welcome, [player_name]!"
    
    label start:
    if persistent.gameplay == 0:
        # First playthrough: Start at Chapter 1
        $ persistent.chapter = 1
        $ persistent.chapter_progress = 0  # At the beginning of Chapter 1
        call start_ch01
        $ persistent.gameplay = 1

    elif persistent.gameplay == 1:
        if persistent.chapter == 1 and persistent.chapter_progress == 0:
            call start_ch01
            $ persistent.chapter_progress = 1 
        elif persistent.chapter == 1 and persistent.chapter_progress == 1:
            call ch_02  
            $ persistent.chapter_progress = 2 
        elif persistent.chapter == 2:
            call ch_04  

    elif persistent.gameplay == 2:
        if persistent.chapter == 3:
            call ch_07

