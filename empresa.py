from validate_docbr import CNPJ

class Empresa:

    def __init__(self, cnpj, nome):
        self._nome = nome
        if self.cnpj_e_valido(cnpj):
            self._cnpj = cnpj
        else:
            raise ValueError('CNPJ inválido')

    def __str__(self):
        return f'Nome: {self.nome}\nCNPJ: {self.cnpj}'

    @property
    def cnpj(self):
        return self._cnpj

    @property
    def nome(self):
        return self._nome

    @staticmethod
    def cnpj_e_valido(cnpj):
        objeto_cnpj = CNPJ()
        return objeto_cnpj.validate(cnpj)


if __name__ == '__main__':
    cnpj = '29.369.431/0001-01'
    nome = 'Nova Burite'

    empresa = Empresa(cnpj, nome)

    print(empresa)
