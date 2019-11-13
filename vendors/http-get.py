# -*- coding: utf-8 -*-

from urllib import request
from urllib import parse

url = "http://localhost/pyurl.php"

res = request.urlopen(url)
res = res.read()
res = res.decode("utf-8")

print(res)
