# -*- coding:utf-8 -*-
# 导入 web.py模块
import web

# urls = (
#     '/','Index'
# )
# URL结构，第一部分是正则表达式，用来匹配一个URL
# hello :第二部分是处理请求的类的名字
urls = (
    '/hello','Index'
)
app = web.application(urls, globals())

# web.template.render对象用于加载templates/目录下的html文件
render = web.template.render('templates/',base ="layout" )

# class Index(object):
#     def GET(self):
#         # web.input
#         form = web.input(name = "Nobody", greet = None)
#
#         if form.greet:
#             greeting = "%s, %s" % (form.name, form.greet)
#             return render.index(greeting = greeting)
#         else:
#             return "ERROR: greet is required."

class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(name = "Nobody", greet = "Hello")
        greeting = "%s, %s" % (form.greet, form.name)
        return render.index(greeting = greeting)


# 开始提供网页服务
if __name__ == "__main__":
    app.run()
