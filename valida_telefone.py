import re


def limpa_numero(numero):
    numero_limpo = [digito for digito in numero if digito.isdigit()]
    return ''.join(numero_limpo)


class ValidaTelefone:

    def __init__(self, numero):
        self._numero = limpa_numero(numero)

    @property
    def numero(self):
        return self._numero

    def valida_telefone(self):
        padrao = "([1-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        verifica = re.search(padrao, self.numero)

        if verifica:
            return [True, self.mask_celular()]
        else:
            return [False]

    def mask_celular(self):
        if len(self.numero) == 11:
            return f'({self.numero[:2]}){self.numero[2:7]}-{self.numero[7:]}'
        else:
            return f'({self.numero[:2]}){self.numero[2:6]}-{self.numero[6:]}'


