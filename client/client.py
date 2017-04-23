import abc
from ctypes import *

import client.wrappers as wrappers
import client.data as data
from acpc_agent_lib import playerlib


class Agent(object):
    @abc.abstractmethod
    def on_game_start(self, game_wrapper):
        pass

    @abc.abstractmethod
    def on_next_round(self, match_state_wrapper, is_acting_player, possible_actions_wrapper, action_wrapper):
        pass

    @abc.abstractmethod
    def on_game_finished(self, match_state_wrapper):
        pass


class Client(object):
    def __init__(self, game_file_path, dealer_hostname, dealer_port):
        super().__init__()
        self.game_file_path = game_file_path
        self.dealer_hostname = dealer_hostname
        self.dealer_port = dealer_port

        self.agent = None

        # Data object references
        self.game = None
        self.match_state = None
        self.possible_actions = None

    def play_game(self, agent):
        self.agent = agent

        on_game_start_func = CFUNCTYPE(None, POINTER(wrappers.GameWrapper))(self.on_game_start)
        on_next_round_func = CFUNCTYPE(None, POINTER(wrappers.MatchStateWrapper), c_bool,
                                       POINTER(wrappers.PossibleActionsWrapper),
                                       POINTER(wrappers.ActionWrapper))(self.on_next_round)
        on_game_finished_func = CFUNCTYPE(None, POINTER(wrappers.MatchStateWrapper))(self.on_game_finished)
        playerlib.playGame(bytes(self.game_file_path, 'utf-8'),
                           bytes(self.dealer_hostname, 'utf-8'),
                           bytes(self.dealer_port, 'utf-8'),
                           on_game_start_func,
                           on_next_round_func,
                           on_game_finished_func)

    def init_objects(self, game_wrapper, match_state_wrapper, possible_actions_wrapper, action_wrapper):
        self.possible_actions = data.PossibleActionsWrapper(possible_actions_wrapper)

    def on_game_start(self):
        # self.agent.on_game_start()
        pass

    def on_next_round(self, is_acting_player):
        # self.agent.on_next_round(match_state_wrapper, is_acting_player, possible_actions_wrapper, action_wrapper)
        pass

    def on_game_finished(self):
        # self.agent.on_game_finished(match_state_wrapper)
        pass
