from physics.vectors import Vector


class Body:
    """
    Something that consists of matter

    Velocity is a vector whose magnitude is in m/s
    """

    def __init__(self, canvas, identifier, x, y, velocity=Vector(x=0, y=0)):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.id = identifier
        self.velocity = velocity

    def move(self, time):
        """
        moves ball as far as it would go with current velocity in time seconds
        """
        horizontal_movement = int(self.velocity.horizontal_component * time)
        vertical_movement = int( - (self.velocity.vertical_component * time))

        self.canvas.move(self.id, horizontal_movement, vertical_movement)
        self.x += horizontal_movement
        self.y += vertical_movement