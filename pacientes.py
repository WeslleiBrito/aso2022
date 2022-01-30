from consulta_api_cep import BuscaEndereco
from validate_docbr import CPF

class Pacientes:

    def __init__(self, nome, rg, cpf, cep=''):
        self._nome = nome
        self._RG = self.limpa_rg(rg)
        if cep != '':
            consulta_cep = BuscaEndereco(cep)
            self._cep = consulta_cep.cep
            self._logradouro = consulta_cep.logradouro
            self._bairro = consulta_cep.bairro
            self._localidade = consulta_cep.localidade
            self._uf = consulta_cep.uf
        else:
            self._cep = False

        if self.valida_cpf(cpf)[0]:
            self._cpf = self.valida_cpf(cpf)[1]
        else:
            raise ValueError('CPF inválido')

    def __str__(self):
        if self._cep:
            return f'{[self._cep, self._logradouro, self._bairro, self._localidade, self._uf]}'
        else:
            return ''

    @property
    def nome(self):
        return self._nome

    @property
    def RG(self):
        return self._RG

    @property
    def cpf(self):
        return f'{self._cpf}'

    @staticmethod
    def limpa_cpf(cpf):
        cpf_limpo = [digito for digito in cpf if digito.isdigit()]
        return ''.join(cpf_limpo)

    @staticmethod
    def limpa_rg(rg):
        rg_limpo = [digito for digito in rg if digito.isdigit()]
        return '.'.join(rg_limpo)

    def valida_cpf(self, cpf):
        objeto_cpf = CPF()
        return [objeto_cpf.validate(self.limpa_cpf(cpf)), self.limpa_cpf(cpf)]


if __name__ == '__main__':
    paciente = Pacientes('Wesllei', '13.638.538-99', '053.539.705-43', '44092492')

    print(paciente)
