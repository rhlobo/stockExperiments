# -*- coding: utf-8 -*-


import os
import sys

from datetime import datetime as d

import configurations as config
import bigtempo.auditor as auditor
from instances import data_engine


def _get_test_data_filename(reference, symbol=None):
    symbol_part = '' if not symbol else '{%s}' % symbol
    return '%s%s.csv' % (reference, symbol_part)


def _get_test_data_filepath(reference, symbol=None):
    return os.path.join(config.DATASOURCE_TEST_DATA_DIR,
                        _get_test_data_filename(reference, symbol))


auditor.generate_multiple(data_engine,
                          data_engine
                          .select()
                          .all()
                          .difference('RAW')
                          .difference('NORMALIZATION_FACTOR:SPLITS:PCT_CHANGE(1):RAW_BOVESPA'),
                          'PETR4',
                          None,
                          None,
                          _get_test_data_filepath,
                          sys.modules[__name__])


auditor.generate_multiple(data_engine,
                          data_engine.select().all().difference('RAW'),
                          'PETR4',
                          d(2008, 1, 1),
                          d(2008, 12, 31),
                          _get_test_data_filepath,
                          sys.modules[__name__])


auditor.generate_multiple(data_engine,
                          data_engine.select('NORMALIZATION_FACTOR:SPLITS:PCT_CHANGE(1):RAW_BOVESPA'),
                          'PETR4',
                          None,
                          d(2013, 8, 7),
                          _get_test_data_filepath,
                          sys.modules[__name__])
