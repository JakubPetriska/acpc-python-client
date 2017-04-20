#ifndef PLAYER_H
#define PLAYER_H

#include <inttypes.h>

int playGame(char const *gameFilePath,
             char *dealerHostname,
             char const *dealerPort,
             void (*on_game_start_func)(Game *),
             void (*on_next_round_func)());

#endif /* PLAYER_H */
