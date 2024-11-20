from operacoesDB import *

LISTA_CATEGORIAS = ('Reclamação', 'Sugestão', 'Elogio')

def exibirListaFormatada(manifestacoes):
    for item in range(len(manifestacoes)):
        print(
            '────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────')
        print(' ', str(manifestacoes[item][0]) + 'ª\n   •Autor:', manifestacoes[item][3], '\n   •Categoria:',
              manifestacoes[item][2], '\n   •Descrição:', manifestacoes[item][1])


def exibirCategoriasParaEscolha():
    print("Escolha uma categoria.")
    for item in range(len(LISTA_CATEGORIAS)):
        print('     ', str(item + 1), '-', LISTA_CATEGORIAS[item])
    categoriaEscolhida = input('» ')

    if categoriaEscolhida.isdigit():
        categoriaEscolhida = int(categoriaEscolhida)
        if categoriaEscolhida > 0 and categoriaEscolhida <= len(LISTA_CATEGORIAS):
            return categoriaEscolhida
        return -1
    else:
        print('O campo categoria só aceita numeros inteiros de 1 a ' + str(len(LISTA_CATEGORIAS)) + '.')
        return -1


def listarManifestacoes(conexao):
    manifestacoes = listarBancoDados(conexao, "SELECT * FROM manifestacoes;")
    if len(manifestacoes) > 0:
        exibirListaFormatada(manifestacoes)

    else:
        print("Nenhuma manifestação cadastrada!")


def cadastrarNovaManifestacoes(conexao):
    print('Digite os dados pedidos a seguir para cadastrar uma nova manifestação.')
    autor = input("Autor » ")

    categoriaEscolhida = exibirCategoriasParaEscolha()

    descricao = input("Descrição » ")

    if descricao == '' or autor == '' or categoriaEscolhida == '':
        print("Para cadastrar uma nova manifestação você deve preencher todos os campos.")

    else:
        if categoriaEscolhida != -1:
            sql = 'INSERT INTO manifestacoes (descricao, autor, categoria) VALUES (%s, %s, %s)'
            valores = [descricao, autor, LISTA_CATEGORIAS[categoriaEscolhida - 1]]
            insertNoBancoDados(conexao, sql, valores)
            print("Manifestação cadastrada com sucesso!.")

        else:
            print('Categoria inválida')


def quantidadeDeManifestacoes(conexao):
    quantidade = listarBancoDados(conexao, "SELECT COUNT(*) FROM manifestacoes;")[0][0]

    if quantidade != 0:
        print("Atualmente temos", str(quantidade), "manifestações cadastradas no sistema.")
    else:
        print("Nenhuma manifestação cadastrada.")


def buscarManifestacaoPeloCodigo(conexao):
    codigoDaManifestacao = input("Digite o codigo da manifestação que você deseja buscar. » ")

    if codigoDaManifestacao.isdigit():
        manifestacoes = listarBancoDados(conexao, "SELECT * FROM manifestacoes WHERE codigo = %s;",
                                         [codigoDaManifestacao])
        if codigoDaManifestacao != "":
            if len(manifestacoes) > 0:
                exibirListaFormatada(manifestacoes)
            else:
                print("Não existe nenhuma manifestação associada a esse código")
        else:
            print("Código da manifestação não pode ser um texto vazio, tente novamente.")
    else:
        print('O codigo da manifestação deve ser um número inteiro')


def buscarManifestacaoPelaCategoria(conexao):
    categoriaEscolhida = exibirCategoriasParaEscolha()

    if categoriaEscolhida != -1:
        manifestacoes = listarBancoDados(conexao, "SELECT * FROM manifestacoes WHERE categoria = %s;",
                                         [LISTA_CATEGORIAS[int(categoriaEscolhida) - 1]])
        if categoriaEscolhida != "":
            if len(manifestacoes) > 0:
                exibirListaFormatada(manifestacoes)

            else:
                print("Não existe nenhuma manifestações associadas a essa categoria")

        else:
            print("Código da categoria não pode ser um texto vazio, tente novamente.")

    else:
        print('Categoria inválida')


def excluirManifestacaoPeloCodigo(conexao):
    codigoDaManifestacao = input("Digite o codigo da manifestação que você deseja excluir. » ")

    if codigoDaManifestacao.isdigit():
        if codigoDaManifestacao != "":
            if excluirBancoDados(conexao, "DELETE FROM manifestacoes WHERE codigo = %s;", [codigoDaManifestacao]) > 0:
                print("Manifestação excluída com sucesso!")
            else:
                print("Não existe nenhuma manifestação associada a esse código")

        else:
            print("Código da manifestação não pode ser um texto vazio, tente novamente.")

    else:
        print('O codigo da manifestação deve ser um número inteiro')