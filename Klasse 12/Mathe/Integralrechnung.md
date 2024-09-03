# Integralrechnung

Näherungswerte kann der Flächeninhalt mithilfe von Balken durch Kästchenzählen berechnet werden.

## Orientierter Flächeninhalt

Flächeninhalt zwischen Funktionsgraph und $x$-Achse können eine Konkrete Bedeutung haben
➡️ Kennzeichnung: $+A$ oder $-A$

Bei orientiertem Flächeninhalt sind Flächen oberhalb der $x$-Achse mit positivem Vorzeichen und unterhalb der $x$-Achse mit negativem Vorzeichen versehen.

Geometrische Bedeutung des Integrals: Summe der orientierten Flächeninhalte

> ⚠️ Die Summe der orientierten Flächeninhalte zwischen den Graphen einer Funktion $f$ und der $x$-Achse im Intervall $[a:b]$ ist das Integral von $a$ bis $b$ der Funktion $f$.

### Näherungsweise Berechnen von Integralen

**Beispiel**
$f(x)=x^{2}$
$\int^{2}_\limits{0}x^{2}\cdot\text{d}x$

➡️ Zerlegung der Fläche in Trapeze

Der Fehler wird umso kleiner, je größer die Zerlegung ist.

### Untersumme und Obersumme

![](Working%20Materials/Integrale/Unter%20&%20Obersumme.png)

Anzahl Rechtecke $n$
$\lim\limits_{n\to\infty}U_{n}=\lim\limits_{n\to\infty}O_{n}=\int\limits_{a}^{b}f(x)\text{d}x$

### Hauptsatz der Differential- und Integralrechnung

Eine stetige Funktion $f$ ist die Ableitung der Integralfunktion $I$. Es gilt $I'(x)=f(x)$.
➡️ Integriert man eine Funktion und differenziert man sie anschließend wieder, so erhält man die Ausgangsfunktion.

## Stammfunktion und unbestimmtes Integral

Integrieren und Differenzieren sind also entgegengesetzte Rechenoperatoren.

### Integration mithilfe der Stammfunktion

Eine Funktion $F$ heist Stammfunktion zu einer gegeben Funktion $f$, wenn $f$ die Ableitung von $F$ ist ($f=F'$).

### Bilden von Stammfunktionen

$\int x^{3}\mathtt{d}x=\frac{1}{4}x^{4}$
$\int \sqrt{x}\mathtt{d}x=\int x^{\frac{1}{2}}\mathtt{d}x=\frac{2}{3}x^{\frac{3}{2}}=\frac{2}{3}\sqrt{x^{3}}$

Konstanten fallen beim Ableiten weg. Jede reelle Zahl kann als Konstante an die Stammfunktion angefügt werden. Das bedeutet, dass jede Funktion unendlich viele Stammfunktionen hat.

### Ermitteln von Stammfunktion

| Funktion               | Integral                              |
| ---------------------- | ------------------------------------- |
| $f(x)=0$               | $F(x)=c$                              |
| $f(x)=n$               | $F(x)=nx$                             |
| $f(x)=nx$              | $F(x)=\frac{n}{2}x^{2}$               |
| $f(x)=x^{n}$           | $F(x)=\frac{1}{n+1}x^{n}$             |
| $f(x)=\sqrt[m]{x^{n}}$ | $F(x)=\frac{m+n}{m}\sqrt[m]{x^{m+n}}$ |
| $f(x)=\frac{1}{x}$     | $F(x)=\ln{x}$                         |
| $f(x)=e^{x}$           | $F(x)=e^{x}$                          |
| $f(x)=a^{x}$           | $F(x)= \frac{1}{\ln{a}}a^{x}$         |
| $f(x)=n\cdot g(x)$     | $F(x)=n \cdot G(x)$                   |
| $f(x)=g(x)\pm h(x)$    | $F(x)=G(x)\pm H(x)$                   |
| $f(x)=g(mx+n)$         | $F(x)= \frac{1}{m}G(mx+n)$            |
| $f(x)=\sin{x}$         | $F(x)=-\cos{x}$                       |
| $f(x)=\cos{x}$         | $F(x)=\sin{x}$                        |

## Das bestimmte Integral

$$\int\limits_{a}^{b}f(x)\;\mathrm{d}x=F(b)-F(a)$$ 
Ist eine Funktion $F$ in einem Interfall $I$ stetig und $F$ eine Stammfunktion von $f$, dann gilt $\forall a,b\in I$ die Gleichung $\int\limits_{a}^{b}f(x)\;\mathrm{d}x=F(b)-F(a)$.

### Vorgehensweise beim Berechnen bestimmter Integrale

1. Ermitteln einer Stammfunktion $F$ und $f$
2. Bestimmung der Randwerte $F(a)$ und $F(b)$
3. Bildung der Differenz $F(b)-F(a)$

$$\int\limits_{a}^{b}=[F(x)]_{a}^{b}=F(b)-F(a)$$

**Beispiel**
$\int\limits_{1}^{3}x^{2}\;\mathrm{d}x=[\frac{1}{3}x^{3}]_{1}^{3}=\frac{1}{3}3^{3}- \frac{1}{3}1^{3}=\frac{26}{3}$

### Berechnung von Flächeninhalten

**Beispiel**
Gesucht wird die Fläche, die von der Funktion $f(x)=-x^{2}+4x$ und der x-Achse eingeschlossen wird.

Nullstellen berechnen
$-x^{2}+4x=0$
$x=0$
$x^{2}=4x$
$x=4$

$\int\limits_{0}^{4}-x^{2}+4x\;\mathrm{d}x=[- \frac{1}{3}x^{3}+2x^{2}]_{0}^{3}=- \frac{1}{3}4^{3}+2\cdot4^{2}=\frac{32}{3}$

**Bedingungen**
- Fläche ist oberhalb der x-Achse
- untere Integrationsgrenze ist kleiner als obere Integrationsgrenze
- keine Nullstelle und keine Polstellen im Integrationsintervall

## Fläche zwischen zwei Funktionen

Wenn $f$ und $g$ zwei Funktionen sind, die auf dem Intervall $[a:b]$ stetig sind und $g(x)\le f(x)$ für alle $x$ in $[a:b]$, dann ist die Fläche, die von beiden Funktionen eingeschlossen wird gleich

$$A=\int_{a}^{b}[f(x)-g(x)]\;\mathrm{d}x$$

Wenn die Funktionen Schnittpunkte besitzen, so muss man Teilintegrale für diese Abschnitte aufstellen.

## Graphisch Integrieren

- Nullstellen des Graphen werden zu den Extremstellen des Integrals
- Extremstellen des Graphen werden zu den Wendestellen des Integrals
- Positive Werte des Graphen werden zum positiven Anstieg des Integrals

## Rotationskörper

$$V=\pi \int_{a}^{b} \big(f(x)\big)^{2}\;\mathrm{d}x$$
## Bodenlänge einer Funktion

$\displaystyle\begin{split}l&=\sqrt{\Delta x^{2}+\Delta y^{2}}\\ &=\sum\limits_{i=1}^{n}\sqrt{\Delta x^{2}+\Delta y_{i}^{2}}\\ &=\sum\limits_{i=1}^{n}\sqrt{\Delta x^{2}(1+\frac{\Delta y_{i}^{2}}{\Delta x^{2}})}\\ &=\sum\limits_{i=1}^{n}\sqrt{1+\frac{\Delta y_{i}^{2}}{\Delta x^{2}}}\Delta x^{2}\\ &=\int_{a}^{b}\sqrt{1+\frac{\Delta y_{i}}{\Delta x}^{2}}\;\mathrm{d}x\\ &=\int_{a}^{b}\sqrt{1+f'(x)^{2}}\;\mathrm{d}x\end{split}$