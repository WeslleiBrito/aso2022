import requests
import json


class ConsultaCNPJ(object):

    def __init__(self, CNPJ, lista_consulta):
        self._cnpj = CNPJ
        self._lista_consulta = lista_consulta

    def __str__(self):
        return f'{self.recebe_dados_cadastro()}'

    def recebe_dados_cadastro(self):

        url = f'https://receitaws.com.br/v1/cnpj/{self._cnpj}'
        querystring = {"token": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX", "cnpj": "06990590000123", "plugin": "RF"}
        resposta = requests.request('GET', url, params=querystring)

        resposta = json.loads(resposta.text)

        return [resposta[chave] for chave in self._lista_consulta]


if __name__ == '__main__':
    informacoes = ['nome', 'fantasia', 'cnpj', 'cep', 'uf', 'municipio', 'bairro', 'logradouro', 'numero']

    consultor = ConsultaCNPJ('01815806000109', informacoes)

    print(consultor)
