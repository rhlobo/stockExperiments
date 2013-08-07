from datetime import datetime as d
import util.testutils as testutils


class TestNormalizatedCotationDatasource(testutils.DatasourceTestCase):

    def test_should_return_correct_normalizated_cotation_using_mocked_data(self):
        testutils.assert_datasource_correctness_using_datafiles(self,
                                                                'PETR4', None, None,
                                                                'NORMALIZED:RAW_BOVESPA',
                                                                'normalized_PETR4.csv',
                                                                ('NORMALIZATION_FACTOR:SPLITS:PCT_CHANGE(1):RAW_BOVESPA', 'normalizationfactor_PETR4.csv'),
                                                                ('RAW_BOVESPA', 'raw_PETR4.csv'))

    def test_should_return_correct_normalizated_cotation_using_mocked_data_no_splits(self):
        testutils.assert_datasource_correctness_using_datafiles(self,
                                                                'NO-SPLITS', None, None,
                                                                'NORMALIZED:RAW_BOVESPA',
                                                                'normalized_NO-SPLITS.csv',
                                                                ('NORMALIZATION_FACTOR:SPLITS:PCT_CHANGE(1):RAW_BOVESPA', 'normalizationfactor_NO-SPLITS.csv'),
                                                                ('RAW_BOVESPA', 'raw_NO-SPLITS.csv'))

    def test_should_return_correct_normalizated_cotation_using_mocked_data_with_splits(self):
        testutils.assert_datasource_correctness_using_datafiles(self,
                                                                'WITH-SPLITS', None, None,
                                                                'NORMALIZED:RAW_BOVESPA',
                                                                'normalized_WITH-SPLITS.csv',
                                                                ('NORMALIZATION_FACTOR:SPLITS:PCT_CHANGE(1):RAW_BOVESPA', 'normalizationfactor_WITH-SPLITS.csv'),
                                                                ('RAW_BOVESPA', 'raw_WITH-SPLITS.csv'))
