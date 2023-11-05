
// vai pegar todas as teclas
const pianoKeys = document.querySelectorAll(".piano-keys .key");

//vai captura o volume do html
const volumeSlider = document.querySelector(".volume-slider input");

// vai capturar a parte do check
const keysCheck = document.querySelector(".keys-check input");


let audio = new Audio("src/tunes/a.wav");

let mapedkeys = []; //nosso vetor com as teclas do teclado

// responsavel pelo som
const playTune = (key) => {
    audio.src = `src/tunes/${key}.wav`
    audio.play();

    //vai ser responsavel chamar a classe para fazer a sombra
    const  clickedKey = document.querySelector(`[data-key="${key}"]`); //vai pegar o lugar certo para nos colocar tag active
    //adicionando a classe active
    clickedKey.classList.add("active");
    //depois passar 150 ele vai remove a tecla active
    setTimeout(()=>{
        clickedKey.classList.remove("active");
    },150);
};

 

pianoKeys.forEach((key) =>{
    console.log(key.dataset.key); //pegar os valores do key
    key.addEventListener("click", () => playTune(key.dataset.key))
    mapedkeys.push(key.dataset.key); //cliando uma lista das teclas 
    
});

// quando teclamos com teclado 
document.addEventListener("keydown", (e)=>{
    if(mapedkeys){ //so chamar quando for clicado as teclas que existe
        playTune(e.key);
    }
});

// responsavel pelo volume
const handleVolume = (e) => {
    audio.volume = e.target.value;
};

volumeSlider.addEventListener ("input", handleVolume);


const showHideKeys = ( ) =>{
    pianoKeys.forEach(key => key.classList.toggle("hide"))
}

keysCheck.addEventListener("click", showHideKeys);
