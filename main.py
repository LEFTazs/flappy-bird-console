from game_functions.game_engine import GameEngine
import time


def main():
    game_engine = GameEngine()
    should_continue = True
    elapsed_time = time.time()
    while should_continue:
        start_time = time.time()
        should_continue = game_engine.tick_game(elapsed_time)
        elapsed_time = time.time() - start_time
    # clear screen after game stopped
    game_engine.console_out.write_frame(" " * (game_engine.console_out.console_height * game_engine.console_out.console_width))


if __name__ == '__main__':
    main()
