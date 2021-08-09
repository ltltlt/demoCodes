'''
  > File Name: jinja.py
  > Author: ty-l
  > Mail: liuty196888@gmail.com
'''

it will convert {{variable}}'s string variable into true variable

control statement need to write in {%...%}
<html>
    <head>
    {% if title %}
    <title>{{title}}</title>
    {% else %}
    <title>notitle</title>
    {% endif %}
    </head>
</html>

使用{% extends "some.html" %}来继承其他文档已有的内容
