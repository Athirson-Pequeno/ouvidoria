from controleDB import *
from operacoesDB import *

conexao = criarConexao("localhost", "root", "36412", "ouvidoria")

nomeTabela = "manifestacao"
opcao = "1"
manifestacoes = []

#Cria um looping de repetição (usando while) que exibe o menu, esse menu aparece enquanto o usuario não esolhe a opção de sair (opção 7)
while opcao != "7":
    opcao = input("\nO que deseja fazer? \n"
                  "\n• 1) Listagem das manifestações."
                  "\n• 2) Criar uma nova manifestação."
                  "\n• 3) Exibir quantidade de manifestações."
                  "\n• 4) Pesquisar manifestações pela categoria."
                  "\n• 5) Pesquisar uma manifestação por código."
                  "\n• 6) Excluir uma manifestação pelo código."
                  "\n• 7) Sair do sistema.\n    » ")

    if opcao == "1":
        listarManifestacoes(conexao)

    elif opcao == "2":
        cadastrarNovaManifestacao(conexao)

    elif opcao == "3":
        quantidadeDeManifestacoes(conexao)

    elif opcao == "4":
        buscarManifestacaoPelaCategoria(conexao)

    elif opcao == "5":
        buscarManifestacaoPeloCodigo(conexao)

    elif opcao == "6":
        excluirManifestacaoPeloCodigo(conexao)

    elif opcao != "7":
        print("Opção inválida.")