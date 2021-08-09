'''
  > File Name: basic_function.py
  > Author: ty-l
  > Mail: liuty196888@gmail.com
'''

import flask
import sqlite3

app = flask.Flask(__name__)
app.open_resource(filename, mode)       # just like open function, and i don't know what it's for. mode can only be r or rb

app.before_request()
app.after_request()
# these two are decorators. the function before_request decorate will called before one request, after_request decorated will called after one request
# 用 before_request() 装饰的函数在每次请求之前 被调用，它没有参数。
# 用 after_request() 装饰的函数是在每次请求结束后被调用，而且它需要传入response。这类函数必须返回同一个response 对象或者一个不同的response对象。
# example:
@app.before_request()
def before():
    flask.g.db = sqlite3.connect('some.db')
@app.after_request()
def after(response):
    flask.g.db.close()
    return response
# flask.g对象只能为一个请求保持信息（每个请求的信息都不同）(如果每个请求都用一个线程，那可以使用thread_local实现)

flask.session       # The session object works pretty much like an ordinary dict, with the difference that it keeps track on modifications.
    flask.session.new   # True if the session is new, False otherwise.
    flask.session.modified  # True if the session object detected a modification.

    # If set to True the session life for permanent_session_lifetime seconds. The default is 31 days.
    # If set to False (which is the default) the session will be deleted when the user closes the browser.
    flask.session.permanent 

flask.url_for(endpoint, **values)
# endpoint – the endpoint of the URL (name of the function)
# Generates a URL to the given endpoint(callable object) with the method provided.
# Variable arguments that are unknown to the target endpoint are appended to the generated URL as query arguments. 
# In case blueprints are active you can shortcut references to the same blueprint by prefixing the local endpoint with a dot (.). references url.
    # note that endpoint can also be 'static', then you must specify a filename keyword, such as flask.url_for('static', filename='somename.css')
    # it's quite useful in use <link> to reference css file in static/somename.css

flask.abort(code)       # Raises an HTTPException for the given status code. such as: page not found(abort(404))

# Returns a response object (a WSGI application) that, if called, redirects the client to the target location.
flask.redirect(location, code=302, Response=None)
# example:
@app.route('/')
def test():
    return flask.redirect('/index')     
    # note: if the return value is string, it will return to the client. if it's callable object, it will be called and return the result to client

flask.flash(message, category='message')
# Flashes a message to the next request. 
# In order to remove the flashed message from the session and to display it to the user, the template has to call get_flashed_messages().
# category – the category for the message. 
    # The following values are recommended: 'message' for any kind of message, 'error' for errors, 'info' for information messages and 'warning' for warnings. However any kind of string can be used as category.

flask.get_flashed_messages(with_categories=False, category_filter=[])
# Pulls all flashed messages from the session and returns them. return a list.
# Further calls in the same request to the function will return the same messages.
# By default just the messages are returned.
# but when with_categories is set to True, the return value will be a list of tuples in the form (category, message) instead.


flask.render_template(template_file, **context)
# Renders a template from the template folder with the given context.
# template_name – the name of the template to be rendered
# context – the variables that should be available in the context of the template.
# example:
# flask.render_template('test.html', llll = 'llll', wwww = 'wwwww')
# here is test.html
# <html><body><p>llll is {{llll}} and wwww is {{wwww}}</p></body></html>

flask.render_template_string(string, **context)
# just like render_template, change file to string


class flask.Config          # Works exactly like a dict but provides ways to fill it from files or special dictionaries. 
flask.Config.from_pyfile(somefile)  # update the config from file

flask.Config.from_envvar(variable_name, silent=False)
# shortcut of flask.Config.from_pyfile(os.environ[variable_name])

config.from_object(obj)
# Updates the values from the given object. An object can be of one of the following two types:
    # a string: in this case the object with that name will be imported
    # an actual object reference: that object is used directly      # Objects are usually either modules or classes.
config.from_object('some.config_dict')
# above equals to:
from some import config_dict
config.from_object(config_dict)


# in all cases, only uppercase keys are added to the config. This makes it possible to use lowercase values in the config file for temporary values that are not added to the config or to define the config keys in the same file that implements the application.
