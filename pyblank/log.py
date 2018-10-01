# -*- coding: utf-8 -*-
"""Sample application log settings"""

from __future__ import unicode_literals, print_function

import logging.handlers
import os.path

PROJECT_NAME = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
PROJECT_LOGGER = logging.getLogger(PROJECT_NAME)
LOG_VERBOSE_FORMAT = "[%(asctime)s] %(name)s:%(levelname)-8s " \
                     "%(filename)s(%(threadName)s):%(lineno)d -> %(message)s"

_VERBOSE_FORMATTER = logging.Formatter(LOG_VERBOSE_FORMAT)

FILE_LOG_HANDLER = logging.handlers.RotatingFileHandler(
    '{}.log'.format(PROJECT_NAME), maxBytes=10000, backupCount=5)
FILE_LOG_HANDLER.setLevel(logging.DEBUG)
FILE_LOG_HANDLER.setFormatter(_VERBOSE_FORMATTER)
