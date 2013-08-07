# -*- coding: utf-8 -*-


import sys

from datetime import datetime as d

import configurations as config
import bigtempo.tester as tester
from instances import data_engine


tester.generate_for_references(data_engine,
                               data_engine.select().all().difference('RAW'),
                               'PETR4',
                               None,
                               None,
                               config.DATASOURCE_TEST_DATA_DIR,
                               sys.modules[__name__])


tester.generate_for_references(data_engine,
                               data_engine.select().all().difference('RAW'),
                               'PETR4',
                               d(2008, 1, 1),
                               d(2008, 12, 31),
                               config.DATASOURCE_TEST_DATA_DIR,
                               sys.modules[__name__])
