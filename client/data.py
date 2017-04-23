from enum import Enum


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
        self.data_holder = wrapper.contents if hasattr(wrapper, 'contents') else wrapper


class PossibleActionsWrapper(_BaseDataObject):
    def __init__(self, wrapper):
        super().__init__(wrapper)

    def get_fold_valid(self):
        return self.data_holder.foldValid

    def get_raise_valid(self):
        return self.data_holder.raiseValid

    def get_raise_min(self):
        return self.data_holder.raiseMin

    def get_raise_max(self):
        return self.data_holder.raiseMax
