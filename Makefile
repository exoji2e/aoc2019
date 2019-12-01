problems = $(shell ls **/day*.py)

all:
	for problem in $(problems); do \
	    echo $$problem ; \
	    pypy $$problem ;\
	done
