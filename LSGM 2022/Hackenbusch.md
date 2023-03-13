# Hackenbusch

* 2 Spieler
* Jeder Spieler hat Hölzer in  seiner Farbe
* Die Länge der Hölzer ist beliebig lang
* Alle Hölzer müssen gerade sein und mit dem Boden verbunden sein
* Jeder Spieler entfernt Hölzer in seiner Farbe
* Hölzer, die nicht mit dem Boden verbunden sind, fallern heraus
* Der Spieler ohne Zugmöglichkeit verliert

## Beispiele

```
	  |
 \ /  |
  |   |
--------
```

Grün gewinnt immer

```
  |   |
  |   |
--------
```

Zweiter Spieler gewinnt immer → Symetrie

```
  |
  |   |
  |   |
--------
```

Rot gewinnt immer

```
   /\
  |  |
-------- 
```

Zweiter Spieler gewinnt → Symetrie

```
	/\
  /-\
-------
```

Grün gewinnt immer

```
 |  |
 |  |  |
 |  |  |
---------
```

Zweiter Spieler gewinnt immer

```
 |-|  |-|
 |-|  |-|
----------
```

Zweiter Spieler gwinnt immer → Symetrie

## Nullspiel

* Der Spieler der beginnt, verliert

## Stellungen

* Definition: Eine Stellung wir beschrieben mit { Zugmöglichkeiten des linken Spielers | Zugmöglichkeiten des rechten Spielers }
* Einer Stellung wird mit einer Zahl bewertet, welche angibt, wie viele Züge der linke Spieler im Vorteil ist → wie viele einzelne Stäbe muss ich dem rechten Spieler geben, damit dies in ein Nullspiel endet?
* Beispiele:

```


----------
```

$0 = { | }$

```
 |  |  |
---------
```

$3 = { 2 |  }$

```
 |  |  |  |
------------
```

$-4 = { | -3 }$
* Addition entspricht Vereinigung der Stellungen
* Wir schreiben $n = { n-1 | }$ für $n >= 1$
* Wir schreiben $n = { | }$ für $n = 0$
* Wir schreiben $n = { | n+1 }$ für $n <= -1$

```
 |
 |  |
------
```

→ x

$-1 < x < 0$

```
 |  |
 |  |  |
---------
```

--> y

$y + y -1 = 0 => y = 1/2$
- - -

```
 |
 |
 |
---
```

Grün gewinnt immer → $1 = { 1 | }$

```
 |  |
 |  |  |
 |  |  |
---------
```

$2x - 1/2 = 0$
$x = 1/4$

```
 |
 |
 |
 |
---
```

Grün gewinnt immer → $1 = { 1 | }$

```
 |  |
 |  |  |
 |  |  |
 |  |  |
---------
```

```
 \ /
  |
-----
```

Grün gewinnt immer → $1 = { 1 | }$

```
 \ / \ /
  |   |
---------
```

```
 |-|
-----
```

Grün gewinnt immer → $1 = { 2 | -1 }$

```
 |-| |-|
---------
```

```
 |
 |-|
-----
```

Zweiter gewinnt immer → $0 = { 1 | -1 }$
- - -

```
 | }
 | } n
 | }
 |
----
```

→ $\frac{1}{2^n}$
