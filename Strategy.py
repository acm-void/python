import math
from collections import namedtuple
from operator import attrgetter
from Void import Tool as Void
from client import *


def init_players():
    players = [
        Player(name="player_1", first_pos=Pos(-1, 0)),
        Player(name="player_2", first_pos=Pos(-3, -2.5)),
        Player(name="player_3", first_pos=Pos(-3, 2.5)),
        Player(name="player_4", first_pos=Pos(-6, -1)),
        Player(name="player_5", first_pos=Pos(-6, 1))
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
            ideal_players = sorted(ideal_players, reverse=True, key=attrgetter('x'))
            print("defensive system Phase #1 :\n" + str(ideal_players))
            act.setPlayerID(ideal_players[0].id)
            act.setPower(100)
            act.setAngle(void.get_angle([ideal_players[0].x, ideal_players[0].y], [void.ball.x, void.ball.y]))

            return act
        else:
            ideal_players = [i for i in void.players if math.sqrt(i.y ** 2) > void.ball.y]
            ideal_players = sorted(ideal_players, key=lambda x: math.sqrt(x.y ** 2)) # |Y|
            print("defensive system Phase #2 :\n" + str(ideal_players))
            act.setPlayerID(ideal_players[0].id)
            act.setPower(100)
            act.setAngle(void.get_angle([ideal_players[0].x, ideal_players[0].y], [void.ball.x, void.ball.y]))
            return act

    elif void.is_offensive_sit() :
        player = void.is_offensive_sit()
        print("offensive system :\n" + str(players))
        act.setAngle(void.get_angle([player.x, player.y], [void.ball.x, void.ball.y]))
        act.setPower(100)
        act.setPlayerID(player.id)
        return act

    else:
        players = sorted(void.players, reverse=True, key=lambda x: x.x)
        print("default system : \n" + str(players))
        act.setAngle(void.get_angle([players[0].x, players[0].y], [void.ball.x, void.ball.y]))
        act.setPower(100)
        act.setPlayerID(players[0].id)

        return act



