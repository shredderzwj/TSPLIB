# -*- coding: utf-8 -*-
# https://my.oschina.net/ahaoboy/blog/1823450

import requests
import os
from lxml import etree
from urllib.parse import urlparse

url = 'http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/index.html'
resp = requests.get(url)
text = resp.text

html = etree.HTML(text)
parse = urlparse(url)
root = 'http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/'
for a in html.xpath('//li/a'):
    name = a.xpath('./@href')[0]
    path = os.path.join('res', name)
    if os.path.exists(path):
        print('已存在%s' % name)
        continue
    durl = root + name
    dresp = requests.get(durl)
    with open(path, 'w') as fp:
        fp.write(dresp.text)
    print(name)
