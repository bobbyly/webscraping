# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 08:21:00 2019

@author: bly6
"""
import sys
import pyautogui as pg
import time
start_time = time.time()
likekc = input('like kc: ')
im = pg.screenshot()

pg.FAILSAFE = True
pg.PAUSE = 0.8

pg.click(1000, 0)
print('i hope KAT is selected')
isthiskat = pg.pixelMatchesColor(160, 125,(30,93,167))
if isthiskat is False:
    sys.exit('i dont think this is KAT')
#worklist selection + click 1
pg.click(800, 175)
pg.click(800, 175)
#go to worksheet 
pg.click(230, 60)
#pause
print('waiting for the method popup')
time.sleep(2)
#enter
pg.typewrite('\n')
#pause
print('waiting for the second method popup')
time.sleep(1.5)
#press tab then enter
pg.typewrite(['\t', '\n'])
#force stock out
pg.click(240, 60)
print('send it!')
time.sleep(2)
#change variables
pg.click(320, 60)
#select sales tab
pg.click(650, 480)
#select first product variable
pg.click(650, 500)
#edit first product variable
pg.click(1330, 500)
#copy row
pg.click(1200, 560)
#scroll across + click 2
pg.doubleClick(1142, 675)
#select style_nbr
pg.click(1140, 545)
#search
pg.click(1240, 450)
#input clipboard (like style)
#pg.hotkey('ctrl','v')
pg.typewrite(likekc)
#pg.typewrite('42462187')
#enter
pg.typewrite('\n')

#break here if error
pg.moveTo(821, 516)
errorcheck = pg.pixelMatchesColor(821, 516, (252, 225, 0))
if errorcheck is True:
    sys.exit('like keycode not in this branch of the tree')
print('searching from the top of the list')
time.sleep(2)
#end of list message
pg.moveTo(784, 512)
eolmsg = pg.pixelMatchesColor(784, 512, (0,109,201))
if eolmsg is True:
    pg.typewrite('\n')

#break here if error
pg.moveTo(821, 516)    
errorcheck = pg.pixelMatchesColor(821, 516, (252, 225, 0))
if errorcheck is True:
    sys.exit('like keycode not in this branch of the tree')

#cancel
pg.click(1097, 545)
#OK
pg.click(1220, 380)
#enter
pg.typewrite('\n')
#enter
pg.typewrite('\n')
#wait until data is collected
pg.moveTo(1521, 1035)
while pg.pixelMatchesColor(1521, 1035, (255, 255, 0)) is True:
    if pg.pixelMatchesColor(1521, 1035, (255, 255, 0)) is False:
        break
    print('waiting...') 
    time.sleep(8)  
print('SORT is no longer yellow, but it might still be tuning')
#enter
pg.typewrite('\n')

#remove location details
pg.click(118, 31)
pg.click(190, 510)
#select allocated column
pg.click(220, 320)
pg.dragTo(220, 395)
#ctrl + C
pg.hotkey('ctrl','c', interval=0.1)

##accept split
#pg.click(808, 66)
##exit
#pg.click(30, 66)
##tab or right arrow
#pg.typewrite('\t')
##enter
#pg.typewrite('\n')

#nav to port splitter
#pg.hotkey('alt', 'tab', interval=0.1)
##macro combination (ctrl shift k)
#pg.keyDown('ctrl')
#pg.keyDown('shift')
#pg.keyDown('k')
#pg.keyUp('k')
#pg.keyUp('ctrl')
#pg.keyUp('shift')
print("seconds taken: ", time.time() - start_time)

