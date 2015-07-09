#!/usr/bin/env ipython -i
from __future__ import print_function

import simplejson as json
import sys
import os
import datetime
import atexit
import pprint
import readline, rlcompleter
from tempfile import mkstemp
from code import InteractiveConsole
import pdb

import tinydb
from tinydb import TinyDB, where
from tinydb.operations import delete, increment, decrement

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *

import adminautomation
from bypassqatesting import drivers
from adminautomation.pages import *
from adminautomation.locators import *
from adminautomation.structures import *

import bypassqatesting


sys.dont_write_bytecode = True

class TermColors(dict):
    COLOR_TEMPLATES= (
            ('Black', '0;30'),
            ('Red', '0;31'),
            ('Green', '0;32'),
            ('Brown', '0;33'),
            ('Blue', '0;34'),
            ('Purple', '0;35'),
            ('Cyan', '0;36'),
            ('LightGray', '0;37'),
            ('DarkGray', '0;30'),
            ('LightRed', '1;31'),
            ('LightGreen', '1;32'),
            ('Yellow', '1;33'),
            ('LightBlue', '1;34'),
            ('LightPurple', '1;35'),
            ('LightCyan', '1;36'),
            ('White', '1;37'),
            ('Normal', '0'),
        )

    NoColor = ''
    _base = '\001\033[{}m\002'

    def __init__(self):
        if os.environ.get('TERM') in ('xterm-color', 'xterm-256color', 'linux', 'screen',
                'screen-256color', 'screen-bce'):
            self.update(dict([(k, self._base.format(v)) for k, v in self.COLOR_TEMPLATES]))
        else:
            self.update(dict([(k, self.NoColor) for k, v in self.COLOR_TEMPLATES]))

_c = TermColors()

# Enable history
HISTFILE='{}/.pyhistory'.format(os.environ['HOME'])
# Read existing history if exists
if os.path.exists(HISTFILE):
    readline.read_history_file(HISTFILE)
# Set number of items stored in history file
readline.set_history_length(300)
def savehist():
    readline.write_history_file(HISTFILE)
atexit.register(savehist)

# Enable color prompt
sys.ps1 = '{0}>>> {1}'.format(_c['Green'], _c['Normal'])
sys.ps2 = '{0}... {1}'.format(_c['Red'], _c['Normal'])

# Pretty print for stdout
def custom_displayhook(value):
    if value is not None:
        try:
            import __builtin__
            __builtin__._ = value
        except ImportError:
            __builtins__._ = value

        pprint.pprint(value)
sys.displayhook = custom_displayhook

# Start external editor with \e
EDITOR = os.environ.get('EDITOR', 'vim')
EDIT_CMD = '\e'

class EditableBufferInteractiveConsole(InteractiveConsole):
    def __init__(self, *args, **kwargs):
        self.last_buffer = []
        InteractiveConsole.__init__(self, *args, **kwargs)

    def runsource(self, source, *args):
        self.last_buffer = [source.encode('utf-8')]
        return InteractiveConsole.runsource(self, source, *args)

    def raw_input(self, *args):
        line = InteractiveConsole.raw_input(self, *args)
        if line == EDIT_CMD:
            fd, tmpfl = mkstemp('.py')
            os.write(fd, b'\n'.join(self.last_buffer))
            os.close(fd)
            os.system('{0} {1}'.format(EDITOR, tmpfl))
            with open(tmpfl, 'r') as f:
                lines = f.readlines()
            os.unlink(tmpfl)
            tmpfl = ''
            for line in lines[:-2]:
                self.push(line)
            line = lines[-1]
        return line

class SeleniumServerURL(object):
    LOCAL = 'http://localhost:4444/wd/hub'
    TUNNEL = 'http://localhost:4445/wd/hub'
    LAB_INTERNAL = 'http://10.0.1.15:4444/wd/hub'

try:
    from dateutil.parser import parser as parse_date
except ImportError:
    print("Unable to import module: dateutil")

try:
    from jedi.utils import setup_readline
    setup_readline()
except ImportError:
    readline.parse_and_bind('tab: complete')


if __doc__ is None:
    c = EditableBufferInteractiveConsole(locals=locals())
    c.interact(banner='')

sys.exit()

