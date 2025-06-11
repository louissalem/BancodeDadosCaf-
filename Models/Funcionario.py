from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, id_funcionario, nome, salario, telefone, cpf):
        self._id_funcionario = id_funcionario  
        self._nome = nome
        self._salario = salario
        self._telefone = telefone
        self.cpf = cpf  
    
    def get_id(self):
        return self._id_funcionario

    def set_id(self, id_funcionario):
        self._id_funcionario = id_funcionario
    
    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome
        
    def get_id_funcionario(self):
        return self._salario
    
    def set_codigo(self, salario):
        self._salario = salario
    
    def get_id_funcionario(self):
        return self._telefone
    
    def set_codigo(self, telefone):
        self._telefone = telefone
        
    @abstractmethod
    def calcularSalario(self):
        pass  