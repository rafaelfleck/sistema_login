from bottle import route, run, Bottle, request, template, get, static_file, error
import os


#static routes
@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')

@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='static/img')

@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static/fonts')

#Inicio da pagina - sera redirecionado para pagina login.html
@route('/')
def login():
    return template('login')

#validação da pagina - sera validado usuario e senha no formulario
def check_login(username, password):
    d = {'Rafael':'teste123', 'aline':'felix123'}

    if d[username] == password:
        return True
    return False

#Ação do fromulario - sera redirecionado para pagina validacao_login.html
@route('/', method='POST')
def acao_login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    return template('verificacao_login', sucesso = check_login(username, password), nome = username)

#Validação da pagina para erro 404
@error(404)
def error404(error):
    return template('page404')


if __name__ == '__main__':
    if os.environ.get('APP_LOCATION') == 'heroku':
        run(host='0.0.0.0', port=int(os.environ.get('PORT',5000)))
    else:
        run(host='localhost', port=8081, debug=True, reloader=True)
