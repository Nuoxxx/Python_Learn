# -*- coding:utf-8 -*-
from uiautomator import device as d
import time

d.screen.on()
d(text="Clock").click()
#打印手机信息
print d.info

####设备按键Key Event Actions of the device

# Turn on screen
d.screen.on()
# Turn off screen
d.screen.off()

# wakeup the device
d.wakeup()
# sleep the device, same as turning off the screen.
d.sleep()

#Press hard/soft key(还有其他健比如 left/right/up/down/center/menu/search)
#delete(or del)/recent(recent apps)/volume_up/volume_down/volume_mute/camera/power
# press home key
d.press.home()
# press back key
d.press.back()
# the normal way to press back key
d.press("back")
# press keycode 0x07('0') with META ALT(0x02) on
d.press(0x07, 0x02)
