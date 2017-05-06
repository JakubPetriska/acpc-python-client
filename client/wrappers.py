from ctypes import *

MAX_ROUNDS = 4
MAX_PLAYERS = 10
MAX_BOARD_CARDS = 7
MAX_HOLE_CARDS = 3
MAX_NUM_ACTIONS = 64
NUM_ACTION_TYPES = 3

# BettingType definition
(limitBetting, noLimitBetting) = (0, 1)

# ActionType definition
(a_fold, a_call, a_raise, a_invalid) = (0, 1, 2, NUM_ACTION_TYPES)


class ActionWrapper(Structure):
    _fields_ = [
        ('type', c_int),
        ('size', c_int)]


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


class StateWrapper(Structure):
    _fields_ = [
        ('handId', c_uint),
        ('maxSpent', c_int),
        ('minNoLimitRaiseTo', c_int),
        ('spent', c_int * MAX_PLAYERS),
        ('action', ((ActionWrapper * MAX_NUM_ACTIONS) * MAX_ROUNDS)),
        ('actingPlayer', ((c_ubyte * MAX_NUM_ACTIONS) * MAX_ROUNDS)),
        ('numActions', c_ubyte * MAX_ROUNDS),
        ('round', c_ubyte),
        ('finished', c_ubyte),
        ('playerFolded', c_ubyte * MAX_ROUNDS),
        ('boardCards', c_ubyte * MAX_BOARD_CARDS),
        ('holeCards', (c_ubyte * MAX_HOLE_CARDS) * MAX_PLAYERS)]


class MatchStateWrapper(Structure):
    _fields_ = [
        ('viewingPlayer', c_ubyte),
        ('state', StateWrapper)]


class PossibleActionsWrapper(Structure):
    _fields_ = [
        ('foldValid', c_bool),
        ('raiseValid', c_bool),
        ('raiseMin', c_uint),
        ('raiseMax', c_uint)]
