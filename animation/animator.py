from game_objects.game_state import GameState

from animation.ascii_art import AsciiArt


class Animator:
    def __init__(self):
        self.background = " "
        self.bird = "o"
        self.pipe = "H"

    def get_frame_for_game_state(self, game_state: GameState, width: int, height: int) -> str:
        if game_state.menu_displayed and game_state.game_over:
            menu_text = "Score: " + str(game_state.score) + " | Highscore: " + str(game_state.highscore) + " | Press ENTER to restart or Q to quit"
            return self.__get_menu_frame(width, height, "gameover.txt", menu_text)
        elif game_state.menu_displayed:
            return self.__get_menu_frame(width, height, "logo.txt")
        else:
            frame: str = ""
            for y in reversed(range(height)):
                for x in range(width):
                    frame += self.__get_character_for_position(x, y, game_state)
            return frame

    def __get_menu_frame(self, width: int, height: int, ascii_art_file: str, menu_text: str = None) -> str:
        ascii_art: AsciiArt = AsciiArt(ascii_art_file)
        frame: str = "#" * width
        upper_rows = int(height / 2 - ascii_art.height / 2)
        for y in range(upper_rows):
            frame += self.__get_fixed_width_string("", width)
        for line in ascii_art.lines:
            frame += self.__get_fixed_width_string(line, width)
        if menu_text is not None:
            frame += self.__get_fixed_width_string("", width)
            frame += self.__get_fixed_width_string(menu_text, width)
        while int(len(frame) / width) + 1 < height:
            frame += self.__get_fixed_width_string("", width)
        frame += "#" * width
        return frame

    def __get_fixed_width_string(self, string: str, width: int) -> str:
        temp = "#"
        spacing = " " * (int((width - 2) / 2) - int(len(string) / 2))
        temp += spacing + string
        while len(temp) + 1 < width:
            temp += " "
        temp += "#"
        return temp

    def __get_character_for_position(self, x: int, y: int, game_state: GameState):
        if game_state.bird.x == x and round(game_state.bird.height) == y:
            return self.bird
        for pipe in game_state.pipes:
            if round(pipe.x) == x and (pipe.bottom_height > y or pipe.top_height < y):
                return self.pipe
        return self.background
