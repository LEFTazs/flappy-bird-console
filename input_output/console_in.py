from pynput import keyboard

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
        should_quit: bool = False

        for input in self.input_cache:
            if input == keyboard.Key.space:
                should_jump = True
            if input == keyboard.Key.enter:
                start_game = True
            try:
                if input.char == 'q':
                    should_quit = True
            except:
                pass

        self.input_cache.clear()

        return Inputs(should_jump, start_game, should_quit)

    def on_keyboard_press(self, key):
        self.input_cache.append(key)

    def on_keyboard_release(self, key):
        pass
