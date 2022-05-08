# Notas de aulas 

## Para habilitar diplay flex


``` css3


<style>
    .flex{
    display: flex; // habilitando flexbox
    max-width: 300px;
    padding: 10px;
    border: 2px solid black;
}

    .item{
        background-color: aqua;
        margin: 5px;
    }
</style>

...
<div class="flex">
    <div class="item">item 1</div>
    <div class="item">item 2</div>
    <div class="item">item 3</di>
</div>
``` 

## Flex-direction

é a propriedade que estabelece o eixo principal do container, definindo assim a direção que os flex items são colocados no flex container.

-  row: 
- row-reserve:
- column: 
- column-reverse:

## flex-wrap 

Serve para quebra de linha, que pode ser

- wrap
- nowrap
- wrap-reverse;

## flex-flow

seria a junção de flex-direction e flex-wrap

## justify-content 

Seria como será organizado os "blocos" dentro do container 

[mozila](https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content)

## align-items

## align-content


## align-self

## flex-grow

## flex-basis

## flex-shrink

## flex

## order

