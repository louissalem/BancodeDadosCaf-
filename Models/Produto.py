from abc import ABC, abstractmethod

class Venda(ABC):
    def __init__(self, id, id_cliente, data_venda, valor_total, id_forma_pagamento):
        self._id = id
        self._id_cliente = id_cliente
        self._data_venda = data_venda
        self._valor_total = valor_total
        self._id_forma_pagamento = id_forma_pagamento

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_id_cliente(self):
        return self._id_cliente

    def set_id_cliente(self, id_cliente):
        self._id_cliente = id_cliente

    def get_data_venda(self):
        return self._data_venda

    def set_data_venda(self, data_venda):
        self._data_venda = data_venda

    def get_valor_total(self):
        return self._valor_total

    def set_valor_total(self, valor_total):
        self._valor_total = valor_total

    def get_id_forma_pagamento(self):
        return self._id_forma_pagamento

    def set_id_forma_pagamento(self, id_forma_pagamento):
        self._id_forma_pagamento = id_forma_pagamento
