from game_functions.game_engine import GameEngine


def main():
    game_engine = GameEngine()
    should_continue = True
    while should_continue:
        should_continue = game_engine.tick_game()
    game_engine.console_out.write_frame(" " * (game_engine.console_out.console_height * game_engine.console_out.console_width))  # clear screen after game stopped


if __name__ == '__main__':
    main()
