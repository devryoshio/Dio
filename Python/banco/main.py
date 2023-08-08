from Banco import Banco

a = Banco (0)

sair = False

while(not sair):
	print("Digite o numero que voce deseja fazer:")
	print("[1]: Deposito")
	print("[2]: Saque")
	print("[3]: Extrato")
	print("[4]: Sair")
	
	opcao = int(input())
	
	if opcao == 1:
		valor = float(input("Digite o valor do deposito:"))
		a.deposito(valor)
	elif opcao == 2:
		valor = float(input("Digite o valor do saque:"))
		a.saque(valor)
	elif(opcao == 3):
		a.extrato()
	elif(opcao == 4):
		sair = True
	else :
		print("Não existe essa opção")


