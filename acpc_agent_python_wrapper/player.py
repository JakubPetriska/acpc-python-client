import os
import sys

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import player_lib as p

if len(sys.argv) < 3:
    print("Usage {game_file_path} {dealer_hostname} {dealer_port}")  # TODO
    sys.exit(1)

p.playGame(sys.argv[0], sys.argv[1], sys.argv[2])
