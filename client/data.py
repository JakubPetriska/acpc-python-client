from enum import Enum

from client import utils


class BettingType(Enum):
    LIMIT = 1,
    NO_LIMIT = 2


class ActionType(Enum):
    FOLD = 1,
    CALL = 2,
    RAISE = 3,
    INVALID = 4


class _BaseDataObject(object):
    def __init__(self, wrapper):
        super().__init__()
        self._data_holder = wrapper.contents if hasattr(wrapper, 'contents') else wrapper


class Game(_BaseDataObject):
    def __init__(self, wrapper):
        super().__init__(wrapper)

    def get_stack(self):
        return self._data_holder.stack

    def get_blind(self):
        return self._data_holder.blind

    def get_raise_size(self):
        return self._data_holder.raiseSize

    def get_betting_type(self):
        return utils.betting_type_int_to_enum(self._data_holder.bettingType)

    def get_num_players(self):
        return self._data_holder.numPlayers

    def get_num_rounds(self):
        return self._data_holder.numRounds

    def get_first_player(self):
        return self._data_holder.firstPlayer

    def get_max_raises(self):
        return self._data_holder.maxRaises

    def get_num_suits(self):
        return self._data_holder.numSuits

    def get_num_ranks(self):
        return self._data_holder.numRanks

    def get_num_hole_cards(self):
        return self._data_holder.numHoleCards

    def get_num_board_cards(self):
        return self._data_holder.numBoardCards


class State(_BaseDataObject):
    def __init__(self, wrapper):
        super().__init__(wrapper)

    def get_stack(self):
        return self._data_holder.stack
