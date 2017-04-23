#ifndef PLAYER_H
#define PLAYER_H

#include <inttypes.h>

int playGame(char const *gameFilePath,
             char *dealerHostname,
             char const *dealerPort,
             void (*on_game_start_callback)(Game *),
             void (*on_next_round_callback)(MatchState *, Action *),
             void (*on_game_finished_callback)(MatchState *));

#endif /* PLAYER_H */
