---
author: karlz
tags:
- Mathe
- FGB
---

# Änderungsrate

- Durchschnittliche Änderungsrate: Differenzenquotient
- Momentane Änderungsrate: Differentialquotient (Ableitung)

# Tangenten

1. Die Tangente ist eine Gerade ($y=mx+n$).
1. Die Tangente hat mit dem Funktionsgrahen den Berührungspunkt gemeinsam.
1. Im Berührungspunkt ist der Anstig der Tangente gleich dem Anstieg des Funktionsgraphen.

## Zu Punkten und Parallelen

1. Ableitung bilden
1. Berührungspunkt bilden
1. $m$ berechnen
1. $n$ berechnen
1. Tangentengleichung angeben


**Beispiel**
$f(x)=x^2\quad x_0=2$
- $f'(x)=2x$
- $P(2|f(2))=P(2|4)$
- $m=f'(2)=4$
- $4=4*2+n\to n=-4$
- $t(x)=4x-4$

## Von externen Punkten

1. Ableitung bilden
1. Gedachter Berührungspunkt $A$ bilden
1. Schnittpunkte $s$ bilden
1. Tangentengleichung angeben

**Beispiel**
$f(x)=\dots$
$f'(x)=\dots$

$Q(x_Q|y_Q)$
$A(x_A|f(x_A))$

$m=\frac{x_Q-f(x_A)}{y_Q-x_A}$
$m=f'(x_A)$

~~~js
s=solve(yQ-f(xA)/(xQ-xA)=f1(xA),xA))
t(x):=tangentline(f(x),x,s)
~~~

## Normale

Die Normale steht senkrecht auf der Tangente.

Normale: $m=-\frac{1}{f'(x)}$

~~~js
normalline(f(x),x,s)
~~~
