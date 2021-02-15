from game_objects.game_state import GameState


class Animator:
    def __init__(self):
        self.background = " "
        self.bird = "o"
        self.pipe = "H"

    def get_frame_for_game_state(self, game_state: GameState, width: int, height: int) -> str:
        frame: str = ""
        for y in reversed(range(height)):
            for x in range(width):
                frame += self.__get_character_for_position(x, y, game_state)
        return frame

    def __get_character_for_position(self, x: int, y: int, game_state: GameState):
        if game_state.bird.x == x and round(game_state.bird.height) == y:
            return self.bird
        for pipe in game_state.pipes:
            if round(pipe.x) == x and (pipe.bottom_height > y or pipe.top_height < y):
                return self.pipe
        return self.background
