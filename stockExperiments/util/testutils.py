# -*- coding: utf-8 -*-


import os
import pandas

import util.fileutils as fileutils


def get_dataframe_from_csv(test_file, filename, test_filename_to_data_dir_function=None):
    filepath = fileutils.get_test_data_file_path(test_file, filename, test_filename_to_data_dir_function)
    return pandas.DataFrame.from_csv(filepath)


class CallableMock(object):
    def __init__(self, mock):
        self.mock = mock

    def __call__(self, *args, **kwargs):
        return self.mock.__call__(*args, **kwargs)

    def __getattr__(self, method_name):
        return self.mock.__getattr__(method_name)


class IterableMock(object):
    def __init__(self, mock):
        self.mock = mock

    def __iter__(self, *args, **kwargs):
        return self.mock.__iter__(*args, **kwargs)

    def __getattr__(self, method_name):
        return self.mock.__getattr__(method_name)


def should_skip_provider_deep_tests():
    return os.environ.get('TESTTYPE') == 'fast'


def get_providers_deep_tests_skip_reason():
    if os.environ.get('TESTTYPE') == 'fast':
        return 'Fast test execution requested through environment variable.'
    return 'Providers deep tests are disabled.'


def assert_data_index_is_ordered(data):
    lastDate = data.ix[0].name
    for row in data.iterrows():
        currDate = row[0]
        assert currDate >= lastDate
        lastDate = currDate


def assert_dataframe_almost_equal(expected, actual, margin=0.0000000001):
    tmp = ((expected.dropna() - actual.dropna()).abs() < margin)
    assert tmp.all().all()
