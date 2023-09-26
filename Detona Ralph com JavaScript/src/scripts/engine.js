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
    },
};

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
}




function addListenerHitBox(){
    state.view.squares.forEach((square) => {
        square.addEventListener("mousedown", ()=> {
            alert("clicou"); 
        });
    });
}


function initialize(){
    moveEnemy();
    addListenerHitBox();
}


initialize();