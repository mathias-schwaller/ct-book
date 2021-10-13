# Zahlen sortieren in Python

Wunderbar, wir können nun Karten sortieren. 
Aber können wir vielleicht noch viel mehr?
Sehen Sie sich den Code genau an.
An welcher Stelle geht es wirklich um Karten?
Wie und wo müsste man den Code ändern um z.B. Zahlen zu sortieren?

```{exercise} Zahlen sortieren in Python
Ändern oder erweitern Sie Ihren Programmiercode um Zahlen anstatt Karten zu sortieren.
```

# Kopie des Codes des vorherigen Abschnitts.

def find_smallest_index(hand):
    index = 0
    for i in range(len(hand)):
        if is_smaller(hand[i], hand[index]):
            index = i
    return index

def remove_smallest_card(hand):    
    i = find_smallest_index(hand)
    card = hand[i]
    del hand[i]
    return card

def stack_sort(hand):
    stack = [];
    while len(hand) > 0:
        stack.append(remove_smallest_card(hand))
    return stack   

Wir benötigen lediglich einen neuen Vergleichsoperator ``is_smaller()``.

def is_smaller(number1, number2):
    return number1 < number2

stack_sort([-11, 12, -6, 45, 1, 54, -55, 88])

import random
n_numbers = 1000

hand = [random.randint(0, n_numbers) for _ in range(n_numbers)]
stack_sort(hand)