"""
flags.py 扩展功能标志
"""
import re

s = """Hello
北京"""

# 只能匹配ascii码
# regex = re.compile(r'\w+',flags=re.A)

# 忽略字母大小写
# regex = re.compile(r'[a-z]+',flags=re.I)

# 让 . 可以匹配\n
# regex = re.compile(r'.+',flags = re.S)

# ^ $ 可以匹配每行的开始结束位置
regex = re.compile(r'Hello$',flags=re.M)

l = regex.findall(s)
print(l)

