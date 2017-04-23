import sys

import client

if len(sys.argv) < 3:
    print("Usage {game_file_path} {dealer_hostname} {dealer_port}")
    sys.exit(1)

client = client.Client(sys.argv[1], sys.argv[2], sys.argv[3])
client.play_game()
