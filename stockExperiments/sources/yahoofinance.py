import collections
import csv
import datetime
import urllib
import urllib2


def historical_prices(symbol, start_date=None, end_date=None):
    response = _ichart_request(symbol, start_date, end_date)
    try:
        raw = csv.reader(response)
        tuple = collections.namedtuple('HistoricalPrice', [directive.lower().replace(' ', '_') for directive in next(raw)])
        return [tuple(*map(_convert_string, row)) for row in raw]
    finally:
        response.close()


def _ichart_request(symbol, start_date, end_date, extra_params=[], resource='table.csv'):
    params = {'s': symbol}
    params.update(extra_params)

    if start_date:
        params.update({
            'a': '%d' % (start_date.month - 1),
            'b': '%d' % (start_date.day),
            'c': '%d' % (start_date.year),
        })
    if end_date:
        params.update({
            'd': '%d' % (end_date.month - 1),
            'e': '%d' % (end_date.day),
            'f': '%d' % (end_date.year),
        })

    data = urllib.urlencode(params)
    return urllib2.urlopen('http://ichart.finance.yahoo.com/%s?%s' % (resource, data))


def _convert_string(field, strptime_string=None, strptime_cache={}):
    if '-' in field:
        return datetime.date(*map(int, field.split('-')))
    elif '.' in field:
        return float(field)
    return int(field)