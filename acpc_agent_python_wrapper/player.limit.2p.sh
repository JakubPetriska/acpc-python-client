#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo $DIR
python $DIR/player.py holdem.limit.2p.reverse_blinds.game $1 $2
