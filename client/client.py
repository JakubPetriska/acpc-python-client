import abc
from ctypes import *

import client.wrappers as wrappers
from acpc_agent_lib import playerlib


class Agent(object):
    @abc.abstractmethod
    def on_game_start(self, game_wrapper):
        pass

    @abc.abstractmethod
    def on_next_round(self, match_state_wrapper, action_wrapper):
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
        # self.agent = agent

    def play_game(self):
        on_game_start_func = CFUNCTYPE(None, POINTER(wrappers.GameWrapper))(self.on_game_start)
        on_next_round_func = CFUNCTYPE(None, POINTER(wrappers.MatchStateWrapper), POINTER(wrappers.ActionWrapper)) \
            (self.on_next_round)
        on_game_finished_func = CFUNCTYPE(None, POINTER(wrappers.MatchStateWrapper))(self.on_game_finished)
        playerlib.playGame(bytes(self.game_file_path, 'utf-8'),
                           bytes(self.dealer_hostname, 'utf-8'),
                           bytes(self.dealer_port, 'utf-8'),
                           on_game_start_func,
                           on_next_round_func,
                           on_game_finished_func)

    def on_game_start(self, game_wrapper):
        print('on game start')
        # print(wrapper_to_str(game_wrapper))
        # print(game_wrapper.contents.bettingType == limitBetting)
        # print(game_wrapper.contents.bettingType == noLimitBetting)

    def on_next_round(self, match_state_wrapper, action_wrapper):
        print('on next round')

    def on_game_finished(self, match_state_wrapper):
        print('on game finished')
