import requests


class BuscaEndereco:

    def __init__(self, cep):
        if self._consulta_cep(cep):
            self._cep = self._consulta_cep(cep)
        else:
            raise ValueError('CEP não localizado.')

    def cep_e_valido(self, cep):

        if len(self._limpa_cep(cep)) == 8:
            return [True, self._limpa_cep(cep)]
        else:
            return False

    def __str__(self):
        return f'CEP: {self.cep}, Rua: {self.logradouro}, Bairro: {self.bairro}, Cidade: {self.localidade}, ' \
               f'Estado: {self.uf}'

    @staticmethod
    def _limpa_cep(cep):
        cep_limpo = []
        for digito in cep:
            if digito in '0123456789':
                cep_limpo.append(digito)
        cep_limpo = ''.join(cep_limpo)
        return cep_limpo

    @property
    def cep(self):
        return self._cep[0]

    @property
    def logradouro(self):
        return self._cep[1]

    @property
    def bairro(self):
        return self._cep[2]

    @property
    def localidade(self):
        return self._cep[3]

    @property
    def uf(self):
        return self._cep[4]

    def _consulta_cep(self, cep):
        cep = self._limpa_cep(cep)
        if len(cep) == 8:
            url = f'https://viacep.com.br/ws/{cep}/json/'
            r = requests.get(url)

            if len(r.json()) == 1:
                return False
            else:
                return [r.json()['cep'], r.json()['logradouro'], r.json()['bairro'], r.json()['localidade'],
                        r.json()['uf']]
        else:
            raise ValueError('CEP inválido')


if __name__ == '__main__':
    endereco = BuscaEndereco('44092440')
    print(endereco)
