from validate_docbr import CNPJ
from consulta_api_cep import BuscaEndereco
import re


class Clinica:

    def __init__(self, nome, cnpj, celular, cep=None, telefone1=None, email=None):
        self._nome = nome
        if CNPJ().validate(str(cnpj)):
            self._cnpj = CNPJ.mask(cnpj)
        else:
            raise ValueError('CNPJ inválido')

        if cep and BuscaEndereco(cep):
            busca = BuscaEndereco(cep)
            self._cep = busca.cep
            self._logradouro = busca.logradouro
            self._bairro = busca.bairro
            self._localidade = busca.localidade
            self._uf = busca.uf

        if self.valida_telefone(celular)[0]:
            self._celular = self.valida_telefone(celular)[1]
        else:
            raise ValueError('Número inválido')

    def __str__(self):
        return f'CEP: {self.cep}, Celular: {self.celular}'

    def valida_telefone(self, numero):
        numero = self.limpa_numero(numero)
        padrao = "([1-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        verifica = re.search(padrao, numero)

        if verifica:
            return [True, self.mask_celular(numero)]
        else:
            return [False]

    def mask_celular(self, numero):
        if len(numero) == 11:
            return f'({numero[:2]}){numero[2:7]}-{numero[7:]}'
        else:
            return f'({numero[:2]}){numero[2:6]}-{numero[6:]}'

    def limpa_numero(self, numero):
        numero_limpo = [digito for digito in numero if digito.isdigit()]
        return ''.join(numero_limpo)

    @property
    def nome(self):
        return self._nome

    @property
    def cnpj(self):
        return self._cnpj

    @property
    def cep(self):
        return self._cep

    @property
    def logradouro(self):
        return self._logradouro

    @property
    def bairro(self):
        return self._bairro

    @property
    def localidade(self):
        return self._localidade

    @property
    def uf(self):
        return self._uf

    @property
    def celular(self):
        return self._celular


if __name__ == '__main__':
    clinica = Clinica('Teste', '29369431000101', cep='44092440', celular='(75)982302834')
    print(clinica)
