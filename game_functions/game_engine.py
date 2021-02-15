from animation.animator import Animator
from game_objects.game_state import GameState
from input_output.console_in import ConsoleIn

from input_output.console_out import ConsoleOut
from input_output.inputs import Inputs


class GameEngine:
    def __init__(self):
        self.console_in = ConsoleIn()
        self.console_out = ConsoleOut()
        self.game_state = GameState(self.console_out.console_height)
        self.animator = Animator()
        self.tick = 0

    def tick_game(self):
        inputs: Inputs = self.console_in.read_inputs()

        self.game_state.apply_inputs(inputs)
        result: bool = self.game_state.move_one_tick(self.tick,
                                               self.console_out.console_width,
                                               self.console_out.console_height)

        frame: str = self.animator.get_frame_for_game_state(self.game_state,
                                                            self.console_out.console_width,
                                                            self.console_out.console_height)
        self.console_out.write_frame(frame)

        self.tick += 1

        return result
