init python:
    # This checks if persistent.gameplay exists. If it doesn't, it will create it and set it to 0.
    if not hasattr(persistent, 'gameplay'):
        persistent.gameplay = 0

init python:
    if not hasattr(persistent, 'chapter_progress'):
        persistent.chapter_progress = 0  # Start at the beginning of progress

    if not hasattr(persistent, 'chapter'):
        persistent.chapter = 1  # Start at Chapter 1

    if not hasattr(persistent, 'gameplay'):
        persistent.gameplay = 0  


label start:
    if persistent.gameplay == 0:
        $ chapter = 1
        call start_ch01

        $ chapter = 2
        call ch_02 

        $ chapter = 3
        call ch_03  

        $ persistent.gameplay = 1

    elif persistent.gameplay == 1:
        $ chapter = 4
        call ch_04 

        $ chapter = 5
        call ch_05 

        $ chapter = 6
        call ch_06  # Calls Chapter 6

        # After completing this set, set persistent.gameplay to 2 to show they are progressing
        $ persistent.gameplay = 2

    # If the player has reached the next stage (persistent.gameplay is 2)
    elif persistent.gameplay == 2:
        $ chapter = 7
        call ch_07  # Calls Chapter 7

    # After all the chapters, this continues the game or ends it.
    "You're now in chapter [chapter]."

    return
