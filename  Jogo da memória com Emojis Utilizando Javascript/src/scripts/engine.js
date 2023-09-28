const emojis = ["😀 ", "😀 ", "😁", "😁", "🤣", "🤣", "😇", "😇", 
                "😍", "😍", "😘", "😘", "😝", "😝", "😡", "😡"];

let openCards = [];

// responsavel por embaralhar
let shuffleEmojis = emojis.sort(() => (Math.random()> 0.5) ? 2 : -1);

for (let i=0; i < emojis.length; i++)
{
    //estamos dizendo que queremos criar a tag div
    let box = document.createElement("div");

    // nome da nossa classe
    box.className = "item";

    //pegando o emoji
    box.innerHTML = shuffleEmojis[i];

    //Quando da o click
    box.onclick = handleClick;

    // criando o "filho"
    document.querySelector(".game").appendChild(box);
}

// responsavel pelo click
function handleClick(){

    //serve para armazena as carta
    if (openCards.length < 2) {
        this.classList.add("boxOpen"); //adiciona classe boxOpen, entao vai mostra a carta
        openCards.push(this); // vai adiciona na nossa lista
    }

    //verifica se duas carta selecionado, caso seja verdade, verifica se eles se correspodem 
    if (openCards.length == 2) {
        setTimeout(checkMatch, 500);
    }
}

//Serve para verirca se deu match as duas carta
function checkMatch(){
    //caso deu martch
    if (openCards[0].innerHTML === openCards[1].innerHTML){
        openCards[0].classList.add("boxMatch"); // vai adiciona class boxMatch
        openCards[1].classList.add("boxMatch");
    } else {
        openCards[0].classList.remove("boxOpen"); //vai adiciona classe boxOpen que vai revirar a carta
        openCards[1].classList.remove("boxOpen");
    }
    
    //tipo zera a nossa lista
    openCards = [];

    //condiçao de vitoria
    //  a quantidade de class que tem vo valor .boxMAtCh corresponde a quantida de emoji
    if (document.querySelectorAll(".boxMatch").length === emojis.length){
        alert("Parabéns, você venceu!")
    }
}