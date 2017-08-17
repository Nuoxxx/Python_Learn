# -*- coding:utf-8 -*-
from uiautomator import device as d
import time
#### 手势

# click (x, y) on screen
d.click(x, y)
# long click (x, y) on screen
d.long_click(x, y)

# swipe from (sx, sy) to (ex, ey)
d.swipe(sx, sy, ex, ey)
# swipe from (sx, sy) to (ex, ey) with 10 steps
d.swipe(sx, sy, ex, ey, steps=10)

# drag from (sx, sy) to (ex, ey)
d.drag(sx, sy, ex, ey)
# drag from (sx, sy) to (ex, ey) with 10 steps
d.drag(sx, sy, ex, ey, steps=10)
