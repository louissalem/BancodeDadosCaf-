from abc import ABC, abstractmethod

class Fornecedor (ABC):
    def __init__(self, id_Produto, id_Pessoa, Cnpj):
        self._id_Produto = id_Produto
        self._idPessoa = id_Pessoa
        self.Cnpj = Cnpj
        
    def get_id_Produto(self):
        return self._id_Produto

    def set_id_Produto(self, id_Produto):
        self._id_Produto = id_Produto
        
    def get_id_Pessoa(self):
        return self._idPessoa

    def set_id_Pessoa(self, id_Pessoa):
        self._id_Pessoa = id_Pessoa
    
    def get_Cnpj(self):
        return self._Cnpj

    def set_Cnpj(self, Cnpj):
        self._Cnpj = Cnpj