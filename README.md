# flask_forum_application

## Ohje

1: .env tiedoston määrittely

Tiedostossa on oltava seuraavat muuttujat:

~~~
DATABASE_URL="<postgresin-URI-tietokantaan>"
SECRET_KEY="<salainen-avain-flaskin-salausta-varten>"
~~~

Jos PostgreSQL on asennettu ![kurssin asennusskriptin](https://github.com/hy-tsoha/local-pg) avulla,
tiedostoon voi pistää suoraan

~~~
DATABASE_URL="postgresql+psycopg2://" 
~~~

2: Riippuvuuksien asentaminen poetryn avulla

~~~
poetry install
~~~

3: Tietokannan scheman määrittäminen

Kun tietokanta on lokaalisti pyörimässä, scheman voi määrittää seuraavasti:

~~~
psql < schema.sql
~~~

4: Sovelluksen käynnistäminen

~~~
poetry run flask --app application/main.py run --debug 
~~~

tai

~~~
bash launch_debug.sh
~~~

## Välipalautus 2 tilanne

Sovelluksessa käyttäjä voi luoda tunnukset ja kirjautua sisään/ulos.

Käyttäjä voi lukea eri keskustelualueilla viestejä.

Sovelluksessa ei voi vielä luoda keskustelualueita tai viestejä.

## Valittu aihe:

Keskustelusovellus (Sama mikä esimerkissä)

Sovelluksessa näkyy keskustelualueita, joista jokaisella on tietty aihe. Alueilla on keskusteluketjuja, jotka muodostuvat viesteistä. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä.

Sovelluksen ominaisuuksia:

* Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
* Käyttäjä näkee sovelluksen etusivulla listan alueista sekä jokaisen alueen ketjujen ja viestien määrän ja viimeksi lähetetyn viestin ajankohdan.
* Käyttäjä voi luoda alueelle uuden ketjun antamalla ketjun otsikon ja aloitusviestin sisällön.
* Käyttäjä voi kirjoittaa uuden viestin olemassa olevaan ketjuun.
* Käyttäjä voi muokata luomansa ketjun otsikkoa sekä lähettämänsä viestin sisältöä. Käyttäjä voi myös poistaa ketjun tai viestin.
* Käyttäjä voi etsiä kaikki viestit, joiden osana on annettu sana.
* Ylläpitäjä voi lisätä ja poistaa keskustelualueita.
* Ylläpitäjä voi luoda salaisen alueen ja määrittää, keillä käyttäjillä on pääsy alueelle.
