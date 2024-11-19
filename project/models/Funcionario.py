from abc import ABC, abstractmethod
from project.models.Endereco import Endereco

class Funcionario(ABC):
    def __init__(self, nome:str, telefone:str, email:str, endereco:Endereco):
        self.nome = nome
        self.telefeone = telefone
        self.email = email
        self.endereco = endereco

    @abstractmethod
    def salario_sinal(self) -> float:
        pass

    def __str__(self) -> str:
        return (
            f"\nNome: {self.nome}"
            f"\nTelefone: {self.telefeone}"
            f"\nEmail: {self.email}"
            f"\nEndereço: {self.endereco}"
        )
    