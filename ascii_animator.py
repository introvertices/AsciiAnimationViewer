from time import sleep              # Used for frame rate and printing execution time
from os import name, system         # Used for clearing the screen


def animate(art,framerate=12,seconds=5):
    '''Animates (or shows a still) of ASCII art from a list.\n 
    Parameters 
    art: the imported file containing art and the list to use i.e art.bounce
    framerate: int, speed animation frames will cycle at, defaults to 12
    seconds: int, duration in seconds, defaults to 5
    '''
    ### Setup #########################################################################################
    try:
        int(framerate)
    except:
        framerate = 8
    
    try:
        int(seconds)
    except:
        seconds = 5

    # Execution of frames takes longer than it should. Over time this adds up to about 1 second per 10 seconds. This offset corrects that.
    offset = 0.009

    # Total frames we're expecting in the animation and the actual frames per millisecond we'll be using for Sleep
    total_frames = framerate * seconds
    framerate_in_ms = (seconds / total_frames) - offset
    
    try: 
        if isinstance(art,list):
            for i in range(1,total_frames):

                print(art[i % len(art)])     
                sleep(framerate_in_ms)
                clear()
        else:
            print("You should use a list to store your artwork to use this module. Exiting...")
    except:
        print("You should use a list to store your artwork to use this module")
















#!-- HELPERS
# Clears the screen for ~aesthetics~
def clear():
    command = 'clear'
    if name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    system(command)
