from time import sleep, time        # Used for frame rate and printing execution time
from os import name, system         # Used for clearing the screen

# !!! - CHANGE THIS - !!! - Change the below to the file your artwork is in. You can have multiple pieces of art in a file if you use lists for each piece.
import example_art as art



def main():
    ### Setup #########################################################################################

    # !- CAN EDIT -!    How many times the screen should clear per second. Lower = slower
    framerate = 8                  

    # !- CAN EDIT -!    How long the animation should play for. Note that this will not always be 100% accurate because ASCII art is code based, not an actual drawing.
    seconds = 20

    # Total frames we're expecting in the animation and the actual frames per millisecond we'll be using for Sleep
    total_frames = framerate * seconds
    framerate_in_ms = (seconds / total_frames) - offset

    # Execution of frames takes longer than it should. Over time this adds up to about 1 second per 10 seconds. This offset corrects that.
    offset = 0.009

    # !!!- CHANGE THIS -!!! - The art you're loading (don't forget to change the py up above in the imports)
    # Examples: art.bounce  art.spin                     
    ascii = art.bounce

    # DEBUG
    # start_time = time()

    for i in range(1,total_frames):

        print(ascii[i % len(ascii)])     
        sleep(framerate_in_ms)
        clear()






    ### Debug #########################################################################################
    # executionTime = (time() - start_time)
    # print(f'Execution should have taken {seconds} seconds, and took {executionTime} seconds')
    # print(f"Execution time is mismatched by: {executionTime - seconds} seconds")






#!-- HELPERS
# Clears the screen for ~aesthetics~
def clear():
    command = 'clear'
    if name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    system(command)


if __name__ == "__main__":
    main()
