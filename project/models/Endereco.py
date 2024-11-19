class Endereco():
    def __init__(self, lougradouro:str, numero:str, complemento:str, cep:str, cidade:str) -> None:
        self.lougradouro = lougradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def __str__(self) -> str:
        return (
            f"\nEndereço: "
            f"\nLougradouro: {self.lougradouro}"
            f"\nNúmero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCep: {self.cep}"
            f"\nCidade: {self.cidade}"
        )
