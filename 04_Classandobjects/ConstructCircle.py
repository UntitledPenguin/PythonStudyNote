class Circle:
    def __init__(self, *args):
        if len(args) == 3:  # Construct from three points
            self.construct_from_points(*args)
        elif len(args) == 2:  # Construct from center and radius
            self.construct_from_center(*args)
        else:
            raise ValueError("Invalid number of arguments")

    def construct_from_points(self, pt1, pt2, pt3):
        self.pt1 = pt1
        self.pt2 = pt2
        self.pt3 = pt3
        self.calculate_center_and_radius()

    def construct_from_center(self, center, radius):
        self.cent = center
        self.r = radius

    def calculate_center_and_radius(self):
        x1, y1 = self.pt1
        x2, y2 = self.pt2
        x3, y3 = self.pt3
        D = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        cx = ((x1**2 + y1**2) * (y2 - y3) + (x2**2 + y2**2) * (y3 - y1) + (x3**2 + y3**2) * (y1 - y2)) / D
        cy = ((x1**2 + y1**2) * (x3 - x2) + (x2**2 + y2**2) * (x1 - x3) + (x3**2 + y3**2) * (x2 - x1)) / D
        self.r = ((x1 - cx) ** 2 + (y1 - cy) ** 2) ** 0.5
        self.cent = (cx, cy)

# Example usage:
circle_A = Circle((0, 0), (4, 0), (0, 3))
print("Center:", circle_A.cent)
print("Radius:", circle_A.r)