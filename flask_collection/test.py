'''
  > File Name: test.py
  > Author: ty-l
  > Mail: liuty196888@gmail.com
'''

import flask

app = flask.Flask(__name__)
app.config.from_object('config')

# flask will use cookie to keep connect with a session

@app.route('/')
def test():
    flask.flash('hello')        # flash the message to this session
    flask.flash('world')
    messages1 = flask.get_flashed_messages()
    print(messages1)
    flask.flash('zzz')
    messages2 = flask.get_flashed_messages()
    print(messages2)
    return ''.join(messages1) + '\n' + ''.join(messages2)
if __name__ == '__main__':
    app.run()
