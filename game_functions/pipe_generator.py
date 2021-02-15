import random

from game_objects.pipe import Pipe


class PipeGenerator:
    @staticmethod
    def generate_pipe(width: int, height: int) -> Pipe:
        max_pipe_hole_size = int(height / 2)
        x = width
        pipe_hole_size = random.choice(range(1, max_pipe_hole_size))
        bottom_height = random.choice(range(1, height - max_pipe_hole_size))
        top_height = bottom_height + pipe_hole_size
        return Pipe(x, top_height, bottom_height)
