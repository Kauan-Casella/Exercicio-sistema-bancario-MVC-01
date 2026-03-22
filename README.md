# Sistema Bancário Simples (Arquitetura MVC)

Este projeto é um exercício de desenvolvimento em Python utilizando a biblioteca Tkinter para a interface gráfica e seguindo o padrão de arquitetura **MVC (Model-View-Controller)**.

#Funcionalidades
* Interface gráfica amigável para cadastro de contas.
* Campos para Nome, CPF e Saldo Inicial.
* Validação e exibição de dados via MessageBox.

#Estrutura do Projeto
O projeto foi dividido para garantir a separação de responsabilidades:

Model.py: Contém a classe `Conta`, responsável por estruturar os dados do usuário.
View.py: Gerencia toda a interface gráfica (janela, campos de entrada e botões) usando Tkinter.
Controller.py: Faz a ponte entre a View e o Model, processando as informações e instanciando os objetos.

#Tecnologias Utilizadas:
Python 3.x
Tkinter (GUI)
