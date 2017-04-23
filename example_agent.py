import random
import sys

import client
from client import wrappers

if len(sys.argv) < 3:
    print("Usage {game_file_path} {dealer_hostname} {dealer_port}")
    sys.exit(1)


class RandomAgent(client.Agent):
    def __init__(self):
        super().__init__()
        self.actions = [wrappers.a_fold, wrappers.a_call, wrappers.a_raise]
        self.action_probabilities = [0] * 3
        self.action_probabilities[0] = 0.06  # fold probability
        self.action_probabilities[1] = (1 - self.action_probabilities[0]) * 0.5  # call probability
        self.action_probabilities[2] = (1 - self.action_probabilities[0]) * 0.5  # raise probability

    def on_game_start(self, game_wrapper):
        pass

    def on_next_round(self, match_state_wrapper, is_acting_player, possible_actions_wrapper, action_wrapper):
        if is_acting_player:
            # Create current action probabilities, leave out invalid actions
            current_probabilities = [0] * 3
            if possible_actions_wrapper.contents.foldValid:
                current_probabilities[0] = self.action_probabilities[0]
            # call is always valid action
            current_probabilities[1] = self.action_probabilities[1]
            if possible_actions_wrapper.contents.raiseValid:
                current_probabilities[2] = self.action_probabilities[2]

            # Normalize the probabilities
            probabilities_sum = sum(current_probabilities)
            current_probabilities = [p / probabilities_sum for p in current_probabilities]

            # Randomly select one action
            action_index = -1
            r = random.random()
            for i in range(3):
                if r <= current_probabilities[i]:
                    action_index = i
                else:
                    r -= current_probabilities[i]
            action_wrapper.contents.type = self.actions[action_index]
            if action_wrapper.contents.type == wrappers.a_raise:
                raise_min = possible_actions_wrapper.contents.raiseMin
                raise_max = possible_actions_wrapper.contents.raiseMax

                raise_size = raise_min + (raise_max - raise_min) * random.random()
                action_wrapper.contents.size = round(raise_size)
            else:
                action_wrapper.contents.size = 0

    def on_game_finished(self, match_state_wrapper):
        pass


client = client.Client(sys.argv[1], sys.argv[2], sys.argv[3])
client.play_game(RandomAgent())
