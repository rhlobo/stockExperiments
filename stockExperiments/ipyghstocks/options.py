# -*- coding: utf-8 -*-


import json
import pandas
import datetime
import util.dateutils as dateutils
import util.pandasutils as pandasutils


CANDLESTICK, COLUMN, LINE = 'candlestick', 'column', 'line'
GROUPING_UNITS = [['week', [1]], ['month', [1, 2, 3, 4, 6]]]


class _AbstractHighChartsOptions(object):

    def asDict(self):
        return self.asDict


class Options(_AbstractHighChartsOptions):

    def __init__(self, title='ipyghstocks'):
        self.asDict = {
            'chart': {
                'alignTicks': False
            },
            'rangeSelector': {
                'selected': 1
            },
            'title': {
                'text': title
            },
            'plotOptions': {
                'candlestick': {
                    'color': 'red',
                    'upColor': 'blue'
                }
            },
            'yAxis': [],
            'series': []
        }

    def json(self):
        return json.dumps(self, cls=_PandasDataFrameJSONEncoder)

    def add(self, obj):
        if not isinstance(obj, Axis) and not isinstance(obj, Series):
            raise ValueError
        self.asDict[('yAxis' if isinstance(obj, Axis) else 'series')].append(obj)
        return self


class Axis(_AbstractHighChartsOptions):

    def __init__(self,
                 name,
                 lineWidth=2,
                 height=340,
                 top=70):
        self.asDict = {
            'title':  {
                'text': name
            },
            'lineWidth': lineWidth,
            'height': height,
            'top': top
        }


class Series(_AbstractHighChartsOptions):

    def __init__(self,
                 name,
                 data,
                 color=None,
                 yAxisIndex=0,
                 chartType=CANDLESTICK,
                 dataGroupingUnits=GROUPING_UNITS):
        self.asDict = {
            'type': chartType,
            'name': name,
            'data': data,
            'yAxis': yAxisIndex,
            'dataGrouping': {
                'units': dataGroupingUnits
            }
        }
        if color:
            self.asDict['color'] = color


class _PandasDataFrameJSONEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, _AbstractHighChartsOptions):
            return obj.asDict
        if isinstance(obj, pandas.DataFrame):
            return self._convertPandasDataFrame(obj)
        if isinstance(obj, pandas.core.series.TimeSeries):
            return self._convertPandasTimeSeries(obj)
        if isinstance(obj, datetime.date) or isinstance(obj, datetime.datetime):
            return self._convertDatetimeDate(obj)
        return obj

    def _convertPandasDataFrame(self, df):
        return pandasutils.dataframe_to_list_of_lists(df)

    def _convertPandasTimeSeries(self, ts):
        return pandasutils.timeseries_to_list_of_lists(ts)

    def _convertDatetimeDate(self, date):
        return dateutils.date_to_timestamp(date)
