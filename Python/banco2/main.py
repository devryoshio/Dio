 

from Conta import Conta

conta = Conta()

sair = False

while(not sair):
	print("Digite o numero que voce deseja fazer:")
	print("[1]: Deposito")
	print("[2]: Saque")
	print("[3]: Extrato")
	print("[4]: Sair")

	opcao = int(input())

	if opcao == 1:
		conta.criar_usuario()
	elif opcao == 2:
		conta.deposito()


