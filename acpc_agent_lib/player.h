#ifndef PLAYER_H
#define PLAYER_H

#include "../acpc_infrastructure/game.h"

int playGameInternal(char const *gameFilePath, char *dealerHostname, char const *dealerPort,
                     Game *game, MatchState * state);

#endif /* PLAYER_H */
