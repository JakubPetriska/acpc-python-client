# ACPC python client

Python wrapper for [AAAI ACPC][1] poker bot infrastructure. The infrastructure
consists of server, acting as a dealer and clients acting as poker players.
The wrapper is built around original client C code from [ACPC][1].

## Prerequisites 
Library was built using Python 3.6. Additionally `gcc` and `make` are needed to
build the native parts. 

## Installation
To use the package clone this repository. After cloning navigate to the root of
the repository and call
```bash
python setup.py install
```

This will install package `acpc_python_client` into your python distribution.


[1]: http://www.computerpokercompetition.org/