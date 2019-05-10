import win32gui
import pyautogui as pg
import sys

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
def focuswindow():
    if __name__ == "__main__":
        #results = []
        top_windows = []
        win32gui.EnumWindows(windowEnumerationHandler, top_windows)
        for i in top_windows:
            if windowname.lower() in i[1].lower(): #looks like it has to be in lowercase
                print
                i
                win32gui.ShowWindow(i[0], 5)
                win32gui.SetForegroundWindow(i[0])
                break
            

#windowname = pg.prompt(text='Window Name', title='Which Window?' , default='Book1 - Excel')
windowname = 'JDA Allocation'
try:
    activewindow = pg.getWindowsWithTitle(windowname)[0]
except:
    print('KAT not open')
    sys.exit()
activewindow.restore()
if activewindow.isMaximized is False:
    activewindow.maximize()
focuswindow()

        


