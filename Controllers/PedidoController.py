from Services import pedido_service

def criar_pedido():
    cliente_id = int(input("ID do cliente: "))
    pedido_service.criar_pedido(cliente_id)

def listar_pedidos():
    pedidos = pedido_service.listar_pedidos()
    for p in pedidos:
        print(p)

def cancelar_pedido():
    pedido_id = int(input("ID do pedido a cancelar: "))
    pedido_service.cancelar_pedido(pedido_id)
