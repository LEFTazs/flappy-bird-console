from game_functions.game_engine import GameEngine


def main():
    game_engine = GameEngine()
    should_continue = True
    while should_continue:
        should_continue = game_engine.tick_game()


if __name__ == '__main__':
    main()
