from datetime import datetime
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/')
def index():
     return render_template('index.html', current_time=datetime.utcnow())


@app.route('/user/<name>/<pronto>/<facu>')
def user(name, pronto, facu):
    return render_template('user.html', name=name, pronto=pronto, facu=facu)


@app.route("/contextorequisicao/<name>") #teste
def contex(name):
    user_agent = request.headers.get('User-Agent')
    url = request.remote_addr
    ip = request.host_url
    return render_template('contex.html', user_agent=user_agent, url=url, ip=ip, name=name)