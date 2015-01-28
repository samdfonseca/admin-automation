#!/bin/bash

NOSE_OPTS="-dv $1"

nosetests ${NOSE_OPTS} tests/login_test.py
nosetests ${NOSE_OPTS} tests/choosevenue_test.py
nosetests ${NOSE_OPTS} tests/suiteaccounts_test.py
