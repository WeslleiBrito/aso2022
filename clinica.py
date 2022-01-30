from validatorPCTE import validatorPCTE as vt
from validate_docbr import CNPJ
from consulta_api_cep import BuscaEndereco

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

    def __str__(self):
        return self.cep

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


if __name__ == '__main__':
    clinica = Clinica('Teste', '29369431000101', cep='44092440')
    print(clinica)




