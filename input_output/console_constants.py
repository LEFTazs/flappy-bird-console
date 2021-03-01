import os

CLS = '\033[0;0f'  # clears the console window
if os.name == 'posix':
    CURSOR_OFF = 'setterm -cursor off'  # removes the cursor from the console
else:
    CURSOR_OFF = ''
SLEEP_TIME = 0.01  # lower values == smoother animation
