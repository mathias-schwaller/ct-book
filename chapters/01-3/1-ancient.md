---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Antike

Die Geschichte der Computer und Algorithmen beginnt 2700 bis 2400 Jahre vor Christus.
Zu dieser Zeit konstruierten vermutlich die Sumerer das älteste bekannte Rechenhilfsmittel, den Abakus.
Er unterstützte sie bei der Addition, Subtraktion, Multiplikation und Division ganzer Zahlen.
Ziel war es Rechenfehler bei einfachen Berechnungen zu verhindern.

Über zweitausend Jahre später erschufen die antiken Griechen eine Art mechanisch-analogen Computer---eine ganz erstaunliche Leistung, die für die kommenden tausend Jahre einzigartig bleiben sollte.
Dieser antike Computer war dazu gedacht, bestimmte Positionen der Himmelskörper zu bestimmen---schon immer wurden wir Menschen von der Frage nach unserem Platz und unserer Bedeutung im Universum angetrieben.

```{figure} ../../figs/history/greeks.png
---
height: 150px
name: greeks
---
Denker*innen Ihrer Zeit: Euklid, Eratosthenes, Hypatia, Quellen: [2](https://en.wikipedia.org/wiki/File:Eratosthene.01.png), [3](https://commons.wikimedia.org/wiki/File:Hypatia_portrait.png).
```

Sumerer, Ägypter, Babylonier, Chinesen, Griechen und andere antike Völker entwickelten Rechenhilfsmittel um insbesondere die Bewegung der Himmelskörper besser zu bestimmen und zu verstehen.
In Alexandria bildete sich das Zentrum der damaligen Wissenschaft.
Es wurden große Anstrengungen unternommen um das Wissen der damals bekannten Welt zu sammeln und zu erweitern.
Bücher von Reisenden wurden händisch kopiert.
Schiffe, die im Hafen ankerten, wurden nach neuen Mitschriften durchsucht.
In der Agora wurde rege über die Laufbahn der Himmelskörper, geometrische Körper und besondere Zahlen diskutiert.

```{figure} ../../figs/history/earth-curvature.png
---
width: 600px
name: fig-earth-curvature
---
Eratosthenes und die Erdkrümmung.
```

Eratosthenes (276 v. Chr. - 194 v. Chr.) war einer der herausragenden Denker dieser Zeit und zugleich Leiter der Bibliothek in Alexandria.
Eines Tages, so erzählt man sich, machte er eine herausragende Entdeckung:
Er beobachtet, dass zur gleichen Zeit zwei Obelisken an verschiedenen Orten unterschiedlich lange Schatten auf die Erde werfen.
Erstaunlicherweise schloss er daraus auf die Krümmung der Erde.
Und, da die Griechen von der Perfektion des Kreises überzeugt waren, folgerte Eratosthenes, dass die Erde eine Kugel sei.
Er war sogar in der Lage die Erdkrümmung relativ genau zu berechnen und dadurch auf den Umfang der Erde zu schließen.
Um seine Berechnungen durchführen zu können bediente er sich vermutlich eines menschlichen Computers, der ihm die Strecke zwischen Alexandria und Syren (ca. 800 km) ablief und berechnete.

```{code-cell} python3
---
tags: [output_scroll]
---
def sieve_of_eratosthenes(N):
    """
    Returns a list of all prime numbers p in ascending order with p < N.
    """
    N = 100
    prime_sieve = [True for i in range(N)]
    prime_sieve[0] = False
    prime_sieve[1] = False
    for i in range(2, int(N**0.5)):
        if prime_sieve[i]:
            for j in range(i**2, N, i):
                prime_sieve[j] = False
    
    primes = []
    for i in range(N):
        if prime_sieve[i]:
            primes.append(i)
    return primes
        
sieve_of_eratosthenes(100)
```

Wir finden also bereits zu dieser Zeit erste Beispiele für eine computergestützte Forschung.
Für lästige und primitive Berechnungen begann man Computer zu beauftragen.
Der Begriff *Computer* sollte lange Zeit auf eine Person anstatt auf eine Maschine hindeuten.
So wurden bis Ende des zweiten Weltkrieg menschliche Computer mit Berechnungen beauftragt.
Oftmals wurde diese Aufgabe von schlecht bezahlten Frauen durchgeführt.
Das zeigt zum einen die geringe Wertschätzung der von Frauen verrichteten Arbeit, wie auch den Stellenwert der Computer.

Zur Zeit der antiken Griechen begann man die ersten uns überlieferten Algorithmen zu entwickeln.
Nach Eratosthenes ist einer der ersten Algorithmen überhaupt benannt: der [Sieb des Eratosthenes](https://de.wikipedia.org/wiki/Sieb_des_Eratosthenes).
Es ist eine clevere Technik um Primzahlen zu berechnen.

```{figure} ../../figs/history/the-elements.jpg
---
height: 150px
name: fig-euklid-elements
---
Ein Fragment der Werke *Die Elemente*, [Quelle](http://www.math.ubc.ca/~cass/Euclid/papyrus/papyrus.html).
```

Doch noch vor Eratosthenes, notierte Euklid von Alexandria (ca 450 v. Chr. - Mitte 350 v. Chr.) in seinem Werk *Die Elemente*, einen Algorithmus für die Berechnung des größten gemeinsamen Teilers ``gcd(a,b)`` zweier natürlicher Zahlen ``a``, ``b``.
Über zweitausend Jahre später finden wir jene Algorithmen in einer anderen Form wieder.

```{code-cell} python3
def gcd(a,b):
    """
    Returns the greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return a

gcd(36, 24)
```

>[The Euclidean algorithm] is the granddaddy of all algorithms, because it is the oldest nontrivial algorithm that has survived to the present day. -- Donald Knuth, The Art of Computer Programming, Vol 2.

Als die praktische Anwendung der Algorithmen gängiger wurde, kamen grundlegende Fragen auf:
Was können wir überhaupt alles berechnen?
Welche fundamentalen Operationen benötigt eine Maschine um all das berechnen zu können was wir im allgemeinen berechnen können?
Wie lange dauert eine Berechnung oder wie schwer ist sie?

Im Zuge dessen stellte sich heraus, dass es zwischen der Logik und der theoretischen Informatik einen sehr starken Zusammenhang gibt.
Berechnungen eines Rechners basieren auf logischen Operationen und das theoretische Prinzip des universellen digitalen Computers (der [universellen Turingmaschine](sec-utm)), wie auch wichtige Grenzen dessen was [berechenbar](def-turing-computable) ist, entstand aus den Arbeiten vieler Logiker.

Den Anfang machten auch hier die Griechen.
Ihnen haben wir ein System des logischen Schließens, die sog. *Syllogismen des Aristoteles*, zu verdanken.
Neben den Syllogismen beschäftigte sich Aristoteles bereits mit dem *Satz vom Widerspruch* und dem *Satz vom ausgeschlossenen Dritten* sowie der Beweistechnik des *indirekten Beweises* -- allesamt fundamentale mathematische Techniken bzw. Fragestellungen.

Zur Zeit des römischen Reichs formulierten die Stoiker das erste aussagelogische Kalkül und auch im Mittelalter sollten sich kleinere Fortschritte im Bereich der Logik ergeben.
Jedoch sollten erst im 19. Jahrhundert, durch Mathematiker wie George Boole, Gottlob Frege und Bertrand Russell, weitreichende Fortschritte möglich werden.

```{figure} ../../figs/history/logicians.png
---
height: 150px
name: logicians
---
Einflussreiche Logiker ihrer Zeit: Georg Boole, Gottlob Frege und Bertrand Russell, Quellen: [1](https://commons.wikimedia.org/wiki/File:George_Boole_color.jpg), [2](https://commons.wikimedia.org/wiki/File:Young_frege.jpg).
```

Im weit entfernten China wurde zwischen 200 vor und 100 nach Christus das Mathematikbuch *Jiu Zhang Suanshu* (*Neun Bücher arithmetischer Technik*) verfasst.
In ihm findet sich einer der noch heute bekanntesten Algorithmen zum Lösen linearer Gleichungssystem: Das sog. *Gaußsche Eliminationsverfahren*.
Es wurde in Europa 1759 vom italienischen Mathematiker Lagrange publiziert und wohl unabhängig davon vom deutschen Mathematiker Gauß im Jahr 1811 entwickelt.
Schon die Babylonier wussten wie sich Gleichungen mit zwei Unbekannten lösen lassen, jedoch waren ihre zu lösenden Probleme durch konkrete oft geometrische Fragestellungen motiviert.
Der Fokus auf die Geometrie war für die Anfänge sicherlich förderlich doch schlussendlich für weitere Fortschritte auch hinderlich.
Die Besonderheit beim *Gaußschen Eliminationsverfahren* ist seine Abstraktion, die zu einer allgemeinen Lösungstheorie für *lineare Gleichungssysteme* führte.

Wie bereits erwähnt, dauerte es tausend Jahre bis an den Fortschritt der antiken Griechen wieder angeknüpft wurde.
Wir wissen natürlich nicht welches, möglicherweise entscheidende Wissen durch die Zerstörung und Plünderung der Bibliothek von Alexandria verloren gegangen ist.