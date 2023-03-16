---
tags:
- topic/math
---

# Analysis

## Grenzwerte

### Grenzwerte Im Unendlichen

- $f(x)=\frac{1}{x²+1}$
	- $x$-Werte werden sehr klein $\to$ $y$-Werte nähern sich der $x$-Achse an
	- $x$-Werte werden sehr sehr groß $\to$ $y$-Werte nähern sich der $x$-Achse an

Nähern sich die Funktionswerte einer Funktion $f(x)$ für unbeschränkt wachsende oder fallende  $x$-Werte einer Zahl $g$ den Grenzwert der Funktion $f(x)$ für $x \to ∞$ bzw. $x\to-∞$. Die Gerade mit der Gleichung $y=g$ nennt man waagerechte Asymtote.

~~~functionplot
---
disableZoom: true
---
f(x)=1/x+2
g(x)=2
~~~

Falls $\lim\limits_{x \to +- ∞} = +∞ || -∞$ besitzt die Funktion keinen GW. Mann spricht dann dort vom Verhalten im Unendlichen.

~~~functionplot
---
disableZoom: true
---
f(x)=2x
~~~

### Potenzfunktionen (Polynomfunktionen)

Potenzfunktionen können mehrere lokale Extrempunkte haben. Dass Verhalten im Unendlichen bezeichnet man als Globalverlauf. (Ermittlung durch Ausklammern der höchsten Potenz.

**Beispiele**
$f(x)=3x³-5x²+2x+8$
$x³(3-5/x+2/x²+8/x³)=\lim\limits_{x\to∞}=x³(3-0+0+0)=3x³=∞$

$f(x)=-7x³+8x²+x-5$
$x³(-7+8/x+2/x²-5/x³)=\lim\limits_{x\to∞} x³(-7 - 0 - 0 - 0) = -7x³ = -∞$

$f(x) = x⁴ + 7x³ - 2x² + 3x + 1$
$f(x) = x⁴(1 + 7/x - 2/x² + 3/x³ + 1/x⁴)=\lim\limits_{x\to∞} x⁴(1 + 0 - 0 + 0 + 0) = x⁴ = ∞$

### Gebrochen Rationale Funktionen

**Beispiele**
$f(x) = (2x² + x - 3) / (3x² - 2x)$
$\frac{x²(2 + 1/x - 3/x²}{x²(3 - 2/x)} =\lim\limits_{x \to ∞} \frac{1(2 + 0 - 0)}{1(3 - 0)} = \frac{2}{3}$

$f(x) = \frac{2x² + x - 3}{x³ - 1}$
$\frac{x²(2 + 1/x - 3/x²}{x²(x - 1/x )} = \lim\limits_{x \to ∞} \frac{1(2 + 0 - 0)}{1(x - 0)} = \frac{2}{x} = 0$

$f(x) = \frac{x³ - 1}{2x² + x - 3}$
$\frac{x²(x - 1/x)}{x²(2 + 1/x - 3/x²)} =\lim\limits_{x \to ∞} \frac{1(x -0)}{1(2 + 0 - 0)} = \frac{x}{2} = ∞$

$f(x)=\frac{3x²-5x}{2x²+1}$
$\frac{x²(3-5/x²)}{x²(2+1/x³)}=\lim\limits_{x\to+-\infty}\frac{3-0}{2+0}=\frac{3}{2}$

$f(x)=\frac{2x²+3}{5x-x²}$
$\frac{x²(2+3/x²)}{x²(5/x-1)}=\lim\limits_{x\to+-\infty}\frac{2+0}{0-1}=-2$

$f(x)=\frac{x²+7}{2x³-x}$
$\frac{x²(1+7/x²)}{x²(2x-1/x)}=\lim\limits_{x\to+-\infty}\frac{1}{2x}=\lim\limits_{x\to+-\infty}0$

$f(x)=\frac{2x³-x}{x²+7}$
$\frac{x²(x-1/x)}{x²(1+7/x²)}=\lim\limits_{x\to\infty}\infty=\lim\limits_{x\to-\infty}-\infty$

$f(x)=\frac{6x²+4}{2x+2}-3x$
$\frac{6x²+4}{2x+2}-\frac{6x²+6x}{2x+2}=\frac{4-6x}{2x+2}=\frac{x(4/x-6)}{x(2+2/x)}=\lim\limits_{x\to\infty}-\frac{6}{2}=-3$

$f(x)=\frac{2}{\sqrt{x}}$
$\lim\limits_{x\to\infty}\frac{2}{\infty}=0$
$\lim\limits_{x\to-\infty}=n.d.$

### Exponentialfunktionen

~~~functionplot
---
disableZoom: true
---
f(x)=exp(x)
~~~

- schneidet die $y$-Achse immer bei $1$
- $\lim\limits_{x\to-\infty}e^x=0$
- $\lim\limits_{x\to\infty}e^x=\infty$

~~~functionplot
---
disableZoom: true
---
f(x)=exp(x*(x^2-4))
~~~

- $\lim\limits_{x\to-\infty}f(x)=0$
- $\lim\limits_{x\to\infty}f(x)=\infty$

~~~functionplot
---
disableZoom: true
---
f(x)=exp(-x)
~~~

- $\lim\limits_{x\to-\infty}f(x)=\infty$
- $\lim\limits_{x\to\infty}f(x)=0$

~~~functionplot
---
disableZoom: true
---
f(x)=-2.71828182846^x
~~~

**Beispiele**
- $\lim\limits_{x\to-\infty}f(x)=0$
- $\lim\limits_{x\to\infty}f(x)=\infty$

$f(x)=5^x$
$\lim\limits_{x\to-\infty}0$
$\lim\limits_{x\to\infty}\infty$

$f(x)=3^{-x}$
$\lim\limits_{x\to-\infty}\infty$
$\lim\limits_{x\to\infty}0$

$f(x)=\frac{2}{3}^x$
$\lim\limits_{x\to-\infty}=\infty$
$\lim\limits_{x\to\infty}=0$

~~~functionplot
---
disableZoom: true
---
f(x)=(2/3)^x
~~~

$f(x)=3^x*2^{-x}$
$3^x*2^{-x}=3^x=\frac{1}{2^x}$
$\lim\limits_{x\to-\infty}0$
$\lim\limits_{x\to\infty}\infty$

### $\sin$-Funktionen

~~~functionplot
---
bounds: [-10,10,-2,2]
disableZoom: true
---
f(x)=sin(x)
~~~

Funktion hat keinen Grenzwert.

### Grenzwert an Einer Stelle

Eine Funktion $f$, die beiderseits einer Stelle $x_0$ definiert ist, hat für $x\to x_0$ den GW $a$, wenn gilt $\lim\limits_{h\to 0}f(x_0+h)=a$ mit $h>0$ und $\lim\limits_{h\to 0}f(x_0-h)=a$ mit $h>0$.

**Beispiele**
$f(x)=x²+3$
 $\lim\limits_{x\to2}f(x)=7$

$f(x)=\frac{x²-4}{x-2}$
$\lim\limits_{x\to2}\frac{(x+2)(x-2)}{x-2}=\frac{x+2}{1}=4$

$f(x)=\frac{2x+3}{x-2}$
$\lim\limits_{x\to2^{(+)}}\infty$
$\lim\limits_{x\to2^{(-)}}-\infty$

$f(x)=\frac{2x+1}{x+1}$
$\lim\limits_{x\to-1^{(+)}}-\infty$
$\lim\limits_{x\to-1^{(-)}}\infty$

### Ermitteln Des GW Durch Die $h$-Methode

$f(x)=\frac{x²-4}{x-2}$
$\lim\limits_{x\to2h\to0}\frac{(x+h)²-4}{(x+h)-2}=\frac{(2+h)^2-4}{(2+h)-2}=\frac{h²+4h}{h}=\frac{h(h+4)}{h(1)}=4$

### Grenzwertsätze

- aus $\lim\limits_{x\to\infty}f(x)=\infty$ folgt $\lim\limits_{x\to\infty}f(x)=\frac{1}{f(x)}=0$
- $\lim\limits_{x\to\infty}\frac{a}{x^n}=0\quad(a=const)$
- $\lim\limits_{x\to\infty}\frac{x^n}{a^x}=0\quad(n\in\mathbb{R},a=const)$

## Stetigkeit

- Eine Funktion $f$ ist in einem offenen Interfall definiert und $a$ eine beliebiege Stelle im Intervall
- Die Funktione $f$ heißt an der Stelle $a$ stetig, falls:
	1. GW an der Stelle $a$ exestiert
	1. GW an der Stelle $a$ stimmt mit Funktionswert an der Stelle a überein
- Ist entweder (1) oder (2) oder beide nicht erfüllt, ist die Funktion unstetig an der Stelle a.
- Eine Funktion heißt stetig, wenn sie an jeder Stelle ihres DB stetig ist.

- $f(x)=x²$, Funktion ist überall stetig.
- $f(x)=\begin{cases}x&\quad-\infty<x<0\\x+1&\quad0\leq x<\infty\end{cases}$, Funktion ist an der Stelle $x=0$ nicht stetig, da linksseitiges und rechtseitiges GW nicht übereinstimmen.
- $f(x)=\frac{x²-4}{x-2}$, Funktion ist nicht stetig, da bei $x=2$ kein Funktionswert existiert. Art der Unstetigkeit: Definitionslücke
- $f(x)=\frac{1}{x²}$, Funktion ist nicht stetig, da kein GW existiert, da bei $x=0$ kein GW und auch kein Funktionswert existiert. Art der Unstetigkeit: Polstelle
-  Vereinfachung: Eine Funktion ist dann stetig, wenn sie ohne abzusetzen zu zeichen ist.

## Ableitungen

### Ableitung Einer Funktion an Einer Stelle

- Sekante: Schneidet an zwei Punkten
- Passante: Schneidet an keinem Punkt
- Tangente: Schneidet an einem Punkt

### Lage Von Tangenten an Funktionsgraphen

- Tangenten und Funktionsgraph haben nur den einen Berührungspunkt gemeinsam.
- Die Tangente geht durch den geht durch den Punkt hindurch.
- Die Tangente schneidet den Graphen an weiteren Punkten.
- Die Tangente berührt den Graphen in einem weiteren Punkt

### Differenzenquotient

Gesucht: Anstieg der Tangente in einem Punkt $P(1|f(1))$

~~~functionplot
---
disableZoom: true
---
f(x)=x^2
g(x)=3x-2
~~~

$m=\frac{y_2-y_1}{x_2-x_1}=\frac{4-1}{2-1}=3$

### Differenzialquotient

Der Grenzwert $h\to0$ liefert den Anstieg der Tangente im Punkt $x_0$.
$m=\lim\limits_{h\to0}\frac{f(x_0+h)-f(x_0)}{h}$

**Beispiel**
$f(x)=\frac{1}{4}x^2$

~~~functionplot
---
disableZoom: true
---
f(x)=1/4x^2
~~~

$m=\lim\limits_{h\to0}\frac{1/4(x+h)^2-1/4}{h}=\lim\limits_{h\to0}\frac{1/4(1+2h+h²)-1/4}{h}=\lim\limits_{h\to0}\frac{2h+1/4h²}{h}=\lim\limits_{h\to0}1/2+1/4h=\lim\limits_{h\to0}1/2$
$f(x)=\frac{1}{4}x²\quad f'(x)=\frac{1}{2}x$
- Durchschnittliche Änderungsrate: Anstieg der Sekante
- Momentane Änderungsrate: Anstiege der Tangente

### Durchschnittliche Und Momentane Änderungsrate

- Durchschnittliche Änderungsrate: Differenzenquotient
- Momentane Änderungsrate: Differentialquotient (Ableitung)


$f(x)=x^3-6x^2+8x$

Durchschnittliche Änderungsrate von $x_0=1$ und $x_1=3$
$f(1)=3$
$f(3)=-3$
$m=\frac{f(3)-f(1)}{3-1}=\frac{-6}{2}=-3$

Momentane Änderungsrate $x_0=2$
$f'(x)=3x²-12x+8$
$f'(2)=-4$

### Anstiegswinkel

**Beispiel**
$f(x)=x^2$
Gesucht ist $\measuredangle$, den die Tangente an $f$ in $x=3$ mit der $x$-Achse einschließt.
$\tan{a}=\frac{G_k}{A_k}=m=f'(x)$

### Funktionen Mit Stellen, an Denen Keine Ableitung Existiert

- Bsp.: $f(x)=|x^2-1|$
~~~functionplot
---
disableZoom: true
---
f(x)=abs(pow(x,2)-1)
~~~

Knick bei $x=1$ und $x=-1$
→ $m$ nicht eindeutig bestimmbar
von rechts bei $x=1$: $m=2$
von links bei $x=1$: $m-2$

→ Es gibt keine Ableitung an den Stellen x=1 bzw. x=-1. Also gibt es an diesen Stellen auch keine Tangente.
- Definition:
	- Eine Funktion heißt differenzierbar, an der Stelle a, falls der GW $\lim\limits_{x\to a}\frac{f(x)-f(a)}{x-a}$ existiert.
	- Dieser GW ist die Ableitung $f'(a)$ der Funktion $f$ an der Stelle $a$.
	- Existiert der GW nicht, so heißt die Funktion nicht differenzierbar an der Stelle $a$.

### Herleitung Der Ableitungsregel Für Potenzfunktionen

- Bsp.: $f(x)=x²$
	- $f'(x_0)=\lim\limits_{h\to0}\frac{f(x_0+h)-f(x_0)}{h}$
	- $=\lim\limits_{h\to0}\frac{(x_0+h)^2-x_0^2}{h}=\lim\limits_{h\to0}\frac{2xh+h²}{h}=\lim\limits_{h\to0}2x_0+h=\lim\limits_{h\to0}2x_0$
- Bsp.: $f(x)=2x²$
	- $f'(x_0)=\lim\limits_{h\to0}\frac{f(x_0+h)-f(x_0)}{h}$
	- $=\lim\limits_{h\to0}\frac{2(x_0+h)^2-2x_0^2}{h}=\lim\limits_{h\to0}\frac{4xh+2h²}{h}=\lim\limits_{h\to0}2x_0+h=\lim\limits_{h\to0}4x_0$
- Bsp: $f(x)=x³$
	- $f'(x_0)=\lim\limits_{h\to0}\frac{f(x_0+h)-f(x_0)}{h}$
	- $=\lim\limits_{h\to0}\frac{x_0³+3x_0²h+3x_0h²-x_0³}{h}=\lim\limits_{h\to0}3x_0²+3x_0+h+h²=\lim\limits_{h\to0}3x_0²$

### Ableitungsregeln

| Funktion                           |                                               Ableitung |
|:---------------------------------- | -------------------------------------------------------:|
| $f(x)=n$                           |                                               $f'(x)=0$ |
| $f(x)=nx$                          |                                               $f'(x)=n$ |
| $f(x)=x^n$                         |                                        $f'(x)n*x^{x-1}$ |
| $f(x)=\frac{1}{x}=x^{-1}$          |                          $f'(x)=-1x^{-2}=-\frac{1}{x²}$ |
| $f(x)=e^x$                         |                                             $f´(x)=e^x$ |
| $f(x)=n*g(x)$                      |                                         $f'(x)=n*g'(x)$ |
| $f(x)=g(x)+h(x)$                   |                                     $f'(x)=g'(x)+h'(x)$ |
| $f(x)=g(x)*h(x)$                   |                           $f'(x)=g'(x)*h(x)+h'(x)*g(x)$ |
| $f(x)=\sqrt{x}=x^\frac{1}{2}$      | $f'(x)=\frac{1}{2}x^{-\frac{1}{2}}=\frac{1}{2\sqrt{x}}$ |
| $f(x)=\sqrt[m]{x^n}=x^\frac{n}{m}$ |                          $f'(x)=\frac{n}{m\sqrt[m]{x}}$ |
| $f(x)=\ln{x}$                      |                                     $f'(x)=\frac{1}{x}$ |
| $f(x)=\sin{x}$                     |                                         $f'(x)=\cos{x}$ |
| $f(x)=\cos{x}$                     |                                        $f'(x)=-\sin(x)$ |
| $f(x)=g(h(x))$                     |                                        $f'(g(x))*g'(x)$ |

### Logarithmusfunktion

Logarithmen ist bei Aufgabenstellungen notwendig, bei denen die gesuchte Größe im Exponenten steht,

**Beispiel**
$3^x=81\quad x=\log_3 81$

$\ln{x}$ ist die Unkehrfunktion zur $e$-Funktion.

~~~functionplot
---
bounds: [-3, 10, -3, 10]
disableZoom: true
---
f(x)=exp(x)
g(x)=log(x)
~~~
$\text{DB }x\in\mathbb{R}\quad\text{NSt: }x_N=1$

### Ableitungsfunktionen Mithilfe Der Differentialrechnung

Unter der Ableitungsfunktion einer Funktion $f$ versteht man die Funktion $f'$, welche der Zahl $x$ die Steigung der Tangente im Punkt $P(x|f(x))$ des Graphen $f$ zuordned.

**Beispiel**
$f(x)=\frac{1}{3}x^3-x^2-3x+2$
$f'(x)=x^2-2x-3$

~~~functionplot
---
disableZoom: true
---
f(x)=1/3x^3-x^2-3x+2
f'(x)=x^2-2x-3
~~~
- Extremstellen von $f$ sind $\text{NSt}$ von $f'$
- Ist $f$ monoton steigend/fallend, verläuft $f'$ oberhalb/unterhalb der $x$-Achse

### Tangenten an Funktionsgraphen

1. Die Tangente ist eine Gerade ($y=mx+n$).
1. Die Tangente hat mit dem Funktionsgrahen den Berührungspunkt gemeinsam.
1. Im Berührungspunkt ist der Anstig der Tangente gleich dem Anstieg des Funktionsgraphen.

**Beispiel**
$f(x)=x^2$

Gleichung der Tangente an $f(x)$ in $P(1|f(1))$

1. y-Koordinate berechnen durch einsetzen der x-Koordinate in die Funktionsgleichung.
	- $f(1)=1$ $\to$ $P(1|1)$
1. Anstieg berechnen (1. Ableitung der Funktion)
	- $m$ berechnen: $f'(x)=x^2$, x in $f'(1)=2*1=2$
1. $y=mx+n$
	- $n$ berechnen: $1+2*1+n\quad n=-1$
1. Tangentengleichung angeben
	- $y=2x-1$

~~~functionplot
---
disableZoom: true
---
f(x)=x^2
g(x)=2x-1
~~~

### Tangenten Zur Parrallele

Beispiel $f(x)=-x^2+x+4$. Parallel zur Geraden $g(x)=-x+1$ verläuft eine Tangente an die Funktion f. Ermittle eine Gleichung dieser Tangente.

1. Ableitung von $f$: $f'(x)=-2x+1$
2. $m=-1$ einsetzen: $-1=-2x+1\quad x=1$
3. $y$ berechnen: $y=-(1)^2+1+4=4$
4. $n$ berechnen: $4=-1*1+n\quad n=5$
5. Tangentengleichung angeben
	- $y=-x+5$

~~~mermaid
graph LR
	A[menu]-->A0[4: Analysis]-->A00[1: Ableitung]
	A[menu]-->A1[3: Algebra]-->A10[1: Löse]
~~~

~~~js
solve(...)
tangentline(f(x), x, 3))
~~~

### Tangenten Zum Punkt

Beispiel $f(x)-\frac{1}{4}x^2$. Vom Punkt $Q(0|2)$ werden Tangenten an $f$ gelegt. Ermittle die Gleichung der Tangenten.

$m=f'(x_B)$
$m=\frac{y_2-y_1}{x_2-x_1}=\frac{2-y_B}{0-x_B}$
$f'(x_B)=\frac{2-f(x_B)}{-x_B}$

~~~js
f(x):= ...
f1(x):= ...
solve(f1(x)=(2-f(x))/(-x), x)
tangentline(f(x), x, 2 sqrt(2))
tangentline(f(x), x, -2 sqrt(2))
~~~

### Normale

Die Normale steht senkrecht auf der Tangente. Damit gilt: $m_n=-\frac{1}{m_t}$.

~~~functionplot
---
disableZoom: true
---
f(x)=(2/1)x
t(x)=-(1/2)x-2.5
~~~

Gegeben ist die Funktion $f(x)=x^2-4$. Gesucht ist die Gleichung der Normalen am Punkt $P(1|f(1))$.

1. Ermittlung der y-Koordinate durch einsetzen der x-Koordinate in $f(x)$
	- $f(1)=1²-4=-3$ => $P(1|-3)$
1. Ermittlung des Anstiegs der Tangente im Punkt $P$.
	- $f'(x)=2x$
	- $m_n=-\frac{1}{f'(x)}=-\frac{1}{2}$
1. Einsetzen des Punktes und des Anstiegs in die allgemeine Geradengleichung.
	- $y=mx+n$
	- $-3=-\frac{1}{2}*1+n$
	- $n=-2.5$
1. Normalgleichung aufschreiben
	- $y=-\frac{1}{2}x-2.5$


~~~mermaid
graph LR
	A[menu]-->A0[4: Analysis]-->A00[A: Normalterm]
~~~

~~~js
normalline(f, x, s)
~~~

## Eigenschaften Von Funktionen

### Achsen

- $x$-Achse: Abzissenachse
- $y$-Achse: Ordinatenachse
- $z$-Achse: Applikatenachse

### Nullstellen

Funktion $0$ setzen.
$0=f(x)$

#### Vielfachheit Von NSt

$f(x)=x^2-4$
$0=x^2-4$
$4=x^2$
$x_1=2$
$x_1=-2$

Funktionsgraph schneidet die x-Achse bei $x=-2$ und $x=2$

- - -

$f(x)=x^2-2x+1$
$0=x^2-2x+1$
$x_{1,2}=1\pm\sqrt{1-1}$
$x_1=1$
Funktionsgraph berührt die $x$-Achse bei $x=1$. 
→ Extremstelle

### Schnittpunkt Mit Der $Y$-Achse

Bei der Funktion $0$ einsetzen.
$y=f(0)$

### Definitionsbereich

Teilen durch $0$.
$f(x)=\frac{n}{x}$
Wurzeln mit Werten unter $0$.
$f(x)=\sqrt{x}$
Logarithmus mit Werten unter $0$

Einschränkungen durch die Aufgabenstellung

### Wertebereich

### Asymptoten

#### Waagerechte Asymptoten

Berechnung über den Grenzwert im Unendlichen.

**Beispiel**
$f(x)=\frac{2x^2-1}{x-x^2}$
$\lim\limits_{x\to\pm\infty}f(x)=-2$

Die waagerechte Asymptote hat also die Gleichung $y=-2$.

#### Senkrechte Asymptoten

Senkrechte Asymptoten sind Polstellen. Polstellen sind die Definitionslücken gebrochen-rationaler Funktionen. Man ermittelt sie, indem man den Nenner gleich $0$ setzt.

**Beispiel**
$f(x$)$=-\$frac{x^2-4}{x+1}$
$0=x+1\quad x=-1$

Die senkrechte Asymptote in unserem Beispiel hat also die Gleichung $x=-1$.

#### Schräge Asymtoten

Sie existieren.

### Symmetrie

#### Achsensymmetrie

Achsensymmetrie zur $y$-Achse: $f(x)=f(-x)$

~~~functionplot
---
disableZoom: true
bounds: [-8,12,-4,16]
---
f(x)=(x-2)^2
~~~

#### Punktsymmetrie

$f(x)=-f(-x)$
$-f(x)=f(-x)$

~~~functionplot
---
disableZoom: true
---
f(x)=x^3
~~~

**Beispiele**
$f(x)=2x^3+4x$
$-f(-x)=-(2(-x)^3+4(-x))$
$-f(-x)=-(-2x^3-4x)$
$-f(x)=2x^3+4x$

$f(x)=\frac{x^2-2x}{x^4}$
$-f(-x)=(\frac{(-x)^2-2(-x)}{(-x)^4})$
$-f(-x)=-(\frac{x^2+2x}{x^4})$
$-f(-x)=\frac{-x^2-2x}{x^4}$

Für ganzrationale Funktionen gilt: 
- nur geradzahlige Exponenten: achsensymmetrisch zur $y$-Achse
- nur ungeradzahlige Exponenten: punktsymmetrisch zum Koordinatenursprung

### Extrempunkte / Extremstellen

~~~functionplot
---
bounds: [-4, 4, -2, 2]
---
f(x)=-0.01x^3*(x-2)*(x+3)^2*(x^2+1)
~~~

An Extremstellen gilt: 
- $f'(x)=0$ (notwendig)
- $f''(x)!=0$ (hinreichend)

**Beispiel**
$f(x)=x^2-2x+1$
$f'(x)=2x-2$
$f''(x)=2$

$0=2x-2\to x=1$

#### Nachweis Der Art Des Extremus

- Minimum: $f''(x_E)>0$
- Maximum: $f''(x_E)<0$
oder
- Minimum: $f'(x)=-\to f'(x)=+$
- Maximum: $f'(x)=+\to f'(x)=-$

~~~functionplot
f(x)=x^2
~~~

**Beispiel**
$f(x)=x^2$
$f'(x)=2x$
$f''(x)=2$

$0=2x_E\quad x_E=0$

Mimimum, da:
- $f'(-1)=-2$
- $f(1)=2$

#### Absolute Extrema

Ist $f$ in einem abgeschlossenen Intervall $[a, b]$ definiert, so ergeben sich die absoluten Extrema, indem man die relativen Extrema bestimmt und mit den Funktionswerten am Rand vergleicht (Randwerte).

### Wendepunkte / Wendestellen

Ist $f$ im Intervall $]a,b[$ differenzierbar und geht der Graph $f$ beim Durchlaufen eines Punktes $W(x_W|y_W)$ von einer Rechtskurve in eine Linkskurve (oder umgekehrt) über, so heißt $W$ ein Wendepunkt und die Stelle $x_W$ eine Wendestelle von $f$.

Die Tangent in $W$ heißt Wendetangente. Ein Wendepunkt mit horizontaler Tangente heißt Sattelpunkt (Terassenpunkt).

- notwendige Bedingung: $f''(x)=0$
- hinreichende Bedingung: $f'''(x)\neq0$

**Beispiel**
$f(x)=x^4-x^3+x$
$f'(x)=4x^3-3x^2+1$
$f''(x)=12x^2-6x$
$f'''(x)=24x-6$

$0=12x^2-6x$
$x_1=0$
$x_2=\frac{1}{2}$

$f'''(0)=-6$
$f'''(\frac{1}{2})=6$

## Extremwertaufgaben

= Aufgabenstellungen, bei denen eine Größe einen extremalen Wert annehmen soll.
(Min oder Max)

Muster für die Lösung von Extremwertaufgaben
1. Aufstellen einer Gleichung für die Größe, die einen extremalen Wert annehmen soll. (Hauptbedingung)
1. Formulieren der Nebenbedingungen (Gleichungen, die berücksichtigt werden müssen)
1. Aufstellen der Zielfunktion durch Einsetzen der Nebenbedingung in die Hauptbedingung
1. Ermitteln der Stelle, für die die Zielfunktion maximal oder minimal wird

## Steckbriefaufgaben

Bestimmen von ganzrationalen Funktionen anhand gegebener Eigenschaften
= Umkehrung der Kurvendiskussion

1. Gesuchte Funktionsgleichung in allgemeiner Form aufschreiben und die 1. und 2. Ableitung bilden.
1. Gegebene Bedingungen in Gleichungen für die unbekannten Koeffizienten übersetzen
1. Lineares Gleichungssystem Lösen

**Beispiel**
Gesucht ist die Gleichung einer ganzrationalen Funktion 4. Grades, deren Graph im Nullpunkt des Koordinatensystems die Wendetangente mit der Gleichung y=x hat und in Punkt $P(2|4)$ die Steigung 0 hat.
- $f(x)=ax^4+bx^3+cx^2+dx+e$
- $f'(x)=4ax^3+3bx^2+2cx+d$
- $f''(x)=12ax^2+6bx+2c$

1. $f''(x)=0$
1. $f(0)=0$
1. $f(2)=4$
1. $f'(2)=0$
1. $f'(0)=1$

$$\begin{pmatrix*}[l]
  0=e \\
  0=2c \\
  4=16a+12b+4c+2d+e \\
  0=32+a+12b+4c+d \\
  1=d
 \end{pmatrix*}
 =\begin{pmatrix*}[l]
  a=-0.5 \\
  b=1.25 \\
  c=0 \\
  d=1 \\
  e=0
 \end{pmatrix*}$$

## Ortskurven
Kurven, die durch bestimmte Orte einer Funktionsschar gehen. (Maximum, Minimum, Wendepunkt).

1. Berechnung der x- und y-Koordinate in Abhängigkeit vom Parameter für die gesuchte Eigenschaft.
2. Umstellen der x-Koordinate nach dem Parameter.
3. Einsetzen des Parameters in die y-Koordinate und ggf. zusammenfassen.

**Beispiel**
Für jeden Wert $k$ ($k\in\mathbb{R},k>0$) ist die Funkion $f_k$ gegeben mit $f_k(x)=(k-2x)*e^x (x\in\mathbb{R})$. Gesucht ist die Ortkurve die durch alle lokalen Extrempunkte geht.
1. 
$f_k'(x)=(k-2x)*e^x+-2e^x$
$0=e^x(k-2x-2)$
$0=-2+k-2x$
$2x=-2+k$
$x=-1+\frac{k}{2}$
$y=(k-2x)e^x$
2.
$x=-1+\frac{k}{2}$
$x+1=\frac{k}{2}$
$2x+2=k$
3.
$y=2e^x$

# Matrizen

Eine Matrix ist eine Anordnung von Zahlen in Tabellenform. Matritzen werden mit Großbuchstaben bezeichnet

$\begin{pmatrix}a_{1,1}&a_{1,2}&\cdots&a_{1,n}\\a_{2,1}&a_{2,2}&\cdots&a_{1,n}\\ \vdots&\vdots&\ddots&\vdots \\ a_{m,1}&a_{m,2}&\cdots&a_{m,n}\end{pmatrix}$

## Addition Und Subtraction

Addition und Subtraktion von Matrizen ist nur möglich, wenn beide Matrizen denselben Rang haben. Man addiert beziehungsweise subtrahiert die einzelnen Elemente.

## Skalarmultiplikation

Jedes Element des Skalars wird mit dem Skalarprodukt multipliziert.

## Transponierte

Man erhält die Transponierte zu einer Matrix, indem man Zeilen und Spalten vertaucht.

$\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}^T=\begin{pmatrix}1&4\\2&5\\3&6\end{pmatrix}$

## Matrizenmultiplikation

Matrizenmultiplikation ist nur dann möglich, wenn die 1 Matrix so viele Spalten hat, wie die 2. Matrix Zeilen hat.

## Einheitsmatrix

$\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}$

# Vektoren

# Stochastik

Auch Binomialverteilte Zufallsgrößen (BV ZG)

## Klassische Wahrscheinlichkeit

**Beispiel**
Idealer Würfel $P(X=6)=\frac{1}{6}$

## Pfadregeln

Mehrstufiges Zufallsexperiment

**Beispiel**
4 rote und 8 blaue Kugeln

~~~mermaid
graph TB;
	A[ ]
	A-->A0[rot]
	A-->A1[blau]
	A0-->A00[rot]
	A0-->A01[blau]
	A1-->A10[rot]
	A1-->A11[blau]
~~~
$X$ Anzahl der roten Kugeln

### Pfadmultiplikatiosregel

Bei mehrstufigen ZV ist die Wahrscheinlichkeit eines Ereignisses gleich dem Produkt der Wahrscheinlichkeit längs des zugehörigen Pfades.

**Beispiel**
$P(X=2)=\frac{4}{12}*\frac{4}{12}$

### Pfadadditionsregel

Setzt sich bei einem mehrstufigen Zufallsexperiment ein Ereignis aus verschiedenen Pfaden zusammen, erhält man die Wahrscheinlichkeit., durch Addition der einzelnen Pfad-Wahrscheinlichkeit

**Beispiel**
$P(X=1)=\frac{4}{12}*\frac{8}{12}+\frac{8}{12}*\frac{4}{12}=\frac{4}{9}$

### Ziehen Ohne Zurücklegen

Beim ziehen ohne Zurücklegen ändern sich in den folgenden Stufen des Zufallsexperimentes die Wahrscheinlichkeiten.

### Komplementärregel

Ereignis + Gegenergeignis = 1 $P(A)+P(\bar{A})=1$

**Beispiel**
$P(X\geq1)\geq1-P(X=0)$
$1-P(X=0)=1-\frac{8}{12}*\frac{8}{12}=1-\frac{2}{3}*\frac{2}{3}=1-\frac{4}{9}=\frac{5}{9}$

## Fakultät

$n!=n*(n-1)*(n-2)*\dots*1$

**Beispiel**
$5!=5*4*3*2*1=120$
$4!=4*3*2*1=24$

### Abzählverfahren

**Beispiel**
Pferderennen, 12 Pferde
Einlauf  der ersten 3 Pferde soll vorausgesagt werden.

## Satz über die total Wahrscheinlichkeit

Ereignisse $A$ und $B$.
$P(B)=P(A)*P_{A}(B)+P(\bar{A})*P_{\bar{A}}(B)$

~~~mermaid
graph TB;
	A[ ]
	A-->A0[rot]
	A-->A1[blau]
	A0-->A00[rot]
	A0-->A01[blau]
	A1-->A10[rot]
	A1-->A11[blau]
~~~

## Satz von Bayes

$P_B(A)=\frac{P(A\cap B)}{P(A)*P_{A}(B)+B(\bar{A})*P_{\bar{A}}(B)}$

## Darstellung bedingter Wahrscheinlichkeit mithilfe einer Vierfeldertafel

**Beispiel**
Ein Schüler fährt an $50\%$ der Schultage mit dem Bus. In $70\%$ dieser Fälle kommt er pünktlich. Durchschnittlich kommt er an $60\%$ der Tage pünktlich. Heute kommt der Bus Pünktlich. Mit welcher Wahrscheinlichkeit hat er den Bus benutzt?

|           | $B$    | $\bar{B}$ | Total |
| --------- | ------ | --------- | ----- |
| $P$       | $0.35$ | $0.25$    | $0.6$ |
| $\bar{P}$ | $0.15$ | $0.25$    | $0.4$ |
| Total     | $0.5$  | $0.5$     | $1$   |

$P_{P}(B)=\frac{0.35}{0.6}$

Heute fährt er nicht mit dem Bus. Mit welcher Wahrscheinlichkeit kommt er zu spät?

$P_\bar{B}(\bar{P})=\frac{0.25}{0.5}$

$P(B\cap P)=0.35\quad P(B\cap\bar{P})=0.15$

## Unabhängigkeit zufälliger Ereignisse

Zwei Ereignisse $A$ und $B$ heißen stochastich voneinander unabhängig genau dann, wenn gilt $P_{A}(B)=P(B)$ und $P_{B}(A)=P(A)$

### Multiplikationssatz

Sind A und B stochastisch voneinander unabhängig, dann gilt: $P(A\cap B)=P(A)*P(B)$

**Beispiel**
Tankstellenbesitzer Til weiß aus Erfahrung, dass $30\%$ seiner Kunden Superbenzin tanken, wobei $40\%$ von diesen die Automarke M fahren.
Außerdem weiß er, dass $42\%$ aller seiner Kunden weder Fahrer der Automarke M sind, noch Super tanken.

|           | $S$    | $\bar{S}$ | Total |
| --------- | ------ | --------- | ----- |
| $M$       | $0.12$ | $0.28$    | $0.4$ |
| $\bar{M}$ | $0.18$ | $0.42$    | $0.6$ |
| Total     | $0.3$  | $0.7$     | $1$   |

$P(A\cap B)=P(M)*P(S)=0.4*0.3=0.12$
