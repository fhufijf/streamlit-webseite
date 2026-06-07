import streamlit as st
import json
import pandas as pd

st.title("Quiz")
st.subheader("Man kann die Anzahl fragen ändern!")
st.write("(Drück die Optionen um Fragen zu lösen.)")

st.divider()

quiz = """[
    {
    "frage": "Welches chemische Element hat das Symbol 'W'?",
    "optionen": [
        "Wasserstoff",
        "Wolfram",
        "Weißgold",
        "Wismut"
    ],
    "antwort": "Wolfram"
    },
    {
    "frage": "Wer komponierte die Oper 'Die Zauberflöte'?",
    "optionen": [
        "Wolfgang Amadeus Mozart",
        "Ludwig van Beethoven",
        "Johann Sebastian Bach",
        "Richard Wagner"
    ],
    "antwort": "Wolfgang Amadeus Mozart"
    },
  {
    "frage": "Wie viele Planeten hat unser Sonnensystem seit 2006 offiziell?",
    "optionen": [
      "10",
      "12",
      "8",
      "9"
    ],
    "antwort": "8"
  },
  {
    "frage": "In welchem Jahr fiel die Berliner Mauer?",
    "optionen": [
      "1985",
      "1991",
      "1987",
      "1989"
    ],
    "antwort": "1989"
  },
  {
    "frage": "Welches Land hat die meisten offiziellen Amtssprachen?",
    "optionen": [
      "Südafrika",
      "Indien",
      "Schweiz",
      "Kanada"
    ],
    "antwort": "Südafrika"
  },
  {
    "frage": "Was ist die Hauptstadt von Kasachstan seit 2019?",
    "optionen": [
      "Almaty",
      "Nur-Sultan",
      "Astana",
      "Taschkent"
    ],
    "antwort": "Nur-Sultan"
  },
  {
    "frage": "Welcher Planet ist der kleinste im Sonnensystem?",
    "optionen": [
      "Venus",
      "Mars",
      "Merkur",
      "Neptun"
    ],
    "antwort": "Merkur"
  },
  {
    "frage": "Wie viele Tasten hat ein klassisches Klavier?",
    "optionen": [
      "88",
      "92",
      "84",
      "100"
    ],
    "antwort": "88"
  },
  {
    "frage": "Welcher deutsche Physiker erhielt den Nobelpreis für die Quantenmechanik?",
    "optionen": [
      "Albert Einstein",
      "Werner Heisenberg",
      "Max Planck",
      "Otto Hahn"
    ],
    "antwort": "Werner Heisenberg"
  },
  {
    "frage": "Welches Meer ist das salzhaltigste der Erde?",
    "optionen": [
      "Rotes Meer",
      "Totes Meer",
      "Persischer Golf",
      "Don-Juan-See"
    ],
    "antwort": "Totes Meer"
  },
  {
    "frage": "Welcher Kontinent hat die größte Anzahl an Ländern?",
    "optionen": [
      "Europa",
      "Amerika",
      "Afrika",
      "Asien"
    ],
    "antwort": "Afrika"
  },
  {
    "frage": "Wie nennt man ein fünfseitiges Vieleck?",
    "optionen": [
      "Hexagon",
      "Pentagon",
      "Heptagon",
      "Quadrat"
    ],
    "antwort": "Pentagon"
  },
  {
    "frage": "Welcher Künstler ist bekannt für Schmelzende Uhren?",
    "optionen": [
      "Picasso",
      "Kandinsky",
      "Salvador Dalí",
      "Miro"
    ],
    "antwort": "Salvador Dalí"
  },
  {
    "frage": "Wie heißt das größte Korallenriff der Welt?",
    "optionen": [
      "Great Barrier Reef",
      "Rotes Riff",
      "Karibisches Riff",
      "Indopazifisches Riff"
    ],
    "antwort": "Great Barrier Reef"
  },
  {
    "frage": "Was ist kein Bestandteil der DNA?",
    "optionen": [
      "Adenin",
      "Thymin",
      "Guanin",
      "Uracil"
    ],
    "antwort": "Uracil"
  },
  {
    "frage": "In welchem Land befindet sich der Kilimandscharo?",
    "optionen": [
      "Kenia",
      "Tansania",
      "Uganda",
      "Äthiopien"
    ],
    "antwort": "Tansania"
  },
  {
    "frage": "Wie viele Sekunden hat eine Stunde?",
    "optionen": [
      "3.000",
      "5.600",
      "3.600",
      "6.000"
    ],
    "antwort": "3.600"
  },
  {
    "frage": "Welches Element ist bei Raumtemperatur flüssig?",
    "optionen": [
      "Quecksilber",
      "Silber",
      "Eisen",
      "Zink"
    ],
    "antwort": "Quecksilber"
  },
  {
    "frage": "Was ist die größte Insel der Welt (ohne Kontinente)?",
    "optionen": [
      "Borneo",
      "Neuguinea",
      "Madagaskar",
      "Grönland"
    ],
    "antwort": "Borneo"
  },
  {
    "frage": "Welcher deutsche Schriftsteller schrieb 'Der Steppenwolf'?",
    "optionen": [
      "Franz Kafka",
      "Hermann Hesse",
      "Thomas Mann",
      "Bertolt Brecht"
    ],
    "antwort": "Hermann Hesse"
  },
  {
    "frage": "Welches Land hat die meisten Vulkaneruptionen pro Jahr?",
    "optionen": [
      "Indonesien",
      "Japan",
      "Italien",
      "USA"
    ],
    "antwort": "Indonesien"
  },
  {
    "frage": "Wie heißt der kleinste Knochen im menschlichen Körper?",
    "optionen": [
      "Steigbügel",
      "Hammer",
      "Amboss",
      "Steigbügel"
    ],
    "antwort": "Steigbügel"
  },
  {
    "frage": "Welcher Physiker ist bekannt für die Entdeckung des Photoeffekts?",
    "optionen": [
      "Isaac Newton",
      "Galileo Galilei",
      "Albert Einstein",
      "Nikola Tesla"
    ],
    "antwort": "Albert Einstein"
  },
  {
    "frage": "Wie viele Zähne hat ein erwachsener Mensch normalerweise?",
    "optionen": [
      "28",
      "32",
      "30",
      "34"
    ],
    "antwort": "28"
  },
  {
    "frage": "Welche Stadt wird auch als 'Stadt der tausend Brücken' bezeichnet?",
    "optionen": [
      "Paris",
      "Venedig",
      "Amsterdam",
      "St. Petersburg"
    ],
    "antwort": "St. Petersburg"
  },
  {
    "frage": "Welches Gas macht den größten Anteil der Erdatmosphäre aus?",
    "optionen": [
      "Stickstoff",
      "Sauerstoff",
      "Kohlenstoffdioxid",
      "Argon"
    ],
    "antwort": "Stickstoff"
  },
  {
    "frage": "Wer schrieb den Roman 'Krieg und Frieden'?",
    "optionen": [
      "Dostojewski",
      "Leo Tolstoi",
      "Anton Tschechow",
      "Nikolai Gogol"
    ],
    "antwort": "Leo Tolstoi"
  },
  {
    "frage": "Welches Metall wird am häufigsten in der Elektronik verwendet?",
    "optionen": [
      "Gold",
      "Aluminium",
      "Kupfer",
      "Silber"
    ],
    "antwort": "Kupfer"
  },
  {
    "frage": "Wie lautet die chemische Formel von Ammoniak?",
    "optionen": [
      "H2O",
      "CO2",
      "CH4",
      "NH3"
    ],
    "antwort": "NH3"
  },
  {
    "frage": "Wer war der erste Mensch im Weltraum?",
    "optionen": [
      "Neil Armstrong",
      "Juri Gagarin",
      "Buzz Aldrin",
      "Alan Shepard"
    ],
    "antwort": "Juri Gagarin"
  },
  {
    "frage": "Wie viele Nullen hat eine Billion (deutsche Zählweise)?",
    "optionen": [
      "12",
      "9",
      "15",
      "18"
    ],
    "antwort": "12"
  },
  {
    "frage": "Welches Land gewann die Fußball-Weltmeisterschaft 2014?",
    "optionen": [
      "Brasilien",
      "Argentinien",
      "Deutschland",
      "Spanien"
    ],
    "antwort": "Brasilien"
  },
  {
    "frage": "Welcher Fluss ist der längste der Welt?",
    "optionen": [
      "Amazonas",
      "Yangtse",
      "Mississippi",
      "Nil"
    ],
    "antwort": "Nil"
  },
  {
    "frage": "Welcher Komponist schrieb die 'Mondscheinsonate'?",
    "optionen": [
      "Ludwig van Beethoven",
      "Johann Sebastian Bach",
      "Wolfgang Amadeus Mozart",
      "Frédéric Chopin"
    ],
    "antwort": "Ludwig van Beethoven"
  },
  {
    "frage": "Was ist die Hauptstadt von Neuseeland?",
    "optionen": [
      "Auckland",
      "Christchurch",
      "Wellington",
      "Hamilton"
    ],
    "antwort": "Wellington"
  },
  {
    "frage": "Wie nennt man die Wissenschaft vom Wetter?",
    "optionen": [
      "Geologie",
      "Meteorologie",
      "Astronomie",
      "Biologie"
    ],
    "antwort": "Meteorologie"
  },
  {
    "frage": "Welcher Planet ist bekannt als der 'Rote Planet'?",
    "optionen": [
      "Venus",
      "Jupiter",
      "Saturn",
      "Mars"
    ],
    "antwort": "Mars"
  },
  {
    "frage": "Wie viele Bundesländer hat Deutschland?",
    "optionen": [
      "16",
      "14",
      "18",
      "20"
    ],
    "antwort": "16"
  },
  {
    "frage": "Welches Organ produziert Insulin im menschlichen Körper?",
    "optionen": [
      "Leber",
      "Niere",
      "Bauchspeicheldrüse",
      "Milz"
    ],
    "antwort": "Bauchspeicheldrüse"
  },
  {
    "frage": "Welcher Film gewann den Oscar für den besten Film im Jahr 1994?",
    "optionen": [
      "Forrest Gump",
      "Pulp Fiction",
      "The Shawshank Redemption",
      "Lion King"
    ],
    "antwort": "Forrest Gump"
  },
  {
    "frage": "In welchem Jahr endete der Dreißigjährige Krieg?",
    "optionen": [
      "1640",
      "1648",
      "1652",
      "1638"
    ],
    "antwort": "1648"
  },
  {
    "frage": "Welches Element hat die Ordnungszahl 79?",
    "optionen": [
      "Silber",
      "Platin",
      "Gold",
      "Kupfer"
    ],
    "antwort": "Gold"
  },
  {
    "frage": "Welcher Fußballspieler gewann die meisten Ballon d'Or-Auszeichnungen bis 2023?",
    "optionen": [
      "Cristiano Ronaldo",
      "Zinedine Zidane",
      "Ronaldinho",
      "Lionel Messi"
    ],
    "antwort": "Lionel Messi"
  },
  {
    "frage": "Welches klassische Werk stammt von Johann Wolfgang von Goethe?",
    "optionen": [
      "Faust",
      "Die Leiden des jungen Werther",
      "Wilhelm Tell",
      "Der Prozess"
    ],
    "antwort": "Faust"
  },
  {
    "frage": "Welcher Wissenschaftler entdeckte die Röntgenstrahlen?",
    "optionen": [
      "Marie Curie",
      "Wilhelm Conrad Röntgen",
      "Isaac Newton",
      "Nikola Tesla"
    ],
    "antwort": "Wilhelm Conrad Röntgen"
  },
  {
    "frage": "Welche Filmreihe basiert auf den Büchern von J.R.R. Tolkien?",
    "optionen": [
      "Harry Potter",
      "Die Chroniken von Narnia",
      "Der Herr der Ringe",
      "Game of Thrones"
    ],
    "antwort": "Der Herr der Ringe"
  },
    {
    "frage": "Wie viele Minuten dauert ein reguläres Handballspiel?",
    "optionen": [
        "60",
        "45",
        "90",
        "30"
    ],
    "antwort": "60"
    },
    {
    "frage": "Welche Kultur ist bekannt für die Erfindung der Hieroglyphen?",
    "optionen": [
        "Mesopotamien",
        "Griechenland",
        "China",
        "Ägypten"
    ],
    "antwort": "Ägypten"
    },
    {
    "frage": "Wer war der erste Bundeskanzler der Bundesrepublik Deutschland?",
    "optionen": [
        "Willy Brandt",
        "Konrad Adenauer",
        "Helmut Kohl",
        "Ludwig Erhard"
    ],
    "antwort": "Konrad Adenauer"
    },
    {
    "frage": "Welcher Physiker entwickelte die Relativitätstheorie?",
    "optionen": [
        "Albert Einstein",
        "Max Planck",
        "Niels Bohr",
        "Erwin Schrödinger"
    ],
    "antwort": "Albert Einstein"
    },
    {
    "frage": "Welcher Regisseur ist bekannt für Filme wie 'Psycho' und 'Vertigo'?",
    "optionen": [
        "Stanley Kubrick",
        "Francis Ford Coppola",
        "Alfred Hitchcock",
        "Martin Scorsese"
    ],
    "antwort": "Alfred Hitchcock"
    },
  {
    "frage": "Welches Land gewann die erste Fußball-Weltmeisterschaft 1930?",
    "optionen": [
      "Uruguay",
      "Brasilien",
      "Italien",
      "Argentinien"
    ],
    "antwort": "Uruguay"
  },
  {
    "frage": "Wie heißt die größte Wüste der Erde?",
    "optionen": [
      "Sahara",
      "Antarktische Wüste",
      "Arabische Wüste",
      "Gobi"
    ],
    "antwort": "Sahara"
  },
  {
    "frage": "Welcher Komponist schrieb die 'Neunte Symphonie'?",
    "optionen": [
      "Johann Sebastian Bach",
      "Wolfgang Amadeus Mozart",
      "Franz Schubert",
      "Ludwig van Beethoven"
    ],
    "antwort": "Johann Sebastian Bach"
  },
  {
    "frage": "Welche Pflanze ist bekannt für die größte Blüte der Welt?",
    "optionen": [
      "Seerose",
      "Sonnenblume",
      "Rafflesie",
      "Titanwurz"
    ],
    "antwort": "Seerose"
  },
  {
    "frage": "Welcher deutsche Schauspieler spielte die Hauptrolle in 'Das Boot'?",
    "optionen": [
      "Jürgen Prochnow",
      "Dieter Laser",
      "Klaus Kinski",
      "Armin Mueller-Stahl"
    ],
    "antwort": "Jürgen Prochnow"
  },
  {
    "frage": "Welcher Wissenschaftszweig beschäftigt sich mit dem Verhalten von Atomen und Molekülen?",
    "optionen": [
      "Biologie",
      "Chemie",
      "Physik",
      "Geologie"
    ],
    "antwort": "Biologie"
  },
  {
    "frage": "Wie viele Goldmedaillen gewann Michael Phelps bei den Olympischen Spielen 2008?",
    "optionen": [
      "8",
      "7",
      "6",
      "9"
    ],
    "antwort": "8"
  },
  {
    "frage": "Welcher Regisseur führte Regie bei dem Film 'Blade Runner' aus dem Jahr 1982?",
    "optionen": [
      "Ridley Scott",
      "James Cameron",
      "Steven Spielberg",
      "Martin Scorsese"
    ],
    "antwort": "Ridley Scott"
  },
  {
    "frage": "In welcher Sportart wird der Davis Cup ausgetragen?",
    "optionen": [
      "Golf",
      "Tennis",
      "Rugby",
      "Cricket"
    ],
    "antwort": "Golf"
  },
  {
    "frage": "Welches literarische Werk stammt von Franz Kafka?",
    "optionen": [
      "Der Prozess",
      "Faust",
      "Die Verwandlung",
      "Die Blechtrommel"
    ],
    "antwort": "Der Prozess"
  },
  {
    "frage": "In welchem Jahr begann die Französische Revolution?",
    "optionen": [
      "1789",
      "1799",
      "1776",
      "1789"
    ],
    "antwort": "1789"
  },
  {
    "frage": "Welches deutsche Bundesland hat die meisten Einwohner?",
    "optionen": [
      "Bayern",
      "Hessen",
      "Nordrhein-Westfalen",
      "Baden-Württemberg"
    ],
    "antwort": "Bayern"
  },
  {
    "frage": "In welcher Stadt steht das berühmte Bauwerk 'Kölner Dom'?",
    "optionen": [
      "Köln",
      "Düsseldorf",
      "Frankfurt",
      "München"
    ],
    "antwort": "Köln"
  },
  {
    "frage": "Welches deutsche Bundesland ist flächenmäßig das größte?",
    "optionen": [
      "Baden-Württemberg",
      "Nordrhein-Westfalen",
      "Niedersachsen",
      "Bayern"
    ],
    "antwort": "Baden-Württemberg"
  },
  {
    "frage": "Wer schrieb die deutsche Nationalhymne?",
    "optionen": [
      "Johann Wolfgang von Goethe",
      "Friedrich Schiller",
      "August Heinrich Hoffmann von Fallersleben",
      "Heinrich Heine"
    ],
    "antwort": "Johann Wolfgang von Goethe"
  },
  {
    "frage": "Welches Automobilunternehmen hat seinen Sitz in Wolfsburg?",
    "optionen": [
      "BMW",
      "Volkswagen",
      "Mercedes-Benz",
      "Audi"
    ],
    "antwort": "BMW"
  },
  {
    "frage": "Welches deutsche Bundesland ist für das Oktoberfest bekannt?",
    "optionen": [
      "Bayern",
      "Sachsen",
      "Hessen",
      "Thüringen"
    ],
    "antwort": "Bayern"
  },
  {
    "frage": "Welcher deutsche Physiker entwickelte die Relativitätstheorie?",
    "optionen": [
      "Max Planck",
      "Werner Heisenberg",
      "Otto Hahn",
      "Albert Einstein"
    ],
    "antwort": "Max Planck"
  },
  {
    "frage": "Wie heißt die größte Insel Deutschlands?",
    "optionen": [
      "Sylt",
      "Rügen",
      "Fehmarn",
      "Usedom"
    ],
    "antwort": "Sylt"
  },
  {
    "frage": "Welcher deutsche Fußballverein gewann die meisten Meisterschaften?",
    "optionen": [
      "FC Bayern München",
      "Borussia Dortmund",
      "Hamburger SV",
      "Werder Bremen"
    ],
    "antwort": "FC Bayern München"
  },
  {
    "frage": "Welches Meer grenzt im Norden an Deutschland?",
    "optionen": [
      "Ostsee",
      "Mittelmeer",
      "Nordsee",
      "Schwarzes Meer"
    ],
    "antwort": "Nordsee"
  },
  {
    "frage": "Welches deutsche Schloss diente als Vorlage für das Dornröschenschloss von Disney?",
    "optionen": [
      "Schloss Neuschwanstein",
      "Schloss Hohenzollern",
      "Schloss Heidelberg",
      "Schloss Sanssouci"
    ],
    "antwort": "Schloss Neuschwanstein"
  },
  {
    "frage": "Welcher Fluss ist der längste in Deutschland?",
    "optionen": [
      "Elbe",
      "Rhein",
      "Donau",
      "Main"
    ],
    "antwort": "Elbe"
  },
  {
    "frage": "Welches Land gewann die Copa América 2019?",
    "optionen": [
      "Brasilien",
      "Argentinien",
      "Chile",
      "Uruguay"
    ],
    "antwort": "Brasilien"
  },
  {
    "frage": "Welcher Verein hat die meisten UEFA Champions League-Titel gewonnen?",
    "optionen": [
      "Real Madrid",
      "AC Mailand",
      "FC Bayern München",
      "Liverpool FC"
    ],
    "antwort": "Real Madrid"
  },
  {
    "frage": "Wie viele WM-Finals hat Deutschland insgesamt erreicht (bis 2022)?",
    "optionen": [
      "6",
      "8",
      "5",
      "7"
    ],
    "antwort": "6"
  },
  {
    "frage": "Wie viele Spieler befinden sich bei einer Fußballmannschaft insgesamt im Kader während eines Spiels (gemäß FIFA-Regeln, Stand 2025)?",
    "optionen": [
      "20",
      "23",
      "26",
      "18"
    ],
    "antwort": "20"
  },
  {
    "frage": "Wer war der Trainer der deutschen Mannschaft bei der WM 2014?",
    "optionen": [
      "Jürgen Klinsmann",
      "Hansi Flick",
      "Joachim Löw",
      "Franz Beckenbauer"
    ],
    "antwort": "Joachim Löw"
  },
  {
    "frage": "Welcher Spieler hat die meisten Bundesliga-Spiele absolviert?",
    "optionen": [
      "Karl-Heinz Körbel",
      "Manfred Kaltz",
      "Lothar Matthäus",
      "Klaus Fichtel"
    ],
    "antwort": "Karl-Heinz Körbel"
  },
  {
    "frage": "Welcher Spieler war als 'Der Bomber der Nation' bekannt?",
    "optionen": [
      "Gerd Müller",
      "Karl-Heinz Rummenigge",
      "Jürgen Klinsmann",
      "Miroslav Klose"
    ],
    "antwort": "Gerd Müller"
  },
  {
    "frage": "Welches Land gewann die Fußball-Europameisterschaft 2016?",
    "optionen": [
      "Deutschland",
      "Frankreich",
      "Spanien",
      "Portugal"
    ],
    "antwort": "Portugal"
  },
  {
    "frage": "Welcher Verein trägt den Spitznamen 'Die Fohlen'?",
    "optionen": [
      "Borussia Mönchengladbach",
      "Borussia Dortmund",
      "Eintracht Frankfurt",
      "VfL Wolfsburg"
    ],
    "antwort": "Borussia Mönchengladbach"
  },
  {
    "frage": "Welcher Spieler war Kapitän der deutschen Nationalmannschaft beim WM-Finale 2014?",
    "optionen": [
      "Philipp Lahm",
      "Bastian Schweinsteiger",
      "Manuel Neuer",
      "Thomas Müller"
    ],
    "antwort": "Philipp Lahm"
  },
  {
    "frage": "Wie viele Mannschaften spielen normalerweise in der Bundesliga?",
    "optionen": [
      "16",
      "18",
      "20",
      "14"
    ],
    "antwort": "18"
  },
  {
    "frage": "In welchem Jahr wurde die deutsche Nationalmannschaft erstmals bei einer WM-Vorrunde ausgeschieden?",
    "optionen": [
      "1978",
      "2018",
      "2018",
      "2002"
    ],
    "antwort": "2018"
  },
  {
    "frage": "Welcher Vogel hat eine Feder auf dem Kopf, die wie ein 'Ausrufungszeichen' aussieht?",
    "optionen": [
      "Kranich",
      "Fasan",
      "Sekretär",
      "Klippschliefer"
    ],
    "antwort": "Kranich"
  },
  {
    "frage": "Welches Tier hat die meisten Zähne?",
    "optionen": [
      "Schnecke",
      "Hai",
      "Krokodil",
      "Piranha"
    ],
    "antwort": "Schnecke"
  },
  {
    "frage": "Welche Vogelart legt die größten Eier im Verhältnis zur Körpergröße?",
    "optionen": [
      "Adler",
      "Kiwi",
      "Pfau",
      "Strauß"
    ],
    "antwort": "Adler"
  },
  {
    "frage": "Welches Tier hat das größte Gehirn im Verhältnis zu seiner Körpergröße?",
    "optionen": [
      "Elefant",
      "Ameise",
      "Delfin",
      "Krake"
    ],
    "antwort": "Krake"
  },
  {
    "frage": "Welches Insekt lebt in Staaten mit einem König statt einer Königin?",
    "optionen": [
      "Ameise",
      "Termite",
      "Biene",
      "Wespe"
    ],
    "antwort": "Termite"
  },
  {
    "frage": "Welches Tier kann eine Geschwindigkeit von über 100 km/h erreichen?",
    "optionen": [
      "Antilope",
      "Strauß",
      "Jaguar",
      "Wanderfalke"
    ],
    "antwort": "Antilope"
  },
  {
    "frage": "Welcher Vogel kann am längsten gleiten, ohne zu fliegen?",
    "optionen": [
      "Seeadler",
      "Albatros",
      "Geier",
      "Fregattvogel"
    ],
    "antwort": "Seeadler"
  },
  {
    "frage": "Welches Reptil kann über seine Haut Wasser aufnehmen?",
    "optionen": [
      "Dornenteufel",
      "Gecko",
      "Chamäleon",
      "Leguan"
    ],
    "antwort": "Dornenteufel"
  },
  {
    "frage": "Welches Tier kann monatelang ohne Nahrung auskommen und extreme Dehydrierung überleben?",
    "optionen": [
      "Kamel",
      "Wüstenfuchs",
      "Skorpion",
      "Tardigrad"
    ],
    "antwort": "Kamel"
  },
  {
    "frage": "Welches Tier hat Zähne auf seiner Zunge?",
    "optionen": [
      "Hai",
      "Schnecke",
      "Seeschnecke",
      "Muschel"
    ],
    "antwort": "Hai"
  },
  {
    "frage": "Wie heißt das einzige giftige Säugetier Europas?",
    "optionen": [
      "Waldmaus",
      "Maulwurf",
      "Wasserspitzmaus",
      "Igel"
    ],
    "antwort": "Waldmaus"
  },
  {
    "frage": "Welches Tier hat die Fähigkeit, sich selbst vollständig zu regenerieren, inklusive Gehirn?",
    "optionen": [
      "Seestern",
      "Planarie",
      "Krake",
      "Axolotl"
    ],
    "antwort": "Seestern"
  },
  {
    "frage": "Welches Land war der Hauptgegner der Alliierten im Pazifikraum während des Zweiten Weltkriegs?",
    "optionen": [
      "China",
      "Sowjetunion",
      "Indien",
      "Japan"
    ],
    "antwort": "Japan"
  },
  {
    "frage": "Welche Stadt wurde 1945 durch die erste Atombombe im Zweiten Weltkrieg zerstört?",
    "optionen": [
      "Hiroshima",
      "Nagasaki",
      "Tokio",
      "Osaka"
    ],
    "antwort": "Hiroshima"
  },
  {
    "frage": "Welche Hochkultur entwickelte die Keilschrift als Schriftsystem?",
    "optionen": [
      "Sumerer",
      "Ägypter",
      "Griechen",
      "Babylonier"
    ],
    "antwort": "Sumerer"
  },
  {
    "frage": "Wer war der letzte Zar von Russland?",
    "optionen": [
      "Nikolaus II.",
      "Peter der Große",
      "Alexander III.",
      "Iwan der Schreckliche"
    ],
    "antwort": "Nikolaus II."
  },
  {
    "frage": "Wer war der erste Präsident der Vereinigten Staaten von Amerika?",
    "optionen": [
      "Thomas Jefferson",
      "George Washington",
      "Abraham Lincoln",
      "John Adams"
    ],
    "antwort": "George Washington"
  },
  {
    "frage": "Welche Stadt war das Zentrum der Renaissance in Italien?",
    "optionen": [
      "Rom",
      "Venedig",
      "Florenz",
      "Mailand"
    ],
    "antwort": "Florenz"
  },
  {
    "frage": "Welche berühmte Schlacht fand 1066 in England statt?",
    "optionen": [
      "Schlacht bei Hastings",
      "Schlacht bei Waterloo",
      "Schlacht am Harzhorn",
      "Schlacht von Agincourt"
    ],
    "antwort": "Schlacht bei Hastings"
  },
  {
    "frage": "Wie hieß das Handelsnetzwerk im Mittelalter, das Ostasien mit Europa verband?",
    "optionen": [
      "Gewürzstraße",
      "Atlantikroute",
      "Seidenstraße",
      "Nordmeerpassage"
    ],
    "antwort": "Gewürzstraße"
  },
  {
    "frage": "Wer war der Anführer der Mongolen während ihrer größten Expansion?",
    "optionen": [
      "Kublai Khan",
      "Dschingis Khan",
      "Tamerlan",
      "Ögedei Khan"
    ],
    "antwort": "Kublai Khan"
  },
  {
    "frage": "Wann begann der Zweite Weltkrieg?",
    "optionen": [
      "1939",
      "1941",
      "1933",
      "1945"
    ],
    "antwort": "1939"
  },
  {
    "frage": "Wann begann der Bau der Berliner Mauer?",
    "optionen": [
      "1949",
      "1961",
      "1989",
      "1953"
    ],
    "antwort": "1961"
  },
  {
    "frage": "Wann fand die Berliner Luftbrücke statt?",
    "optionen": [
      "1947",
      "1949",
      "1948-1949",
      "1950"
    ],
    "antwort": "1947"
  },
  {
    "frage": "Wann wurde die Berliner Mauer geöffnet?",
    "optionen": [
      "1985",
      "1987",
      "1991",
      "1989"
    ],
    "antwort": "1989"
  },
  {
    "frage": "Welches Abkommen führte zur Teilung Deutschlands nach dem Zweiten Weltkrieg?",
    "optionen": [
      "Münchner Abkommen",
      "Potsdamer Abkommen",
      "Versailler Vertrag",
      "Jalta-Konferenz"
    ],
    "antwort": "Münchner Abkommen"
  },
  {
    "frage": "Wer entdeckte den Seeweg nach Indien um das Kap der Guten Hoffnung?",
    "optionen": [
      "Christoph Kolumbus",
      "Ferdinand Magellan",
      "Vasco da Gama",
      "James Cook"
    ],
    "antwort": "Christoph Kolumbus"
  },
  {
    "frage": "Welches Ereignis markierte das Ende der Antike?",
    "optionen": [
      "Der Tod Julius Caesars",
      "Der Fall Roms 476 n. Chr.",
      "Die Schlacht von Actium",
      "Der Beginn der Kreuzzüge"
    ],
    "antwort": "Der Tod Julius Caesars"
  },
  {
    "frage": "Welcher Herrscher gilt als Begründer des Heiligen Römischen Reiches?",
    "optionen": [
      "Karl der Große",
      "Otto II.",
      "Otto I.",
      "Friedrich Barbarossa"
    ],
    "antwort": "Karl der Große"
  },
  {
    "frage": "Welcher Vertrag beendete den Ersten Weltkrieg offiziell?",
    "optionen": [
      "Versailler Vertrag",
      "Friedensvertrag von Brest-Litowsk",
      "Münchner Abkommen",
      "Genfer Konvention"
    ],
    "antwort": "Versailler Vertrag"
  },
  {
    "frage": "Welcher deutsche Staatsmann wurde als 'Eiserner Kanzler' bezeichnet?",
    "optionen": [
      "Wilhelm II.",
      "Friedrich III.",
      "Ludwig II.",
      "Otto von Bismarck"
    ],
    "antwort": "Wilhelm II."
  },
  {
    "frage": "Was war das Hauptziel der Kreuzzüge im Mittelalter?",
    "optionen": [
      "Förderung des Handels",
      "Entdeckung neuer Gebiete",
      "Verbreitung des Christentums",
      "Rückeroberung des Heiligen Landes von den Muslimen"
    ],
    "antwort": "Förderung des Handels"
  },
  {
    "frage": "Wer ist der Sänger der Band Die Ärzte?",
    "optionen": [
      "Campino",
      "Farin Urlaub",
      "Bela B",
      "Rodriguez"
    ],
    "antwort": "Campino"
  },
  {
    "frage": "Wie heißt das Musikfestival, das jährlich in Wacken, Schleswig-Holstein, stattfindet und als eines der größten Heavy-Metal-Festivals der Welt gilt?",
    "optionen": [
      "Rock am Ring",
      "Hurricane Festival",
      "Wacken Open Air",
      "Southside Festival"
    ],
    "antwort": "Rock am Ring"
  },
  {
    "frage": "Welcher Song von Michael Jackson, bekannt für sein ikonisches Musikvideo, war in den 80ern ein Riesenerfolg in Deutschland?",
    "optionen": [
      "Thriller",
      "Billie Jean",
      "Bad",
      "Beat It"
    ],
    "antwort": "Thriller"
  },
  {
    "frage": "Welche Künstlerin performte den Titelsong zur deutschen Netflix-Serie 'How to Sell Drugs Online (Fast)'?",
    "optionen": [
      "Nina Chuba",
      "Loredana",
      "Juju",
      "Katja Krasavice"
    ],
    "antwort": "Nina Chuba"
  },
  {
    "frage": "Welche deutsche Band feierte in den letzten Jahren große Erfolge mit Indie-Pop-Songs wie 'Leiser'?",
    "optionen": [
      "AnnenMayKantereit",
      "Von Wegen Lisbeth",
      "Provinz",
      "Kraftklub"
    ],
    "antwort": "AnnenMayKantereit"
  },
  {
    "frage": "Welches Instrument spielte Udo Lindenberg hauptsächlich?",
    "optionen": [
      "Schlagzeug",
      "Gitarre",
      "Klavier",
      "Bassgitarre"
    ],
    "antwort": "Schlagzeug"
  },
  {
    "frage": "Welcher Song von Provinz war in den Charts erfolgreich und handelt von einer bestimmten Person?",
    "optionen": [
      "Hymne",
      "Tessa",
      "Was Besseres",
      "Tanz für mich"
    ],
    "antwort": "Hymne"
  },
  {
    "frage": "Welche deutsche Sängerin, auch bekannt als Moderatorin, hatte einen Hit mit 'Wir beide'?",
    "optionen": [
      "Helene Fischer",
      "Michelle",
      "Sarah Connor",
      "Lena Meyer-Landrut"
    ],
    "antwort": "Helene Fischer"
  },
  {
    "frage": "Welches Lied von Kraftwerk ist bekannt für seinen minimalistischen und elektronischen Klang und gilt als wegweisend für die elektronische Musik?",
    "optionen": [
      "Autobahn",
      "Radioactivity",
      "Trans-Europa Express",
      "Das Model"
    ],
    "antwort": "Autobahn"
  },
  {
    "frage": "Welche deutsche Band kombiniert Metal mit mittelalterlichen Einflüssen und verwendet oft Dudelsäcke und Drehleiern?",
    "optionen": [
      "Rammstein",
      "In Extremo",
      "Oomph!",
      "Die Apokalyptischen Reiter"
    ],
    "antwort": "Rammstein"
  },
  {
    "frage": "Von welchem Künstler stammt der Song 'Vermissen' featuring Henning May?",
    "optionen": [
      "Quadro",
      "Trettmann",
      "Juju",
      "Sido"
    ],
    "antwort": "Quadro"
  },
  {
    "frage": "Wer sang über viele Jahre das Titellied der deutschen Fernsehserie 'Tatort'?",
    "optionen": [
      "Klaus Lage",
      "Peter Maffay",
      "Herbert Grönemeyer",
      "Udo Lindenberg"
    ],
    "antwort": "Klaus Lage"
  },
  {
    "frage": "Wie heißt das aktuelle Album von Kontra K (Stand 2025)?",
    "optionen": [
      "Erde & Knochen",
      "Blut & Glorie",
      "Aus dem Licht in den Schatten zurück",
      "Vollmond"
    ],
    "antwort": "Erde & Knochen"
  },
  {
    "frage": "Welcher deutsche Pianist und Komponist ist bekannt für seine Interpretationen von Bach?",
    "optionen": [
      "Wilhelm Kempff",
      "Lang Lang",
      "Daniel Barenboim",
      "Alfred Brendel"
    ],
    "antwort": "Wilhelm Kempff"
  },
  {
    "frage": "Welche Band veröffentlichte das Album 'Mutter'?",
    "optionen": [
      "Die Ärzte",
      "Tokio Hotel",
      "Rammstein",
      "Nena"
    ],
    "antwort": "Die Ärzte"
  },
  {
    "frage": "Unter welchem Künstlernamen ist der deutsche Sänger Marius Müller-Westernhagen auch bekannt?",
    "optionen": [
      "Quadro",
      "Westernhagen",
      "Müller",
      "Marius"
    ],
    "antwort": "Quadro"
  },
  {
    "frage": "Welches Passwort würde unser IT-Team NIEMALS erlauben?",
    "optionen": [
      "123456",
      "qwertz",
      "passwort",
      "iloveexcel"
    ],
    "antwort": "123456"
  },
  {
    "frage": "Was sollte man bei uns in der Büroküche lieber lassen?",
    "optionen": [
      "Kaffee kochen",
      "Spülmaschine einräumen",
      "Klatsch und Tratsch",
      "Fisch aufwärmen"
    ],
    "antwort": "Kaffee kochen"
  },
  {
    "frage": "Wer kommt fast immer als Letzter zum Meeting?",
    "optionen": [
      "Sandra",
      "Tobi",
      "Nina",
      "Tom"
    ],
    "antwort": "Sandra"
  },
  {
    "frage": "Wer hat einmal aus Versehen ein GIF in die Kundengruppe geschickt?",
    "optionen": [
      "Stefan",
      "Caro",
      "Nico",
      "Niemand… offiziell"
    ],
    "antwort": "Stefan"
  },
  {
    "frage": "Was war unser chaotischstes Team-Event bisher?",
    "optionen": [
      "Bowling-Nachmittag",
      "Online Pub Quiz",
      "Wanderung ohne Karte",
      "Weihnachtswichteln mit falschem Budget"
    ],
    "antwort": "Bowling-Nachmittag"
  },
  {
    "frage": "Wer hat einen persönlichen Reminder im Kalender mit dem Titel 'Pause machen, verdammt nochmal!'?",
    "optionen": [
      "Marie",
      "Benedikt",
      "Laura",
      "Sebastian"
    ],
    "antwort": "Marie"
  },
  {
    "frage": "Wer bringt regelmäßig Kuchen mit, ohne Anlass?",
    "optionen": [
      "Jan",
      "Miriam",
      "Kerstin",
      "Dominik"
    ],
    "antwort": "Jan"
  },
  {
    "frage": "Was passiert meistens, wenn alle im Homeoffice sind?",
    "optionen": [
      "Totale Ruhe",
      "Plötzlich Teams-Calls ohne Ende",
      "Kühlschrank wird geplündert",
      "Niemand antwortet mehr auf Slack"
    ],
    "antwort": "Totale Ruhe"
  },
  {
    "frage": "Was würde passieren, wenn wir Max einen Tag Chef sein lassen?",
    "optionen": [
      "Alle würden früher gehen",
      "Meetings würden durch Karaoke ersetzt",
      "Slack wird gelöscht",
      "Homeoffice-Pflicht für immer"
    ],
    "antwort": "Alle würden früher gehen"
  },
  {
    "frage": "Welches Emoji benutzen wir am häufigsten in unserem Teamchat?",
    "optionen": [
      "🔥",
      "🎉",
      "👍",
      "🙈"
    ],
    "antwort": "🔥"
  },
  {
    "frage": "Welche Teambuilding-Aktion fanden wir letztes Jahr am besten?",
    "optionen": [
      "Online-Yoga",
      "Escape Room",
      "Pub Quiz",
      "Kuchen-Wettbewerb"
    ],
    "antwort": "Online-Yoga"
  },
  {
    "frage": "Was passiert fast immer, wenn Heinz 'nur kurz was zeigen will'?",
    "optionen": [
      "Er zeigt es schnell und geht",
      "Es dauert 30 Minuten",
      "Wir sind am Ende alle verwirrt",
      "Der Beamer stürzt ab"
    ],
    "antwort": "Er zeigt es schnell und geht"
  },
  {
    "frage": "Wer schrieb die 'Harry Potter'-Buchreihe?",
    "optionen": [
      "J.R.R. Tolkien",
      "J.K. Rowling",
      "Stephen King",
      "George R.R. Martin"
    ],
    "antwort": "J.R.R. Tolkien"
  },
  {
    "frage": "Welches Bier hat den höchsten Alkoholgehalt der Welt?",
    "optionen": [
      "Westvleteren 12",
      "Utopias von Samuel Adams",
      "Snake Venom",
      "Tactical Nuclear Penguin"
    ],
    "antwort": "Snake Venom"
  },
  {
    "frage": "In welchem Jahr wurde die Europäische Union gegründet?",
    "optionen": [
      "1990",
      "1991",
      "1992",
      "1993"
    ],
    "antwort": "1993"
  },
  {
    "frage": "Wer war der erste Bundeskanzler der Bundesrepublik Deutschland?",
    "optionen": [
      "Willy Brandt",
      "Ludwig Erhard",
      "Konrad Adenauer",
      "Helmut Schmidt"
    ],
    "antwort": "Konrad Adenauer"
  },
  {
    "frage": "Welcher Champagner wird traditionell bei der Formel-1-Siegerehrung gesprüht?",
    "optionen": [
      "Moët & Chandon",
      "Dom Pérignon",
      "Krug",
      "Veuve Clicquot"
    ],
    "antwort": "Moët & Chandon"
  },
  {
    "frage": "Welches der sieben Weltwunder der Antike steht noch heute?",
    "optionen": [
      "Hängende Gärten von Babylon",
      "Koloss von Rhodos",
      "Leuchtturm von Alexandria",
      "Pyramiden von Gizeh"
    ],
    "antwort": "Pyramiden von Gizeh"
  },
  {
    "frage": "Welche Sprache wird in Brasilien hauptsächlich gesprochen?",
    "optionen": [
      "Spanisch",
      "Französisch",
      "Portugiesisch",
      "Italienisch"
    ],
    "antwort": "Spanisch"
  },
  {
    "frage": "Wie heißt der Mars-Rover, der 2021 auf dem Mars gelandet ist?",
    "optionen": [
      "Curiosity",
      "Perseverance",
      "Opportunity",
      "Spirit"
    ],
    "antwort": "Curiosity"
  },
  {
    "frage": "Welcher deutsche Dichter schrieb 'Faust'?",
    "optionen": [
      "Johann Wolfgang von Goethe",
      "Friedrich Schiller",
      "Heinrich Heine",
      "Gotthold Ephraim Lessing"
    ],
    "antwort": "Johann Wolfgang von Goethe"
  },
  {
    "frage": "Welches Unternehmen entwickelte das erste kommerzielle Smartphone?",
    "optionen": [
      "Apple",
      "Nokia",
      "IBM",
      "Motorola"
    ],
    "antwort": "Apple"
  },
  {
    "frage": "Welche Band sang 'Hotel California'?",
    "optionen": [
      "Fleetwood Mac",
      "Eagles",
      "Led Zeppelin",
      "Pink Floyd"
    ],
    "antwort": "Fleetwood Mac"
  },
  {
    "frage": "Wie viele Mitgliedstaaten hat die NATO derzeit (2025)?",
    "optionen": [
      "28",
      "29",
      "30",
      "32"
    ],
    "antwort": "28"
  },
  {
    "frage": "Wie nennt man die traditionellen deutschen Weihnachtspyramiden?",
    "optionen": [
      "Weihnachtstürme",
      "Adventspyramiden",
      "Weihnachtspyramiden",
      "Kerzenpyramiden"
    ],
    "antwort": "Weihnachtspyramiden"
  },
  {
    "frage": "Was ist eine 'Feuerzangenbowle'?",
    "optionen": [
      "Ein Weihnachtsgebäck",
      "Ein Weihnachtsmarkt-Spiel",
      "Ein alkoholisches Heißgetränk mit brennendem Zuckerhut",
      "Eine Art Glühwein mit Früchten"
    ],
    "antwort": "Ein alkoholisches Heißgetränk mit brennendem Zuckerhut"
  },
  {
    "frage": "Was ist die meistverkaufte Weihnachtsbaumart in den Niederlanden und Belgien?",
    "optionen": [
      "Fichte",
      "Nordmanntanne",
      "Chinesische Hatschie-Tanne",
      "Blautanne"
    ],
    "antwort": "Fichte"
  },
  {
    "frage": "Welche Wurst wird traditionell mit Kartoffelsalat an Heiligabend gegessen?",
    "optionen": [
      "Bratwurst",
      "Wiener Würstchen",
      "Currywurst",
      "Weißwurst"
    ],
    "antwort": "Bratwurst"
  },
  {
    "frage": "Was ist eigentlich gar kein Weihnachtslied?",
    "optionen": [
      "Jingle Bells",
      "Last Christmas",
      "All I Want for Christmas Is You",
      "Stille Nacht"
    ],
    "antwort": "Jingle Bells"
  },
  {
    "frage": "Wenn du mit jemandem unter einem Mistelzweig stehst zu Weihnachten, was bedeutet das?",
    "optionen": [
      "Dass ihr euch küssen dürft",
      "7 Jahre gemeinsames Glück",
      "Finanzieller Wohlstand für beide",
      "Ihr dürft zusammen 3 Wünsche äußern"
    ],
    "antwort": "Dass ihr euch küssen dürft"
  },
  {
    "frage": "Welche Pflanze wird auch 'Weihnachtsstern' genannt?",
    "optionen": [
      "Stechpalme",
      "Mistelzweig",
      "Efeu",
      "Poinsettie"
    ],
    "antwort": "Stechpalme"
  },
  {
    "frage": "Wie heißt das traditionelle deutsche Weihnachtsgebäck mit Mandeln?",
    "optionen": [
      "Lebkuchen",
      "Stollen",
      "Spekulatius",
      "Pfefferkuchen"
    ],
    "antwort": "Lebkuchen"
  },
  {
    "frage": "Wie sagt man 'Frohe Weihnachten' auf Spanisch?",
    "optionen": [
      "Buon Natale",
      "Fén fistdaoge",
      "Feliz Natal",
      "Feliz Navidad"
    ],
    "antwort": "Buon Natale"
  },
  {
    "frage": "In welchem Land begann der Brauch, Weihnachtskarten zu versenden?",
    "optionen": [
      "Deutschland",
      "Vereinigte Staaten",
      "England",
      "Frankreich"
    ],
    "antwort": "Deutschland"
  },
  {
    "frage": "Welche Fleischspeise ist ein Klassiker am deutschen Weihnachtstisch?",
    "optionen": [
      "Schweinebraten",
      "Gänsebraten",
      "Sauerbraten",
      "Rinderbraten"
    ],
    "antwort": "Schweinebraten"
  },
  {
    "frage": "Wie heißt der berühmteste Weihnachtsmarkt Deutschlands?",
    "optionen": [
      "Dresdner Striezelmarkt",
      "Kölner Weihnachtsmarkt",
      "Münchner Christkindlmarkt",
      "Nürnberger Christkindlmarkt"
    ],
    "antwort": "Dresdner Striezelmarkt"
  },
  {
    "frage": "In welcher deutschen Serie spielt Kida Khodr Ramadan einen Clan-Chef in Berlin-Neukölln?",
    "optionen": [
      "Dogs of Berlin",
      "4 Blocks",
      "Luden",
      "Knallerfrauen"
    ],
    "antwort": "Dogs of Berlin"
  },
  {
    "frage": "Welche deutsche Serie, die auf einem Roman basiert, zeigt eine junge Frau, die in einem parfümbezogenen Kriminalfall ermittelt?",
    "optionen": [
      "Liebes Kind",
      "Parfum",
      "Dark",
      "Bad Banks"
    ],
    "antwort": "Liebes Kind"
  },
  {
    "frage": "Welche Schauspielerin spielt die Hauptrolle in der deutschen Miniserie 'Unorthodox' über eine Frau, die aus einer chassidischen Gemeinde flieht?",
    "optionen": [
      "Shira Haas",
      "Liv Lisa Fries",
      "Lisa Vicari",
      "Marleen Lohse"
    ],
    "antwort": "Shira Haas"
  },
  {
    "frage": "Welche deutsche Serie zeigt eine dystopische Zukunft, in der drei Geschwister nach einem globalen Blackout überleben müssen?",
    "optionen": [
      "Dark",
      "Tribes of Europa",
      "Biohackers",
      "Parfum"
    ],
    "antwort": "Dark"
  },
  {
    "frage": "Welche österreichische Serie auf Netflix folgt einer Familie, die nach einem Flugzeugabsturz in den Alpen überlebt?",
    "optionen": [
      "Die Toten vom Bodensee",
      "Altes Geld",
      "Vorstadtweiber",
      "SOKO Wien"
    ],
    "antwort": "Die Toten vom Bodensee"
  },
  {
    "frage": "Welcher Schauspieler spielt die Hauptrolle in der deutschen Neuverfilmung von 'Im Westen nichts Neues' aus 2022?",
    "optionen": [
      "Volker Bruch",
      "Jannis Niewöhner",
      "Felix Kammerer",
      "Tom Schilling"
    ],
    "antwort": "Volker Bruch"
  },
  {
    "frage": "Welcher Film gewann den Goldenen Bären auf der Berlinale 2025?",
    "optionen": [
      "Oslo Stories: Träume",
      "The Blue Trail",
      "If I Had Legs I’d Kick You",
      "Das Licht"
    ],
    "antwort": "Oslo Stories: Träume"
  },
  {
    "frage": "Welche Schauspielerin spielte die Hauptrolle in 'Frühstück bei Tiffany'?",
    "optionen": [
      "Audrey Hepburn",
      "Marilyn Monroe",
      "Grace Kelly",
      "Elizabeth Taylor"
    ],
    "antwort": "Audrey Hepburn"
  },
  {
    "frage": "Welche deutsche Serie, die in Hamburg spielt, zeigt das Leben eines Stand-up-Comedians und seiner Freunde?",
    "optionen": [
      "Luden",
      "Dogs of Berlin",
      "4 Blocks",
      "How to Sell Drugs Online (Fast)"
    ],
    "antwort": "Luden"
  },
  {
    "frage": "Welche deutsche Serie, die in Köln spielt, erzählt die Geschichte einer Anwältin, die in die Welt der organisierten Kriminalität gerät?",
    "optionen": [
      "4 Blocks",
      "Dreißig Tage",
      "Tatort",
      "Skyline"
    ],
    "antwort": "4 Blocks"
  },
  {
    "frage": "Welche britische Schauspielerin erhielt den Goldenen Ehrenbären für ihr Lebenswerk auf der Berlinale 2025?",
    "optionen": [
      "Kate Winslet",
      "Emma Thompson",
      "Tilda Swinton",
      "Judi Dench"
    ],
    "antwort": "Kate Winslet"
  },
  {
    "frage": "Welcher deutsche Film von 2023 mit Sandra Hüller wurde für den Oscar als bester internationaler Film nominiert?",
    "optionen": [
      "Toni Erdmann",
      "Das Lehrerzimmer",
      "Anatomie eines Falls",
      "Die Fabelmans"
    ],
    "antwort": "Toni Erdmann"
  },
  {
    "frage": "Welche Serie, die in Berlin spielt, zeigt einen jungen Mann, der als Drogendealer in die kriminelle Unterwelt gerät?",
    "optionen": [
      "4 Blocks",
      "Dogs of Berlin",
      "How to Sell Drugs Online (Fast)",
      "Luden"
    ],
    "antwort": "4 Blocks"
  },
  {
    "frage": "Welcher Schauspieler spielte die Hauptrolle in 'Forrest Gump'?",
    "optionen": [
      "Tom Hanks",
      "Brad Pitt",
      "Johnny Depp",
      "Leonardo DiCaprio"
    ],
    "antwort": "Tom Hanks"
  },
  {
    "frage": "Welche Serie, die in Hamburgs Rotlichtviertel St. Pauli spielt, erzählt die Geschichte der 'Nutella-Bande'?",
    "optionen": [
      "Knallerfrauen",
      "Der Tatortreiniger",
      "Luden",
      "Liebes Kind"
    ],
    "antwort": "Knallerfrauen"
  },
  {
    "frage": "Welche österreichische Serie, die in Wien spielt, zeigt eine Gruppe von Frauen, die mit Intrigen und Geheimnissen konfrontiert sind?",
    "optionen": [
      "Vorstadtweiber",
      "Sisi",
      "Die Toten vom Bodensee",
      "M – Eine Stadt sucht einen Mörder"
    ],
    "antwort": "Vorstadtweiber"
  },
  {
    "frage": "Welcher Schauspieler ist bekannt für seine Rolle als Kommissar Thiel in der deutschen Krimiserie 'Tatort' aus Münster?",
    "optionen": [
      "Til Schweiger",
      "Jan Josef Liefers",
      "Axel Prahl",
      "Klaus J. Behrendt"
    ],
    "antwort": "Til Schweiger"
  },
  {
    "frage": "Welche Schweizer Serie kombiniert Krimi und Humor in einer Kleinstadt in Graubünden?",
    "optionen": [
      "Wilder",
      "Quartier des Banques",
      "Tschugger",
      "Der Pass"
    ],
    "antwort": "Wilder"
  },
  {
    "frage": "Welche österreichische Netflix-Serie porträtiert Sigmund Freud als Detektiv in einem Mystery-Thriller?",
    "optionen": [
      "Freud",
      "Der Pass",
      "Tribes of Europa",
      "Das Boot"
    ],
    "antwort": "Freud"
  },
  {
    "frage": "Welche deutsche Serie, die in München spielt, zeigt eine junge Frau, die als Hackerin für einen Geheimdienst arbeitet?",
    "optionen": [
      "Deutschland 89",
      "Bad Banks",
      "Parfum",
      "You Are Wanted"
    ],
    "antwort": "You Are Wanted"
  },
  {
    "frage": "Welcher Film zeigt eine Gruppe von Freunden, die ein mysteriöses Brettspiel spielen, das die Realität verändert?",
    "optionen": [
      "Die unendliche Geschichte",
      "Labyrinth",
      "Der goldene Kompass",
      "Jumanji"
    ],
    "antwort": "Die unendliche Geschichte"
  },
  {
    "frage": "Welcher türkische Regisseur wurde beim Berlinale Co-Production Market 2025 für sein Projekt 'Dreamgirl' mit dem ARTEKino International Award ausgezeichnet?",
    "optionen": [
      "Kaan Müjdeci",
      "Ayşe Polat",
      "Wissam Charaf",
      "Zarrar Kahn"
    ],
    "antwort": "Kaan Müjdeci"
  },
  {
    "frage": "Welcher Schauspieler, bekannt aus 'Germany’s Next Topmodel', war 2025 Gast auf dem Finale der Show in Köln?",
    "optionen": [
      "Daniel Brühl",
      "Elyas M’Barek",
      "Heidi Klum",
      "Moritz Bleibtreu"
    ],
    "antwort": "Daniel Brühl"
  },
  {
    "frage": "Welche Schweizer Serie, die in Genf spielt, zeigt eine Bankerin, die in einen internationalen Finanzskandal verwickelt ist?",
    "optionen": [
      "Tschugger",
      "Quartier des Banques",
      "Wilder",
      "Der Pass"
    ],
    "antwort": "Tschugger"
  },
  {
    "frage": "Welcher Wein wird aus der Traubensorte Pinot Noir hergestellt und ist berühmt in der Region Burgund?",
    "optionen": [
      "Roter Burgunder",
      "Chardonnay",
      "Beaujolais",
      "Sauvignon Blanc"
    ],
    "antwort": "Roter Burgunder"
  },
  {
    "frage": "Welches Schweizer Gericht wird aus geriebenen Kartoffeln zubereitet und in der Pfanne knusprig gebraten?",
    "optionen": [
      "Fondue",
      "Raclette",
      "Rösti",
      "Älplermagronen"
    ],
    "antwort": "Fondue"
  },
  {
    "frage": "Welches ist ein typisches Schweizer Gericht aus Fleisch und Soße?",
    "optionen": [
      "Fondue",
      "Zürcher Geschnetzeltes",
      "Raclette",
      "Älplermagronen"
    ],
    "antwort": "Fondue"
  },
  {
    "frage": "Welches ist ein traditionelles österreichisches Gericht aus Kalbfleisch und Rahm?",
    "optionen": [
      "Tafelspitz",
      "Gulasch",
      "Kalbsrahmgulasch",
      "Wiener Schnitzel"
    ],
    "antwort": "Tafelspitz"
  },
  {
    "frage": "Welche Traube ist die Hauptsorte für den österreichischen Grünern Veltliner?",
    "optionen": [
      "Veltliner",
      "Riesling",
      "Chardonnay",
      "Sauvignon Blanc"
    ],
    "antwort": "Veltliner"
  },
  {
    "frage": "Welches österreichische Gericht besteht aus dünnen Scheiben rohem Rindfleisch, die mit einer Soße aus Kapern, Zwiebeln und Senf serviert werden?",
    "optionen": [
      "Tafelspitz",
      "Beef Tatar",
      "Gulasch",
      "Sachertorte"
    ],
    "antwort": "Tafelspitz"
  },
  {
    "frage": "Welches ist ein traditionelles Schweizer Dessert aus Eiern, Milch und Zucker?",
    "optionen": [
      "Tiramisu",
      "Mousse au Chocolat",
      "Zuger Kirschtorte",
      "Crème Brûlée"
    ],
    "antwort": "Tiramisu"
  },
  {
    "frage": "Welches ist ein traditionelles deutsches Gericht aus Fleisch und Kohl?",
    "optionen": [
      "Sauerkraut mit Würstchen",
      "Kohlrouladen",
      "Kassler mit Kraut",
      "Eintopf mit Kohl"
    ],
    "antwort": "Sauerkraut mit Würstchen"
  },
  {
    "frage": "Welches deutsche Brot ist für seine dunkle Farbe und seinen leicht süßlichen Geschmack bekannt?",
    "optionen": [
      "Baguette",
      "Ciabatta",
      "Weißbrot",
      "Pumpernickel"
    ],
    "antwort": "Baguette"
  },
  {
    "frage": "Welches Gericht besteht aus dünnen Scheiben rohem Fleisch oder Fisch, oft serviert mit einer Soße?",
    "optionen": [
      "Gulasch",
      "Paella",
      "Carpaccio",
      "Risotto"
    ],
    "antwort": "Gulasch"
  },
  {
    "frage": "Welches ist ein typisches deutsches Gericht aus Fleisch in Gelee?",
    "optionen": [
      "Sülze",
      "Pressack",
      "Blutwurst",
      "Leberwurst"
    ],
    "antwort": "Sülze"
  },
  {
    "frage": "Welches ist ein typisches deutsches Gericht aus Kartoffeln und Speck?",
    "optionen": [
      "Bauernfrühstück",
      "Kartoffelsalat",
      "Bratkartoffeln",
      "Kartoffelpüree"
    ],
    "antwort": "Bauernfrühstück"
  },
  {
    "frage": "Welches ist ein typisches Schweizer Dessert aus Schokolade und Sahne?",
    "optionen": [
      "Tiramisu",
      "Mousse au Chocolat",
      "Zuger Kirschtorte",
      "Crème Brûlée"
    ],
    "antwort": "Tiramisu"
  },
  {
    "frage": "Welches ist ein typisches deutsches Weihnachtsgebäck?",
    "optionen": [
      "Lebkuchen",
      "Croissant",
      "Baguette",
      "Muffin"
    ],
    "antwort": "Lebkuchen"
  },
  {
    "frage": "Aus welcher Region Deutschlands stammt der Riesling ursprünglich?",
    "optionen": [
      "Baden-Württemberg",
      "Rheingau",
      "Bayern",
      "Sachsen"
    ],
    "antwort": "Baden-Württemberg"
  },
  {
    "frage": "Welches Land ist der Ursprung des Gerichts 'Feijoada', ein Eintopf aus schwarzen Bohnen und Fleisch?",
    "optionen": [
      "Spanien",
      "Mexiko",
      "Portugal",
      "Brasilien"
    ],
    "antwort": "Spanien"
  },
  {
    "frage": "Welches ist ein typisches Schweizer Gericht aus Kartoffeln und Käse?",
    "optionen": [
      "Fondue",
      "Raclette",
      "Älplermagronen",
      "Rösti"
    ],
    "antwort": "Fondue"
  },
  {
    "frage": "Welches ist ein typisches österreichisches Gericht aus Topfen?",
    "optionen": [
      "Apfelstrudel",
      "Sachertorte",
      "Kaiserschmarrn",
      "Topfennockerl"
    ],
    "antwort": "Apfelstrudel"
  },
  {
    "frage": "Welches ist ein traditionelles österreichisches Dessert aus Schokolade?",
    "optionen": [
      "Apfelstrudel",
      "Sachertorte",
      "Kaiserschmarrn",
      "Topfennockerl"
    ],
    "antwort": "Apfelstrudel"
  },
  {
    "frage": "Welches ist ein traditionelles Schweizer Gericht aus geschmolzenem Käse?",
    "optionen": [
      "Fondue",
      "Raclette",
      "Rösti",
      "Bündnerfleisch"
    ],
    "antwort": "Fondue"
  },
  {
    "frage": "Welches Getränk ist ein traditioneller österreichischer Digestif aus Kräutern und Gewürzen?",
    "optionen": [
      "Schnaps",
      "Wein",
      "Unterberger",
      "Bier"
    ],
    "antwort": "Schnaps"
  },
  {
    "frage": "Welcher Wein wird in der Region Bordeaux hauptsächlich aus den Trauben Cabernet Sauvignon und Merlot hergestellt?",
    "optionen": [
      "Chablis",
      "Sauternes",
      "Burgunder",
      "Claret"
    ],
    "antwort": "Chablis"
  },
  {
    "frage": "Welches ist ein traditionelles österreichisches Dessert aus Marillen?",
    "optionen": [
      "Marillenknödel",
      "Apfelstrudel",
      "Kaiserschmarrn",
      "Sachertorte"
    ],
    "antwort": "Marillenknödel"
  },
  {
    "frage": "Welches Gewürz ist ein Hauptbestandteil des indischen Gewürzmischung 'Garam Masala'?",
    "optionen": [
      "Paprika",
      "Kurkuma",
      "Kreuzkümmel",
      "Kardamom"
    ],
    "antwort": "Paprika"
  },
  {
    "frage": "Welche Aussage über lineare Regression ist korrekt?",
    "optionen": [
      "Sie ist nur bei quadratischen Daten sinnvoll",
      "Sie verwendet ausschließlich Mittelwerte",
      "Sie passt immer perfekt auf alle Datenpunkte",
      "Sie versucht, die Summe der Abweichungsquadrate zu minimieren"
    ],
    "antwort": "Sie ist nur bei quadratischen Daten sinnvoll"
  },
  {
    "frage": "Wie lautet die Formel zur Berechnung der Kombinationsanzahl (n über k)?",
    "optionen": [
      "n/k",
      "n! × k!",
      "n! / (k! × (n – k)!)",
      "n × k!"
    ],
    "antwort": "n/k"
  },
  {
    "frage": "Was ist die Matrixtransponierte von [[1,2],[3,4]]?",
    "optionen": [
      "[[1,3],[2,4]]",
      "[[4,2],[3,1]]",
      "[[2,1],[4,3]]",
      "[[3,1],[4,2]]"
    ],
    "antwort": "[[1,3],[2,4]]"
  },
  {
    "frage": "Ein Würfel wird dreimal geworfen. Wie viele mögliche Ergebnisse gibt es?",
    "optionen": [
      "36",
      "2160",
      "128",
      "216"
    ],
    "antwort": "36"
  },
  {
    "frage": "Was ist der Median der Zahlenreihe: 3, 8, 9, 14, 18?",
    "optionen": [
      "8",
      "9,5",
      "9",
      "10"
    ],
    "antwort": "8"
  },
  {
    "frage": "Was bedeutet eine Korrelation von r = –1?",
    "optionen": [
      "Keine Korrelation",
      "Perfekte negative lineare Beziehung",
      "Schwache positive Beziehung",
      "Perfekte Übereinstimmung"
    ],
    "antwort": "Keine Korrelation"
  },
  {
    "frage": "Was ist das Ergebnis von lim(x→0) (sin(x)/x)?",
    "optionen": [
      "1",
      "∞",
      "nicht definiert"
    ],
    "antwort": "1"
  },
  {
    "frage": "Welche Funktion ist keine lineare Funktion?",
    "optionen": [
      "f(x) = 3x + 2",
      "f(x) = x² + 1",
      "f(x) = –5x",
      "f(x) = 0,5x – 3"
    ],
    "antwort": "f(x) = 3x + 2"
  },
  {
    "frage": "Was ist das geometrische Mittel von 4 und 9?",
    "optionen": [
      "8",
      "5",
      "6",
      "√36"
    ],
    "antwort": "6"
  },
  {
    "frage": "Was ergibt (x + 3)²?",
    "optionen": [
      "x² + 6x + 9",
      "x² + 9",
      "x² + 3",
      "x² + 3x + 3"
    ],
    "antwort": "x² + 6x + 9"
  },
  {
    "frage": "Was ist die Umkehrung einer logischen Implikation (A ⇒ B)?",
    "optionen": [
      "¬A ⇒ ¬B",
      "B ⇒ A",
      "A ⇔ B",
      "¬B ⇒ ¬A"
    ],
    "antwort": "¬A ⇒ ¬B"
  },
  {
    "frage": "Ein Datensatz ist rechtsschief. Was bedeutet das?",
    "optionen": [
      "Der Median ist größer als der Mittelwert",
      "Der Modus liegt ganz rechts",
      "Der Mittelwert liegt rechts vom Median",
      "Alle Daten sind gleich verteilt"
    ],
    "antwort": "Der Median ist größer als der Mittelwert"
  }
]"""

  # Session State initialisieren

with st.echo(code_location="below"):
  if "answers" not in st.session_state:
      st.session_state.answers = {}  # Speichert die gewählte Antwort pro Frage-Index

  richtig = 0
  falsch = 0

  quiz_py = json.loads(quiz)

  if "resultate" not in st.session_state:
      st.session_state.resultate = [None] * len(quiz_py)

  anzahl_fragen = st.slider("Wie viel Fragem wilst du beantworten?: ", min_value=1, max_value=len(quiz_py))

  def optionen(i, frage_data):
      global richtig, falsch
      st.write("Das ist Frage", i + 1 ,"von", anzahl_fragen)

      st.write(f"**Robot:** {frage_data['frage']}")
      
      # Prüfen, ob für diese Frage bereits eine Antwort existiert
      hat_geantwortet = i in st.session_state.answers
      
      # Optionen anzeigen (deaktiviert, wenn schon geantwortet wurde)
      options = frage_data["optionen"]
      selection = st.pills(
          "Optionen:", 
          options, 
          selection_mode="single", 
          disabled=hat_geantwortet, 
          key=f"pills_{i}"
      )
      
      # Wenn gerade etwas ausgewählt wurde, im Session State speichern und neu laden
      if selection is not None and not hat_geantwortet:
          st.session_state.answers[i] = selection
          st.rerun()
          
      # Feedback anzeigen basierend auf dem gespeicherten Zustand
      if hat_geantwortet:
          gespeicherte_auswahl = st.session_state.answers[i]
          if gespeicherte_auswahl == frage_data["antwort"]:
              st.success(f"Robot: Richtig!!! Deine Antwort: {gespeicherte_auswahl}")
              richtig += 1
              st.session_state.resultate[i] = 1
          else:
              st.error(f"Robot: Falsch!!! Richtige Antwort wäre: {frage_data['antwort']}")
              falsch += 1
              st.session_state.resultate[i] = -1
              
      st.divider()

  # Quiz-Schleife
  for i, fragen in enumerate(quiz_py):
      if i < anzahl_fragen:
        optionen(i, fragen)

  st.write("Du hast", richtig, "richtig von", len(quiz_py))
  
  def chart():
    df_1 = pd.DataFrame(
        {
            "Wert": ["richtig", "falsch"],
            "Anzahl": [richtig, falsch],
            "col3": ["#FA1414", "#21FF3A"],
        }
    )

    st.bar_chart(df_1, x="Wert", y="Anzahl", color="col3")

    resultate = [r for r in st.session_state.resultate if r is not None]

    df_2 = pd.DataFrame(
        {
            "richtig": resultate,
        }
    )
    df_2["falsch"] = 1 - df_2["richtig"]

    st.area_chart(df_2, color=["#21FF3A", "#FA1414"])

    st.line_chart(df_2, color=["#21FF3A", "#FA1414"])

  if richtig or falsch > 0:
    chart()
  st.divider()