import unittest
from unittest import TestSuite

from test.structures_tests import GameTest, ActionTest, PossibleActionsTest, MatchStateTest, StateTest

test_classes = [ActionTest, GameTest, StateTest, MatchStateTest, PossibleActionsTest]


def load_tests(loader, tests, pattern):
    suite = TestSuite()
    for test_class in test_classes:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite


if __name__ == "__main__":
    unittest.main()
