from game_objects.game_state import GameState

from animation.ascii_art import AsciiArt


class Animator:
    def __init__(self):
        self.background = " "
        self.bird = "o"
        self.pipe = "H"

    def get_menu_frame(self, width: int, height: int) -> str:
        logo: AsciiArt = AsciiArt("logo.txt")
        drawn_rows = 0
        frame: str = "#" * width
        drawn_rows += 1
        upper_rows = int(height / 2 - logo.height / 2)
        for y in range(upper_rows):
            frame += "#" + " " * (width - 2) + "#"
        drawn_rows += upper_rows
        for line in logo.lines:
            temp = "#" + " " * (int(width / 2 - logo.width / 2) - 1) + line + " " * (int(width / 2 - logo.width / 2) - 1)
            if len(temp) < width:
                temp += " " * (width - len(temp) - 1) + "#"
            frame += temp
        drawn_rows += logo.height
        while drawn_rows + 1 < height:
            frame += "#" + " " * (width - 2) + "#"
            drawn_rows += 1
        frame += "#" * width
        drawn_rows += 1
        assert drawn_rows == height
        assert len(frame) == width * height
        return frame

    def get_frame_for_game_state(self, game_state: GameState, width: int, height: int) -> str:
        if game_state.menu_displayed:
            return self.get_menu_frame(width, height)
        else:
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
