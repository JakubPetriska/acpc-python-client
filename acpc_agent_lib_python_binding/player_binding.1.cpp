#include <boost/python.hpp>
#include <Python.h>
extern "C" {
#include "../acpc_agent_lib/player.h"
}
#include <iostream>

void playGame(char const *gameFilePath, char *dealerHostname, char const *dealerPort, PyObject *agent, Game *game)
{
  PyObject *result = PyObject_CallMethod(agent, "before_game_start", NULL);
  if (result != NULL) Py_DECREF(result);
  
  playGameInternal(gameFilePath, dealerHostname, dealerPort, game);
}

BOOST_PYTHON_MODULE(player_lib)
{
  using namespace boost::python;
  def("playGame", playGame);

  // ACPC lib enums and structs
  enum_<BettingType>("BettingType")
      .value("limitBetting", limitBetting)
      .value("noLimitBetting", noLimitBetting);

  enum_<ActionType>("ActionType")
      .value("a_fold", a_fold)
      .value("a_call", a_call)
      .value("a_raise", a_raise)
      .value("a_invalid", a_invalid);

  class_<Action>("Action")
      .def_readonly("type", &Action::type)
      .def_readonly("size", &Action::size);

  class_<Game>("Game")
      .def_readonly("stack", &Game::stack)
      .def_readonly("blind", &Game::blind)
      .def_readonly("raiseSize", &Game::raiseSize)
      .def_readonly("bettingType", &Game::bettingType)
      .def_readonly("numPlayers", &Game::numPlayers)
      .def_readonly("numRounds", &Game::numRounds)
      .def_readonly("firstPlayer", &Game::firstPlayer)
      .def_readonly("maxRaises", &Game::maxRaises)
      .def_readonly("numSuits", &Game::numSuits)
      .def_readonly("numRanks", &Game::numRanks)
      .def_readonly("numHoleCards", &Game::numHoleCards)
      .def_readonly("numBoardCards", &Game::numBoardCards);
}