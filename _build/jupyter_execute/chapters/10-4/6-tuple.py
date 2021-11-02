# Tupel - tuple

Listen und [Tupel](https://docs.python.org/3/library/stdtypes.html#tuple) (wie auch Zeichenketten, und ``range``) sind allesamt [Sequenzen](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) und haben dadurch sehr ähnliche Eigenschaften.
Einzig bei der Erstellung verwenden wir statt der eckigen die runden Klammern:

numbers = (1, 2, 3, 4, 5)
numbers

Die Indexierung ist identisch.

numbers = (1, 2, 3, 4, 5)
print(numbers[2:4])

Der große Unterschied lieft in der Veränderbarkeit, denn Tupel ``tuple`` sind **unveränderlich** (engl. **immutable**)!
Aber Vorsicht ist geboten, denn das bedeutet nicht, dass wir ein Tupel überhaupt nicht verändern können.
Was wir jedoch nicht verändern können sind die **Adressen** bzw. ``id``s seiner Elemente!

Folgender Code führt zu einem Fehler:

numbers = (1, 2, 3, 4, 5)
numbers[2] = -10

Doch können wir eine *Datenstruktur* die Element eines Tupels ist durchaus verändern:

numbers = (1, 2, [3, 4, 5])
numbers[2][0] = 'a'
numbers

Tupel werden oft verwendet wenn wir eine Ansammlung von heterogenen Datentypen zusammenfassen wollen und wir explizit ausdrücken bzw. sicher gehen wollen, dass dieses Tupel nicht verändert wird. 
Zum Beispiel ein Tupel was das Alphabet repräsentiert.
Dieses wird sich und soll sich auch nicht verändern.

alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
alphabet

``Python`` bietet eine etwas hässliche Abkürzung für die Erstellung eines Tupels mit nur einem Element:

singleton = 1,
singleton

entspricht

singleton = (1,)
singleton

Achtung

number = (1)
number

funktioniert nicht!

Python bietet auch das Konzept des *tuple-packing* und *tuple-unpacking*, was enorm praktisch ist:

triple = (1, 2, 3)
x, y, z = triple  # unpacking
print(f'x = {x}')
print(f'y = {y}')
print(f'z = {z}')
packing = x, y, z # packing
print(f'packing = {packing}')

Ziemlich cool, wie wir finden.
Das ist insbesondere praktisch wenn Sie eine Funktion schreiben möchten, die mehr als ein Rückgabewert hat:

import random as rnd
def random_rgb_color():
    r = rnd.randint(0, 255)
    g = rnd.randint(0, 255)
    b = rnd.randint(0, 255)

    return r, g, b

r, g, b = random_rgb_color()
print(f'red = {r}, green = {g}, blue = {b}')

Im Falle der Listen hat der ``+=``-Operator die Liste verändert.
Was glauben Sie macht der ``+=``-Operator für Tupel?
Ist er definiert?
Testen wir es aus:

numbers = (1, 2, 3, 4, 5)
numbers += (6,7,8)
numbers

Kein Fehler!
Wird nun doch also doch ``numbers``?
Ja und nein.
Der Speicherbereich des ursprünglichen Tupels bleibt unverändert, stattdessen wird eine Kopie angelegt.

numbers = (1, 2, 3, 4, 5)
numbers_copy = numbers
print(f'id before += {id(numbers)}')
numbers += (6,7,8)
print(f'id after += {id(numbers)}')
print(f'id after += of the original {id(numbers_copy)}')
print(f'numbers: {numbers}')
print(f'numbers_copy: {numbers_copy}')

````{exercise} Tupel vs Listen (Effizienz)
:label: tuple-vs-lists-appending-exercise
Welche der folgenden Code-Teile benötigt nach Ihrer meinung mehr Computerressourcen und warum?

Listenerzeugung durch Anhängen:

```python
numbers = []
i = 0
while i < 100:
    numbers += [i]
    i += 1
numbers
```

Tupelerzeugung durch Anhängen:

```python
numbers = tuple()
i = 0
while i < 100:
    numbers += (i,)
    i += 1
numbers
```
````

```{solution} tuple-vs-lists-appending-exercise
:label: tuple-vs-lists-appending-solution
:class: dropdown

Die Tupelerzeugung durch Anhängen ist deutlich langsamer und speicherintensiver, denn bei jeder Konkatenation ``+=`` wird ``numbers`` im Speicher kopiert.
Der Code erzeugt damit 100 unterschiedliche Tupel!
Im Fall der Liste wird einfach nur ein Element hinten dran gehängt.

```