# Project properties
INCLUDES_PATH = ../acpc_agent_lib/
DEPENDENT_LIB_NAME = player

LIB_NAME = player_lib
SOURCES = player_binding.cpp


# Python properties
PYTHON_VERSION = 3.5m
PYTHON_HOME = /home/jakub/anaconda3/envs/general3.5
PYTHON_INCLUDE = $(PYTHON_HOME)/include/
PYTHON_LIB = $(PYTHON_HOME)/lib

# Location of the Boost Python include files and library
BOOST_LIB = /home/jakub/Libs/boost_1_63_0
BOOST_INC = $(BOOST_LIB)/boost

CC = g++
GPP_SETTINGS = -std=c++11
GPP_COMPILATION_SETTINGS = $(GPP_SETTINGS) \
	-I$(PYTHON_INCLUDE) -I$(PYTHON_INCLUDE)python$(PYTHON_VERSION) -fPIC
GPP_LINKING_PYTHON_SETTINGS = -lpython$(PYTHON_VERSION) -lboost_python-py35 -l$(DEPENDENT_LIB_NAME)
GPP_LINKING_SETTINGS = $(GPP_SETTINGS) \
	-shared -L$(INCLUDES_PATH)

OBJECTS = $(SOURCES:.cpp=.o)

$(LIB_NAME).so: objects
	$(CC) $(GPP_LINKING_SETTINGS) \
		-Wl,-soname,$(LIB_NAME).so,-rpath=$(INCLUDES_PATH) \
		-o $(LIB_NAME).so $(OBJECTS) \
		$(GPP_LINKING_PYTHON_SETTINGS)
	cp $(LIB_NAME).so ../$(LIB_NAME)/

objects: $(SOURCES)
	$(CC) $(GPP_COMPILATION_SETTINGS) -c $(SOURCES)

clean:
	rm $(OBJECTS)
	rm $(LIB_NAME).so
