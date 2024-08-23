class ContaBancaria:
    def __init__(self, titular, senha):
        self.titular = titular  # Atributo público e obrigatório
        self.__saldo = 0        # Atributo privado inicializado com 0
        self.__senha = senha    # Atributo privado e obrigatório

    def consultar_saldo(self, senha):
        if self.validar_senha(senha):
            return f"Saldo atual: R$ {self.__saldo:.2f}"
        else:
            return "Senha incorreta."

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return f"Depósito de R$ {valor:.2f} realizado com sucesso."
        else:
            return "Valor de depósito inválido."

    def sacar(self, valor, senha):
        if self.validar_senha(senha):
            if valor > 0 and valor <= self.__saldo:
                self.__saldo -= valor
                return f"Saque de R$ {valor:.2f} realizado com sucesso."
            else:
                return "Valor de saque inválido ou saldo insuficiente."
        else:
            return "Senha incorreta."

    def alterar_senha(self, senha_atual, nova_senha):
        if self.validar_senha(senha_atual):
            self.__senha = nova_senha
            return "Senha alterada com sucesso."
        else:
            return "Senha atual incorreta."

    def validar_senha(self, senha):
        return senha == self.__senha
