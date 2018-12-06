import random
import math
from collections import namedtuple
from operator import attrgetter
from Void import Tool as Void
from client import *


def init_players():
    players = [
        Player(name="Isco", first_pos=Pos(-1, 0)),
        Player(name="Zidane", first_pos=Pos(-3, -2.5)),
        Player(name="Raul", first_pos=Pos(-3, 2.5)),
        Player(name="Modric", first_pos=Pos(-6, -0.7)),
        Player(name="Casillas", first_pos=Pos(-6, 0.7))
    ]
    return players


def do_turn(game):
    act = Triple()

    Player = namedtuple("Player", ["x", "y", "id"])
    Ball = namedtuple("Ball", ["x", "y"])

    ball = Ball(game.getBall().getPosition().getX(), game.getBall().getPosition().getY())
    players = []
    for i in range(5):
        players.append(
            Player(
                game.getMyTeam().getPlayer(i).getPosition().getX(),
                game.getMyTeam().getPlayer(i).getPosition().getY(),
                i
            )
        )

    void = Void(players=players, ball=ball)

    if void.is_defensive_sit():
        ideal_players = [i for i in void.players if i.x < void.ball.x]

        if ideal_players:
            ideal_players = sorted(ideal_players, reverse=False,
                                   key=lambda x: void.calculate_distance(x.x, void.ball.x, x.y, void.ball.y))

            print("defensive system Phase #1 :\n" + str(ideal_players))
            act.setPlayerID(ideal_players[0].id)
            act.setPower(
                void.calculate_distance(ideal_players[0].x, void.ball.x - 1, ideal_players[0].y, void.ball.y) * 11)
            act.setAngle(void.get_angle([ideal_players[0].x, ideal_players[0].y], [void.ball.x - 1, void.ball.y]))

            return act
        else:
            ideal_players = [i for i in void.players]
            ideal_players = sorted(ideal_players, reverse=True, key=lambda x: math.sqrt(x.y ** 2))  # |Y|
            ideal_players = sorted(ideal_players[:2], reverse=False,
                                   key=lambda x: void.calculate_distance(x.x, void.ball.x, x.y, void.ball.y))
            print("defensive system Phase #2 :\n" + str(ideal_players))
            act.setPlayerID(ideal_players[0].id)
            act.setPower(
                void.calculate_distance(ideal_players[0].x, void.ball.x - 1.5, ideal_players[0].y, void.ball.y) * 10)
            act.setAngle(void.get_angle([ideal_players[0].x, ideal_players[0].y], [void.ball.x - 1.5, void.ball.y]))
            return act

    elif void.is_offensive_sit() and not void.is_first_shot(game):
        players = void.is_offensive_sit()
        players = sorted(players[0:-2], reverse=True, key=lambda x: x.x)
        print("offensive system :\n" + str(players))
        act.setAngle(void.get_angle([players[0].x, players[0].y], [void.ball.x, void.ball.y]))
        act.setPower(100)
        act.setPlayerID(players[0].id)
        return act

    else:
        players = [i for i in void.players if i.x < void.ball.x]
        if void.is_first_shot(game=game):
            act.setAngle(random.randint(-10, 10))
        elif players:
            players = sorted(void.players, reverse=False, key=lambda x: x.x)
            players = sorted(players, reverse=False,
                             key=lambda x: void.calculate_distance(x.x, void.ball.x, x.y, void.ball.y))
            print("default system : \n" + str(players))
            if void.ball.y > 0:
                act.setAngle(void.get_angle([players[0].x, players[0].y], [void.ball.x, void.ball.y + 0.3]))
            else:
                act.setAngle(void.get_angle([players[0].x, players[0].y], [void.ball.x, void.ball.y - 0.3]))
        else:
            players = [i for i in void.players]
            players = sorted(players, reverse=True, key=lambda x: math.sqrt(x.y ** 2))
            act.setAngle(void.get_angle([players[0].x, players[0].y], [-6, -2 if players[0].y < 0 else 2]))
        act.setPower(100)
        act.setPlayerID(players[0].id)

        return act
