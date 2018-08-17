cxx = python
EXEC = FlowSolver
EXECTest = test

all:
	$(cxx) $(EXEC).py

test:
	$(cxx) $(EXECTest).py
