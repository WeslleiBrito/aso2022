from validate_docbr import CNPJ
from validadores.valida_telefone import ValidaTelefone
from validadores.valida_email import ValidaEmail
from api_externas.captura_dados_empresa_por_cnpj import ConsultaCNPJ


class Clinica(object):

    def __init__(self, cnpj, celular=None, telefone=None, email=None):

        if CNPJ().validate(str(cnpj)):

            informacoes = ['nome', 'fantasia', 'cnpj', 'cep', 'uf', 'municipio', 'bairro', 'logradouro', 'numero']
            consultor = ConsultaCNPJ(cnpj, informacoes).recebe_dados_cadastro()
            self._nome = consultor[0]
            self._fantasia = consultor[1]
            self._cnpj = consultor[2]
            self._cep = consultor[3]
            self._uf = consultor[4]
            self._localidade = consultor[5]
            self._bairro = consultor[6]
            self._logradouro = consultor[7]
            self._numero = consultor[8]
        else:
            raise ValueError('CNPJ inválido')

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
        else:
            self._telefone = telefone

        if email:
            objeto_email = ValidaEmail(email)
            if objeto_email.email:
                self._email = email
            else:
                raise ValueError('Email inválido')
        else:
            self._email = email

    def __str__(self):

        return f'Nome: {self.nome}, CEP: {self.cep}, Celular: {self.celular}, Telefone: {self.telefone}, Email: {self.email}'

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
    clinica = Clinica('29369431000101', '75982302834')
    print(clinica)
