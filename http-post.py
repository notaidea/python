# -*- coding: utf-8 -*-

from urllib import request
from urllib import parse

url = "http://localhost/pyurl.php"

data = {"name" : "peter", "age" : 18}
data = parse.urlencode(data)
data = data.encode("utf-8")

newUrl = request.Request(url, data)
res = request.urlopen(newUrl)
res = res.read()
res = res.decode("utf-8")

print(res)