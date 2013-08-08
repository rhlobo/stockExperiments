# -*- coding: utf-8 -*-


class DatasourceLogger(object):

    def __init__(self):
        self.logs = []

    def log(self, description, dataframe):
        self.logs.append((description, dataframe))

    def print_summary(self):
        for description, dataframe in self.logs:
            title = description + ' ' + ((80 - len(description) - 1) * '-')
            size = len(dataframe.index)
            start = '-------------------' if size is 0 else dataframe.index[0]
            end = '-------------------' if size is 0 else dataframe.index[-1]
            print '[ %s : %s ] ~ %i \t > \t %s' % (start, end, size, title)
        for description, dataframe in self.logs:
            print ''
            title = description + ' ' + ((80 - len(description) - 1) * '-')
            print title
            print dataframe.head(2)
            print dataframe.tail(2)


def assure_is_valid_set(obj):
    if not obj:
        obj = set()
    elif not isinstance(obj, set):
        try:
            obj = set(obj)
        except:
            obj = set()
    return obj


def slice(slicable, start=None, end=None):
    if start and end:
        return slicable[start:end]
    if start:
        return slicable[start:]
    if end:
        return slicable[:end]
    return slicable


def assert_dataframe_almost_equal(expected, actual, margin=0.0000000001):
    tmp = ((expected.dropna() - actual.dropna()).abs() < margin)
    assert tmp.all().all()
