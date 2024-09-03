---
author: karlz
tags:
  - Mathe
  - FGB
---


## Ebenen in Parameterform

### Parameterdarstellung einer Ebene

$E:\vec{x}=\begin{pmatrix}1\\2\\3\end{pmatrix}+u\begin{pmatrix}1\\2\\3\end{pmatrix}+v\begin{pmatrix}1\\2\\3\end{pmatrix}$

### Punktprobe in der Parameterdarstellung einer Ebene

Liegt $P(5|-5|20)$ in $E:\vec{x}=\begin{pmatrix}1\\2\\3\end{pmatrix}+k\begin{pmatrix}1\\-1\\2\end{pmatrix}+l\begin{pmatrix}0\\-2\\5\end{pmatrix}$?
$\begin{pmatrix}5\\-5\\20\end{pmatrix}=\begin{pmatrix}1\\2\\3\end{pmatrix}+k\begin{pmatrix}1\\-1\\2\end{pmatrix}+l\begin{pmatrix}3\\4\\2\end{pmatrix}$

Gleichungssystem lösen
$5=-10-2k$
$-5=2-k+4l$
$20=3+2k+2l$

$k=-7.5$
$t=-5.25$

$20=3+2\cdot-7.5+2\cdot-5.25$
$20\ne-35.75$
Gleichung geht nicht auf, Punkt liegt somit nicht in der Ebene.

## Ebenen in Koordinatenform

### Koordinatendarstellung einer Ebene

$1.5=2x+3y+z$

### Parametergleichung zu Koordinatenform

$\vec{x}=\begin{pmatrix}1\\1\\3.5\\\end{pmatrix}+k\begin{pmatrix}2\\0\\4\end{pmatrix}+t\begin{pmatrix}1\\1\\5\end{pmatrix}$

Eleminieren der Parameter
$x=1+2k+t$
$y=1+t$
$z=3.5+4k+5t$

$t=y-1$
$2k=x-1-t$
$2k=x-1-y+1$
$k=\frac{x-y}{2}$

$z=3.5+4\cdot \frac{x-y}{2}+5\cdot(y-1)$
$z=3.5+2x-2y+5y-5$
$1.5=2x+3y-z$

### Punktprobe in der Koordinatenform einer Ebene

Liegt $P(1|2|3)$ in $E$ mit $2x+3y-1z=1.5$?

$2\cdot1+3\cdot2-3=1.5$
$5\ne1.5$
Gleichung geht nicht auf, Punkt liegt nicht in der Ebene.

Liegt $Q(-1|1|-0.5)$ in $E$ mit $2x+3y-1z=1.5$?

$2\cdot-1+3\cdot1-1\cdot-0.5=1.5$
$1.5=1.5$
Gleichung geht auf, Punkt liegt in der Ebene.

### Koordinatenform zu Parametergleichung

$2x+3y-z=1.5$

2 der Koordinaten mit Parametern ersetzen
$x=t\quad y=k$
$2t+3k-z=1.5$

Dritte Koordinate in Abhängigkeit von den Parametern darstellen
$z=2t+3k-1.5$

$\vec{x}=\begin{pmatrix}0\\0\\-1.5\end{pmatrix}+t\begin{pmatrix}1\\0\\2\end{pmatrix}+k\begin{pmatrix}0\\1\\3\end{pmatrix}$

### Schrägbild mithilfe von Spurpunkten

Spurpunkte sind die Schnittpunkte der Ebene mit den Koordinatenachsen.

$E:2x+y+4z=6$

$2x=6\quad x=3$
$P_{x}(3|0|0)$

$y=6$
$P_{y}(0|6|0)$

$4z=6\quad z=\frac{3}{2}$
$P_{z}(0|0| \frac{3}{2})$

![](../Working%20Materials/Vektoren/Schrägbild%20Ebene.png)

## Besondere Lage von Ebenen

$ax+by+cz=d$

### Koordinatenebenen

x-y-Ebene $z=0$

### Parallele zur Ebene

Parallel zur x-y-Ebene $z=d\ne 0$

### Parallele zur Achse

x-Achse $by+cz=d$

## Lagebeziehung Ebene-Ebene

- identisch
- parallel
- Schnittgerade

## Lagebeziehungen Ebene-Geraden

- Schnittpunkt $g \perp E$
- Parallel $g\parallel E$
- Gerade in Ebene $g\in E$
## Spezialität bei der Punktprobe

Liegt $P$ im Parallelogramm $ABCD$ mit $A(1|2|3)$, $B(2|5|-1)$, $C(3|-2|1)$ und $D(2|-5|5)$?

Ebenengleichung aufstellen
$\vec{x}=\vec{0A}+k\vec{AB}+t\vec{AD}$
$\vec{x}=\begin{pmatrix}1\\2\\3\end{pmatrix}+s\begin{pmatrix}1\\3\\-4\end{pmatrix}+t\begin{pmatrix}1\\-7\\2\end{pmatrix}$

### Beziehung von Geraden zu Ebenen

- Schnittpunkt $g \perp E$
- Parallel $g\parallel E$
- Gerade in Ebene $g\in E$

#### Gegeben in Parameterform

$g: \vec{x}=\begin{pmatrix}5\\6\\1\end{pmatrix}+k\begin{pmatrix}-1\\-2\\3\end{pmatrix}$
$E: \vec{x}=\begin{pmatrix}1\\0\\0\end{pmatrix}+r\begin{pmatrix}-1\\6\\0\end{pmatrix}+s\begin{pmatrix}0\\0\\20\end{pmatrix}$

$5-k=1-r$
$6-2k=6r$
$1+3k=20s$

$r=-\frac{1}{4}$
$s=\frac{49}{80}$
$k=\frac{15}{4}$

$S(\frac{5}{4}|- \frac{3}{2}|\frac{49}{4})$

- - -

Falls Ausgabe `"false"`: $g\parallel E$
Falls Ausgabe `c1, c2`: Es gibt unendlich viele Lösungen, $g\in E$

#### Gegeben in Koordinatenform

$g: \vec{x}=\begin{pmatrix}5\\6\\1\end{pmatrix}+k\begin{pmatrix}-1\\-2\\3\end{pmatrix}$
$E: \vec{x}=\begin{pmatrix}1\\0\\0\end{pmatrix}+r\begin{pmatrix}-1\\6\\0\end{pmatrix}+s\begin{pmatrix}0\\0\\20\end{pmatrix}$

$5-k=1-r$
$6-2k=6r$
$1+3k=20s$

$r=-\frac{1}{4}$
$s=\frac{49}{80}$
$k=\frac{15}{4}$

$6(5-t)+(6-2t)=6$
$30-6t+6-2t=6$
$8t=30$
$t=\frac{15}{4}$

$t$ in $g$ einsetzen
$S(1.25|-1.5|12.25)$
