#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR
export PYTHONPATH=$PYTHONPATH:$DIR/../
python player.py ../acpc_infrastructure/holdem.limit.2p.reverse_blinds.game $1 $2
