'''
  > File Name: main.py
  > Author: ty-l
  > Mail: liuty196888@gmail.com
'''

import flask
import flask_wtf
import wtforms
import wtforms.validators
import sqlite3

app = flask.Flask(__name__)
app.config.from_pyfile('config.py')

class myform(flask_wtf.FlaskForm):
    theid = wtforms.StringField('id', validators = [wtforms.validators.DataRequired()])
    password = wtforms.StringField('password', validators = [wtforms.validators.DataRequired])
class myform2(flask_wtf.FlaskForm):
    title = wtforms.StringField('title', validators = [wtforms.validators.DataRequired()])
    content = wtforms.TextAreaField('content', validators = [wtforms.validators.DataRequired])

@app.before_request
def before_request():
    flask.g.db = sqlite3.connect('little.db')
@app.after_request
def after_request(response):
    flask.g.db.close()
    return response

@app.route('/')
@app.route('/index')
def index_f():
    return flask.render_template('index.html')
@app.route('/login', methods=['POST', 'GET'])
def login_f():
    ltyform = myform()
    errors = []
    if flask.request.method == 'POST':
        if flask.session.get('loginin', None):      # check whether login before
            errors.append('already login in. are you crazy?')
        if ltyform.theid.data != app.config['USERNAME']:
            errors.append('bad user name!')
        if ltyform.password.data != app.config['PASSWORD']:
            errors.append('bad password!')
        else:
            flask.session['loginin'] = True
            flask.session['name'] = ltyform.theid.data
            return flask.redirect(flask.url_for('show_f'))
    return flask.render_template('login.html', ltyform = ltyform, errors = errors)
@app.route('/show')
def show_f():
    ltyform1 = myform2()
    cursor = flask.g.db.cursor()
    cursor.execute('select * from articles')
    articles = [dict(iid=row[0], title=row[1], content=row[2]) for row in cursor]
    print(articles)
    return flask.render_template('show.html', ltyform1 = ltyform1, cursor=articles)
@app.route('/logout')
def logout_f():
    flask.session.pop('loginin', None)
    flask.session.pop('name', None)
    return flask.render_template('logout.html')
@app.route('/add_entry', methods=['POST'])
def add_entry_f():
    if not flask.session.get('loginin', None):
        flask.abort(401)
    if flask.request.form['title'] and flask.request.form['content']:
        flask.g.db.execute('insert into articles(title, content) values(?, ?)', (flask.request.form['title'], flask.request.form['content']))
        flask.g.db.commit()
        flask.flash('New article add success!')
    else:
        if not flask.request.form['title']:
            flask.flash('you should write your title')
        else:
            flask.flash('you should write something in your content!!')
    return flask.redirect(flask.url_for('show_f'))

if __name__ == '__main__':
    app.run()
