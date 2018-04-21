import unittest
from acpc_python_client import read_game_file


class GameUtilsTest(unittest.TestCase):
    def test_read_game_file(self):
        game = read_game_file('test.game')
        self.assertEqual(game.get_num_players(), 3)
        self.assertEqual(game.get_num_rounds(), 4)

        self.assertEqual(game.get_blind(0), 5)
        self.assertEqual(game.get_blind(1), 10)
        self.assertEqual(game.get_blind(2), 0)

        self.assertEqual(game.get_num_hole_cards(), 2)

        self.assertEqual(game.get_num_board_cards(0), 0)
        self.assertEqual(game.get_num_board_cards(1), 3)
        self.assertEqual(game.get_num_board_cards(2), 1)
        self.assertEqual(game.get_num_board_cards(3), 1)

        self.assertEqual(game.get_num_ranks(), 13)
        self.assertEqual(game.get_num_suits(), 4)
