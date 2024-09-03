# Komplexe Zahlen

- Es existiert eine komplexe Zahl $i$ mit $i^{2}=-1$.
- Menge aller komplexen Zahlen: $\mathbb{C}$
- Darstellung von $z\in\mathbb{C}: z=a+b i \quad(a,b\in\mathbb{R})\quad a=Re(z)\quad b=Im(z)$

**Beispiel**
$z_{i}=2+5i$
$Re(z)=2$
$Im(z)=5$

## Rechenregeln

$u,v\in\mathbb{C}: u=a+bi\;\wedge\;v=c+di\quad(a,b,c,d\in\mathbb{R})$

$u+v=(a+c)+(b+d)i\implies Re(u+v)=a+c\quad Im(u+v)=b+d$
$u\cdot v=(a+bi)(c+di)=ac+adi+bdi^2=(ac-bd)+(ad+bc)i$
$\bar{u}:=a-bi$
$u+\bar{u}=a+bi+a-bi=2a=2\;Re(u)$
$u\cdot\bar{u}=(a+bi)(a-bi)=a^{2}+b^{2}$
$\sqrt{a^{2}+b^{2}}={|u|}^{2}$

$\frac{u}{v}=\frac{u\cdot\bar{v}}{v\cdot\bar{v}}=\frac{(a+bi)(c-di)}{c^{2}+d^{2}}=\frac{(ac+bd)+(bc-ad)i}{c^{2}+d^{2}}$

---

$\frac{5+3i}{-1+i}=\frac{(5+3i)(-1-i)}{(-1+i)(-i-i)}=1-4i$

$|(1+i)(2-i)|=|2-i+2i-i^{2}|=|2+i-i^{2}|=|3+i|=\sqrt{3^{2}+1^{2}}=\sqrt{10}$

$\frac{u}{\bar{u}}=\frac{a+bi}{a-bi}=\frac{(a+bi)(a+bi)}{(a-bi)(a+bi)}=\frac{a^{2}-b^{2}+2abi}{a^{2}+b^{2}}$

# Definition Möbiustransformation

Definition: $M:\mathbb{C^{\infty}\to\mathbb{C^{\infty}}},z\to \frac{az+b}{cz+d}\quad(a,b,c,d\in\mathbb{C},ad-bc\neq0)$ heißt Möbiustransformation.

Motivationsbeispiel: Mit welcher Funktion lässt sich der Kreis $k_{1}$ auf den Kreis $k_{2}$ abbilden?

# Elementare Möbiustransformationen

## Verschiebung

Verschiebung um den Vektor $b$: $M_{v}(z)=z+b\quad(a=1,c=0,d=1)$
$b=Re(b)+Im(b)i$

## Inversion

Inversion $M_{i}(z)=\frac{1}{z}\quad(a=0,b=1,c=1,d=0)$

Gerade wird auf einen Kreis abgebildet
$z_{0}=1\implies M_{i}(z_{0})=\frac{1}{z_{0}}=1$
$z_{1}=1+i\implies M_{i}(z_{1})=\frac{1}{z_{1}}=\frac{1-i}{2}$
$z_{2}=1-i\implies M_{i}(z_{2})=\frac{1}{z_{2}}=\frac{1+i}{2}$

---

$z_{0}=2i\implies M_{i}(z_{0})=\frac{1}{z_{0}}=\frac{-2i}{4}=- \frac{1}{2}i$
$z_{1}=2+2i\implies M_{i}(z_{1})=\frac{1}{z_{1}}=\frac{1}{2+2i}= \frac{2-2i}{8}=\frac{1}{4}-\frac{1}{4}i$
$z_{2}=-2+2i\implies M_{i}(z_{2})=\frac{1}{z_{2}}=\frac{1}{-2+2i}= \frac{-2-2i}{8}=-\frac{1}{4}-\frac{1}{4}i$

---

Je weiter der Abstand der Gerade zum Koordiatenursprung ist, in desto kleinere Kreise werden sie transformiert

## Dreh-Streckung

$M_{0}(z)=a\cdot z\quad(b=0,c=0,d=1)$
$a\in\mathbb{C}\quad(a=|a|\cdot e^{i\alpha})$ Streckung um den Faktor $|a|$ sowie Drehung un den Winkel $\alpha$.

**Beispiel**
$a=2+i$, d.h. $M_{0}(z)=(2+i)z$
$M_{0}(z_{0})=M_{0}(0)=0$
$M_{1}(z_{1})=M_{1}(1+i)=(2+i)(1+i)=2+2i+i+i^{2}=1+3i$
$M_2(z_{2})=M_{2}(-1-i)=-1-3i$
