# libs que iremos utilizar neste projeto
from flask import Flask, render_template, request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estudantes.db' # conexao com o banco de dados
app.config['SECRET_KEY'] = "random string" # para criptografar as sessões


# desde que você tem as classes relaciandas ao banco, o ORM faz o processo de criar, recuperar e converter
db = SQLAlchemy(app)
class Estudantes(db.Model):
    # definição dos tipos de dados do banco
    id = db.Column('student_id', db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    cidade = db.Column(db.String(50))
    email = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    # objeto
    def __init__(self, nome, cidade, email, pin):
        self.nome = nome
        self.cidade = cidade
        self.email = email
        self.pin = pin


# lista todos os estudantes
@app.route('/')
def show_all():
    # renderiza os dados em tela
    return render_template('show_all.html', estudantes = Estudantes.query.all())

# adiciona novo estudante
# GET para quando você errar o preenchimento e precisa informar ao usuário
# POST para recuperar e salvar os dados
@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        # verifica os dados que foram preenchidos
        if not request.form['nome'] or not request.form['cidade'] or not request.form['email'] or not request.form['pin']:
            # caso algum deles não for preenchido, avisa ao usuário
            flash('Preencha todo os campos', 'Erro')
            return render_template('new.html')  # renderiza os dados em tela

        # Recupera os dados preenchidos e coloca em um objeto
        estudante = Estudantes(request.form['nome'], request.form['cidade'], request.form['email'], request.form['pin'])
        db.session.add(estudante) # salva no banco
        db.session.commit() # commit da transação
        flash('Registro salvo com sucesso') # coloca uma mensagem para a próxima página
        return redirect(url_for('show_all')) # redireciona para a próxima página

# atualiza um estudante
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    estudante = Estudantes.query.get(id)  # recupera o estudando pelo Id

    # verifica os dados que foram preenchidos
    if request.method == 'POST':
        if not request.form['nome'] or not request.form['cidade'] or not request.form['email'] or not request.form['pin']:
            # caso algum deles não for preenchido, avisa ao usuário
            flash('Preencha todo os campos', 'Erro')
        else:
            # atualiza o objeto os dados do objeto
            estudante.nome = request.form['nome']
            estudante.cidade = request.form['cidade']
            estudante.email = request.form['email']
            estudante.pin = request.form['pin']
            db.session.commit() # commit das atualizações
            flash('Registro salvo com sucesso')  # coloca uma mensagem para a próxima página
            return redirect(url_for('show_all')) # redireciona para a página que exibe os estudantes
    return render_template('update.html', estudante=estudante) # renderiza os dados em tela com os dados originais


# deleta um estudante
@app.route('/delete/<int:id>')
def delete(id):
    estudante = Estudantes.query.get(id) # recupera o estudando pelo Id
    db.session.delete(estudante) # deleta o estudante
    db.session.commit() # commit da operação
    flash('Estudate: ' + str(id) + ' foi deletado') # retorna a mensagem de sucesso ao deletar para a próxima página
    return redirect(url_for('show_all')) # redireciona para a página que exibe os estudantes


if __name__ == '__main__':
    app.app_context().push() # recupera o contexto da aplicação que está usando o banco
    db.create_all() # cria todas as instâncias da database se não existirem
    app.run(host="0.0.0.0", port="5000", debug=True)