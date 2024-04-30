# Yatzy

## Dokumentaatio
- [Vaatimusmäärittely](https://github.com/Sokirates/ot-harjoitustyo/blob/main/dokumentaatio/Vaatimusm%C3%A4%C3%A4rittely.md)
- [Tuntikirjanpito](https://github.com/Sokirates/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/Sokirates/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)
- [Arkkitehtuuri](https://github.com/Sokirates/ot-harjoitustyo/blob/main/dokumentaatio/Arkkitehtuuri.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```
2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```
Raportti generoituu _htmlcov_-hakemistoon.


### Releases
[Viikko5](https://github.com/Sokirates/ot-harjoitustyo/releases/tag/viikko5)
[Viikko6](https://github.com/Sokirates/ot-harjoitustyo/releases/tag/viikko6)


