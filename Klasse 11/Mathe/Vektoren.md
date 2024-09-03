# Vektoren

## Kartesiches Koordinatensystem

- Alle Achsen stehen $\perp$ aufeinander
- Achsen: $x,y,z$ oder $x_{1},x_{2},x_{3}$
- Koordinatenebenen:
	- $x-y$-Ebene
	- $x-z$-Ebene
	- $y-z$-Ebene
- Zeichnungen im räumlichen Koordinatensystem
	- $y-z$-Ebene ist Zeichenebene
	- $x$-Achse im 45°-Winkel zeichnen
	- Einheiten auf der $x$-Achse um $\frac{1}{2}\sqrt{2}$ verkürzt

## Dreidimensionaler Vektor

Ein dreidimensionaler Vektor ist ein Zahlentripel, das man in Spaltenform schreibt. Der Vektor, der $A$ auf $A'$ abbildet, wird mit $\vec{AA'}$ oder $\vec{a}$ bezeichnet.

### Berechnung des Betrages eines Vektors

$|\vec{a}|=\sqrt{x_{a}^{2}+y_{a}^{2}+z_{a}^{2}}$

### Ortsvektor

Der Ortsvektor eines Punktes P beginnt im Koordinatenursprung $\vec{0P}$.

### Addition und Subtraktion von Vektoren

$A(-6,5,5)$
$B(4,-2,0)$

$\vec{AB}=A+B$

### Dreiecksregel

$\vec{PQ}+\vec{QR}=\vec{PR}$

### Vervielfachen von Vektoren

Ein Vektor wird vervielfacht, indem man jede Koordinate mit der selben reellen Zahl multipliziert.

- Geometrische Bedeutung: Der Vektorpfeil hat die r-fache Länge

Ist $r<0$, haben die Pfeile die entgegengesetzte Richtung

### Mittelpunkt einer Strecke

**Beispiel**
$A(1|2|3)$
$B(3|8|5)$
$\vec{OM}=\begin{pmatrix}1\\2\\3\end{pmatrix}+\frac{1}{2}\begin{pmatrix}3\\8\\5\end{pmatrix}$

### Schwerpunkt eines Dreiecks

**Beispiel**
$A(2|1|4)$
$B(3|-5|5)$
$C(1|3|5)$
$\vec{OS}=\frac{1}{3}\begin{pmatrix}\begin{pmatrix}2\\1\\4\end{pmatrix}+\begin{pmatrix}3\\-5\\5\end{pmatrix}+\begin{pmatrix}1\\3\\-3\end{pmatrix}\end{pmatrix}=\begin{pmatrix}2\\-\frac{1}{3}\\2\end{pmatrix}$



$k,t\in\mathbb{R}$

$0\ge k\ge1$
$0\ge t\ge1$

$k+t\ge1$

### Einheitsvektor

Der Einheitsvektor ist ein Vektor mit der Länge 1.

$\vec{v}=\begin{pmatrix}1\\2\\-2\end{pmatrix}$
$|\vec{v}|=\sqrt{1^{2}+2^{2}+(2)^{2}}=\sqrt{9}=3$
$\vec{v}_{e}=\frac{1}{|\vec{v}|}\vec{v}=\frac{1}{3}\begin{pmatrix}1\\2\\-2\end{pmatrix}$

### Linearkombination von Vektoren

Als Linearkombination von Vektoren bezeichnet man die Summe von Vielfachen des Vektors.

$\vec{a}=k\vec{b}t\vec{c}+s\vec{d}$

## Lineare Abhängigkeit und Unabhängigkeit von Vektoren

Zwei Vektoren sind linear abhängig, wenn sie Vielfache voneinander sind.

$k\vec{a}=\vec{b}$

### Punktprobe

Liegt ein Punkt $P$ auf der Geraden $G$, so musses einen Wert für den Parameter $k$ geben, der die Gleichung $\vec{x}=\vec{0A}+k\vec{AB}$ erfüllt.

**Beispiel**
$\vec{x}=\begin{pmatrix}2\\-2\\0\end{pmatrix}+k\begin{pmatrix}3\\5\\-1\end{pmatrix}$
$P(-7|-17|3)$

$-7=2+3k\quad k=-3$
$-17=-2+5k\quad k=-3$
$3=0-1k\quad k=-3$

### Geometrische Deutung

$\vec{x}=\begin{pmatrix}2\\-2\\0\end{pmatrix}+k\begin{pmatrix}3\\5\\-1\end{pmatrix}$
$P(-7|-17|3)$
Der Vektor zeigt den Punkt auf einer Geraden an. $k$ gibt dabei an, wo genau der Punkt auf der Geraden liegt.

### Besondere Lage von Geraden

Parallel zur $y-z$-Ebene: $\vec{x}=\begin{pmatrix}1\\2\\3\end{pmatrix}+k\begin{pmatrix}1\\0\\2\end{pmatrix}$

Parallel zur $x-y$-Ebene: 
$\vec{x}=\begin{pmatrix}1\\2\\3\end{pmatrix}+k\begin{pmatrix}1\\2\\0\end{pmatrix}$

Parallel zur $x$-Achse: 
$\vec{x}=\begin{pmatrix}1\\2\\3\end{pmatrix}+k\begin{pmatrix}1\\0\\0\end{pmatrix}$

Parallel zur $y$-Achse: 
$\vec{x}=\begin{pmatrix}1\\2\\3\end{pmatrix}+k\begin{pmatrix}0\\2\\0\end{pmatrix}$

Parallel zur $z$-Achse: 
$\vec{x}=\begin{pmatrix}1\\2\\3\end{pmatrix}+k\begin{pmatrix}0\\0\\3\end{pmatrix}$

### Lagebeziehung von Geraden im Raum

- parallel
- identisch
- windschief
- schneiden sich

#### Untersuchen der LB von Geraden

~~~mermaid
graph TB;
A[Sind sie vielfache voneinander?]
A-- ja -->A0[parallel oder identisch]
A0-->A00[Punktprobe]
A00-- w.A. -->A001[identisch]
A00-- ø -->A002[parallel]
A-- nein -->A1[windschief oder Schnittpunkt]
A1-->A10[gleichsetzen]
A10-- w.A -->A100[Schnittpunt]
A10-- ø -->A101[windschief]
~~~

Wenn in beiden Gleichungen der Parameter denselben Buchstaben hat, muss einer der beiden umbenannt werden.

**Beispiel**
$\vec{x}=\begin{pmatrix}3\\0\\1\end{pmatrix}+t\begin{pmatrix}2\\5\\-2\end{pmatrix}$
$\vec{x}=\begin{pmatrix}5\\5\\-1\end{pmatrix}+t\begin{pmatrix}1\\4\\2\end{pmatrix}$

Richtungsvektoren
$\begin{pmatrix}2\\5\\-2\end{pmatrix}=k\begin{pmatrix}1\\4\\2\end{pmatrix}$

Gleichsetzen
$3+2t=5+k$
$5t=5+4k$
$1-2t=-1+2k$

$t=1+\frac{4}{5}k$
$1-2(1+\frac{4}{5}k)=-1+2k$
$-1-\frac{4}{5}k=-1+2k$

**Beispiel**
$\vec{x}=\begin{pmatrix}3\\0\\1\end{pmatrix}+t\begin{pmatrix}2\\5\\-2\end{pmatrix}$
$\vec{x}=\begin{pmatrix}2\\-1\\7\end{pmatrix}+t\begin{pmatrix}-4\\-10\\4\end{pmatrix}$

Richtungsvektoren
$-2=4k$
$5=-10k$
$-2=4k$

Gleichsetzen
$3=2-4k$
$0=-1-10k$
$1=7+4k$

## Ebenen

Ebenen sind eindeutig bestimmt durch:
- 3 Punkte, die nicht auf einer Geraden liegen
- 1 Punkt und ein Normalenvektor
- 2 parallele Geraden
- 1 Punkt und 2 verschiedene Richtungen

### Parameterdarstellung einer Ebene

**Beispiel**
$A(1|2|3)$
$\vec{u}=\begin{pmatrix}1\\-1\\2\end{pmatrix}$
$\vec{v}=\begin{pmatrix}3\\4\\2\end{pmatrix}$

$E:\vec{x}=\begin{pmatrix}1\\2\\3\end{pmatrix}+k\begin{pmatrix}1\\-1\\2\end{pmatrix}+t\begin{pmatrix}3\\4\\2\end{pmatrix}$

**Beispiel**
$A(1|2|3)$
$B(4|1|5)$
$C(-3|2|1)$

$F: \vec{x}=\begin{pmatrix}1\\2\\3\end{pmatrix}+k\begin{pmatrix}3\\-1\\2\end{pmatrix}+t\begin{pmatrix}-4\\0\\-2\end{pmatrix}$

### Punktprobe in der Parameterdarstellung einer Ebene

$3=1+3k+t$
$2=2+5k+t$

$2k=-2$
$k=-1$
$3=1-3+t$
$t=5$

$5=3+1+10$
$5\ne14$

### Koordinatengleichung einer Ebene

$\vec{x}=\begin{pmatrix}1\\1\\3.5\end{pmatrix}+s\begin{pmatrix}2\\0\\4\end{pmatrix}+t\begin{pmatrix}1\\1\\5t\end{pmatrix}$

$x=1+2s+t$
$y=1+t$
$z=3.5+4s+5t$

$t=y-1$
$x=1+2s+y-1$
$2s=x-y$
$s=0.5(x-y)$

$z=3.5+2(x-y)+5y-5$
$z=-1.5+2x+3y$
$1.5=2y+3y+z$

Jede Ebene kann durch die Koordinatenstellung der Form $ax+by+cz=d$ beschrieben werden. Ein Punkt $P(x,y,z)$ liegt genau dann in der Ebene, wenn seine Koordinaten die Koordinatengleichung erfüllen.

Jede Koordinatengleichung der Form $ax+by+cz=d$ mit $a\ne0$ oder $b\ne0$ oder $c\ne0$ beschreibt eine Ebene.

Der Normalvektor $\vec{n}=\begin{pmatrix}a\\b\\c\end{pmatrix}$ ist der Vektor, der Senkrecht auf der Ebene steht.

### Punktprobe in der Koordinatengleichung einer Ebene

**Beispiel**
Liegt $P(1|2|3)$ in $E$ mit $2x+3y-1z=1.5$?

$2*1+3*2-3=1.5$
$5\ne1.5$

### Schrägbild mithilfe der Spurpunkte

Spurpunkte sind die Schnittpunkte mit den Koordinatenachsen

**Beispiel**
$E: 2x+y+4z=6$

$2x=6\quad x=3$
$S_{x}(3|0|0)$

$y=6$
$S_{y}(0|6|0)$

$4z=6\quad z=1.5$
$S_{z}(0|0|\frac{3}{2})$

Ebene ist gegeben in der Form $ax+by+cz=1$

| Achse   | Schnittpunkt        |
| ------- | ------------------- |
| x-Achse | $(\frac{1}{a};0;0)$ |
| y-Achse | $(0;\frac{1}{b};0)$ |
| z-Achse | $(0;\frac{1}{c};0)$ |

**Beispiel**
$E: 2x+y+4z=6$
$E: \frac{1}{3}x+\frac{1}{6}y+\frac{2}{3}z=1$

$S_{x}(3|0|0)$
$S_{y}(0|6|0)$
$S_{z}(0|0|\frac{3}{2})$

### Besondere Lage von Ebenen

$ax+by+cz=d$

**Koordinatenebenen**
Koordinatenebene $y$-$z$-Ebene
$x=0$

Koordinatenebene $x$-$z$-Ebene
$y=0$

Koordinatenebene $x$-$y$-Ebene
$z=0$

**Ebenen parallel zu den Koordinatenebenen**
Parallel zur $y$-$z$-Ebene
$x=d$

Parallel zur $x$-$z$-Ebene
$y=d$

Parallel zur $x$-$y$-Ebene
$z=d$

**Ebenen parallel zu den Koordinatenachsen**
Parallel zur x-Achse
$by+cz=d$

Parallel zur y-Achse
$ax+cz=d$

Parallel zur z-Achse
$ax+by=d$

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

$6(5-t)+(6-2t)=6$
$30-6t+6-2t=6$
$8t=30$
$t=\frac{15}{4}$

$t$ in $g$ einsetzen
$S(1.25|-1.5|12.25)$

## Licht und Schatten

Falls Licht auf einen Gegenstand fällt, wird ein Schatten erzeugt.

**Beispiel**
Ein 3m hoher Kletterpfahl steht $\perp$ zur x-y-Ebene. Sein Fußpunkt hat die Koordinaten F(0|0|0). Das Sonnenlicht verläuft in Richtung des Vektors $\vec{v}=\begin{pmatrix}3\\1\\-4\end{pmatrix}$. Eine Einheit entspricht einen Meter.

Geradengleichung des Sonnenstrahls durch die Spitze des Kletterbaums: $\vec{x}=\begin{pmatrix}0\\0\\3\end{pmatrix}+k\begin{pmatrix}0\\0\\3\end{pmatrix}$

$z=0$
$3-4k=0\quad k=\frac{3}{4}$

$\begin{pmatrix}0\\0\\3\end{pmatrix}+ \frac{3}{4}\begin{pmatrix}3\\1\\-4\end{pmatrix}=\begin{pmatrix}\frac{9}{4}\\\frac{\\3}{4}\\0\end{pmatrix}$
$\vec{FS}=\sqrt{(\frac{9}{4})^{2}+ (\frac{3}{4})^{2}}=2.34m$

**Beispiel**
- quaderförmiges Objekt mit den Eckpunkten A,B,C,D,E,F,G und H
- Grundfläche $4m \times4m$
- Höhe $3m$
- Sonnenstrahlen $\vec{v}=\begin{pmatrix}\end{pmatrix}$
1. Welche Eckpunkte bestimmen die Schattenfläche?
	$A(4|0|0)$
	$B(4|4|0)$
	$C(0|4|0)$
	$D(0|0|0)$
	$E(4|0|3)$
	$F(4|4|3)$
	$G(0|4|3)$
	$H(0|0|3)$
	$[E,F,G]$ (wegen $\vec{v}$)
2. Schattenpunkte ermitteln$\vec{x}=\begin{pmatrix}4\\0\\3\end{pmatrix}+k\begin{pmatrix}2\\3\\-2\end{pmatrix}$
	$z=0$
	$0=3-2k$
	$k=\frac{3}{2}$
	$\vec{0E}=\begin{pmatrix}4\\0\\3\end{pmatrix}+ \frac{3}{2}\begin{pmatrix}2\\3\\-2\end{pmatrix}=\begin{pmatrix}7\\4.5\\0\end{pmatrix}$
	$\vec{0F}=\begin{pmatrix}4\\4\\3\end{pmatrix}+ \frac{3}{2}\begin{pmatrix}2\\3\\-2\end{pmatrix}=\begin{pmatrix}7\\8.5\\0\end{pmatrix}$
	$\vec{0G}=\begin{pmatrix}0\\4\\3\end{pmatrix}+ \frac{3}{2}\begin{pmatrix}2\\3\\-2\end{pmatrix}=\begin{pmatrix}3\\8.5\\0\end{pmatrix}$
3. Fläche berechnen
	$4m*3m+4m*4.5m=4m*7.5m=30m^{2}$

### Punktförmig Lichtquelle

**Beispiel**
Laserstrahl geht von $L(3|4|2)$. Gesucht ist der Schattenpunkt von $P(1|2|-3)$ in der x-y-Ebene.
Lichtstrahl $\vec{x}=\begin{pmatrix}3\\4\\2\end{pmatrix}+k\begin{pmatrix}-2\\-2\\-5\end{pmatrix}$

## Lagebeziehungen von Ebenen

- identisch
- parallel
- Schnittgerade

### Ebenen gegeben in Parameterform

**Beispiel**
$E_{1}: \vec{x}=\begin{pmatrix}6\\0\\4\end{pmatrix}+r\begin{pmatrix}-3\\0\\4\end{pmatrix}+s\begin{pmatrix}-3\\4\\-4\end{pmatrix}$
$E_{2}\vec{x}=\begin{pmatrix}0\\8\\0\end{pmatrix}+k\begin{pmatrix}0\\0\\4\end{pmatrix}+t\begin{pmatrix}6\\-8\\0\end{pmatrix}$

Geraden gleichsetzen
$E_{1}=E_{2}$
```python
>>> solve([] + r[] + s[] = [] + k[] + t[], r, s, k, t)
r=0 and s=(c-1) and t=(c+1)/2 and k=c
```

Parameter mit Konstante in einer der Ebenen einsetzen
$\vec{x}=\begin{pmatrix}6\\0\\4\end{pmatrix}+s\begin{pmatrix}-3\\4\\-4\end{pmatrix}$

Oder zwei Parameter mit Variable einsetzen
$\vec{x}=\begin{pmatrix}0\\8\\0\end{pmatrix}+c\begin{pmatrix}0\\0\\4\end{pmatrix}+ \frac{c+1}{2}\begin{pmatrix}6\\-8\\0\end{pmatrix}$
$\vec{x}=\begin{pmatrix}0\\8\\0\end{pmatrix}+\begin{pmatrix}3c\\ -4c-4\\4c\end{pmatrix}=\begin{pmatrix}3\\4\\0\end{pmatrix}+c\begin{pmatrix}3\\-4\\4\end{pmatrix}$
Ebenen schneiden sich!


**Beispiel**
$E_{1}:\vec{x}=\begin{pmatrix}1\\1\\1\end{pmatrix}+r\begin{pmatrix}2\\3\\1\end{pmatrix}+s\begin{pmatrix}1\\-2\\4\end{pmatrix}$
$E_{2}:\vec{x}=\begin{pmatrix}1\\1\\1\end{pmatrix}+r\begin{pmatrix}4\\6\\2\end{pmatrix}+s\begin{pmatrix}2\\-4\\8\end{pmatrix}$
```python
r=2c and s=2c and t=c and k=c
```
Die Parameter der Ebenen sich Vielfache von einander.
Ebenen sind identisch!

### Ebenen gegeben in Koordinatenform

$E_{1}:3x-2y+z=10$
$E_{2}:x+2y-2z=-2$

$E_{1}+E_{2}:4x-z=8$

Wir ersetzen einen Parameter
$4x-t=8$
$4x=8+t$
$x=2+ \frac{1}{4}t$

In Ebene einsetzen
$2+ \frac{1}{4}t+2y-2t=-2$
$2y=-4+ \frac{7}{4}t$
$y=-2+ \frac{7}{8}t$

$\vec{x}=\begin{pmatrix}2\\-2\\0\end{pmatrix}+t\begin{pmatrix} \frac{1}{4}\\ \frac{7}{8}\\1\end{pmatrix}$

Identische Ebenen sind Vielfache voneinander
$E_{1}:2x+y-3z=1$
$E_{2}:6x+3y-9z=3$

Parallele Ebenen sind keine Vielfache voneinander, aber die beiden Normalenvektoren sind vielfache
$E_{1}:2x+y-3z=1$
$E_{2}:6x+3y-9z=5$

### Ebenen in Parameter- und Koordinatenform

$E_{1}:x+2y-z=2$
$E_{2}:\vec{x}=\begin{pmatrix}1\\3\\2\end{pmatrix}+k\begin{pmatrix}3\\1\\-2\end{pmatrix}+t\begin{pmatrix}1\\4\\1\end{pmatrix}$

Parameterform in Koordinatenform einsetzen
$1+3k+t+2(3+k+4t)-(2-2k+t)=2$
$7k+8t+5=2$
$t=- \frac{3}{8}- \frac{7}{8}k$

Parameter in Parameterform einsetzen
$\vec{x}=\begin{pmatrix}1\\3\\2\end{pmatrix}+k\begin{pmatrix}3\\1\\-2\end{pmatrix}+(- \frac{3}{8}- \frac{7}{8}k)\begin{pmatrix}1\\4\\1\end{pmatrix}=\begin{pmatrix} \frac{5}{8}\\ \frac{5}{2}\\ \frac{13}{8}\end{pmatrix}+k\begin{pmatrix} \frac{17}{8}\\- \frac{5}{2}\\-3\end{pmatrix}$
