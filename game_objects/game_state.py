from game_functions.pipe_generator import PipeGenerator
from game_objects.bird import Bird
from input_output.inputs import Inputs


class GameState:
    def __init__(self, height: int):
        self.bird = Bird(int(height/2))
        self.pipes = []
        self.generate_pipes_every_x_ticks = 25

    def apply_inputs(self, inputs: Inputs):
        if inputs.should_jump:
            self.bird.speed = self.bird.jumpspeed

    def move_one_tick(self, tick: int, width: int, height: int) -> bool:
        self.__tick_pipes(tick, width, height)
        self.__tick_bird()
        return self.__check_endgame_conditions()

    def __tick_pipes(self, tick: int, width: int, height: int):
        for pipe in self.pipes:
            pipe.x -= 0.75
        self.pipes = [pipe for pipe in self.pipes if not pipe.x < 0]
        if tick % self.generate_pipes_every_x_ticks == 0:
            pipe = PipeGenerator.generate_pipe(width, height)
            self.pipes.append(pipe)

    def __tick_bird(self):
        self.bird.height += self.bird.speed
        self.bird.speed -= self.bird.accel

    def __check_endgame_conditions(self):
        if self.bird.height < 0:
            return False
        for pipe in self.pipes:
            if round(pipe.x) == round(self.bird.x):
                if self.bird.height > pipe.top_height or self.bird.height < pipe.bottom_height:
                    return False
        return True
