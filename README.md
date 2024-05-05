# Flask Keskustelusovellus

[Käyttöohje](#käyttöohje)

[Lopullinen palautus](#lopullinen-palautus)

[Välipalautus 3 tilanne](#välipalautus-3-tilanne)

[Välipalautus 2 tilanne](#välipalautus-2-tilanne)

[Valittu Aihe](#valittu-aihe)

## Käyttöhje

### Sovelluksen lokaalinen käynnistys

1: .env tiedoston määrittely

Tiedostossa on oltava seuraavat muuttujat:

~~~
SQLALCHEMY_DATABASE_URI="<postgresin-URI-tietokantaan>"
SECRET_KEY="<salainen-avain-flaskin-salausta-varten>"
WTF_CSRF_SECRET_KEY="<salainen-avain-csrf-suojaustokenin-salausta-varten>"
~~~

Jos PostgreSQL on asennettu ![kurssin asennusskriptin](https://github.com/hy-tsoha/local-pg) avulla,
tiedostoon voi pistää suoraan

~~~
SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://" 
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

Debug versiona:

~~~
poetry run flask --app application/main.py run --debug 
~~~

tai

~~~
bash launch_debug.sh
~~~

Tavallisena:

~~~
poetry run flask --app application/main.py run 
~~~

tai

~~~
bash launch.sh
~~~

### Sovelluksen demokomennot

Halutessaan sovellukseen voi lisätä demodataa seuraavalla komennolla:

~~~
poetry run flask --app application/main.py user create-demo
~~~
tai
~~~
bash create_demo.sh
~~~
Tämä demodatan luomien käyttäjien tileille ei voi kirjautua. Ne ovat vain esimerkkinä. Käyttäjäominaisuuksien testaamiseen kannattaa luoda uusi tili.

Tietokannan datan voi nollata seuraavalla komennolla (taulut kuitenkin pysyvät):

~~~
poetry run flask --app application/main.py database wipe
~~~

Tietylle käyttäjälle voi antaa ylläpitäjäoikeudet seuraavalla komennolla:

~~~
poetry run flask --app application/main.py user give-admin <käyttäjän-nimi>
~~~

Sen voi myös poistaa seuraavasti:

~~~
poetry run flask --app application/main.py user remove-admin <käyttäjän-nimi>
~~~

## Lopullinen palautus

Sovelluksessa käyttäjä voi luoda tunnukset ja kirjautua sisään/ulos.

Käyttäjä voi lukea eri keskustelualueilla viestejä.

Käyttäjä voi luoda keskusteluketjuja, kommentoida niihin sekä poistaa tai muokata omia viestejään.

Ylläpitäjä voi luoda keskustelualueen, muokata sen ominaisuuksia tai poistaa sen kokonaan.

Keskustelualueen voi tehdä yksityiseksi, jolloin vain tietyt käyttäjät pääsevät lukemaan ja kommentoimaan sinne.

## Välipalautus 3 tilanne

Sovelluksessa käyttäjä voi luoda tunnukset ja kirjautua sisään/ulos.

Käyttäjä voi lukea eri keskustelualueilla viestejä.

Käyttäjä voi luoda keskusteluketjuja ja vastata niihin.

Ylläpitäjä voi luoda keskustelualueen /create_forum osoitteessa.

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
