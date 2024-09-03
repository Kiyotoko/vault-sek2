# Vektoren

## Abstände und Winkel

### Skalarprodukt

Unter einem Skalarprodukt versteht man die Zahl $\vec{a}\cdot\vec{b}=\begin{pmatrix}x_{a} \\ y_{a} \\ z_{a} \end{pmatrix}\circ\begin{pmatrix}x_{b} \\ y_b \\ z_{b}\end{pmatrix}=x_{a}\cdot x_{b}+y_{a}\cdot y_{b}+z_{a}\cdot z_{b}$

Anwendung Berechnung von Winkeln zwischen Vektoren: $\cos{\alpha}=\frac{\vec{a}\circ\vec{b}}{|\vec{a}|\cdot|\vec{b}|}$
**Beispiel**
$\cos{\alpha}=\frac{9}{\sqrt{14}\cdot \sqrt{30}}$
$\cos{\alpha}=0.439155$


### Orthogonalität zweier Vektoren

Zwei Vektoren sind orthogonal zueinander, wenn das Skalarprodukt Null ist.

Unter dem Schnittwinkel zweier Geraden versteht man den kleineren der beiden Winkel.

Winkel im Dreieck können stumpfe Winkel sein. $\cos{\gamma}=\frac{\vec{CA}\cdot\vec{CB}}{|\vec{CA}|\cdot|\vec{CB}|}$

Um $\gamma$ richtig zu berechnen, verwendet man die beiden Vektoren, die vom Punkt $C$ wegführen oder zum Punkt hinführen.

### Winkel zwischen zwei Ebenen

$E_{1}-E_{2}$
$\cos{\alpha}=\frac{\vec{n_{1}}\circ\vec{n_{2}}}{|\vec{n_{1}}|\cdot|\vec{n_{2}}|}$

$\vec{n_{1}}$: Normalvektor von $E_{1}$
$\vec{n_{2}}$: Normalvektor von $E_{2}$

### Winkel zwischen Gerade und Ebene

$\sin{\alpha}=\frac{\vec{v}\circ\vec{n}}{|\vec{v|\cdot|\vec{n}}|}$
$\vec{v}$: Richtungsverkter der Geraden
$\vec{n}$: Normalvektor der Ebene

## Normalenform einer Ebene

$[\vec{x}-\vec{p}]\circ\vec{n}=0$

**Beispiel**
$P(1|2|3)$ und verläuft $\bot$ zu $\vec{v}=\begin{pmatrix}2 \\ -1 \\ 3\end{pmatrix}$
$\Bigg[\vec{x}-\begin{pmatrix}1 \\ 2 \\ 3\end{pmatrix}\Bigg]\circ\begin{pmatrix}2 \\ -1 \\ 3\end{pmatrix}=0$
$\Bigg[\begin{pmatrix}x \\ y \\ z\end{pmatrix}-\begin{pmatrix}1 \\ 2 \\ 3\end{pmatrix}\Bigg]\circ\begin{pmatrix}2 \\ -1 \\ 3\end{pmatrix}=0$

$(x-1)\cdot2+(y-2)\cdot(-1)+(z-3)\cdot3=0$
$2x-2-y+2+3z-9=0$
$2x-y+3z=9$

## Orthogonalität von 3 Vektoren

**Beispiel**
$\vec{a}=\begin{pmatrix}2 \\ -3 \\ 1\end{pmatrix}$
$\vec{b}=\begin{pmatrix}1 \\ 2 \\ -1\end{pmatrix}$
Gesucht ist ein Vektor $\vec{c}$ mit $\vec{c}\bot\vec{a}\wedge\vec{c}\bot\vec{b}$.
$\vec{c}=\begin{pmatrix}x \\ y \\ z\end{pmatrix}$
$\vec{c}\circ\vec{a}=0$
$\vec{c}\circ\vec{b}=0$
$\begin{pmatrix}x \\ y \\ z\end{pmatrix}\circ\begin{pmatrix}2 \\ -3 \\ 1\end{pmatrix}=0$
$\begin{pmatrix}x \\ y \\ z\end{pmatrix}\circ\begin{pmatrix}1 \\ 2 \\ -1\end{pmatrix}=0$

$2x-3y+z=0$
$x+2y-z=0$
$3x-y=0$

Wir setzen $x=1$ ein.
$1+6-z=0$
$c=7$
$\vec{x}=\begin{pmatrix}2 \\ 6 \\ 14\end{pmatrix}$

## Das Vektorprodukt

**Beispiel**
$\begin{pmatrix}2 \\ -3 \\ 1\end{pmatrix}\times\begin{pmatrix}1 \\ 2 \\ -1\end{pmatrix}=\begin{pmatrix}3-2 \\ 1+2 \\ 4+3\end{pmatrix}=\begin{pmatrix}1 \\ 3 \\ 7\end{pmatrix}$

Das Ergebnis des Vektorprodukts $\vec{a}\times\vec{b}$ ist ein Vektor, der Senkrecht auf $\vec{a}$ und Senkrecht auf $\vec{b}$ steht.

$\begin{pmatrix}x_{a} \\ y_a \\ z_a\end{pmatrix}\times\begin{pmatrix}x_{b} \\ y_{b} \\ z_{b} \end{pmatrix}=\begin{pmatrix}y_{a}z_{b}-z_{a}y_{b} \\ z_{a}x_{b}-x_{a}z_{b} \\ x_{a}y_{b}-y_{a}x_{b}\end{pmatrix}$

### Geometrische Bedeutung

- Ergebnis ist ein Vektor, der $\bot$ auf beiden Vektoren steht
- Betrag des Vektorproduktes ist der Flächeninhalt des aufgespannten Parallelogrammes $A=|\vec{a}\times\vec{b}|$
- Die Hälfte des Betrags des Vektorproduktes ist der Flächeninhalt des Dreiecks

## Spatprodukt
 
$V_{Spat}=|(\vec{a}\times\vec{b})\circ\vec{c}|$
Volumen eines Prismas mit den Vektoren $\vec{a}$, $\vec{b}$ und $\vec{c}$.

### Geometrische Bedeutung

- Volumen eines 3-seitigen Prismas $V=\frac{1}{2}|(\vec{a}\times\vec{b})\circ\vec{c}|$
- Volumen einer 4-seitigen Pyramide $V=\frac{1}{3}|(\vec{a}\times\vec{b})\circ\vec{c}|$
- Volumen einer 3-seitigen Pyramide $V=\frac{1}{6}|(\vec{a}\times\vec{b})\circ\vec{c}|$

## Abstände / Spiegelpunkte

### Abstand Punkt-Ebene

- Aufstellen einer Geradengleichung durch $P E$
- Schnittpunkt der Gerade mit der Ebene $E$ ermitteln
- $|\vec{PS}|$ berechnen

**Beispiel**
$E: 2x+y+2z=-2$
$P(2|-1|2)$
$g: \begin{pmatrix}2 \\ -1 \\ 2\end{pmatrix}+k\begin{pmatrix}2 \\ 1 \\ 2\end{pmatrix}$
$2(2+2k)+(-1+k)+2(2+2k)=-2$
$4+4k-1+k+4+4k=-2$
$9k=-9$
$k=-1$
$S(0|-2|0)$
$\vec{PS}=\begin{pmatrix}-2 \\ -1 \\ -2\end{pmatrix}$
$|\vec{PS}|=\sqrt{9}=3$

### Über Hesse'sche Normalenform

Man erhält die HNI einer Ebene, indem man die Ebenengleichung $ax+by+cz+d=0$ durch den Betrag des Normalenvektors teilt..
Den Abstand eines Punktes von der Ebene erhält man, indem man die Koordinaten des Punktes in die HNF der Ebene einsetzt.

**Beispiel**
$E:2x+y+2z=-2$
$P(2|-1|2)$
$HNF: \frac{2x+y+2z+2}{\sqrt{2^{2}+1^{2}+2^{2}}}=0$
$\frac{2x+y+2z+2}{3}=0$

$d=\frac{2\cdot2-1+2\cdot2+2}{3}=\frac{9}{3}=3$

### Spiegelpunkte

$\vec{0P'}=\vec{0P}+2\cdot\vec{PS}$
$\vec{0P'}=\vec{0S}+\vec{PS}$

**Beispiel**
$E:5x-y+4z=-12$
$P(17|15|11)$

$g\text{ durch }P\bot E:\vec{x}=\begin{pmatrix}17 \\ 15 \\ 11\end{pmatrix}+k\begin{pmatrix}5 \\ -1 \\ 4\end{pmatrix}$
$5(17+5k)-(15-k)+4(11+4k)=-12$
$85+25k-15+k+44+16k=-12$
$42k=-126$
$k=-3$

$S(2|18|-1)$
$\vec{PS}=\begin{pmatrix}-15 \\ 3 \\ -12\end{pmatrix}$
$\vec{0P'}=\begin{pmatrix}17 \\ 15 \\ 11\end{pmatrix}+2\begin{pmatrix}-15 \\ 3 \\ -12\end{pmatrix}=\begin{pmatrix}-13 \\ 21 \\ -13\end{pmatrix}$

Für den Abstand bei Ebene zu Gerade beziehungsweise Ebene zu Ebene wählt man einen beliebigen Punkt, und fährt dann fort wie oben. Bedingung ist, dass diese nicht parallel sind.

### Abstand Punkt Gerade

$g:\vec{x}=\begin{pmatrix}6 \\ 1 \\ 6\end{pmatrix}+k\begin{pmatrix}3 \\ -2 \\ 4\end{pmatrix}$
$P(4|-5|8)$
$Q(6+3k|1-2k|6+4k)$
$\vec{PQ}=\begin{pmatrix}6+3k-4 \\ 1-2k+5 \\ 6+4k-8\end{pmatrix}=\begin{pmatrix}2+3k \\ 6-2k \\ -2+4k\end{pmatrix}$
$d=\sqrt{(2+3k)^{2}+(6-2k)^{2}+(-2+4k)^{2}}$

Eingabe ins Grafikmenü des TR u. Minimum anzeigen lassen

$TP(0.48|6.41)$

Abstand $P-g$: $6.1$

#### Über Hilfsebene

- Aufstellen der Gleichung einer Hilfsebene durch $P\bot g$
- Berechnen des Schnittpunktes $S$ der Hilfsebene mit $g$
- Berechnen des Abstandes Schnittpunkt  $S-P$

**Beispiel**
$\vec{x}=\begin{pmatrix}6 \\ 1 \\ 6\end{pmatrix}=k\begin{pmatrix}3 \\ -2 \\ 4\end{pmatrix}$
$P(4|-5|8)$

$3x-2y+5z=z$
$4\cdot4-2\cdot(-5)+4\cdot8=12+10+32=54$

Hilfsebene
$3x-2y+4z=54$

Einsetzen der Gerade
$3(6+3k)-2(1-2k)+4(6+4k)=54$
$k=\frac{14}{29}$

Schnittpunkt durch Variable in Gerade einsetzen
$S(7.448|1.414|5.172)$

Abstand zwischen $P$ und $S$
$|\vec{PS}|\approx6.1$

#### Über Vektorprodukt

$g:\vec{x}=\begin{pmatrix}6 \\ 1 \\ 6\end{pmatrix}+k\begin{pmatrix}3 \\ -2 \\ 4\end{pmatrix}$
$P(4|-5|8)$

Für $k=1$ erhält man einen weiteren Punkt auf $g$, hier $(9|-1|10)$

Die Fläche $A$ eines aufgespannten Parallelogramms mit den Seiten $\vec{a}=\vec{G_{0}P}$ und $\vec{b}=\vec{G_{1}P}$

$A=|\vec{a}\times\vec{b}|$
$h=\frac{A}{\vec{b}}=6.1$

Logische Schlussfolgerung aus Abstandsrechnung Punkt zu Gerade
- Berechnung des Abstandes $g_{1}-g_{2}$ für $g_{1}\|g_{2}$ -> beliebigen Punkt auf $g_{1}$ wählen, dann weiter wie Abstand $P-g$

### Abstand windschiefer Geraden

#### Über Hilfsebene

- Aufstellen einer Ebenengleichung, die $g_{1}$ enthält und parallel zu $g_{2}$ verläuft
- Beliebigen Punkt auf $g_{2}$ wählen
- Berechnen des Abstandes des Punktes von der Hilfsebene

**Beispiel**
$g_{1}:\vec{x}=\begin{pmatrix}-2 \\ 3 \\ 5\end{pmatrix}+k\begin{pmatrix}1 \\ 2 \\ 0\end{pmatrix}$
$g_{2}:\vec{x}=\begin{pmatrix}1 \\ -6 \\ 2\end{pmatrix}+t\begin{pmatrix}2 \\ 6 \\ 1\end{pmatrix}$

Ebene aufstellen
$E:\vec{x}=\begin{pmatrix}-2 \\ 3 \\ 5\end{pmatrix}+k\begin{pmatrix}1 \\ 2 \\ 0\end{pmatrix}+t\begin{pmatrix}2 \\ 6 \\ 1\end{pmatrix}$
$2x-y+2z=3$

$\frac{2x-y+2z-3}{\sqrt{2^{2}+(-1)^{2}+2^{2}}}=0$
$d=\frac{2\cdot1-(-6)+2\cdot2-3}{3}=\frac{2+6+4-3}{3}=3$

#### Über Skalarprodukt

$g_{1}:\vec{x}=\begin{pmatrix}-2 \\ 3 \\ 5\end{pmatrix}+k\begin{pmatrix}1 \\ 2 \\ 0\end{pmatrix}$
$g_{2}:\vec{x}=\begin{pmatrix}1 \\ -6 \\ 2\end{pmatrix}+t\begin{pmatrix}2 \\ 6 \\ 1\end{pmatrix}$

Punkt auf $g_{1}: A$ und Punkt auf $g_{2}:B$
Kürzeste Verbindung von $g_{1}$ zu $g_{2}$ ist der Abstand von $A$ zu $B$
$\overrightarrow{AB}\bot g_{2}\wedge\overrightarrow{AB}\bot g_{2}$

$A(-2+k|3+2k|5)$
$B(1+2t|-6+6t|2+t)$

$\overrightarrow{AB}=\begin{pmatrix}3+2t-k \\ -9+6t+2k \\ 3+t\end{pmatrix}$

$\begin{pmatrix}3+2t-k \\ -9+6t+2k \\ 3+t\end{pmatrix}\circ\begin{pmatrix}1 \\ 2 \\ 0\end{pmatrix}=0$
$\begin{pmatrix}3+2t-k \\ -9+6t+2k \\ 3+t\end{pmatrix}\circ\begin{pmatrix}2 \\ 6 \\ 1\end{pmatrix}=0$

$3+2t-k-18+12t-4k=0$
$14t-5k-15=0$

$6+4t-2k-54+36t-12k-3+t=0$
$41t-14k-51=0$

Gleichungssystem lösen
```js
t=5 k=11
```

$A(9|25|5)$
$B(11|24|7)$
$|\overrightarrow{AB}|=\sqrt{2^{2}+(-1)^{2}+2^{2}}$
