"""
import headers
"""

import torch

# user code begin

stripStr = "  this is a string!  \n  "
stripStrProcessed = stripStr.rstrip()
print(stripStrProcessed)
stripStrProcessed = stripStrProcessed.strip()
print(stripStrProcessed)
strJoinList = ['1', '2', '3']
print('#'.join(strJoinList))
strJoin = ('#'.join(strJoinList))
print(strJoin)
print(strJoin.split('#'))
lastName = b'\xe5\x8a\x89'
print(lastName.decode('utf-8'))

setSet = {num for num in range(1, 20) if num % 5 == 0}
print(setSet)
set1 = {1, 2, 4}
set2 = {2, 4, 5}
print(set1 ^ set2)



