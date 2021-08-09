'''''''''''''''''''''''''''''''''''''''''''''''''''
  > System:		Archlinux
  > Author:		ty-l6
  > Mail:		liuty196888@gmail.com
  > File Name:		url_for.py
  > Created Time:	2016-12-10 Sat 09:09
'''''''''''''''''''''''''''''''''''''''''''''''''''

import flask
app = flask.Flask(__name__)

flask.url_for(endpoint, _external=False, **kargs)
# endpoint should be a function name
# if _external is True, return absolutely url
# kargs will pass as argument

@app.route('/<name>')
def index(name):
    return name
flask.url_for('index', name='ss')   # got '/ss'
flask.url_for('index', _external=True, name='ww')   # 'localhost:5000/ww'
flask.url_for('index', name='www', a='11', b='22')  # /www?a=11&b=22

flask.url_for('static', filename='css/my.css', _external=True)
# localhost:5000/static/css/my.css
