from abc import ABC, abstractmethod

class Cliente (ABC):
    def __init__(self,  id_cliente, nome, telefone, cpf):
        self._id_cliente=  id_cliente 
        self._nome = nome
        self._telefone = telefone
        self.cpf = cpf
        
    def get_id(self):
        return self._id_cliente

    def set_id(self,  id_cliente):
        self._id_cliente =  id_cliente
        
    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome
    
    def get_telefone(self):
        return self._telefone

    def set_telefone(self, telefone):
        self._telefone = telefone