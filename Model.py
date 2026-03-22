class Cliente:
    def __init__(self, nome, CPF):
        self.nome = nome
        self.CPF = CPF


class Conta:
    def __init__(self,titular, saldo):
        self.saldo = saldo
        self.titular = titular




class BancoDados:
    def __init__(self):
        self.lista_contas = []


    #Criando um método

    def salvar_conta (self, nova_conta):

        self.lista_contas.append(nova_conta)











