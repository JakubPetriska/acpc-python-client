import unittest
import ctypes as ctypes

import acpc_agent_lib_test_utils as lib
from client.data import Game

from client.wrappers import GameWrapper


class GameTest(unittest.TestCase):
    def test_game_wrapper(self):
        game_wrapper = GameWrapper()
        lib.test_utils.fillTestGame(ctypes.pointer(game_wrapper))
        self.assertEqual(game_wrapper.numPlayers, 10)

    def test_game_data_object(self):
        game_wrapper = GameWrapper()
        lib.test_utils.fillTestGame(ctypes.pointer(game_wrapper))

        game = Game(game_wrapper)
        self.assertEqual(game.get_num_players(), 10)
