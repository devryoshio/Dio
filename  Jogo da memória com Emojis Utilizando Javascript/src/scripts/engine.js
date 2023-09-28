const emojis = ["🐵", "🐵", "🐷", "🐷", "🐶", "🐶", "🐸", "🐸", 
                "🐟", "🐟", "🐞", "🐞", "🐔", "🐔", "🦇", "🦇"];

let openCards = [];

// responsavel por embaralhar
let shuffleEmojis = emojis.sort(() => (Math.random()> 0.5 ? 2 : -1));


for (let i=0; i < emojis.length; i++)
{
    //estamos dizendo que queremos criar a tag div
    let box = document.createElement("div");

    // nome da nossa classe
    box.className = "item";

    //pegando o emoji
    box.innerHTML = shuffleEmojis[i];

    // criando o "filho"
    document.querySelector(".game").appendChild(box);
}