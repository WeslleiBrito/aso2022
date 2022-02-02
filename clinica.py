from validate_docbr import CNPJ
from consulta_api_cep import BuscaEndereco
from valida_telefone import ValidaTelefone
from valida_email import ValidaEmail


class Clinica:

    def __init__(self, nome, cnpj, celular, cep=None, telefone=None, email=None):
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

        objeto_valida = ValidaTelefone(celular)
        verifica = objeto_valida.valida_telefone()

        if verifica[0]:
            self._celular = verifica[1]
        else:
            raise ValueError('Número inválido')

        if telefone:

            objeto_valida = ValidaTelefone(telefone)
            verifica = objeto_valida.valida_telefone()

            if verifica[0]:
                self._telefone = verifica[1]
            else:
                raise ValueError('Número inválido')

        if email:
            objeto_email = ValidaEmail(email)
            if objeto_email.email:
                self._email = email
            else:
                raise ValueError('Email inválido')

    def __str__(self):
        return f'CEP: {self.cep}, Celular: {self.celular}, Telefone: {self.telefone}, Email: {self.email}'

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

    @property
    def telefone(self):
        return self._telefone

    @property
    def email(self):
        return self._email


if __name__ == '__main__':
    clinica = Clinica('Teste', '29369431000101', '(75)982302834', '44092440', '7534821982', 'wesllei.wbs@gmail.com')
    print(clinica)
