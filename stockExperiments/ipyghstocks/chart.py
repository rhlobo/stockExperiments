# -*- coding: utf-8 -*-


from IPython.display import HTML as export
import random
from ipyghstocks import options as options


def plot(configuration):
    cid = _generate_id()
    html = (_generate_container_html(cid) +
            _generate_javascript(cid, configuration.json() if isinstance(configuration, options.Options) else configuration) +
            _importLibs(cid))
    return export(html)


def _generate_id():
    return 'x%030x' % random.randrange(256 ** 15)


def _generate_container_html(container_id):
    return r'<div id="%s" style="min-height: 500px; min-width: 500px; border: 1px solid gray;" />​' % (container_id)


def _generate_javascript(container_id, code):
    return '''
           <script>
               function draw%s() {
                   $('#%s').highcharts('StockChart', %s);
               }
           </script>
           ''' % (container_id, container_id, code)


def _importLibs(container_id):
    return r'''
            <script>
                $.getScript("http://code.highcharts.com/stock/highstock.js", function(script, textStatus, jqXHR) {
                    $.getScript("http://code.highcharts.com/stock/modules/exporting.js", function(script, textStatus, jqXHR) {
                        draw%s();
                    });
                });
            </script>
           ''' % (container_id)
