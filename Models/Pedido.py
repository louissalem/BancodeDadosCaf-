from abc import ABC, abstractmethod

class Pedido (ABC):
    def __init__(self, val_Total, id, id_Item, DataHora_Pedido, id_FormaPagamento, mesa):
        self._val_Total= val_Total
        self._id = id
        self._id_Item = id_Item
        self._id_FormaPagamento = id_FormaPagamento
        self._DataHora_Pedido = DataHora_Pedido
        self._mesa = mesa
        
        
    def get_val_Total(self):
        return self._val_Total

    def set_val_Total(self, val_Total):
        self._val_Total = val_Total
        
    def get_id(self): 
        return self._id

    def set_id(self, id):
        self._id = id
    
    def get_id_Item(self):
        return self._id_Item

    def set_id_Item(self, id_Item):
        self._id_Item = id_Item
    
    def get_DataHora_Pedido(self):
        return self._DataHora_Pedido

    def set_DataHora_Pedido(self, DataHora_Pedido):
        self._DataHora_Pedido = DataHora_Pedido 
        
    def get_id_FormaPagamento(self):
        return self._id_FormaPagamento
    
    def set_id_FormaPagamento(self, id_FormaPagamento):
        self._id_FormaPagamento = id_FormaPagamento
    
    def get_id_mesa(self):
        return self._mesa
    
    def set_id_mesa (self, id_mesa):
        self._id_mesa = id_mesa