public interface IConta{
	
	void sacar(double valor);
	void depositar(double valor);
	void transferir(double valor, IConta contaDestino);
	void imprimirExtrato();
	
}


// interface seria .h do C, a classe Conta seria onde fica o corpo da funções 
