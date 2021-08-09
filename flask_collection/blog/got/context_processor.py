'''''''''''''''''''''''''''''''''''''''''''''''''''
  > System:		Archlinux
  > Author:		ty-l6
  > Mail:		liuty196888@gmail.com
  > File Name:		context_processor.py
  > Created Time:	2016-12-18 Sun 12:42
'''''''''''''''''''''''''''''''''''''''''''''''''''

context processor 上下文处理器

Flask 上下文处理器自动向模板的上下文中插入新变量。上下文处理器在模板渲染之前运行，并且可以在模板上下文中插入新值。

上下文处理器是一个返回字典的函数，这个字典的键值最终将传入应用中所有模板的上下文

@app.context_processor
def somef():
    return dict(x=1)        # 之后x在模板中可用

变量不仅限于值，上下文处理器也可以使某个函数在模板中可用

@setupmethod
def context_processor(self, f):
    self.template_context_processors[None].append(f)
    return f

在蓝本中要使用app_context_processor，否则是注册仅此蓝本的上下文处理器
