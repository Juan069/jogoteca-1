from flask import Flask, render_template

app = Flask(__name__)

lista = ['God of War', 'LoL', 'Batman']

@app.route('/inicio')
def ola():
    return render_template('lista.html',titulo='Meus Jogos', jogos=lista)

app.run()