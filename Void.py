import math


# toolbox for starters
class Tool(object):

    def __init__(self, players, ball):
        self.players = players
        self.ball = ball

    @staticmethod
    def get_angle(input1, input2):

        x1 = input1[0]
        x2 = input2[0]

        y1 = input1[1]
        y2 = input2[1]

        angle = math.fabs(math.degrees(math.atan((y2 - y1) / (x2 - x1))))
        # Calculate the angle from the chosen player to the ball
        if x2 > x1:
            if y2 < y1:
                angle = 360 - angle
        else:
            if y2 < y1:
                angle += 180
            else:
                angle = 180 - angle

        return angle

    # calculate the distance for attacking
    @staticmethod
    def calculate_distance(x1, x2, y1, y2):
        distance = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
        return distance

    def is_defensive_sit(self):
        if self.ball.x < 0:
            return True
        else:
            return False

    def is_offensive_sit(self):
        ball_angle_up = self.get_angle(
            [
                self.ball.x,
                self.ball.y
            ],
            [
                7,
                1
            ]
        )
        ball_angle_down = self.get_angle(
            [
                self.ball.x,
                self.ball.y
            ],
            [
                7,
                -1
            ]
        )
        for i in self.players :
            if self.get_angle([i.x, i.y], [self.ball.x, self.ball.y]) in range(int(ball_angle_down), int(ball_angle_up)):
                return i
            else:
                return False


