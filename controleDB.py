from operacoesDB import *

LISTA_CATEGORIAS = ('Reclamação', 'Sugestão', 'Elogio')


# Printa os itens no terminal
def exibirListaFormatada(manifestacoes):
    # Realiza um for na lista e exibe cada item
    for item in range(len(manifestacoes)):
        print(
            '────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
        print(' -', str(manifestacoes[item][0]) +
              'ª\n   •Autor:', manifestacoes[item][3],
              '\n   •Categoria:', manifestacoes[item][2],
              '\n   •Descrição:', manifestacoes[item][1])


# Exibe a lista de categoria disponiveis para o usuário escolher
def exibirCategoriasParaEscolha():

    print("Escolha uma categoria.")

    #Exibe as categorias disponiveis
    for item in range(len(LISTA_CATEGORIAS)):
        print('     ', str(item + 1), '-', LISTA_CATEGORIAS[item])

    #Captura a escolha do usuário
    escolha = input('» ')

    #Verifica se a variavel contém um número inteiro
    if escolha.isdigit():
        #Converte a escolha para um número inteiro
        escolha = int(escolha)
        #Verifica se é uma escolha válida
        if escolha > 0 and escolha <= len(LISTA_CATEGORIAS):
            #Retorna a escolha
            return escolha

    return -1


# Lista as manifestações buscando a partir de um banco de dados
def listarManifestacoes(conexao):
    # Seleciona lista de manifestações e armazena em uma variavel
    manifestacoes = listarBancoDados(conexao, "SELECT * FROM manifestacoes;")

    # Verifica se a lista de manifestação contém algum item
    if len(manifestacoes) > 0:
        # Se tiver um item ou mais chama o método que exibe os dados para o usuario
        exibirListaFormatada(manifestacoes)

    else:
        # Se a lista está vazia exibe para o usuario que a lista está vazia
        print("Nenhuma manifestação cadastrada!")


# Cadastar nova manisfestação
def cadastrarNovaManifestacao(conexao):
    print('Digite os dados pedidos a seguir para cadastrar uma nova manifestação.')

    # Coleta o nome do autor e armazena na variavel autor
    autor = input("Autor » ")

    # Chama o método que exibe a lista de categorias disponiveis
    categoriaEscolhida = exibirCategoriasParaEscolha()

    # Coleta a descrição e armazena na variavel descrição
    descricao = input("Descrição » ")

    # Verifica se todos os campos estão preenchidos
    if descricao == '' or autor == '' or categoriaEscolhida == '':
        print("Para cadastrar uma nova manifestação você deve preencher todos os campos.")

    else:
        if categoriaEscolhida != -1:
            # Insere a manifestação no banco de dados
            sql = 'INSERT INTO manifestacoes (descricao, autor, categoria) VALUES (%s, %s, %s);'
            valores = [descricao, autor, LISTA_CATEGORIAS[categoriaEscolhida - 1]]
            insertNoBancoDados(conexao, sql, valores)
            print("Manifestação cadastrada com sucesso!.")

        else:
            print('Categoria inválida')


# Busca a quantidade de manifestações cadastradas
def quantidadeDeManifestacoes(conexao):
    quantidade = listarBancoDados(conexao, "SELECT COUNT(*) FROM manifestacoes;")[0][0]

    # Se tem uma ou mais manifestação cadastrada ele exibe para o usuário a quantidade
    if quantidade != 0:
        print("Atualmente temos", str(quantidade), "manifestações cadastradas no sistema.")
    # Senãi ele exibe que não tem nenhuma cadastrada
    else:
        print("Nenhuma manifestação cadastrada.")


# Retorna a manifestação pelo código dela
def buscarManifestacaoPeloCodigo(conexao):
    # Pergunta ao usuario o codigo da manifestação que ele deseja buscar
    codigoDaManifestacao = input("Digite o codigo da manifestação que você deseja buscar. » ")

    # Verifica se a variavel é um numero inteiro
    if codigoDaManifestacao.isdigit():
        manifestacoes = listarBancoDados(conexao, "SELECT * FROM manifestacoes WHERE codigo = %s;",
                                         [codigoDaManifestacao])

            # Se tiver uma manifestação ou mais cadastrada ele exibe para o usuário
        if len(manifestacoes) > 0:
            exibirListaFormatada(manifestacoes)

        else:
            print("Não existe nenhuma manifestação associada a esse código")

    else:
        print('O codigo da manifestação deve ser um número inteiro')


# Retorna a manifestação pelo categoria
def buscarManifestacaoPelaCategoria(conexao):
    # Busca a categoria
    categoriaEscolhida = exibirCategoriasParaEscolha()

    # Verifica se a categoria é válida
    if categoriaEscolhida != -1:
        manifestacoes = listarBancoDados(conexao, "SELECT * FROM manifestacoes WHERE categoria = %s;",
                                         [LISTA_CATEGORIAS[int(categoriaEscolhida) - 1]])

        if len(manifestacoes) > 0:
            exibirListaFormatada(manifestacoes)

        else:
            print("Não existe nenhuma manifestações associadas a essa categoria")

    else:
        print('Categoria inválida')


# Excluir a categoria pelo código
def excluirManifestacaoPeloCodigo(conexao):
    codigoDaManifestacao = input("Digite o codigo da manifestação que você deseja excluir. » ")

    # Verifica se a variavel é um numero inteiro
    if codigoDaManifestacao.isdigit():
        if codigoDaManifestacao != "":
            qtdLinhasAfetadas = excluirBancoDados(conexao, "DELETE FROM manifestacoes WHERE codigo = %s;",
                                                  [codigoDaManifestacao])
            # Se as linhas afetadas forem maior que 1 ele mostra ao usuario o sucesso
            if qtdLinhasAfetadas > 0:
                print("Manifestação excluída com sucesso!")
            else:
                print("Não existe nenhuma manifestação associada a esse código")
    else:
        print('O codigo da manifestação deve ser um número inteiro')
