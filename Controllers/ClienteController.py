from Services import cliente_service

def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    telefone = input("Telefone: ")
    cpf = input("CPF: ")

    cliente_service.inserir_cliente(nome, telefone, cpf)

def atualizar_cliente():
    id_cliente = int(input("ID do cliente: "))
    novo_telefone = input("Novo telefone: ")
    novo_nome = input("Novo nome: ")
    cliente_service.atualizar_dados_cliente(id_cliente, novo_telefone, novo_nome)

def listar_pedidos_cliente():
    id_cliente = int(input("ID do cliente: "))
    pedidos = cliente_service.buscar_pedidos_do_cliente(id_cliente)
    print(pedidos)

def verificar_cpf():
    cpf = input("CPF a verificar: ")
    existe = cliente_service.validar_cpf_duplicado(cpf)
    print("CPF já cadastrado?" , existe)
