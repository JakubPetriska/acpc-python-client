#include <boost/python.hpp>
extern "C" {
  #include "../acpc_agent_lib/player.h"
}

BOOST_PYTHON_MODULE(player_lib)
{
    using namespace boost::python;
    def("playGame", playGame);
}