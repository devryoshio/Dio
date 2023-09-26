


function Pessoa(nome, idade){
    this.nome = nome
    this.idade = idade
}

Pessoa.prototype.falar = function{}{
    console.log('Meu nome e'+ ${this.nome})
}


const prof =  new Pessoa('Renan', 30)

prof.falar()
