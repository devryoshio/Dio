public class Main {

	public static void main(String[] args) {
		Cliente javanilson = new Cliente();
		javanilson.setNome("Javanilson");
		
		Conta cc = new ContaCorrente(javanilson);
		Conta poupanca = new ContaPoupanca(javanilson);

		cc.depositar(100);
		cc.transferir(100, poupanca);
		
		cc.imprimirExtrato();
		poupanca.imprimirExtrato();
	}

}
