# -*- coding: utf-8 -*-


import pandas

import util.dateutils as dateutils
from instances import data_engine


@data_engine.for_synched(data_engine.select('NORMALIZED'))
def _factory(source_reference):

    @data_engine.datasource('MONTHLY:%s' % (source_reference),
                            dependencies=[source_reference],
                            lookback=31,
                            frequency='M',
                            tags=['MONTHLY', 'STOCK_TICKS'])
    class Monthly(object):

        def evaluate(self, context, symbol, start=None, end=None):
            df_norm = context.dependencies(source_reference)
            df_index = dateutils.range(start, end, frequency='M')

            result = pandas.DataFrame(columns=df_norm.columns, index=df_index)

            result['open'] = df_norm['open'].resample('M', how='first')
            result['high'] = df_norm['high'].resample('M', how='max')
            result['low'] = df_norm['low'].resample('M', how='min')
            result['close'] = df_norm['close'].resample('M', how='last')
            result['volume'] = df_norm['volume'].resample('M', how='sum')

            return result.dropna()
