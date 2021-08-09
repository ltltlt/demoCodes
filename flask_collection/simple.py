'''
  > File Name: simple.py
  > Author: ty-l
  > Mail: liuty196888@gmail.com
'''

import flask

app = flask.Flask(__name__)

@app.route('/')
def hello():
    myhtml = '''
    <html>
        <body>
            <h1 style="text-align:center;color='yellow'">hello</h1>
            <p>hey, nice to meet you!</p>
            he says:<blockquote>his handsome</blockquote>
        </body>
    </html>
    '''
    return myhtml
@app.route('/name/<somename>')      # 用<>扩起来的部分会被当作参数传到函数中
def name(somename=None):
    return flask.render_template('hello.html', name=somename)       # it will search hello.html in ./templates/hello.html

@app.route('/post/<int:post_id>')       # post/后的路径名只接受int型，如果提供字符串会显示404
def show_post(post_id):
    return 'Post %d' % post_id
@app.route('/post1/<path:post_str>')       # post1/后的路径名接受字符串，字符串可以包括/(不以/作为分割符，默认str以/作为分割符)
def show_post1(post_str, method=['GET', 'POST']):
    return 'Post1 %s' % post_str

if __name__ == '__main__':
    app.run(host='localhost', debug=True)       # i guess use debug=True will call cgitb.enable()
