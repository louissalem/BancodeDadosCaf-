def verificar_venda(id_cliente, data_venda, valor_total, id_forma_pagamento):
    if not isinstance(id_cliente, int) or id_cliente <= 0:
        return False, "❌ ID do cliente inválido."

    if not isinstance(data_venda, str) or len(data_venda.strip()) == 0:
        return False, "❌ Data da venda não pode estar vazia."

    try:
        float(valor_total)
    except ValueError:
        return False, "❌ Valor total deve ser um número."

    if not isinstance(id_forma_pagamento, int) or id_forma_pagamento <= 0:
        return False, "❌ ID da forma de pagamento inválido."

    return True, "✅ Dados da venda estão corretos."

def verificar_produto(descricao, val_unitario, id_fornecedores):
    if not isinstance(descricao, str) or len(descricao.strip()) == 0:
        return False, "❌ Descrição do produto inválida."

    try:
        float(val_unitario)
    except ValueError:
        return False, "❌ Valor unitário deve ser um número."

    if not isinstance(id_fornecedores, int) or id_fornecedores <= 0:
        return False, "❌ ID do fornecedor inválido."

    return True, "✅ Dados do produto estão corretos."

def verificar_cliente(nome, telefone):
    if not isinstance(nome, str) or len(nome.strip()) == 0:
        return False, "❌ Nome do cliente não pode estar vazio."

    if not isinstance(telefone, str) or len(telefone.strip()) < 8:
        return False, "❌ Telefone inválido."

    return True, "✅ Dados do cliente estão corretos."

# Exemplo de uso
if __name__ == "__main__":
    valido, msg = verificar_venda(1, "2025-05-28 14:30", 250.0, 2)
    print(msg)
