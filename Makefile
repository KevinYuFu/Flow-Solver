cxx = python
EXEC = flow
EXECTest = test

all:
	$(cxx) $(EXEC).py

test:
	$(cxx) $(EXECTest).py
