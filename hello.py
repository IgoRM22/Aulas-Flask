from datetime import datetime
from flask import Flask, render_template
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


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route("/user/Igor%20Ramos/PT3019284/IFSP")
def user():
    return '<h1>Avaliação contínua: Aula 030</h1><h2>Aluno: Igor_Ramos</h2><h2>Prontuário: PT3019284</h2><h2>Instituição: IFSP</h2><p><a href="/">Voltar</a></p>'

@app.route("/contextorequisicao")
def context():
    user_agent = request.headers.get('User-Agent')
    url = request.remote_addr
    ip = request.host_url
    return '<h1>Avaliação contínua: Aula 030</h1><h2>Seu navegador é: {}</h2><h2>O IP do computador remoto é: {}</h2><h2>O host da aplicação é: {}</h2><p><a href="/">Voltar</a></p>'.format(user_agent, url, ip)