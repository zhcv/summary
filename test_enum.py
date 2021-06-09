from enum import Enum

class Color(Enum):
    # 为序列值指定value值
    green = 1
    red = 1
    blue = 3

print(Color['green'])

print(Color.red)
