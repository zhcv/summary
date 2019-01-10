# UnicodeDecodeError: 'utf8' codec can't decode byte 0x9c
##
[reference](http://docs.python.org/howto/unicode.html#the-unicode-type) 
[refer2](https://stackoverflow.com/questions/12468179/unicodedecodeerror-utf8-codec-cant-decode-byte-0x9c)
```python
import json
str = unicode(str, errors='ignore')
object = json.loads(str)

## method2
import codecs
with codecs.open(file_name, 'r',encoding='utf-8', errors='ignore') as fdata:
   objects = json.loads(fdata)
```

