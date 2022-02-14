class SteeringWheel:
    STARTING_POSITION = 0
    RIGHT_TURN_STEP = 15
    LEFT_TURN_STEP = 15

    def __init__(self, color, diameter):
        self.color = color
        self.diameter = diameter
        self.position = self.STARTING_POSITION
        self.car = object()
        self.__manufacturer_number = 'sdjalsdkjasd'  # Private data of our SteeringWheel

    @property
    def manufacturer_number(self):
        return self.__manufacturer_number

    def turn_right(self):
        self.position = self.STARTING_POSITION
        self.position += self.RIGHT_TURN_STEP

    def turn_left(self):
        self.position = self.STARTING_POSITION
        self.position += self.LEFT_TURN_STEP

    def volume_up(self):
        self.car.radio.volume += 1

    def volume_down(self):
        self.car.radio.volume -= 1
