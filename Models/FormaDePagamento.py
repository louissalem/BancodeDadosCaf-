from abc import ABC, abstractmethod

class FormaDePagamento (ABC):
    def __init__(self, id, cliente, pagamento, dinheiro, pix, cartão):
        self._id= id 
        self._cliente = cliente
        self._pagamento = pagamento
        self.dinheiro = dinheiro
        self.pix = pix
        self.cartão = cartão
        
    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id
        
    def get_cliente(self):
        return self._cliente 

    def set_cliente(self, cliente):
        self._cliente = cliente
    
    def get_pagamento(self):
        return self._pagamento

    def set_pagamento(self, pagamento):
        self._pagamento = pagamento
    
    def get_dinheiro(self):
        return self._dinheiro

    def set_dinheiro(self, dinheiro):
        self._dinheiro = dinheiro

    def get_pix(self):
        return self._pix

    def set_pix(self, pix):
        self._pix = pix
    
    def get_cartão(self):
        return self._cartão 

    def set_cartão(self, cartão):
        self._cartão = cartão
    