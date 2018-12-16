from bottle import route, run, Bottle, request, template

@route('/')
@route('/user/<nome>')
def index(nome='Desconhecido'):
    return '<center><h1>Ola '+ nome +'</h1></center>'

@route('/artigo/<id>')
def artigo(id):
    return '<center><h1>Você esta lendo o artigo '+ id +'</h1></center>'


@route('/pagina/<id>/<nome>')
def pagina(id, nome):
    return '<h1>Você está vendo a página'+ id+' com nome '+nome+'</h1>'
     return '''
        <form action="/login" method="post">
            username: <input name="username" type="text" />
            password: <input name="password" type="password" />
            <input values="login" type="submit" />
        </form>
        '''
