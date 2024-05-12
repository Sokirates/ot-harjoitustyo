# Käyttöohje

Lataa projektin viimeisimmän releasen lähdekoodi.

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:
```
poetry install
```
Käynnistä ohjelma komennolla:
```
poetry run invoke start
```
## Alkunäkymä

Alkunäkymässä voit tehdä näitä toimintoa:
1. Aloittaa pelin painamalla SPACE
2. Lopettaa pelin painamalla ESC 
3. Katsoa ohjeet painamalla 1

## Ohjenäkymä

Ohjenäkymässä voit tehdä näitä toimintoa:
1. Lukea ohjeen
2. Palata aloitusnäkymään painamalla 2
3. Aloittaa pelin painamalla SPACE

## Pelinäkymä

Pelinäkymässä voit tehdä näitä toimintoa:
1. Heittää noppia painamalla SPACE, kun heittoja on jäljellä.
2. Pistämään pisteen pistetaulukkoon (tyhjään kohtaan) painamalla näppäistöstä kyseisen merkin
ja lopuksi painamalla ENTER.
3. Lukitsemaan halutun nopan painamalla ENTER kyseisen nopan päällä. 
