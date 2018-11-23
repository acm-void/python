import math
# toolbox for starters
class Tool():

    def get_angle(self, input1, input2):

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


