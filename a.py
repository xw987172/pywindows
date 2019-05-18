# coding : utf8
import win32gui,win32api,win32con

#win = win32gui.FindWindow(None,"桌面")

win = win32gui.FindWindow(None,"代码生成器")
hhand = win32gui.FindWindowEx(win, None,None,"") 
hhand = win32gui.FindWindowEx(hhand, None,None,"HELP") #HELP按钮

left,top,right,bottom = win32gui.GetWindowRect(hhand) 

win32api.SetCursorPos([int((left+right)/2),int((top+bottom)/2)]) #放置鼠标指针

win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0) #鼠标单次点击


