import requests

class Filme:
    """Classe principal"""

    def __init__(self, nome):
        """Método construtor da classe"""
        self.nome = nome


    def replace_string(self):
        """Método para trocar os espaco pelo caracter +"""

        self.nome = self.nome.replace(' ', '+')
        return self.nome

    
    def realizar_request(self):
        """Método para fazer a requisição da api do site OMDBapi"""

        #chamada de método
        nome = self.replace_string()
        
        #chave de acesso da api
        api_chave = "chave da api"

        # url da requisição
        url = f'http://www.omdbapi.com/?t={nome}&apikey={api_chave}'

        # realizando a requisição e convertendo os dados em um json
        response = requests.get(url)
        dados = response.json()

        return dados