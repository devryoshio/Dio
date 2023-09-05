 
from datetime import datetime
from tabulate import tabulate


class Banco:
	def __init__(self, deposito = 0):

		self.saldo = deposito;
		self.quantidadeSaque = 0;
		self.listaExtrato = []


	def deposito(self, deposito):
		print("===|Deposito|===")
		tmp = {}
		data_atual = datetime.today().date()
		data_formatada = data_atual.strftime("%d-%m-%Y")

		if(deposito > 0):
			self.saldo += deposito
			tmp['data'] = data_formatada
			tmp['tipo'] = "Deposito"
			tmp['valor'] = deposito
			self.listaExtrato.append(tmp)
			print(f"Deposito de RS{deposito:.2f} foi realizado com sucesso!")
		else:
			print("Valor do deposito errado")
		print("=================")

	def extrato(self):
		print("===|Extrato|===")
		if not self.listaExtrato:
			print("Não foram realizadas movimentações")
		else:
			#4print("Data         Tipo      Valor")
			#for elemento in self.listaExtrato:
			print(tabulate(self.listaExtrato, headers="keys", tablefmt="grid"))
				#print(f"{elemento['data']} {elemento['tipo']}   R$ {elemento['valor']:.2f} ")3

			print(f"saldo: R$ {self.saldo:.2f}")
		print("=================")

	def saque(self, saque):
		print("===|saque|===")
		if saque <= 0:
			print(f"Não foi possivel: O valor R${saque:.2f}\nEsta errado")
			return;

		if saque > 500:
			print(f"Não foi possivel: O valor R${saque:.2f}\nultrapassa o limite do saque que é R$ 500.00")
			return;

		if saque > self.saldo:
			print(f"Não foi possivel: O valor R${saque:.2f}\nultrapassa o limite do valor do saldo que  é R$ {self.saldo:.2f}")
			return;

		data_atual = datetime.today().date()
		data_formatada = data_atual.strftime("%d-%m-%Y")

		if(self.quantidadeSaque == 0):
			self.dataSaque = data_formatada

		if(self.dataSaque == data_formatada):
			self.quantidadeSaque  += 1
		else:
			self.quantidadeSaque  = 1
			self.dataSaque = data_formatada

		if(self.quantidadeSaque < 4):
			tmp = {}
			self.saldo -= saque
			tmp['data'] = data_formatada
			tmp['tipo'] = "Saque"
			tmp['valor'] = -1*saque
			self.listaExtrato.append(tmp)
			print(f"Saque de RS{saque:.2f} foi realizado com sucesso!")
		else:
			print("Não foi possivel: Já ultrapassou o limite de saque diário que é 3")
		print("=================")


