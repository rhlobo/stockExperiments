# -*- coding: utf-8 -*-


import os
import datetime


def _determine_root_data_dir():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(script_dir, '..', 'data'))


START_DATE = datetime.date(2000, 1, 1)
NORMALIZATION_PCT_CHANGE_LIMIT = 0.35

COTAHIST_INPUT_DATA_DIR = os.path.join(_determine_root_data_dir(), 'input', 'cotahist')
DATASOURCE_TEST_DATA_DIR = os.path.join(_determine_root_data_dir(), 'tests', 'datasources')
