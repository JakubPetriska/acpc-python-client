#ifndef PLAYER_H
#define PLAYER_H

#include <inttypes.h>
#include <stdbool.h>

/*
Tells the client what actions are possible.
Call is always possible.
*/
typedef struct
{
    bool foldValid;
    bool raiseValid;
    int32_t raiseMin, raiseMax;
} PossibleActions;

int playGame(char const *gameFilePath,
             char *dealerHostname,
             char const *dealerPort,
             void (*initObjects)(Game *, MatchState *, PossibleActions *, Action *),
             void (*on_game_start_callback)(),
             void (*on_next_round_callback)(bool isActingPlayer),
             void (*on_game_finished_callback)());

#endif /* PLAYER_H */
