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

import heapq

""" <<<Game Begin>>> """

game = hlt.Game()

game.ready("Bot")

logging.info("Successfully created bot! My Player ID is {}.".format(game.my_id))

""" <<<Game Loop>>> """

target = Position(20, 5)
stages = {'go_to_collect', 'collecting', 'back_home'}
ship_stage = {}

while True:
    game.update_frame()
    me = game.me
    game_map = game.game_map

    command_queue = []

    for ship in me.get_ships():        
        if ship.id not in ship_stage:
            ship_stage[ship.id] = 'go_to_collect'

        if ship_stage[ship.id] == 'go_to_collect':
            halite_values = {}
            direction_values = {}
            for direction in [Direction.North, Direction.South, Direction.East, Direction.West]:
                pos = ship.position.directional_offset(direction)

                if not game_map[pos].is_occupied:
                    halite_values[pos] = game_map[pos].halite_amount
                    direction_values[pos] = direction

            if len(halite_values) > 0:
                highest_halite_pos = max(halite_values, key=halite_values.get)
                direction = direction_values[highest_halite_pos]
                game_map[ship.position.directional_offset(direction)].mark_unsafe(ship)

                command_queue.append(ship.move(direction))

            else:
                command_queue.append(ship.stay_still())

            ship_stage[ship.id] = 'collecting'
            logging.info("change to collecting state")
        
        elif ship_stage[ship.id] == 'collecting':
            command_queue.append(ship.stay_still())

            if ship.halite_amount >= constants.MAX_HALITE:
                ship_stage[ship.id] = 'back_home'
                logging.info("change to go collect")

            elif game_map[ship.position].halite_amount <= 20:
                ship_stage[ship.id] = 'go_to_collect'
                logging.info("change to go collect")
        
        elif  ship_stage[ship.id] == 'back_home':
            d = Position(0,0)
            d.x = me.shipyard.position.x - ship.position.x
            d.y = me.shipyard.position.y - ship.position.y
            
            '''cmd = Direction.Still
            if d.x > 0:
                cmd = Direction.East
            elif d.x < 0:
                cmd = Direction.West
            elif d.y > 0:
                cmd = Direction.South
            elif d.y < 0:
                cmd = Direction.North'''
            
            # A*
            source = ship.position
            target = me.shipyard.position
            #target = me.shipyard.location()
            open = [source]
            close = [] # node is evaluated
            come_from = {}

            gScore = {}
            hScore = 0
            fScore = {} # gScore + hScore
            fScore[source] = gScore[source] + hScore

            while len(open) > 0:
                #search for shortest path
                selected = open[0]

                for o in open:
                    if fScore[o] < fScore[selected]:
                        selected = o
                
                current_node = selected

                # check alredy in destination location
                if current_node == target:
                    pass # stop

                close.append(current_node)
                open.remove(current_node)

                # add unexplored node and put in openset
                neighbors = getNeighbors(current_node)
                for neighbor in neighbors:
                    # add neighbor in openset
                    open.append(neighbor)
                    # calculate fScore
                    #hScore = neighbor.distance(target)
                    fScore[neighbor] = gScore[neighbor] + hScore
                    come_from[neighbor] = current_node
                    #pass

            # check ship
            if game_map[ship.position.directional_offset(cmd)].is_occupied:
                cmd = Direction.Still

            game_map[ship.position.directional_offset(cmd)].mark_unsafe(ship)
            command_queue.append(ship.move(cmd))

            if ship.position == me.shipyard.position:
                ship_stage[ship.id] = 'go_to_collect'
                logging.info("change to go collect")

    if game.turn_number <= 50 and me.halite_amount >= constants.SHIP_COST and not game_map[me.shipyard].is_occupied:
        command_queue.append(me.shipyard.spawn())
    elif game.turn_number < 200:
        pass

    else:
        # last game
        pass

    game.end_turn(command_queue)

