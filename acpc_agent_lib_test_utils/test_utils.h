#ifndef TEST_UTILS_H
#define TEST_UTILS_H

#include "../acpc_infrastructure/game.h"
#include "../acpc_agent_lib/player.h"


void fillTestAction(Action * action);

void fillTestGame(Game * game);

void fillTestState(State * state);

void fillTestMatchState(MatchState * matchState);

void fillTestPossibleActions1(PossibleActions * possibleActions);

void fillTestPossibleActions2(PossibleActions * possibleActions);

void fillTestPossibleActions3(PossibleActions * possibleActions);

#endif /* TEST_UTILS_H */
