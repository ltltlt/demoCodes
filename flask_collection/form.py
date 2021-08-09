'''
  > File Name: form.py
  > Author: ty-l
  > Mail: liuty196888@gmail.com
'''

# Web 表单是在任何一个 web 应用程序中最基本的一部分。我们将使用表单允许用户写文章，以及登录到应用程序中。
# 使用flask-wtf, 其封装了WTForms并恰当的集成进flask中
import flask
from flask_wtf import FlaskForm      # Only the flask-wtf extension has the special Form class which can handle CSRF automatically / other stuff.
                                # flask_wtf.Form is the subclass of wtforms.Form
import wtforms      # use forms fields
import wtforms.validators

app = flask.Flask(__name__)
app.config.from_object('config')        # tell the app to read config from ./config.py

class myform(FlaskForm):
    theid = wtforms.StringField('id', validators = [wtforms.validators.DataRequired()])     # make sure it's not empty
    # theid() return this: <input id="theid" name="theid" type="text" value="">

    remember_me = wtforms.BooleanField('remember me', default=False)
    # remember_me return this: <input id="remerber_me" name="remerber_me" type="checkbox" value="y">

    password = wtforms.StringField('password', validators = [wtforms.validators.DataRequired()])
    # 只有当wtforms.(.*)Field在某个类中声明并且实例化此类，此Field才可调用，例：上面theid()
    # 如果Field在类外面声明，则其是为UboundField，不能调用。这种神奇机制我也不知道是怎么实现的
@app.route('/login', methods=['POST', 'GET'])
def login():
    ltyform = myform()
    if ltyform.validate_on_submit():
        message = 'user: %s password: %s remember me: %s login success'
        flask.flash(message % (ltyform.theid.data, ltyform.password.data, str(ltyform.remember_me.data)))
        return flask.redirect('/index')
    else:
        return flask.render_template('login.html', title='Login In', form = ltyform)

if __name__ == '__main__':
    app.run(debug=True)
