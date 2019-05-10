# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 13:35:57 2019

@author: bly6
"""

import sys
import pyautogui as pg
import win32gui

pg.FAILSAFE = True
pg.PAUSE = 0.5

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
def focuswindow():
    if __name__ == "__main__":
        #results = []
        top_windows = []
        win32gui.EnumWindows(windowEnumerationHandler, top_windows)
        for i in top_windows:
            if windowname.lower() in i[1].lower(): # var has to be in lowercase
                print
                i
                win32gui.ShowWindow(i[0], 5)
                win32gui.SetForegroundWindow(i[0])
                break


windowname = 'JDA Allocation'
try:
    activewindow = pg.getWindowsWithTitle(windowname)[0]
except:
    print('KAT not open')
    sys.exit()
activewindow.restore()
if activewindow.isMaximized is False:
    activewindow.maximize()

pg.click(1000, 0)
print('i hope KAT is selected')

isthiskat = pg.pixelMatchesColor(160, 125,(30,93,167))
if isthiskat is False:
    print('i don\'t think this is KAT. '
          'i\'ll see if i can bring it into focus.')
    try:
        for i in pg.getAllTitles():
            trackwindows = pg.getWindowsWithTitle(i)[0]
            if windowname in str(trackwindows):
                trackwindows.maximize()
                break
            else:
                trackwindows.minimize()
        focuswindow()
        print('i had to minimize everything to bring KAT into focus')
    except:
        sys.exit('sorry, but i can\'t bring KAT into focus')
    
print('i hope this is finally KAT')    
