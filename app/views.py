from app import app
from flask import request
from flask import make_response
from flask import redirect
from flask import render_template
from flask_bootstrap import Bootstrap
bootstrap=Bootstrap(app)
#from models import User,Post,Role_User,Role_Admin

@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name,title='zhao')


#def index():
#    return  redirect('http://www.baidu.com')


#def index():
#    response=make_response("<h6>it's a cookie</h6>")
#    response.set_cookie('answer,40')
#    return response


'''
def index():
    user_agent=request.headers.get('User-Agent')
    return "<p>your browers is %s </p> " % (user_agent)

@app.route('/user/<name>')
def user(name):

    return 'hello %s' % (name)
'''
