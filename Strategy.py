import math
import random

from client import *


def init_players():
    '''
    Here you can set each of your player's name and your team formation.
    In case of setting wrong position, server will set default formation for your team.
    '''

    players = [Player(name="player_1", first_pos=Pos(-6.5, 0)),
               Player(name="player_2", first_pos=Pos(-2, 1)),
               Player(name="player_3", first_pos=Pos(-5, -2)),
               Player(name="player_4", first_pos=Pos(-5, 2)),
               Player(name="player_5", first_pos=Pos(-2, -1))]
    return players


def get_angle(object1, object2):
    x1 = object1[0]
    x2 = object2[0]
    y1 = object1[1]
    y2 = object2[1]

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


def do_turn(game):
    act = Triple()
    '''
    Write your code here
    At the end you have to set 3 parameter:
        player id -> act.setPlyerID()
        angle -> act.setAngle()
        power -> act.setPower()
    '''

    # Sample code for shooting a random player in the ball direction with the maximum power:
    #
    # player_id = random.randint(0, 4)
    # act.setPlayerID(player_id)
    #
    # x1 = game.getMyTeam().getPlayer(player_id).getPosition().getX()
    # y1 = game.getMyTeam().getPlayer(player_id).getPosition().getY()
    # x2 = game.getBall().getPosition().getX()
    # y2 = game.getBall().getPosition().getY()
    # angle = math.fabs(math.degrees(math.atan((y2 - y1) / (x2 - x1))))
    # # Calculate the angle from the chosen player to the ball
    # if x2 > x1:
    #     if y2 < y1:
    #         angle = 360 - angle
    # else:
    #     if y2 < y1:
    #         angle += 180
    #     else:
    #         angle = 180 - angle
    # act.setAngle(angle)
    #
    # act.setPower(100)

    if (game.getBall().getPosition().getX()):
        players = {game.getMyTeam().getPlayer(i).getX(): i for i in range(4)}
        ideal_players = {}
        for k, v in players:
            if k < game.getBall().getPosition().getX():
                ideal_players[k] = v  # ideal player would be a player with x lower than the ball !

        if( len(ideal_players) ):  # if there were any ideal_player
            ideal_players = sorted(ideal_players)
            angle = get_angle( # get angle between nearest ideal_player and ball
                [
                    game.getMyTeam().getPlayer(ideal_players[0]).getX(),
                    game.getMyTeam().getPlayer(ideal_players[0]).getY()
                ],
                [
                    game.getBall().getX(),
                    game.getBall().getY()
                 ]
            )
            act.setPlayerID(ideal_players[0])  # select nearest ideal_player
            act.setPower(100)  # :|
            act.setAngle(angle)  # :|
        else:
            pass  # TODO : write sth to : defend when we have no ideal_player


    else:
        pass  # TODO : add offensive strategy

    return act
