# -*- coding: utf-8 -*-

import hashlib

str1 = "hello"
m = hashlib.md5()

#update()的参数必须是字节
#m.update(b'123')
m.update(bytes('123123', "utf-8"))
#m.update(str1.encode("utf-8"))

print(m.hexdigest())