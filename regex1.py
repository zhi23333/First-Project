"""
regex1.py re模块 功能函数演示2
生成 match 对象
"""

import re

s = "今年是2019年,建国70周年"

pattern = r"\d+"
# 返回迭代对象
it = re.finditer(pattern,s)
for i in it:
    print(i.group()) # 获取match对象对应内容

# 完全匹配
obj = re.fullmatch(r'.+',s)
print(obj.group())

# 匹配开始位置
obj = re.match(r'\w+',s)
print(obj.group())

# 匹配第一处
obj = re.search(r'\d+',s)
print(obj.group())