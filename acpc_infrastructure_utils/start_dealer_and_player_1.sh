#!/bin/bash
if [ ! -d logs ]
then
    mkdir logs
fi
ACPC_UTILS_DIR=./acpc_infrastructure_utils
ACPC_DIR=./acpc_infrastructure
$ACPC_UTILS_DIR/_start_dealer_and_player_1.pl \
  ./logs/matchName \
  $ACPC_DIR/holdem.limit.2p.reverse_blinds.game \
  1000 0 Alice $ACPC_UTILS_DIR/example_player.limit.2p.sh Bob