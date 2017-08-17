# -*- coding:utf-8 -*-
from uiautomator import device as d
import time

#Retrieve/Set Orientation设置或恢复屏幕方向
#natural or n
#left or l
#right or r
#upsidedown or u (can not be set)

# retrieve orientation, it may be "natural" or "left" or "right" or "upsidedown"
orientation = d.orientation
# set orientation and freeze rotation.
# notes: "upsidedown" can not be set until Android 4.3.
d.orientation = "l" # or "left"
d.orientation = "r" # or "right"
d.orientation = "n" # or "natural"

#Freeze/Un-Freeze rotation锁定/解锁屏幕方向
# freeze rotation
d.freeze_rotation()
# un-freeze rotation
d.freeze_rotation(False)

#Take screenshot
# take screenshot and save to local file "home.png", can not work until Android 4.2.
d.screenshot("home.png")

#Dump Window Hierarchy
# dump the widown hierarchy and save to local file "hierarchy.xml"
d.dump("hierarchy.xml")
# or get the dumped content(unicode) from return.
xml = d.dump()

#Open notification or quick settings
# open notification, can not work until Android 4.3.
d.open.notification()
# open quick settings, can not work until Android 4.3.
d.open.quick_settings()

#Wait for idle or window update
# wait for current window to idle
d.wait.idle()
# wait until window update event occurs
d.wait.update()
