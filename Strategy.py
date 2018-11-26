import math
import random
# import VoidTool

from client import *


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


def init_players():
    '''
    Here you can set each of your player's name and your team formation.
    In case of setting wrong position, server will set default formation for your team.
    '''

    players = [Player(name="player_1", first_pos=Pos(-1, 0)),
               Player(name="player_2", first_pos=Pos(-3, -2.5)),
               Player(name="player_3", first_pos=Pos(-3, 2.5)),
               Player(name="player_4", first_pos=Pos(-6, -1)),
               Player(name="player_5", first_pos=Pos(-6, 1))]
    return players

#calculate the distance for attacking
def calculate_distance(x1, x2, y1, y2):
    distance = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
    return distance


def do_turn(game):
    act = Triple()

    if (game.getBall().getPosition().getX() >= 0):
        id = random.randint(0, 4)
        act.setPlayerID(id)
        act.setAngle(
            get_angle(
                [
                    game.getMyTeam().getPlayer(id).getPosition().getX(),
                    game.getMyTeam().getPlayer(id).getPosition().getY()
                ],
                [
                    game.getBall().getPosition().getX(),
                    game.getBall().getPosition().getY()
                ]
            )
        )
        act.setPower(100)
        return act
    else:
        ideal_plyers = {game.getMyTeam().getPlayer(i).getPosition().getX(): i
                        for i in range(5)
                        if game.getMyTeam().getPlayer(i).getPosition().getX() < game.getBall().getPosition().getX()}
        if(ideal_plyers):
            ideal_plyers = sorted(ideal_plyers.items(), key=lambda kv: kv[1])
            print(ideal_plyers)
            angle = get_angle(
                [
                    game.getMyTeam().getPlayer(ideal_plyers[0][1] - 1).getPosition().getX(),
                    game.getMyTeam().getPlayer(ideal_plyers[0][1] - 1).getPosition().getY()
                ],
                [
                    game.getBall().getPosition().getX(),
                    game.getBall().getPosition().getY()
                ]
            )
            act.setPlayerID(ideal_plyers[0][1] - 1)
            act.setAngle(angle)
            act.setPower(100)
            return act
