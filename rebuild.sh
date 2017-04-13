#!/bin/bash
cd acpc_agent_lib
make clean
make

cd ../acpc_agent_lib_python_binding
make clean
make
