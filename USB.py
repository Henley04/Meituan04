# -*- coding: UTF-8 -*-
import sys
import time
import uiautomator2 as u2
from interval import Interval
import PySimpleGUI as Sg
from threading import Thread
from tkinter import *  # 导入tkinter库
from tkinter import font  # 从tkinter库中调用font模块，对字体的属性进行系统的设置
from tkinter.messagebox import *  # 从tkinter库中调用messagebox模块,生成弹窗界面

"""
*** WARNING ***
Deletes file without asking for verification will occur errors!


"""

d = u2.connect()
layout = [
    [Sg.Text('开始程序?Start?')],
    [Sg.Yes(), Sg.No()]
]
window = Sg.Window('USB', layout)  # GUI标题
event, value = window.Read()
window.Close()
if event in (None, 'No'):  # 如果用户关闭窗口或点击`No`
    sys.exit()

try:
    while True:
        # 当前时间
        now_localtime = time.strftime("%HH:%MM:%SS", time.localtime())
        # 当前时间（以时间区间的方式表示）
        now_time = Interval(now_localtime, now_localtime)
        print(now_time)
        time_interval = Interval("05:59:58", "06:01:00")  # Pass with test!
        print(time_interval)

        if now_time in time_interval:  # OK
            time.sleep(1.98)
            d.xpath('//android.support.v4.view.ViewPager/android.view.ViewGroup[1]/android.view.ViewGroup[1]/'
                    'android.view.ViewGroup'
                    '[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[3]').click()
            d.implicitly_wait(2)
            d.xpath('//*[@text="我知道了"]').click_exists(0.1)  # Server Error button
            d.xpath('//*[@resource-id="android:id/content"]'
                    '/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                    'android.widget.FrameLayout[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]'
                    '/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]'
                    '/android.view.ViewGroup[1]/android.view.ViewGroup[1]').click_exists()
            while True:  # Try many times to connect to server...
                d.xpath('//android.support.v4.view.ViewPager/android.view.ViewGroup[1]/android.view.ViewGroup[1]/'
                        'android.view.ViewGroup'
                        '[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/'
                        'android.view.ViewGroup[3]').click_exists()  # Shopping cart/buy button
                d.implicitly_wait(0.1)
                d.click(0.485, 0.521)  # if Err exist ,Press Server Error notice button
                d.xpath('//android.support.v4.view.ViewPager/android.view.ViewGroup[1]/android.view.ViewGroup[1]/'
                        'android.view.ViewGroup'
                        '[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/'
                        'android.view.ViewGroup[3]').click_exists()  # Retry
                d.xpath('//*[@resource-id="android:id/content"]'
                        '/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                        'android.widget.FrameLayout[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]'
                        '/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]'
                        '/android.view.ViewGroup[1]/'
                        'android.view.ViewGroup[1]').click_exists()  # Try Give information to server again...
                d(text='12:00-12:30').click_exists()
                d(text='11:00-11:30').click_exists()
                d(text='9:00-9:30').click_exists()
                d.xpath('//*[@resource-id="android:id/content"]'
                        '/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/'
                        'android.widget.FrameLayout[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]'
                        '/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]'
                        '/android.view.ViewGroup[1]/'
                        'android.view.ViewGroup[1]').click_exists()  # Try Give information to server again...


except KeyboardInterrupt:
    layout1 = [
        [Sg.Text('Exit with Err:KeyboardInterrupt')],
        [Sg.Yes()]
    ]
    window1 = Sg.Window('USB', layout1)  # GUI标题
    _, value1 = window1.Read()
    window1.Close()

except RuntimeError:
    showerror(title="Error", message='Connection Err:Check ADB, USB connect and Developer Settings')  # 显示弹窗
except:
    print('except')
