import abc


class Agent:
    @abc.abstractmethod
    def before_game_start(self):
        pass

    @abc.abstractmethod
    def on_game_state_changed(self):
        pass

    @abc.abstractmethod
    def on_game_over(self):
        pass
