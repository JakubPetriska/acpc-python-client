# import sys
#
# import player_lib
#
# player_lib.fuckIt()
# from api.agent import Agent
#
# if len(sys.argv) < 3:
#     print("Usage {game_file_path} {dealer_hostname} {dealer_port}")
#     sys.exit(1)
#
#
# class MyAgent(Agent):
#     def before_game_start(self):
#         print('hi there')
#
# agent = MyAgent()
#
# game = player_lib.Game()
# matchState = player_lib.MatchState()
# player_lib.playGame(sys.argv[1], sys.argv[2], sys.argv[3], agent, game, matchState)
# print(game.stack)
# print(len(game.stack))
# print(game.stack[0])
# print(game.stack[9])
# print(game.stack[10])
# print('end')

import player_lib as player

a = player.lib.fuckIt()
print(a)
