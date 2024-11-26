# PROGRAMAR EM LINGUAGEM ESTRUTURADA - NOITE
#
# EQUIPE
#     Antenor de Queiroz Brito Neto
#     Athirson Souza Pequeno
#     Camilla Souza da Silva
#     Fabiano Lucio da Silva Brito
#     Kaique Bezerra de Oliveira
#     Lessandro Costa de Freitas
#     Millena Nunes Dantas
#     Pedro Jorge Marques Pereira


#Modelo da tabela usada

# CREATE TABLE `manifestacoes` (
#   `codigo` int NOT NULL AUTO_INCREMENT,
#   `descricao` varchar(200) DEFAULT NULL,
#   `categoria` varchar(45) DEFAULT NULL,
#   `autor` varchar(45) DEFAULT NULL,
#   PRIMARY KEY (`codigo`)
# )

from controleBD import *
from operacoesBD import *

conexao = criarConexao('localhost', 'root', '36412', 'ouvidoria')

opcao = '1'

while opcao != '7':
    opcao = input('\nO que deseja fazer? \n'
                  '\n• 1) Listagem das manifestações.'
                  '\n• 2) Criar uma nova manifestação.'
                  '\n• 3) Exibir quantidade de manifestações.'
                  '\n• 4) Pesquisar manifestações pela categoria.'
                  '\n• 5) Pesquisar uma manifestação por código.'
                  '\n• 6) Excluir uma manifestação pelo código.'
                  '\n• 7) Sair do sistema.\n    » ')

    if opcao == '1':
        listarManifestacoes(conexao)

    elif opcao == '2':
        cadastrarNovaManifestacao(conexao)

    elif opcao == '3':
        quantidadeDeManifestacoes(conexao)

    elif opcao == '4':
        buscarManifestacaoPelaCategoria(conexao)

    elif opcao == '5':
        buscarManifestacaoPeloCodigo(conexao)

    elif opcao == '6':
        excluirManifestacaoPeloCodigo(conexao)

    elif opcao != '7':
        print('Opção inválida.')