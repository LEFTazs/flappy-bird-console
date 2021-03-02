from game_functions.pipe_generator import PipeGenerator
from input_output.inputs import Inputs

from game_objects.bird import Bird


class GameState:
    def __init__(self, height: int):
        self.bird = Bird(int(height/2))
        self.pipes = []
        self.pipe_generation_threshold = 1.3
        self.elapsed_time_accumulator = 0
        self.menu_displayed = True
        self.should_quit = False

    def apply_inputs(self, inputs: Inputs):
        if self.menu_displayed:
            if inputs.start_game:
                self.menu_displayed = False
            if inputs.should_quit:
                self.should_quit = True
        else:
            if inputs.should_jump:
                self.bird.speed = self.bird.jumpspeed

    def move_one_tick(self, tick: int, width: int, height: int, elapsed_time: float) -> bool:
        if not self.menu_displayed:
            self.__tick_pipes(tick, width, height, elapsed_time)
            self.__tick_bird(elapsed_time)
            return self.__check_endgame_conditions()
        return not self.should_quit

    def __tick_pipes(self, tick: int, width: int, height: int, elapsed_time: float):
        self.elapsed_time_accumulator += elapsed_time
        for pipe in self.pipes:
            pipe.x -= pipe.speed * elapsed_time
        self.pipes = [pipe for pipe in self.pipes if not pipe.x < 0]
        if self.elapsed_time_accumulator > self.pipe_generation_threshold:
            pipe = PipeGenerator.generate_pipe(width, height)
            self.pipes.append(pipe)
            self.elapsed_time_accumulator = 0

    def __tick_bird(self, elapsed_time: float):
        self.bird.speed -= self.bird.accel * elapsed_time
        self.bird.height += self.bird.speed

    def __check_endgame_conditions(self):
        if self.bird.height < 0:
            return False
        for pipe in self.pipes:
            if round(pipe.x) == round(self.bird.x):
                if self.bird.height > pipe.top_height or self.bird.height < pipe.bottom_height:
                    return False
        return True
