import os
import sys
import time

from input_output.console_constants import CLS, CURSOR_OFF, SLEEP_TIME


class ConsoleOut:
    def __init__(self):
        self.clear_console = 'clear' if os.name == 'posix' else 'CLS'
        self.console_width = os.get_terminal_size().columns
        self.console_height = os.get_terminal_size().lines

    def write_frame(self, string_to_write: str):
        sys.stdout.write(string_to_write)
        sys.stdout.flush()

        if os.name == 'posix':
            os.system(CURSOR_OFF)
            print(CLS, end='')
        else:
            sys.stdout.write(CLS)
