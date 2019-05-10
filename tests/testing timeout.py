# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 14:27:35 2019

@author: BLY6
"""
timeout = 4
compMsgWait = 0
var3 = 0
"""
while timeout < 15:
    print(timeout)
    timeout += 1
    while timeout > 2:
        print('more than 2')
        timeout += 1
        break
"""

while compMsgWait < 2:
    print('compmsgwait'+str(compMsgWait))
    timeout += 1
    compMsgWait += 1
    if timeout > 5:
        break
print(timeout)
while var3 < 5:
    print('var'+str(var3))
    timeout += 1
    var3 +=1
    if timeout > 5:
        break
print('the approve button is now green')

