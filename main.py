import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# construir funcionalidades
@app.route('/')
def homepage():
  return 'Funcionando'

# Segundo endpoint
@app.route('/endpoint2')
def pegarvendas():
  tabela = pd.read_csv('table.csv')
  total_vendas = tabela['Vendas'].sum()
  resposta = {'total_vendas': total_vendas}
  return jsonify(resposta)


# roda a API
app.run(host='0.0.0.0')

