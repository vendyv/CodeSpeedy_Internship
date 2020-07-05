class Circle:
    def __init__(self, circleX, circleY):
        self.circleX = circleX
        self.circleY = circleY
        # X and Y coordinates of circle with respect to the window

class State:
    def __init__(self, rect, circle):
        self.rect = rect
        self.circle = circle
        # States of rectangle (catcher) and circle (ball)
