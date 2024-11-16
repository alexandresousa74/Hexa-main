import os, datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))

app = Flask('__name__')
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config['SECRET_KEY'] = 'V$3423faghYtGs'

db = SQLAlchemy(app)

class Clientes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    empresa = db.Column(db.String(80), nullable=False)
    contato = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    telefone = db.Column(db.String(10), nullable=False)
    cidade = db.Column(db.String(80), nullable=False)
    segmento = db.Column(db.String(80), nullable=False)

class Projetos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(80), nullable=False)
    servicos = db.Column(db.String(80), nullable=False)
    valor = db.Column(db.String(10), nullable=False)
    inicio = db.Column(db.String(10), nullable=False)
    fim = db.Column(db.String(10), nullable=False)

class Servicos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(80), nullable=False)
    valor = db.Column(db.String(10), nullable=False)
    segmento = db.Column(db.String(80), nullable=False)

@app.route('/')
def index():
    projetos = Projetos.query.all()
    return render_template('index.html', projetos = projetos)

@app.route('/clientes')
def clientes():
    clientes = Clientes.query.all()
    return render_template('clientes.html', clientes = clientes)

@app.route('/servicos')
def servicos():
    servicos = Servicos.query.all()
    return render_template('servicos.html', servicos = servicos)

def get_cliente(cliente_id):
    cliente = Clientes.query.filter_by(id=cliente_id).first()
    if cliente is None:
        abort(404)
    return cliente

def get_projeto(projeto_id):
    projeto = Projetos.query.filter_by(id=projeto_id).first()
    if projeto is None:
        abort(404)
    return projeto

def get_servico(servico_id):
    servico = Servicos.query.filter_by(id=servico_id).first()
    if servico is None:
        abort(404)
    return servico

@app.route('/projetos/<int:projeto_id>')
def projeto(projeto_id):
    projeto = get_projeto(projeto_id)
    return render_template('projeto.html', projeto = projeto)

@app.route('/clientes/<int:cliente_id>')
def cliente(cliente_id):
    cliente = get_cliente(cliente_id)
    return render_template('cliente.html', cliente = cliente)

@app.route('/servicos/<int:servico_id>')
def servico(servico_id):
    servico = get_servico(servico_id)
    return render_template('servico.html', servico = servico)

@app.route('/novo_cliente', methods=('GET', 'POST'))
def novo_cliente():
    if request.method == 'POST':
        empresa = request.form['empresa']
        contato = request.form['contato']
        email = request.form['email']
        telefone = request.form['telefone']
        cidade = request.form['cidade']
        segmento = request.form['segmento']

        if not empresa:
            flash('Digite o nome da empresa!')
        else:
            cliente = Clientes(empresa=empresa, contato=contato, email=email, telefone=telefone, cidade=cidade, segmento=segmento)
            db.session.add(cliente)
            db.session.commit()
            return redirect(url_for('clientes'))
    return render_template('novo_cliente.html')

@app.route('/novo_projeto', methods=('GET', 'POST'))
def novo_projeto():
    if request.method == 'POST':
        cliente = request.form['cliente']
        servicos = request.form['servicos']
        valor = request.form['valor']
        inicio = request.form['inicio']
        fim = request.form['fim']

        if not cliente or not servicos:
            flash('Digite o nome do cliente e do serviço!')
        else:
            projeto = Projetos(cliente=cliente, servicos=servicos, valor=valor, inicio=inicio, fim=fim)
            db.session.add(projeto)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('novo_projeto.html')

@app.route('/novo_servico', methods=('GET', 'POST'))
def novo_servico():
    if request.method == 'POST':
        descricao = request.form['descricao']
        valor = request.form['valor']
        segmento = request.form['segmento']

        if not descricao:
            flash('Digite a descrição do serviço!')
        else:
            servico = Servicos(descricao=descricao,valor=valor, segmento=segmento)
            db.session.add(servico)
            db.session.commit()
            return redirect(url_for('servicos'))
    return render_template('novo_servico.html')

@app.route('/clientes/<int:cliente_id>/edit', methods=('GET', 'POST'))
def edit_cliente(cliente_id):
    cliente = get_cliente(cliente_id)

    if request.method == 'POST':
        empresa = request.form['empresa']
        contato = request.form['contato']
        email = request.form['email']
        telefone = request.form['telefone']
        cidade = request.form['cidade']
        segmento = request.form['segmento']

        if not empresa:
            flash('Digite o nome da empresa!')
        else:
            cliente.empresa = empresa
            cliente.contato = contato
            cliente.email = email
            cliente.telefone = telefone
            cliente.cidade = cidade
            cliente.segmento = segmento
            db.session.commit()
            return redirect(url_for('clientes'))

    return render_template('edit_cliente.html', cliente=cliente)

@app.route('/clientes/<int:cliente_id>/delete', methods=('POST',))
def delete_cliente(cliente_id):
    cliente = get_cliente(cliente_id)
    db.session.delete(cliente)
    db.session.commit()
    flash('"{}" foi apagado com sucesso!'.format(cliente.empresa))
    return redirect(url_for('clientes'))

@app.route('/projetos/<int:projeto_id>/edit', methods=('GET', 'POST'))
def edit_projeto(projeto_id):
    projeto = get_projeto(projeto_id)

    if request.method == 'POST':
        cliente = request.form['cliente']
        servicos = request.form['servicos']
        valor = request.form['valor']
        inicio = request.form['inicio']
        fim = request.form['fim']

        if not cliente or not servicos:
            flash('Digite o nome do cliente e do serviço!')
        else:
            projeto.cliente=cliente
            projeto.servicos=servicos
            projeto.valor=valor
            projeto.inicio=inicio
            projeto.fim=fim
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('edit_projeto.html', projeto=projeto)

@app.route('/<int:projeto_id>/delete', methods=('POST',))
def delete_projeto(projeto_id):
    projeto = get_projeto(projeto_id)
    db.session.delete(projeto)
    db.session.commit()
    flash('"{}" foi apagado com sucesso!'.format(projeto.cliente))
    return redirect(url_for('index'))

@app.route('/servicos/<int:servico_id>/edit', methods=('GET', 'POST'))
def edit_servico(servico_id):
    servico = get_servico(servico_id)

    if request.method == 'POST':
        descricao = request.form['descricao']
        valor = request.form['valor']
        segmento = request.form['segmento']

        if not descricao:
            flash('Digite a descrição do serviço!')
        else:
            servico.descricao = descricao
            servico.valor = valor
            servico.segmento = segmento
            db.session.commit()
            return redirect(url_for('servicos'))

    return render_template('edit_servico.html', servico=servico)

@app.route('/servicos/<int:servico_id>/delete', methods=('POST',))
def delete_servico(servico_id):
    servico = get_servico(servico_id)
    db.session.delete(servico)
    db.session.commit()
    flash('"{}" foi apagado com sucesso!'.format(servico.descricao))
    return redirect(url_for('servicos'))