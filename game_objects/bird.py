class Bird:
    def __init__(self, height: int):
        self.x = 2
        self.starting_height = height
        self.height = height
        self.speed = 0
        self.accel = 0.03
        self.jumpspeed = 0.7

    def reset(self):
        self.x = 2
        self.height = self.starting_height
        self.speed = 0
        self.accel = 0.03
        self.jumpspeed = 0.7
