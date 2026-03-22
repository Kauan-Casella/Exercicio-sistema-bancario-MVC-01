#Camada responsável por pegar os dados que o usuário digitou na Entry (interface) da View e transformar em objetos do Model e manda de volta para a View Exibir


from Model import Cliente, Conta

def cadastrar_conta(banco_objeto, nome, CPF, saldo):    #O banco_objeto é um parâmetro que será preenchido com um objeto, o meu_bd, objeto da classe BancoDados, esse objeto carrega consigo a lista vazia criada e tudo que a classe BancoDados tiver para dentro dela.
    """Esse é o controller:
    Os parâmetros nome, CPF, etc... são os dados recebidos pela View
    Esses dados serão usados para preencher os parâmetros dos objetos
    """

    #Se o usuário não digitar nome ou CPF o programa não deve retornar nada

    if not nome or not CPF:
        return None



    #Criando os objetos(instanciando os models)

    #Criamos o objeto Cliente com os dados fornecidos pelo usuário (dados brutos)
    novo_cliente = Cliente(nome, CPF)

    #Criamos o objeto Conta, passando o objeto Cliente para o parâmetro titular, primeiro parâmetro do construtor da Classe Conta
    nova_conta = Conta(novo_cliente, saldo)


    #Quando eu criar o objeto meu_bd no main, chamar a função cadastrar_conta e passar meu_bd para preencher parâmetro banco_objeto, essa chamada abaixo será executada e adicionará  a conta na lista de contas
    banco_objeto.salvar_conta(nova_conta)

    #Retorna a conta
    return nova_conta














