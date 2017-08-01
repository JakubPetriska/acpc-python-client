import ctypes
import unittest

from acpc_python_client.data.betting_type import BettingType
from acpc_python_client.data.game import Game
from acpc_python_client.data.match_state import MatchState
from acpc_python_client.wrappers import GameWrapper, MatchStateWrapper
from acpc_python_client.wrappers import (
    MAX_ROUNDS,
    MAX_PLAYERS,
    MAX_BOARD_CARDS,
    MAX_HOLE_CARDS,
    MAX_NUM_ACTIONS
)
from test import agent_lib_test_utils as lib

NUM_PLAYERS = 7
NUM_ROUNDS = 2
CURRENT_ROUND = 1
NUM_HOLE_CARDS = 2


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
        self.assertEqual(self.game.get_num_hole_cards(), 2)

        for i in range(NUM_ROUNDS):
            self.assertEqual(self.game.get_num_board_cards(i), i)
        for i in range(NUM_ROUNDS, MAX_ROUNDS):
            with self.assertRaises(ValueError):
                self.game.get_num_board_cards(i)


class StateTest(unittest.TestCase):
    def setUp(self):
        game_wrapper = GameWrapper()
        lib.test_utils.fillTestGame(ctypes.pointer(game_wrapper))
        wrapper = MatchStateWrapper()
        lib.test_utils.fillTestState(ctypes.pointer(wrapper))
        match_state = MatchState(wrapper, Game(game_wrapper))
        self.state = match_state.get_state()

    def test_values(self):
        self.assertEqual(self.state.get_max_spent(), 8)
        self.assertEqual(self.state.get_min_no_limit_raise_to(), 22)

        for i in range(NUM_PLAYERS):
            self.assertEqual(self.state.get_spent(i), 18 + i)
        for i in range(NUM_PLAYERS, MAX_PLAYERS):
            with self.assertRaises(ValueError):
                self.state.get_spent(i)

        # TODO test get_action
        # for i in range(NUM_PLAYERS):
        #     for j in range(NUM_PLAYERS):
        #     self.assertEqual(self.state.get_action(i), 18 + i)
        # for i in range(NUM_PLAYERS, MAX_PLAYERS):
        #     with self.assertRaises(ValueError):
        #         self.state.get_action(i)

        # TODO test get_acting_player

        for i in range(CURRENT_ROUND + 1):
            self.assertEqual(self.state.get_num_actions(i), 7 + i)
        for i in range(CURRENT_ROUND + 1, MAX_ROUNDS):
            with self.assertRaises(ValueError):
                self.state.get_num_actions(i)

        self.assertEqual(self.state.get_round(), 1)

        for i in range(NUM_PLAYERS):
            self.assertEqual(self.state.get_player_folded(i), True)
        for i in range(NUM_PLAYERS, MAX_PLAYERS):
            with self.assertRaises(ValueError):
                self.state.get_player_folded(i)

        # TODO test get_board_card, need to add board cards sum for round
        # for i in range(CURRENT_ROUND + 1):
        #     self.assertEqual(self.state.get_board_card(i), 82 + i)
        # for i in range(CURRENT_ROUND + 1, MAX_BOARD_CARDS):
        #     with self.assertRaises(ValueError):
        #         self.state.get_board_card(i)

        for i in range(NUM_HOLE_CARDS):
            self.assertEqual(self.state.get_hole_card(i), 2 + 1 * MAX_PLAYERS + i)
        for i in range(NUM_HOLE_CARDS, MAX_HOLE_CARDS):
            with self.assertRaises(ValueError):
                self.state.get_hole_card(i)


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
