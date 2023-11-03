
// vau pegar todas as teclas
const pianoKeys = document.querySelectorAll(".piano-keys .key")

pianoKeys.forEach((key) =>{
    console.log(key.dataset.key); //pegar os valores do key
    
});
