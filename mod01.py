r = "R"
import os
import time
while True:
    # Banner program to move the value of `r` across the screen
    r = "R"
    screen_width = 90  # Define the width of screen where the banner will move


    def move_banner():
        for position in range(screen_width):
            os.system('clear' if os.name == 'posix' else 'cls')  # Clear screen
            print(' ' * position + r)  # Move `r` to the right
            time.sleep(0.0125)  # Pause for a short period of time


    # Run the banner
    move_banner()
