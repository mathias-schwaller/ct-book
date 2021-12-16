(sec-repetition-and-recursion)=
# Wiederholung und Rekursion

Auf der konzeptionellen Ebene erscheinen Wiederholung und Rekursion grundverschieden.
Es sind unterschiedliche Denkweisen.
Wir können rekursiv oder aber in Wiederholungen denken.

```{admonition} Wiederholung und Rekursion
:class: important
Sofern bei der Wiederholung, die Anzahl der Durchläufe nicht zur Laufzeit vor der Ausführung der Wiederholung bekannt sein muss können wir überraschenderweise jede Rekursion in eine Wiederholung und jede Wiederholung in eine Rekursion umwandeln!
```

Dabei lassen sich manche Probleme leichter rekursiv und andere leichter iterativ lösen.

## Wiederholung

Das fundamentale Prinzip der *Wiederholung* ist zentraler Bestandteil des Computational Thinkings.
Blicken wir in den Werkzeugkasten der Algorithmen so finden wir die Wiederholung überall.
Sortieralgorithmen, die Berechnung eine Gleichungssystems, das Verarbeiten eines Bildes, die Schaltflächen einer App, überall finden wir Schleifen, die unsere Informationen *iterativ* verarbeiten.

Nach der Definition eines Algorithmus, muss dieser aus endlich vielen Anweisungen bestehen.
Will man jedoch eine variable Menge an Information verarbeiten, so muss ein Algorithmus abhängig von der Eingabegröße unterschiedlich viele Anweisungen ausführen.
Das bedeutet, dass die Länge des Algorithmus unabhängig von der Anzahl der auszuführenden Anweisungen (für eine gegebenen Eingabe) sein können muss!
Nach dem Schubfachprinzip bedeutet dies wiederum, dass in diesem Fall Teile des Algorithmus öfters durchlaufen werden - Wiederholung muss also in irgendeiner Form stattfinden.

Überraschenderweise hat sich herausgestellt, dass *Wiederholung* in Kombination mit der *Fallunterscheidung* ausreicht, um alles berechnen zu können was wir bisher als natürlich berechenbar ansehen.
Nach der unbeweisbaren Church-Turung-These werden wir keine Problem finden, was natürlich berechenbar aber nicht durch einen Computer berechnet werden kann.
Die Fallunterscheidung in Kombination mit der Wiederholung ist scheinbar ausreichend.

Nun haben Sie vielleicht die Hoffnung, Sie müssten nur die *Wiederholung* und die *Fallunterscheidung* beherrschen und können dann jedes Problem lösen.
Leider sind diese beiden Techniken derart grundlegend, dass sie eine notwendige nicht aber ausreichende Bedingung für die Entwicklung von Algorithmen darstellen.
Wir können das mit der Sprache vergleichen.
Nur weil wir laute von uns geben können, heißt das nicht, dass wir uns in jeder Sprache verständigen können.
Ein weiteres Beispiel wären die Naturwissenschaften.
Nur weil wir die kleinsten Teilchen im Universum verstehen, bedeutet dass nicht, dass wir damit das entstehen von Leben oder anderen emergenten Übergängen erklären können.

Wenn Sie jedoch Erfahrung im entwickeln von Algorithmen gesammelt haben und Algorithmen analysiert und verwendet haben, dann werden Sie beginnen in Wiederholungen zu denken.
Sie werden beginnen in Wiederholungen von Wiederholungen von Wiederholungen zu denken.

Nehmen wir zum Beispiel den [Bubblesort Algorithmus](https://en.wikipedia.org/wiki/Bubble_sort).
Wir möchten eine Liste von Zahlen sortieren.
Wir gehen durch die Liste (1. *Wiederholung*) und wann immer zwei nebeneinander liegende Zahlen falsch sortiert sind, vertauschen wir diese.
Wir wiederholen dies (2. *Wiederholung*) solange bis keine Zahl mehr falsch sortiert ist.

import random as rnd

def bubble_sort(numbers):
    finished = False
    while(not finished):
        finished = True
        for i in range(1,len(numbers)):
            if numbers[i] < numbers[i-1]:
                numbers[i], numbers[i-1] = numbers[i-1], numbers[i]
                finished = False
    
numbers = [1,2,3,4,5,6,7,8,9]
rnd.shuffle(numbers)
print(f'before sorting: {numbers}')
bubble_sort(numbers)
print(f'after sorting: {numbers}')

Die beiden Schleifen liefern uns auch einen Hinweis auf die Laufzeit des simplen Sortieralgorithmus.
Nach jedem ausführen der inneren Schleife befindet sich ein neues Element an seiner korrekten Position.
Damit brauchen wir maximal so viele Durchläufe (1. Wiederholung) wie es Elemente sind.
Jeder Durchlauf benötigt ebenfalls maximal so viel Schritte wie es Elemente sind.
Damit hat der Algorithmus im schlechtesten Fall eine quadratische Laufzeit.

## Rekursion

Rekursion scheint dieses unverständliche Konzept, welches Mathematiker\*innen lieben und vor dem Programmierer\*innen anfänglich davonlaufen.
Derweil würden wir behaupten, dass die *rekursive denkweise* uns Menschen näher ist als das Denken in Wiederholungen.
Rekursive Lösungen sind oft eleganter, kürzer, verständlicher aber leider auch langsamer als iterative Lösungen.

Nehmen wir die Berechnung der Fakultät, einmal iterativ

$$\text{fac}_\text{it}(n) = n \cdot (n-1) \cdot (n-2) \cdot \ldots \cdot 1 = \prod\limits_{i=1}^n i$$

def fac_it(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

fac_it(5)

und einmal rekursiv

$$\text{fac}_\text{rec}(n) = \begin{cases} 1 & \text{ falls } n = 0\\ n \cdot \text{fac}_\text{rec}(n-1) & \text{ sonst}\end{cases}$$

def fac_rec(n):
    if n <= 1:
        return 1
    return n * fac_rec(n-1)

fac_rec(5)

Die Rekursion beinhaltet einen Selbstbezug, wohingegen die iterative Lösung diesen ausbreitet bzw. auflöst.
Betrachten wir die rekursive Lösung benötigen wir für die Berechnung lediglich die Multiplikation und den Selbstbezug - keine Schleife, ja nicht einmal eine Variable.

```{admonition} Rekursion
:name: def-recursion
Als *Rekursion* wird ein Vorgang bezeichnet, welcher sich selbst als Teil enthält oder mithilfe von sich selbst definierbar ist.
```

## Die Türme von Hanoi

Probleme lassen sich immer dann leichter rekursiv lösen, wenn der Selbstbezug offensichtlich oder einfach zu finden ist.
Ein Beispiel sind die sog. [Türme von Hanoi](https://de.wikipedia.org/wiki/T%C3%BCrme_von_Hanoi).

Ein Turm bestehend aus $n$ unterschiedlich breiten Schichten soll von einem Ort 0 zu einem anderen Ort 2 gebracht werden.
Der Turm wird nach oben immer schmaler, d.h., die Schicht die über einer anderen liegt ist schmaler.
Wir können nur eine einzelne Schicht bewegen und wir dürfen keine Schicht auf eine schmälere legen.
Es gibt nur einen zusätzlichen Ablegeort 1.
Wie bringen wir den Turm nun von Ort 1 nach Ort 2?

Hat der Turm nur eine Schicht, ist das Problem schnell gelöst: Bewege Schicht von 0 nach 2.

Besteht der Turm aus zwei Schichten, ist das Problem auch noch einfach zu lösen: 

1. Bewege oberste Schickt von 0 nach 1.
2. Bewege unterste Schicht von 0 nach 2 und
3. Bewege dann die schmälere Schicht von 1 auf 2.

```{figure} ../../figs/art-of-programming/hanoi.png
---
width: 800px
name: fig-hanoi-3
---
Die Türme von Hanoi mit drei Schichten.
```

Wie gehen wir aber für einen allgemeinen Fall mit $n$ Schichten vor?
Nun,

1. wir bringen die obersten $n-1$ Schichten von 0 nach 1,
2. die unterste Schicht von 0 nach 2 und dann 
3. die $n-1$ Schichten von 1 nach 2.

```{figure} ../../figs/art-of-programming/hanoi-abstract.png
---
width: 800px
name: fig-hanoi-abstract
---
Die Türme von Hanoi mit $n$ Schichten.
```

Diese $n-1$ Schichten sind ein Turm, der um eine Schicht kleiner ist.
Auch die eine Schicht ist ein Turm, bestehend aus nur einer Schicht.
Aus dem Problem einen Turm der Höhe $n$ zu verschieben wurde: Verschiebe Turm der Höhe $n-1$ (Selbstbezug) + Verschiebe eine Scheibe (Rest).

Rekursiv zu denken bedeutet oft, dass wir einfach mal davon ausgehen, wir hätten das Problem bereits gelöst.
Wir schreiben in einem deklarativen Stil, d.h., wir schreiben hin was wir wollen und nicht was wir tun.
Wir gehen also davon aus es gäbe eine Funktion ``move_tower(n, fr, to, tmp)``, welche die obersten ``n`` Schichten eines Turms von ``fr`` nach ``to`` bringt und dabei ``tmp`` als Zwischenablage verwendet.

```python
def move_tower(n, fr, to, tmp):
    pass
```

unter dieser Annahme führen bewegen wir den Turm wie oben beschrieben:

```python
def move_tower(n, fr, to, tmp):
    if n == 1:
        move(fr, to)             # real move from upper most stone
    
    move_tower(n-1, fr, tmp, to) # eg 0 -> 1
    move_tower(1, fr, to, tmp)   # eg 0 -> 2
    move_tower(n-1, tmp, to, fr) # eg 1 -> 2
```

Um das ganze vorzuführen modellieren wir einen Turm als Liste von Zahlen und die drei Plätze als Liste der Länge 3.

def move(hanoi, fr, to):
    hanoi[to].insert(0, hanoi[fr][0])
    del hanoi[fr][0]

def move_tower(hanoi, n, fr, to, spare):
    if n == 1:
        move(hanoi, fr, to)
    else:    
        move_tower(hanoi, n-1, fr, spare, to)
        move_tower(hanoi, 1, fr, to, spare)
        move_tower(hanoi, n-1, spare, to, fr)

n = 6
tower = list(range(n))
hanoi = [tower, [], []]
print(hanoi)

move_tower(hanoi, n, 0, 2, 1)
print(hanoi)

Erstaunlich, wie kurz die Lösung am Ende ausfällt.
Es fühlt sich fast so an als hätten wir an irgendeiner Stelle betrogen.
Aber Vorsicht, zu beweisen, dass der Algorithmus korrekt funktioniert ist nicht trivial.
In anderen Worten, es ist nicht offensichtlich, dass der Algorithmus korrekt ist dennoch ist es intuitiv plausibel.
Um eine gute iterative Lösung zu finden braucht es Gehirnschmalz, doch denken Sie daran: Es gibt sie immer!