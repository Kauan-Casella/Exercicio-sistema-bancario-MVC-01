#O main é o View
#Importando as classes e funções de outros arquivos para o View (main) ter acesso
from Controller import cadastrar_conta
from Model import BancoDados
from tkinter import messagebox
import tkinter as tk

#Criando um objeto do tipo BancoDados, esse objeto irá puxar tudo que esta na classe BancoDados, métodos e a lista vazia
meu_bd = BancoDados()


#Função que define o q acontecerá dps do usuário clicar no botão

def ao_clicar_no_botao():
    #Coleta os dados digitados pelo usuário

    n = entrada_nome.get()
    c = entrada_CPF.get()
    s = entrada_saldo.get()

    #Chama o Controller passando o objeto meu_bd, ele salva e nos devolve a conta pronta




    #Criando uma variável p armazenar o objeto nova_conta retornada pela função cadastrar_conta
    conta_criada = cadastrar_conta( meu_bd,n, c, s)

    if conta_criada:
        resumo = (f"CONTA CRIADA\n\n"
                  f"Nome: {conta_criada.titular.nome}\n"     #Precisamos usar o .titular pq ele faz a ponte entre a classe Cliente e Conta, usando ele nós acessamos os atributos da classe Cliente por meio da Conta.
                  f"CPF: {conta_criada.titular.CPF}\n"
                  f"Saldo: R${conta_criada.saldo}")

        messagebox.showinfo("Sucesso", resumo)

    else:
        messagebox.showinfo ("Erro", "Falha ao criar conta. Verifique os dados")


#Tk() é a classe principal do Tkinter. Qnd fazemos janela = tk.Tk() estamos criando um objeto (o molde da janela) e guardamos na variável janela
janela = tk.Tk()

janela.title("Formulário")
janela.geometry("400x300") #Largura e altura da janela


#O label cria o texto e exibe-o na tela
label_nome = tk.Label(janela, text="Digite seu nome:", font=("Arial", 12))
label_nome.grid(row=0, column=0, padx=10, pady=10) #O texto fica na linha 0 e coluna 0


#O Entry cria um campo de preenchimento pro usuário digitar
entrada_nome = tk.Entry(janela, font=("Arial",12))
entrada_nome.grid(row = 0, column = 1, padx = 10, pady = 10) #O campo de preenchimento fica na linha 0 e coluna 1, ou seja, ao lado do texto "Digite seu nome


label_CPF = tk.Label(janela, text="Digite seu CPF:", font=("Arial", 12))
label_CPF.grid(row=1, column=0, padx=10, pady=10)


entrada_CPF = tk.Entry(janela, font=("Arial",12))
entrada_CPF.grid(row = 1, column = 1, padx = 10, pady = 10)


label_saldo = tk.Label(janela, text = "Digite seu saldo:", font=("Arial",12))
label_saldo.grid(row=2, column=0, padx=10, pady=10)

entrada_saldo = tk.Entry(janela, font=("Arial",12))
entrada_saldo.grid(row=2, column = 1, padx = 10, pady = 10)


#Criando o botão

botao_criar  = tk.Button(janela, text="Criar conta", font=("Arial", 12), command = ao_clicar_no_botao)
botao_criar.grid(row=3, column=0, padx=10, pady=10)
janela.mainloop()



