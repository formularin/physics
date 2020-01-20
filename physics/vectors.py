from physics import utils


class Vector:
    """
    A quantity with both direction and magnitude

    2 possible ways of instantiating:
     - cartesian coordinates (`x`, `y`)
     - polar coordinates (`r`, `theta`)

    *MUST BE KEYWORD AGRUMENTS. CANNOT BE POSITIONAL*
    """

    @classmethod
    def get_magnitude(cls, x, y):
        """
        finds length of vector using distance formula
        """
        return utils.distance((x, y), (0, 0))

    @classmethod
    def get_direction(cls, x, y):
        """
        finds angle of vector from coords
        """
        try:
            return utils.atan(y / x)
        except ZeroDivisionError:
            return 0

    @classmethod
    def get_horizontal_component(cls, r, theta):
        """
        finds horizontal component (x coord) 
        of vector from polar coords
        """
        return r * utils.cos(theta)

    @classmethod
    def get_vertical_component(cls, r, theta):
        """
        finds vertical component (y coord)
        of vector from polar coords
        """
        return r * utils.sin(theta)


    def __init__(self, **kwargs):

        if (keys := set(kwargs.keys())) == {"theta", "r"}:
            # polar coords
            self.type = "polar"
            self.theta = kwargs["theta"]
            self.r = kwargs["r"]
        
        elif keys == {"x", "y"}:
            # cartesian coords
            self.type = "cartesian"
            self.x = kwargs["x"]
            self.y = kwargs["y"]

        else:
            raise ValueError
        
    @property
    def magnitude(self):
        if self.type == "polar":
            return self.r
        elif self.type == "cartesian":
            return Vector.get_magnitude(self.x, self.y)
    
    @property
    def direction(self):
        if self.type == "polar":
            return self.theta
        elif self.type == "cartesian":
            return Vector.get_direction(self.x, self.y)

    @property
    def horizontal_component(self):
        if self.type == "polar":
            return Vector.get_horizontal_component(self.r, self.theta)
        elif self.type == "cartesian":
            return self.x

    @property
    def vertical_component(self):
        if self.type == "polar":
            return Vector.get_vertical_component(self.r, self.theta)
        elif self.type == "cartesian":
            return self.y

    def __add__(self, other):
        if (t := type(other)) == type(self):
            return Vector(
                x=(self.horizontal_component + other.horizontal_component),
                y=(self.vertical_component + other.vertical_component))
        else:
            raise TypeError

    def __mul__(self, other):
        if (t := type(other)) in [type(1), type(1.0)]:
            return Vector(
                r=(self.magnitude * other),
                theta=self.direction
            )
        else:
            raise TypeError

    def __str__(self):
        return f"theta = {self.direction}\nr = {self.magnitude}\nx = {self.horizontal_component}\ny = {self.vertical_component}"