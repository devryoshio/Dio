
// seria um tipo construct 
// views sao as variaveis que pegamos do html
// values seria variavel que vai nos ajudar a manejar
// SelectorAll vai pegar todos que tem Id ou classe
const state = {
    view:{
        squares: document.querySelectorAll(".square"),
        enemy: document.querySelector(".enemy"),
        timeLeft: document.querySelector("#time-left"),
        score: document.querySelector("#score"),
    },
  
    values:{
        timeId:null,
        gameVelocity:1000,
        hitPosition:0,
        result:0,
        curretTime:60,
        countDownTimerId: setInterval(countDown, 1000),  // ao criar essa estrutura tb estamos chamandoa funçao 
    },
};

//ele cuida do tempo
function countDown(){
    state.values.curretTime --;

    state.view.timeLeft.textContent = state.values.curretTime;
    if(state.values.curretTime < 0){
        alert("Gamer over: O seu resultado foi:"+state.values.result);
        clearInterval(state.actions.countDownTimerId);
    }
}

function playSound(audioName){
    let audio = new Audio(`./src/audios/${audioName}.m4a`); // nao eh aspa simple mas clase 
    audio.volume = 0.4;
    audio.play();
}



// vai fazer ele mover a cada x tempo
function moveEnemy(){
    state.values.timeId = setInterval(randomSquare, state.values.gameVelocity);
}


// escolher qual quadrante que ele vai aparecer
function randomSquare(){

    //limpando: remover toda classe enemy
    state.view.squares.forEach((squares) => {
        squares.classList.remove("enemy");
    });

    //sotear
    let randomNumber = Math.floor(Math.random()*9);

    // pegando o id
    let randomSquare = state.view.squares[randomNumber];

    //adicionado classe enemy
    randomSquare.classList.add("enemy");

    //guardado o Id
    state.values.hitPosition = randomSquare.id;
}




function addListenerHitBox(){
    state.view.squares.forEach((square) => {

        //ele pega posição do click
        square.addEventListener("mousedown", ()=> {

            //comparando se esta no mesmo quadrante 
            if (square.id === state.values.hitPosition){
                state.values.result++;
                state.view.score.textContent = state.values.result; // coloca o resultado no html
                state.values.hitPosition = null;
                playSound("hit");
            }
        });
    });
}


function initialize(){
    moveEnemy();
    addListenerHitBox();
}


initialize();