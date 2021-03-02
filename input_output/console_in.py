from pynput import keyboard

from input_output.console_constants import CLS
from input_output.inputs import Inputs


class ConsoleIn:
    def __init__(self):
        self.input_cache = []
        listener = keyboard.Listener(
            on_press=lambda key: self.on_keyboard_press(key),
            on_release=lambda key: self.on_keyboard_release(key))
        listener.start()

    def read_inputs(self) -> Inputs:
        should_jump: bool = False
        start_game: bool = False

        for input in self.input_cache:
            if input == keyboard.Key.space:
                should_jump = True
            if input == keyboard.Key.enter:
                start_game = True

        self.input_cache.clear()

        return Inputs(should_jump, start_game)

    def on_keyboard_press(self, key):
        self.input_cache.append(key)
        print(CLS, end='')
        pass

    def on_keyboard_release(self, key):
        pass
