import ctypes
import unittest

from acpc_python_client.data.betting_type import BettingType
from acpc_python_client.data.game import Game
from acpc_python_client.data.match_state import MatchState
from acpc_python_client.wrappers import GameWrapper, MatchStateWrapper
from acpc_python_client.wrappers import (
    MAX_ROUNDS,
    MAX_PLAYERS
)

from test import agent_lib_test_utils as lib

NUM_PLAYERS = 7
NUM_ROUNDS = 2


class GameTest(unittest.TestCase):
    def setUp(self):
        wrapper = GameWrapper()
        self.game = Game(wrapper)
        lib.test_utils.fillTestGame(ctypes.pointer(wrapper))

    def test_values(self):
        for i in range(NUM_PLAYERS):
            self.assertEqual(self.game.get_stack(i), 21 + i)
        for i in range(NUM_PLAYERS, MAX_PLAYERS):
            with self.assertRaises(ValueError):
                self.game.get_stack(i)

        for i in range(NUM_PLAYERS):
            self.assertEqual(self.game.get_blind(i), 89 + i)
        for i in range(NUM_PLAYERS, MAX_PLAYERS):
            with self.assertRaises(ValueError):
                self.game.get_blind(i)

        for i in range(NUM_ROUNDS):
            self.assertEqual(self.game.get_raise_size(i), 13 + i)
        for i in range(NUM_ROUNDS, MAX_ROUNDS):
            with self.assertRaises(ValueError):
                self.game.get_raise_size(i)

        self.assertEqual(self.game.get_betting_type(), BettingType.NO_LIMIT)
        self.assertEqual(self.game.get_num_players(), 7)
        self.assertEqual(self.game.get_num_rounds(), 2)

        for i in range(NUM_ROUNDS):
            self.assertEqual(self.game.get_first_player(i), 42 + i)
        for i in range(NUM_ROUNDS, MAX_ROUNDS):
            with self.assertRaises(ValueError):
                self.game.get_first_player(i)

        for i in range(NUM_ROUNDS):
            self.assertEqual(self.game.get_max_raises(i), 18 + i)
        for i in range(NUM_ROUNDS, MAX_ROUNDS):
            with self.assertRaises(ValueError):
                self.game.get_max_raises(i)

        self.assertEqual(self.game.get_num_suits(), 2)
        self.assertEqual(self.game.get_num_ranks(), 25)
        self.assertEqual(self.game.get_num_hole_cards(), 49)

        for i in range(NUM_ROUNDS):
            self.assertEqual(self.game.get_num_board_cards(i), 52 + i)
        for i in range(NUM_ROUNDS, MAX_ROUNDS):
            with self.assertRaises(ValueError):
                self.game.get_num_board_cards(i)


class MatchStateTest(unittest.TestCase):
    def setUp(self):
        game_wrapper = GameWrapper()
        lib.test_utils.fillTestGame(ctypes.pointer(game_wrapper))
        wrapper = MatchStateWrapper()
        lib.test_utils.fillTestMatchState(ctypes.pointer(wrapper))
        self.match_state = MatchState(wrapper, Game(game_wrapper))

    def test_values(self):
        self.assertEqual(self.match_state.get_state().get_round(), 4)
        self.assertEqual(self.match_state.get_viewing_player(), 5)
