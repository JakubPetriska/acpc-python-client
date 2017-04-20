#include <boost/python.hpp>
#include <Python.h>
extern "C" {
#include "../acpc_agent_lib/player.h"
}
#include <iostream>


void playGame(char const *gameFilePath, char *dealerHostname, char const *dealerPort, 
              PyObject *agent, Game *game, MatchState * state)
{
  PyObject *result = PyObject_CallMethod(agent, "before_game_start", NULL);
  if (result != NULL) Py_DECREF(result);
  
  playGameInternal(gameFilePath, dealerHostname, dealerPort,
                   game, state);
}

extern "C" {
  Game * fuckIt() {
    Game * g = new Game();
    g->numPlayers = 5;
    std::cout << "fuck this, fuck that" << '\n';
    std::cout << "fuck this, fuck that" << ((int) g->numPlayers) << '\n';
    return g;
  }
}

// BOOST_PYTHON_MODULE(player_lib)
// {
//   using namespace boost::python;
//   def("playGame", playGame);

//   // ACPC lib enums and structs
//   enum_<BettingType>("BettingType")
//       .value("limitBetting", limitBetting)
//       .value("noLimitBetting", noLimitBetting);

//   enum_<ActionType>("ActionType")
//       .value("a_fold", a_fold)
//       .value("a_call", a_call)
//       .value("a_raise", a_raise)
//       .value("a_invalid", a_invalid);

//   class_<Action>("Action")
//       .def_readonly("type", &Action::type)
//       .def_readonly("size", &Action::size);

//   class_<Game>("Game")
//       .add_property("stack", make_array(&Game::stack))
//       .add_property("blind", make_array(&Game::blind))
//       .add_property("raiseSize", make_array(&Game::raiseSize))
//       .def_readonly("bettingType", &Game::bettingType)
//       .def_readonly("numPlayers", &Game::numPlayers)
//       .def_readonly("numRounds", &Game::numRounds)
//       .add_property("firstPlayer", make_array(&Game::firstPlayer))
//       .add_property("maxRaises", make_array(&Game::maxRaises))
//       .def_readonly("numSuits", &Game::numSuits)
//       .def_readonly("numRanks", &Game::numRanks)
//       .def_readonly("numHoleCards", &Game::numHoleCards)
//       .add_property("numBoardCards", make_array(&Game::numBoardCards));

//   class_<State>("State");
//     //   .add_property("actingPlayer", make_array(&State::actingPlayer));
  
//   class_<MatchState>("MatchState")
//       .def_readonly("state", &MatchState::state)
//       .def_readonly("viewingPlayer", &MatchState::viewingPlayer);
// }