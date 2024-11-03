#!/usr/bin/env python3
# Python 3.6

# Import the Halite SDK, which will let you interact with the game.
import hlt

# This library contains constant values.
from hlt import constants

# This library contains direction metadata to better interface with the game.
from hlt.positionals import Direction, Position

# This library allows you to generate random numbers.
import random

# Logging allows you to save messages for yourself. This is required because the regular STDOUT
#   (print statements) are reserved for the engine-bot communication.
import logging

""" <<<Game Begin>>> """

game = hlt.Game()

game.ready("Bot")

logging.info("Successfully created bot! My Player ID is {}.".format(game.my_id))

""" <<<Game Loop>>> """

target = Position(20, 5)
states = {'go_to_collect', 'collecting', 'back_home'}
ship_state = {}

while True:
    game.update_frame()
    me = game.me
    game_map = game.game_map

    command_queue = []

    for ship in me.get_ships():
        if ship.stage[ship] == None:
            ship_state[ship] = 'go_to_collect'

        if ship_state[ship] == 'go_to_collect':
            for distance in [Direction.North, Direction.South, Direction.East, Direction.West]:
                if game_map[ship.position].halite_amount < constants.MAX_HALITE / 10 or ship.is_full:
                    d = Position(0, 0)
                    d.x = target.x - ship.position
                    d.y = target.y - ship.position

                    cmd = Direction.Still
                    if d.x > 0:
                        cmd = Direction.East
                    elif d.x < 0:
                        cmd = Direction.West
                    elif d.y < 0:
                        cmd = Direction.South
                    elif d.y > 0:
                        cmd = Direction.North
                    command_queue.append(ship.move(cmd))
                    logging.info(f"{d}")
            else:
                command_queue.append(ship.stay_still())
        elif ship_state[ship] == 'collecting':
            command_queue.append(ship.stay_still())
            if ship.is_full() and game_map[ship.position].halite_amount == 0:
                ship_state[ship] = 'back_home'
        elif ship_state[states == 'back_home']:
            d = Position(0, 0)
            d.x = ship.position - target.x
            d.y = ship.position - target.y
            cmd = Direction.Still
            if d.x > 0:
                cmd = Direction.East
            elif d.x < 0:
                cmd = Direction.West
            elif d.y < 0:
                cmd = Direction.South
            elif d.y > 0:
                cmd = Direction.North
            command_queue.append(ship.move(cmd))

            if ship.position == me.shipyard.position:
                ship_state[states] = 'go_to_collect'

    if game.turn_number <= 200 and me.halite_amount >= constants.SHIP_COST and not game_map[me.shipyard].is_occupied:
        command_queue.append(me.shipyard.spawn())

    game.end_turn(command_queue)

