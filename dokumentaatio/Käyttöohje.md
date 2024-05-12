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
![Alkunäkymä](https://github.com/Sokirates/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/aloitusn%C3%A4kym%C3%A4.png)
## Ohjenäkymä

Ohjenäkymässä voit tehdä näitä toimintoa:
1. Lukea ohjeen
2. Palata aloitusnäkymään painamalla 2
3. Aloittaa pelin painamalla SPACE
![Ohjenäkymä](https://github.com/Sokirates/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/ohjen%C3%A4kym%C3%A4.png)
## Pelinäkymä

Pelinäkymässä voit tehdä näitä toimintoa:
1. Heittää noppia painamalla SPACE, kun heittoja on jäljellä.
2. Pistämään pisteen pistetaulukkoon (tyhjään kohtaan) painamalla näppäistöstä kyseisen merkin, kun heittoja on jäljellä 0.
  Painaa sitten ENTER.
3. Lukita halutun nopan painamalla ENTER kyseisen nopan päällä. 
4. Lopettaa pelin painamalla ESC.
(Jos et halua enään heittää noppia niin lukitse kaikki nopat ja heitä noppia, kunnen heittoja on jäljellä 0)

![Pelinäkymä](https://github.com/Sokirates/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/pelin%C3%A4kym%C3%A4.png)
