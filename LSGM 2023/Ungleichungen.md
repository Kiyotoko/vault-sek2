---
author: karlz
tags:
- topic/math
---

# Multiplizieren / Dividieren Negativer Zahlen

$3x>5x+1|-5x$
$-2x>1|*-\frac{1}{2}$
$x<-\frac{1}{2}$

$a^2+b^2+c^2\geq ab+bc+ca$
$(a-b)^2=a^2+b^2-2ab$
$(a-b)^2\geq 0$
$a^2+b^2-2ab\geq 0$
$a^2+b^2\geq 2ab$
$\frac{a^2+b^2}{2}\geq ab$

$\frac{x}{y}+\frac{y}{x}\geq 2$
$(x-y)^2\geq 0$
$x^2-2xy+y^2\geq 0$
$x^2+y^2\geq2xy$
$xy^{-1}+yx^{-1}\geq 2$

Die Summe zweier positiver Zahlen deren Produkt $1$ ist, ist mindestens $2$.
$xy=1$
$x+y\geq2$
$x=\frac{1}{y}$
$\frac{1}{y}+\frac{y}{1}\geq2$

Is das Produkt von $n$ positiven Zahlen gleich $1$, ist die Summe der der Zahlen mindestens $1$.
$x_0*x_1*\dots*x_n=1$
$x_0+x_1+\dots+x_n\geq n$

$1*1=1$
$1^n=1$
$1+1\geq2$
$x_0=x_1=n*1=n$

$\frac{x^2}{x^4+1}\leq\frac{1}{2}$
$x^2\leq\frac{x^4+1}{2}$
$0\leq x^4+1-2x^2$
$0\leq (x^2-1)^2$

# Bernoulli-Ungleichung

Für alle $x\in\mathbb{R}, x\geq -1$ und $\forall n\in\mathbb{N}$ gilt: $(1+x)^n\geq1+n*x$.
~~~functionplot
---
disableZoom: true
---
f(x)=(1+x)^3
g(x)=1+3x
~~~
Beweis für die Bernoulli-Ungleichung.
- **Indunktionsanfang**: $n=1$
	- $(1+x)^1\geq n+1x$
	- $1+x\geq1+x$
- **Induktionsbehauptung**: $(1+x)^{n+1}\geq1+(n+1)x$
- **Induktionsschritt**
	- $(1+x)^n\geq1+nx$
	- $(1+x)^{n+1}\geq1+nx+x+nx^2$
	- $(1+x)^{n+1}\geq1+x(n+1)+nx^2\geq1+x(n+1)$

# Mittelunggleichungen

- Harmonisches Mittel $\frac{n}{\frac{1}{x_1}+\frac{1}{x_2}+\dots+\frac{1}{x_n}}$
- Geometrisches Mittel $\sqrt[n]{x_1+x_2+\dots+x_n}$
- Arithmetrisches Mittel $\frac{x_1+x_2+\dots+x_n}{n}$
- Quadratisches Mittel $\sqrt{\frac{x_1^2+x_2^2+\dots+x_n^2}{n}}$
→ $HM \leq GM\leq AM\leq QM$
