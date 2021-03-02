from game_functions.game_engine import GameEngine
import time

SEC_PER_UPDATE = 1000 / 60 / 1000


def main():
    game_engine = GameEngine()
    should_continue = True
    previous_time = time.time()
    lag = 0
    while should_continue:
        current_time = time.time()
        elapsed_time = current_time - previous_time
        previous_time = current_time
        lag += elapsed_time

        while lag >= SEC_PER_UPDATE:
            if not game_engine.update():
                should_continue = False
                break
            lag -= SEC_PER_UPDATE

        game_engine.draw()

    # clear screen after game stopped
    game_engine.console_out.write_frame(" " * (game_engine.console_out.console_height * game_engine.console_out.console_width))


if __name__ == '__main__':
    main()
