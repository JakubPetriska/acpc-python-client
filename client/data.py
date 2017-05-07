from enum import Enum

from client import utils


class BettingType(Enum):
    """Represents game type of betting."""
    LIMIT = 1,
    NO_LIMIT = 2


class ActionType(Enum):
    """Represents type of action."""
    FOLD = 1,
    CALL = 2,
    RAISE = 3,
    INVALID = 4


class _BaseDataObject(object):
    def __init__(self, wrapper):
        super().__init__()
        self._data_holder = wrapper.contents if hasattr(wrapper, 'contents') else wrapper


class Game(_BaseDataObject):
    """Game definition."""

    def __init__(self, wrapper):
        super().__init__(wrapper)

    def get_stack(self, player_index):
        """Returns stack size of player.

        Args:
            player_index (int): Index of the player

        Returns:
            int: Player's stack size.

        Raises:
            ValueError: When player_index is greater or equal
                        to number of players in the game.
        """
        if player_index > self.get_num_players():
            raise ValueError(
                'Cannot retrieve stack for player %s with %s players total'
                % (player_index, self.get_num_players()))
        return self._data_holder.stack[player_index]

    def get_blind(self, player_index):
        """Returns player's entry fee.

        Args:
            player_index (int): Index of the player

        Returns:
            int: Player's entry fee (blind).

        Raises:
            ValueError: When player_index is greater or equal
                        to number of players in the game.
        """
        if player_index > self.get_num_players():
            raise ValueError(
                'Cannot retrieve stack for player %s with %s players total'
                % (player_index, self.get_num_players()))
        return self._data_holder.blind

    def get_raise_size(self, round_index):
        """Returns the size of raise for limit games in given round.

        Args:
            round_index (int): Index of the round

        Returns:
            int: Size of the raise in given round.

        Raises:
            ValueError: When round_index is greater or equal
                        to number of rounds in the game.
        """
        if round_index > self.get_num_rounds():
            raise ValueError(
                'Cannot retrieve raise size in round %s in game with %s rounds'
                % (round_index, self.get_num_rounds()))
        return self._data_holder.raiseSize[round_index]

    def get_betting_type(self):
        """Betting type of the game, that is either limited or no-limit.

        Returns:
            BettingType: Betting type of the game.
        """
        return utils.betting_type_int_to_enum(self._data_holder.bettingType)

    def get_num_players(self):
        """Returns number of players in the game.

        Returns:
            int: Number of players in the game.
        """
        return self._data_holder.numPlayers

    def get_num_rounds(self):
        """Returns number of rounds in the game.

        Returns:
            int: Number of rounds in the game.
        """
        return self._data_holder.numRounds

    def get_first_player(self, round_index):
        """Returns first layer in given round of the game.

        Args:
            round_index (int): Index of the round

        Returns:
            int: First layer in given round of the game.

        Raises:
            ValueError: When round_index is greater or equal
                        to number of rounds in the game.
        """
        if round_index > self.get_num_rounds():
            raise ValueError(
                'Cannot retrieve first player in round %s in game with %s rounds'
                % (round_index, self.get_num_rounds()))
        return self._data_holder.firstPlayer[round_index]

    def get_max_raises(self, round_index):
        """Returns number of bets/raises that may be made in given round.

        Args:
            round_index (int): Index of the round

        Returns:
            int: Number of bets/raises that may be made in each round.

        Raises:
            ValueError: When round_index is greater or equal
                        to number of rounds in the game.
        """
        if round_index > self.get_num_rounds():
            raise ValueError(
                'Cannot retrieve max number of raises in round %s in game with %s rounds'
                % (round_index, self.get_num_rounds()))
        return self._data_holder.maxRaises[round_index]

    def get_num_suits(self):
        """Returns number of card suits in the game.

        Returns:
            int: Number of card suits in the game.
        """
        return self._data_holder.numSuits

    def get_num_ranks(self):
        """Returns number of card ranks in the game.

        Returns:
            int: Number of card ranks in the game.
        """
        return self._data_holder.numRanks

    def get_num_hole_cards(self):
        """Returns number of hole cards each player receives at the beginning of the game.

        Returns:
            int: Number of hole cards each player receives at the beginning of the game.
        """
        return self._data_holder.numHoleCards

    def get_num_board_cards(self, round_index):
        """Returns number of board cards that are revealed in given round.

        Args:
            round_index (int): Index of the round

        Returns:
            int: Number of board cards that are revealed in given round.

        Raises:
            ValueError: When round_index is greater or equal
                        to number of rounds in the game.
        """
        if round_index > self.get_num_rounds():
            raise ValueError(
                'Cannot retrieve number of board cards in round %s in game with %s rounds'
                % (round_index, self.get_num_rounds()))
        return self._data_holder.numBoardCards[round_index]


class State(_BaseDataObject):
    def __init__(self, wrapper, game):
        super().__init__(wrapper)
        self._game = game

    def get_max_spent(self):
        return self._data_holder.maxSpent

    def get_min_no_limit_raise_to(self):
        return self._data_holder.minNoLimitRaiseTo

    def get_spent(self, player_index):
        if player_index > self._game.get_num_players():
            raise ValueError(
                'Cannot retrieve spent amount for player %s with %s players total'
                % (player_index, self._game.get_num_players()))
        return self._data_holder.spent[player_index]

    def get_action(self):
        # TODO indexing
        return self._data_holder.action

    def get_acting_player(self):
        # TODO indexing
        return self._data_holder.actingPlayer

    def get_num_actions(self):
        # TODO indexing
        return self._data_holder.numActions

    def get_round(self):
        return self._data_holder.round

    def get_finished(self):
        return self._data_holder.finished

    def get_player_folded(self, player_index):
        if player_index > self._game.get_num_players():
            raise ValueError(
                'Cannot know if player %s folded with %s players total'
                % (player_index, self._game.get_num_players()))
        return self._data_holder.playerFolded[player_index] > 0

    def get_board_card(self,):
        # TODO indexing
        return self._data_holder.boardCards

    def get_hole_cards(self):
        # TODO indexing
        return self._data_holder.holeCards


class MatchState(_BaseDataObject):
    def __init__(self, wrapper, game):
        super().__init__(wrapper)
        self._state = State(wrapper.contents.state, game)

    def get_state(self):
        return self._state

    def get_viewing_player(self):
        return self._data_holder.viewingPlayer
