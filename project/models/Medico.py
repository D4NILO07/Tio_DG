from project.models.Endereco import Endereco
from project.models.Funcionario import Funcionario

class Medico(Funcionario):
    def __init__(self, nome, telefone, email, endereco, crm):
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm 

    def salario_final(self) -> float:
        return 5000.00
    
    def __str__(self):
        return (f"{super().__str__()}"
                f"\nCRM: {self.crm}"
                f"\nSalário final: {self.salario_final():2f}"
                )