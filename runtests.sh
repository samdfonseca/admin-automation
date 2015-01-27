#!/bin/bash

NOSE_OPTS="-c nose.cfg"

nosetests ${NOSE_OPTS} tests/logintest.py
nosetests ${NOSE_OPTS} tests/choosevenuetest.py
nosetests ${NOSE_OPTS} tests/suiteaccountstest.py
