import ctypes as ctypes
import unittest

import acpc_agent_lib_test_utils as lib
from client.data import Game
from client.wrappers import *


class ActionTest(unittest.TestCase):
    def setUp(self):
        self.wrapper = ActionWrapper()

    def test_wrapper(self):
        lib.test_utils.fillTestAction(ctypes.pointer(self.wrapper))
        self.assertEqual(self.wrapper.type, a_call)
        self.assertEqual(self.wrapper.size, 32)


class GameTest(unittest.TestCase):
    def setUp(self):
        self.wrapper = GameWrapper()

    def test_wrapper(self):
        lib.test_utils.fillTestGame(ctypes.pointer(self.wrapper))
        self.assertEqual(len(self.wrapper.stack), MAX_PLAYERS)
        for i in range(MAX_PLAYERS):
            self.assertEqual(self.wrapper.stack[i], 21 + i)

        self.assertEqual(len(self.wrapper.blind), MAX_PLAYERS)
        for i in range(MAX_PLAYERS):
            self.assertEqual(self.wrapper.blind[i], 89 + i)

        self.assertEqual(len(self.wrapper.raiseSize), MAX_ROUNDS)
        for i in range(MAX_ROUNDS):
            self.assertEqual(self.wrapper.raiseSize[i], 13 + i)

        self.assertEqual(self.wrapper.bettingType, noLimitBetting)
        self.assertEqual(self.wrapper.numPlayers, 10)
        self.assertEqual(self.wrapper.numRounds, 9)

        self.assertEqual(len(self.wrapper.firstPlayer), MAX_ROUNDS)
        for i in range(MAX_ROUNDS):
            self.assertEqual(self.wrapper.firstPlayer[i], 42 + i)

        self.assertEqual(len(self.wrapper.maxRaises), MAX_ROUNDS)
        for i in range(MAX_ROUNDS):
            self.assertEqual(self.wrapper.maxRaises[i], 18 + i)

        self.assertEqual(self.wrapper.numSuits, 2)
        self.assertEqual(self.wrapper.numRanks, 25)
        self.assertEqual(self.wrapper.numHoleCards, 49)

        self.assertEqual(len(self.wrapper.numBoardCards), MAX_ROUNDS)
        for i in range(MAX_ROUNDS):
            self.assertEqual(self.wrapper.numBoardCards[i], 52 + i)

    def test_data_object(self):
        lib.test_utils.fillTestGame(ctypes.pointer(self.wrapper))

        game = Game(self.wrapper)
        self.assertEqual(game.get_num_players(), 10)
        # TODO add more


class StateTest(unittest.TestCase):
    def setUp(self):
        self.wrapper = StateWrapper()

    def test_wrapper(self):
        lib.test_utils.fillTestState(ctypes.pointer(self.wrapper))
        self.assertEqual(self.wrapper.handId, 12)
        self.assertEqual(self.wrapper.maxSpent, 8)
        self.assertEqual(self.wrapper.minNoLimitRaiseTo, 22)

        self.assertEqual(len(self.wrapper.spent), MAX_PLAYERS)
        for i in range(MAX_PLAYERS):
            self.assertEqual(self.wrapper.spent[i], 18 + i)

        # TODO add actions test

        self.assertEqual(len(self.wrapper.actingPlayer), MAX_ROUNDS)
        for i in range(MAX_ROUNDS):
            self.assertEqual(len(self.wrapper.actingPlayer[i]), MAX_NUM_ACTIONS)
            for j in range(MAX_NUM_ACTIONS):
                self.assertEqual(self.wrapper.actingPlayer[i][j],
                                 3 + i * MAX_ROUNDS + j)

        self.assertEqual(len(self.wrapper.numActions), MAX_ROUNDS)
        for i in range(MAX_ROUNDS):
            self.assertEqual(self.wrapper.numActions[i], 7 + i)

        self.assertEqual(self.wrapper.round, 8)
        self.assertEqual(self.wrapper.finished, 11)

        self.assertEqual(len(self.wrapper.playerFolded), MAX_PLAYERS)
        for i in range(MAX_PLAYERS):
            self.assertEqual(self.wrapper.playerFolded[i], 33 + i)

        self.assertEqual(len(self.wrapper.boardCards), MAX_BOARD_CARDS)
        for i in range(MAX_BOARD_CARDS):
            self.assertEqual(self.wrapper.boardCards[i], 82 + i)

        # TODO test length
        # for i in range(MAX_PLAYERS):
        #     for j in range(MAX_HOLE_CARDS):
        #         self.assertEqual(self.wrapper.holeCards[i][j],
        #                          2 + i * MAX_PLAYERS + j)


class MatchStateTest(unittest.TestCase):
    def setUp(self):
        self.wrapper = MatchStateWrapper()

    # def test_wrapper(self):
    #     lib.test_utils.fillTestMatchState(ctypes.pointer(self.wrapper))
    #     self.assertEqual(self.wrapper.state.handId, 3)
    #     self.assertEqual(self.wrapper.viewingPlayer, 5)


class PossibleActionsTest(unittest.TestCase):
    def setUp(self):
        self.wrapper = PossibleActionsWrapper()

    def test_wrapper_1(self):
        lib.test_utils.fillTestPossibleActions1(ctypes.pointer(self.wrapper))
        self.assertEqual(self.wrapper.foldValid, True)
        self.assertEqual(self.wrapper.raiseValid, True)
        self.assertEqual(self.wrapper.raiseMin, 5)
        self.assertEqual(self.wrapper.raiseMax, 8)

    def test_wrapper_2(self):
        lib.test_utils.fillTestPossibleActions2(ctypes.pointer(self.wrapper))
        self.assertEqual(self.wrapper.foldValid, False)
        self.assertEqual(self.wrapper.raiseValid, True)
        self.assertEqual(self.wrapper.raiseMin, 34)
        self.assertEqual(self.wrapper.raiseMax, -6)

    def test_wrapper_3(self):
        lib.test_utils.fillTestPossibleActions3(ctypes.pointer(self.wrapper))
        self.assertEqual(self.wrapper.foldValid, True)
        self.assertEqual(self.wrapper.raiseValid, False)
        self.assertEqual(self.wrapper.raiseMin, -154)
        self.assertEqual(self.wrapper.raiseMax, 1)

    def test_value_override(self):
        self.test_wrapper_1()
        self.test_wrapper_2()
        self.test_wrapper_3()
