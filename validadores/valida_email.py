import re

class ValidaEmail:
    def __init__(self, email):
        self._email = self.valida(email)

    @property
    def email(self):
        return self._email

    @staticmethod
    def valida(email):
        padrao = '[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
        resultado = re.search(padrao, email)

        if resultado is not None:
            return True
        return False


if __name__ == '__main__':
    email = 'wesllei.wbs@gmail.com'
    validador = ValidaEmail(email)

    if validador.email:
        print('Email valido')
    else:
        print('Email invalido')
