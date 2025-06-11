from abc import ABC, abstractmethod

class Item (ABC):
    def __init__(self, id_Produto, valor_Unit, quantidade):
        self._id_Produto= id_Produto 
        self._valor_Unit = valor_Unit
        self._quantidade = quantidade

    def get_id_Produto(self):
        return self._id_Produto

    def set_id_Produto(self, id_Produto):
        self._id_Produto = id_Produto 
        
    def get_valor_Unit(self): 
        return self._valor_Unit

    def set_valor_Unit(self, valor_Unit):
        self._valor_Unit = valor_Unit
    
    def get_quantidade(self):
        return self._quantidade

    def set_quantidade(self, quantidade):
        self._quantidade = quantidade
    
