import unittest
import datetime
import os
import configurations as config


class TestConfigurations(unittest.TestCase):

    def test_startDate_configuration_should_return_date_object(self):
        assert isinstance(config.START_DATE, datetime.date)

    def test_startDate_configuration_should_return_2000_01_01(self):
        assert datetime.date(2000, 01, 01) == config.START_DATE

    def test_startDate_configuration_should_always_return_same_date(self):
        assert config.START_DATE == config.START_DATE
        assert config.START_DATE is config.START_DATE

    def test_cotahistInputDataDir_configuration_should_return_string(self):
        assert isinstance(config.COTAHIST_INPUT_DATA_DIR, str)

    def test_cotahistInputDataDir_configuration_should_return_path_that_exists(self):
        assert os.path.exists(config.COTAHIST_INPUT_DATA_DIR)

    def test_cotahistInputDataDir_configuration_should_return_a_folder_path(self):
        assert os.path.isdir(config.COTAHIST_INPUT_DATA_DIR)

    def test_datasourceTestDataDir_configuration_should_return_string(self):
        assert isinstance(config.DATASOURCE_TEST_DATA_DIR, str)

    def test_datasourceTestDataDir_configuration_should_return_path_that_exists(self):
        assert os.path.exists(config.DATASOURCE_TEST_DATA_DIR)

    def test_datasourceTestDataDir_configuration_should_return_a_folder_path(self):
        assert os.path.isdir(config.DATASOURCE_TEST_DATA_DIR)
