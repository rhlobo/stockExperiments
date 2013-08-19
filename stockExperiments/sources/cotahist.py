# -*- coding: utf-8 -*-


import pandas
import util.fileutils as fileutils
import util.datastructutils as structutils
import bovespaparser.bovespaparser as bvparser


class CotahistImporter(object):

    def __init__(self, s_data_dir):
        self.dataFrameMap = {}

        dataMap = structutils.LazyDict(structutils.ListFactory())
        mapping = [("open", 1), ("high", 2), ("low", 3), ("close", 4), ("volume", 5)]

        for symbol, datetime, f_open, f_min, f_max, f_close, volume in _import_data(_get_cotahist_file_paths(s_data_dir)):
            c_symbolData = dataMap.get(symbol)
            c_symbolData.append([datetime, f_open, f_max, f_min, f_close, volume])

        for symbol in dataMap.keys():
            dataMap.get(symbol).sort()
            ll_data = zip(*dataMap.get(symbol))
            ldt_index = ll_data[0]
            ts_dict = dict((s_name, pandas.TimeSeries(ll_data[i_columnIndex], index=ldt_index, name=s_name)) for s_name, i_columnIndex in mapping)
            self.dataFrameMap[symbol] = pandas.DataFrame(ts_dict, columns=['open', 'high', 'low', 'close', 'volume'])

    def getDataFrameMap(self):
        return self.dataFrameMap


def _import_data(ls_filenames):
    result = []
    for s_file in ls_filenames:
        with open(s_file, 'rU') as f:
            result.extend(bvparser.parsedata(f))
    return result


def _get_cotahist_file_paths(s_data_dir):
    return fileutils.listdir(s_data_dir, r'COTAHIST_A[\d]{4}\.txt$')
