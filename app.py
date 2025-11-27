from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html')

@app.route('/iphone')
def iphone():
    return render_template('iphone.html')

@app.route('/ipad')
def ipad():
    return render_template('ipad.html')

@app.route('/macbook')
def macbook():
    return render_template('macbook.html')

@app.route('/acessorios')
def acessorios():
    return render_template('acessorios.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')
@app.route('/tire_suas_duvidas')
def tire_suas_duvidas():
    return render_template('tire_suas_duvidas.html')
app.run()