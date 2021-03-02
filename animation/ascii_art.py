import pathlib


class AsciiArt:
    # a file containing ascii art must always contain the width and the height of the drawing on the first line separated by a space
    # also it must be rectangular
    def __init__(self, file_name: str):
        self.width = 0
        self.height = 0
        self.lines = []
        with open(str(pathlib.Path(__file__).parent.absolute()) + "/" + file_name, "r") as f:
            meta = f.readline().strip().split(" ")
            self.width = int(meta[0])
            self.height = int(meta[1])

            for i in range(self.height):
                self.lines.append(f.readline()[:(self.width - 1)])
