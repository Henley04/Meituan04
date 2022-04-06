import sys
import time
import uiautomator2 as u2
import PySimpleGUI as Sg
d = u2.connect()
d = u2.connect()
layout = [
    [Sg.Text('开始程序?会关闭屏幕 Warning:Closing screen to connect device!')],
    [Sg.Yes(), Sg.No()]
]
window = Sg.Window('USB-HELPER', layout)  # GUI标题
event, value = window.Read()
window.Close()
if event in (None, 'No'):   # 如果用户关闭窗口或点击`No`
    sys.exit()
else:
    d.screen_off()
    d.screen_on()
    d.app_list_running()
    d.app_current
    sys.exit()