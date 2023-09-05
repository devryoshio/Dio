 
from Banco import Banco

class Conta:

    def __init__(self):
        self.usuarios = []

    def criar_usuario(self):
        cpf = input("Informe o CPF (somente número): ")
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        self.usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco, "banco": Banco()})
        print("=== Usuário criado com sucesso! ===")

    def deposito(self):
        money = float(input("O valor do deposito:"))

        dicionario = self.usuarios[0]
        obj = dicionario["banco"]
        obj.deposito(money)
