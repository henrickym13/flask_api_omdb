from django.shortcuts import redirect
from flask.globals import request
from flask import Flask, render_template, url_for
from models.filme import Filme


app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    """Função que exibi a pagina inicial"""

    return render_template("index.html")


@app.route("/buscar", methods=['GET', 'POST'])
def exibir_informacoes():
    """Função para exibir as informaçoes da api na tela"""

    # chamando a classe filme
    filme = Filme(request.form["nome"])

    # iniciando variaveis
    nome = filme.realizar_request()
    classficacao = nome['Rated']
    metascore = nome['Ratings'][2]['Value']

    return render_template("index.html", 
        nome = nome['Title'], ano = nome['Year'], 
        classificacao = classficacao[3:], duracao = nome['Runtime'],
        imdb_nota = nome['Ratings'][0]['Value'],
        rotten = nome['Ratings'][1]['Value'],
        metascore = metascore[0:2],
        poster = nome['Poster'],
        sinopse = nome['Plot'],
        genero = nome['Genre'],
        diretor = nome['Director'],
        roteristas = nome['Writer'],
        artistas = nome['Actors'],
        indicacoes = nome['Awards']
    )

    
@app.errorhandler(KeyError)
def exibir_erro(erro):
    """Função para retornar mensagem de erro"""

    return render_template("erro.html")


@app.errorhandler(IndexError)
def exibir_erro(erro):
    """Função para retornar mensagem de erro"""

    return render_template("erro.html")


if __name__ == "__main__":
    app.run(debug=True)