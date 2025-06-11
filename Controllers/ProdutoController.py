from Services import produto_service

def cadastrar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    fornecedor = input("Fornecedor: ")

    produto_service.inserir_produto(nome, preco, fornecedor)

def listar_produtos():
    produtos = produto_service.listar_produtos()
    for p in produtos:
        print(p)
