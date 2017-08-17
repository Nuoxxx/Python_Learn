# -*- coding:utf-8 -*-
from uiautomator import device as d
import time
import unittest

class MyTestSuite(unittest.TestCase):
    # 初始化工作
    def setUp(self):
        print "--------------初始化工作"

    # 退出清理工作
    def tearDown(self):
        print "--------------退出清理工作"

    #***************************方法**************************************
    # 判断控件是否存在 & text
    def test_Cal(self):
        print "Hello"
        try:
            #d.press.home()
            #d.click(384,1104)
            #time.sleep(1)
            #
            d(className="android.widget.TextView", index = 5).click()
            #d.click(100,1000)
            time.sleep(1)
# d(scrollable=True).scroll.toEnd()
# print "over"
# functionItems = d.UiScrollable(d.UiSelector().className("android.widget.ListView"))
#点击“我的”
            d(resourceId="com.ccvt.dajia:id/my_img").click()
            time.sleep(1)
            #点击某个摄像头
            d.click(540,900)
            time.sleep(1)
            #点击查看录像
            d(resourceId="com.ccvt.dajia:id/video_btn").click()
        except Exception,e:
            print "Error",e
        #self.assertEqual()
#
#print d(className="android.widget.ListView").child().info[u'text']
def test_app():
    test_unit = unittest.TestSuite()
    test_unit.addTest(MyTestSuite("test_Cal"))

if __name__ == "__main__":
    # 测试app
    unittest.main()
# dd=d(className="android.widget.ListView").child(textContains='A'+'p')
# dd=d(className="android.widget.ListView").child(textMatches=r'A(\w+)')
# dd=d(className="android.widget.ListView")
# for ch in xrange(0x41, 0x5A):
#     a=unichr(ch).lower()
    # print a
    # print d(className="android.widget.ListView").child(textContains='A'+a).info[u'text']

    # try:
    #     print dd.child(textContains='A'+a).info[u'text']
    # except:
    #     continue

# print dd.info[u'text']

# a={'Accessibility','Animation'}
# for x in a:
#     print d(className="android.widget.ListView").child(text=x).info
#print d(className="android.widget.ListView").child(text="Arcs").info
