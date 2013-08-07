# -*- coding: utf-8 -*-


import os
import datetime


def _determine_data_dir():
    data_dir = os.path.abspath('sources/data')
    return data_dir if not 'ipy-notebooks' in data_dir else os.path.abspath('../stockExperiments/sources/data')


def _determine_root_data_dir():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(script_dir, '..', 'data'))


START_DATE = datetime.date(2000, 1, 1)
NORMALIZATION_PCT_CHANGE_LIMIT = 0.35

DATA_DIR = _determine_data_dir()
DATASOURCE_TEST_DATA_DIR = os.path.join(_determine_root_data_dir(), 'tests', 'datasources')
