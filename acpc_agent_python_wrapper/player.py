import sys
import json
from ctypes import *

from acpc_agent_lib import playerlib

if len(sys.argv) < 3:
    print("Usage {game_file_path} {dealer_hostname} {dealer_port}")
    sys.exit(1)

MAX_ROUNDS = 4
MAX_PLAYERS = 10

# BettingType definition
(limitBetting, noLimitBetting) = (1, 2)

class GameWrapper(Structure):
    _fields_ = [
        ('stack', c_int * MAX_PLAYERS),
        ('blind', c_int * MAX_PLAYERS),
        ('raiseSize', c_int * MAX_ROUNDS),
        ('bettingType', c_int),
        ('numPlayers', c_ubyte),
        ('numRounds', c_ubyte),
        ('firstPlayer', c_ubyte * MAX_ROUNDS),
        ('maxRaises', c_ubyte * MAX_ROUNDS),
        ('numSuits', c_ubyte),
        ('numRanks', c_ubyte),
        ('numHoleCards', c_ubyte),
        ('numBoardCards', c_ubyte * MAX_ROUNDS)]


def str_game_wrapper(game_wrapper):
    # Create strings containing "name": value from fields on the object in json format
    attribute_names = [field[0] for field in GameWrapper._fields_]
    attribute_vals = [getattr(game_wrapper.contents, field[0]) for field in GameWrapper._fields_]
    attribute_vals_strings = ['[ %s ]' % ', '.join([str(e) for e in attr]) if hasattr(attr, '_length_') else str(attr) for attr in attribute_vals]
    attribute_strings = ['"%s": %s' % attr for attr in zip(attribute_names, attribute_vals_strings)]

    # Pretty print it with json module
    json_string = '{ %s }' % ', '.join(attribute_strings)
    object_str = json.dumps(json.loads(json_string), sort_keys=False, indent=4)
    return 'GameWrapper: %s' % object_str


class GameCallback(object):
    def on_game_start(self, game_wrapper):
        print('on game start')
        print(str_game_wrapper(game_wrapper))

    def on_next_round(self):
        print('on next round')


callback = GameCallback()

on_game_start_func = CFUNCTYPE(None, POINTER(GameWrapper))(callback.on_game_start)
on_next_round_func = CFUNCTYPE(None)(callback.on_next_round)

playerlib.playGame(bytes(sys.argv[1], 'utf-8'),
                   bytes(sys.argv[2], 'utf-8'),
                   bytes(sys.argv[3], 'utf-8'),
                   on_game_start_func,
                   on_next_round_func)
