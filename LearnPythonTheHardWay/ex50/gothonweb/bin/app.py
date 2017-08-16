# -*- coding:utf-8 -*-
# 导入 web.py模块
import web

# urls = (
#     '/','Index'
# )
# URL结构，第一部分是正则表达式，用来匹配一个URL
# hello :第二部分是处理请求的类的名字
urls = (
    '/(.*)','hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello,' + name + '!'


# web.template.render对象用于加载templates/目录下的html文件
# render = web.template.render('templates/')
# class Index(object):
#     def GET(self):
#         greetingContent = "Hello World"
#         # render在templates/目录下寻找index.html并渲染
#         #return render.index(greeting = greetingContent)
#         return render.foo()

# 开始提供网页服务
if __name__ == "__main__":
    app.run()
