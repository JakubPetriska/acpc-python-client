#!/bin/bash
if [ ! -d logs ]
then
    mkdir logs
fi
ACPC_DIR=./acpc_infrastructure
./_start_dealer_and_player_1.pl ./logs/matchName $ACPC_DIR/holdem.limit.2p.reverse_blinds.game 1000 0 Alice ./example_player.limit.2p.sh Bob