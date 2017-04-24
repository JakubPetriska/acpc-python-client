import abc
from ctypes import *

import client.wrappers as wrappers
from acpc_agent_lib import playerlib
from client import utils
from client.data import ActionType, Game


class Agent(object):
    def __init__(self):
        super().__init__()
        self._client = None

    def _setup(self, client, possible_actions_wrapper):
        self._client = client
        self._possible_actions_wrapper = possible_actions_wrapper

    def is_fold_valid(self):
        return self._possible_actions_wrapper.contents.foldValid

    def is_call_valid(self):
        return True

    def is_raise_valid(self):
        return self._possible_actions_wrapper.contents.raiseValid

    def get_raise_max(self):
        return self._possible_actions_wrapper.contents.raiseMax if self.is_raise_valid() else -1

    def get_raise_min(self):
        return self._possible_actions_wrapper.contents.raiseMin if self.is_raise_valid() else -1

    def set_next_action(self, action_type, raise_size=0):
        self._client._set_next_action(action_type, raise_size)

    @abc.abstractmethod
    def on_game_start(self, game):
        pass

    @abc.abstractmethod
    def on_next_round(self, game, match_state, is_acting_player):
        pass

    @abc.abstractmethod
    def on_game_finished(self, game, match_state):
        pass


class Client(object):
    def __init__(self, game_file_path, dealer_hostname, dealer_port):
        super().__init__()
        self._game_file_path = game_file_path
        self._dealer_hostname = dealer_hostname
        self._dealer_port = dealer_port

        self._agent = None

        self._action_wrapper = None

        # Data object references
        self._game = None
        self._match_state = None

        self._action_set = False

    def play_game(self, agent):
        if not agent:
            raise ValueError('No agent provided to Client')
        self._agent = agent

        init_objects_func = CFUNCTYPE(None, POINTER(wrappers.GameWrapper), POINTER(wrappers.MatchStateWrapper),
                                      POINTER(wrappers.PossibleActionsWrapper),
                                      POINTER(wrappers.ActionWrapper))(self._init_objects)
        on_game_start_func = CFUNCTYPE(None)(self._on_game_start)
        on_next_round_func = CFUNCTYPE(None, c_bool)(self._on_next_round)
        on_game_finished_func = CFUNCTYPE(None)(self._on_game_finished)
        playerlib.playGame(bytes(self._game_file_path, 'utf-8'),
                           bytes(self._dealer_hostname, 'utf-8'),
                           bytes(self._dealer_port, 'utf-8'),
                           init_objects_func,
                           on_game_start_func,
                           on_next_round_func,
                           on_game_finished_func)

    def _set_next_action(self, action_type, raise_size):
        self._action_wrapper.contents.type = utils.action_type_enum_to_int(action_type)
        if action_type == ActionType.RAISE:
            self._action_wrapper.contents.size = raise_size
        else:
            self._action_wrapper.contents.size = 0
        self._action_set = True

    def _init_objects(self, game_wrapper, match_state_wrapper,
                      possible_actions_wrapper, action_wrapper):
        self._action_wrapper = action_wrapper
        self._game = Game(game_wrapper)
        self._agent._setup(self, possible_actions_wrapper)

    def _on_game_start(self):
        self._agent.on_game_start(self._game)

    def _on_next_round(self, is_acting_player):
        self._action_set = False
        self._agent.on_next_round(self._game, None, is_acting_player)
        if is_acting_player and not self._action_set:
            raise RuntimeError('No action was set by agent when it was acting')

    def _on_game_finished(self):
        self._agent.on_game_finished(self._game, None)
