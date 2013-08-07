# -*- coding: utf-8 -*-


from ipyghstocks.chart import *
from ipyghstocks.options import *


def candlestick(engine, reference, symbol, start=None, end=None):
    dataframe = engine.get(reference).process(symbol, start, end)
    return plot(Options(reference)
                .add(Axis(symbol))
                .add(Series(reference,
                            dataframe,
                            chartType=CANDLESTICK)))


def percentual(engine, base_reference, reference, symbol, start=None, end=None):
    base = engine.get(base_reference).process(symbol, start, end)
    data = engine.get(reference).process(symbol, start, end)
    return plot(Options(reference)
                .add(Axis('Percentual Change',
                          top=70,
                          height=240))
                .add(Axis(symbol,
                          top=325,
                          height=80))
                .add(Series(reference,
                            data,
                            chartType=CANDLESTICK))
                .add(Series(base_reference,
                            base,
                            yAxisIndex=1,
                            chartType=CANDLESTICK)))


def macd(engine, base_reference, reference, symbol, start=None, end=None):
    base = engine.get(base_reference).process(symbol, start, end)
    data = engine.get(reference).process(symbol, start, end)
    return plot(Options(reference)
                .add(Axis(symbol,
                          top=70,
                          height=200))
                .add(Axis('MACD',
                          top=285,
                          height=120))
                .add(Series(base_reference,
                            base,
                            chartType=CANDLESTICK))
                .add(Series('Histogram',
                            data['histogram'],
                            yAxisIndex=1,
                            chartType=COLUMN,
                            color='blue'))
                .add(Series('MACD',
                            data['macd'],
                            yAxisIndex=1,
                            chartType=LINE,
                            color='purple'))
                .add(Series('Signal',
                            data['signal'],
                            yAxisIndex=1,
                            chartType=LINE,
                            color='orange')))
