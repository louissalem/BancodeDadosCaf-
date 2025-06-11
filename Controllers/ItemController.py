from Services import item_service

def inserir_item():
    pedido_id = int(input("ID do pedido: "))
    produto_id = int(input("ID do produto: "))
    quantidade = int(input("Quantidade: "))
    valor_unit = float(input("Valor unitário: "))

    item_service.inserir_item(pedido_id, produto_id, quantidade, valor_unit)

def listar_itens_pedido():
    pedido_id = int(input("ID do pedido: "))
    itens = item_service.listar_itens_pedido(pedido_id)
    for i in itens:
        print(i)
