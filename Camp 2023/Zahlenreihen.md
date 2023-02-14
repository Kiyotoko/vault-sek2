Eine ganzzahlige Lösung der Gleichung $x^n+y^n=z^n$ ist ein Tripel $(x,y,z)\in\mathbb{Z}^3$, für das $x^n+y^n=z^n$ gilt.

## Pythagoreische Tripel
- Eine Lösung $(x,y,z)\in\mathbb{N}^3$ von $x^2+y^2=z^2$ wird pythagoreisches Tripel genannt.
- Wie viele ganzzahlige Lösungen besitzt die Gleichung $x^2+y^2=25$?
- **Bemerkung** Die ganzzahligen Lösungen von $x^2+y^2=z^2$ sind:
	- $(0,0,0)$
	- $(\pm a,0,\pm a)$ und $(0,\pm a, \pm a)\forall a\in\mathbb{N}$
	- $(x,y,z)$, wenn $(|x|,|y|,|z|)$ ein pythagoreisches Tripel ist.
- **Lemma** Sei $(x,y,z)$ ein pythagoreisches Tripel von $d=ggT{x,y}$. Dann gilt:
	1. $(\frac{x}{d},\frac{y}{d},\frac{z}{d})$ ist ein pythagoreisches Tripel
	2. $ggt(\frac{x}{d}\frac{y}{d})=1$
- **Beweis**
	1. Es gilt $x^2+y^2=z^2$ sowie $d|x  d|y$
		- → $d|(x^2+y^2)$ → $d|z^2$ → $d|z$
		- Offensichtlich folgt aus $x^2+y^2=z^2$: $\frac{x^2+y^2}{d}=\frac{z^2}{d}$ → $(\frac{x^2}{d})+(\frac{y^2}{d})=(\frac{z^2}{d})$
	2. Angenommen,  $ggt(\frac{x}{d}\frac{y}{d})>1, k\in\mathbb{N}_{>1}$: 
		- $k|\frac{x}{d}$ und $k|\frac{y}{d}$ → $k|\frac{x}{ggT(x,y)}$ und $k|\frac{y}{ggT(x,y)}$
		- $x=n_1k ggT(x,y)$ und $y=n_2k ggT(x,y)$
- **Definition** Ein pythagoreisches Tripel $(x,y,z)\in\mathbb{N}^3$ heißt primitiv, wenn gilt $ggT(x,y)=1$.
- **Lemma** Sei $(x,y,z)$ ein primitives pythagoreisches Tripel, dann ist entweder x oder y eine gerade Zahl
- **Beweis** 
	1. Wenn $ggT(x,y)=1$ können x und y nicht beide durch 2 teilbar sein.
		- Angenommen, $x=1\mod2$ und $y=1\mod2$. Dann $n_1,n_2\in\mathbb{N}$: $x=2n_1+1$ und $y=2n_1+1$
		- $z^2=x^2+y^2=(2n_1+1)^2+(2n_2+1)^2=4n_1^2+4n_2^2+4n_1+4n_2+2=4(n_1^2+n_2^2+n_1+n_2)$
## Euklids Klassifikationssatz
- **Satz** Die folgenden Aussagen sin äquivalent:
	1. $(x,y,z)\in\mathbb{N^3}$ ist ein primitives pythagoreisches Tripel mit $x=0\mod2$
	2. mit $m>n,ggT(m,n)=1$ und $m\neq n\mod2$, sodass $x=2mn$ und $y=m^2-n^2$ und $z=m^2+n^2$
- **Beweis**
	- Zunächst zeigt man $(ii)\to(i)$
	- $x^2+y^2=(2mn)^2+(m^2-n^2)^2=4m^2n^2-2m^2n^2$
	- Angenommen, $ggT(x,y)>1$ $d:=ggT(x,y)$ → $p\in\mathbb{N}$ mit $p\text{ prim}$ und $p|d$
		1. $p=2\to p=2$ und $p|x$
		2. $p\neq 2\to p=1\mod2$ und $p|y$ und $p|x$ → $p|x^2+y^2$ → $p|z^2$ → $p|z$
	- Weiter gilt: $y+z=m^2-n^2+m^2+n^2=2m^2$ → $p|2m^2$ → $p|2n^2$
	- Also folgt $ggT(x,y)=1$ und $(x,y,z)$ ist ein primitives pythagoreisches Tripel.
- **Aufgabe**
	-  Konstruiere ein primitives pythagoreisches Tripel mit $m=3$ und $n=2$:
		- $(x=12,y=5,z=13)$
	- Da $x=0\mod2$: $e=2r$ → $x^2=4r^2$
	- Weiter gilt $x^2+y^2=z^2$ → $4r^2=z^2-y^2=(z-y)(z+y)$
	- Aufgrund dessen, dass $y=z\mod2$, gilt:
	- $z-y=z+y=0\mod2$
	- $y+z=2s$ und $z-y=2t$
	- $2z=2z+y-y=(z+y)+(z-y)=2s+2t$ → $z=s+t$
	- $2y=(y+z)+(y-z)=2s-2t$ → $y=s-t$
	- Weiter gilt nun: $x^2+4r^2=z^2-y^2=(z-y)(z+y)=4st$ → $r^2=s*t$
- **Definition**
	- Für $n\in\mathbb{Z}^3$ von $x^n+y^n=z^n$ trivial, wenn gilt: $x=0$ oder $y=0$ oder $z=0$.
	- Sie heißt nicht-trivial, wenn gilt: $x\neq0$ oder $y\neq0$ oder $z\neq0$.
- **Satz**
	- Die Gleichung $x^4+y^4=z^4$ besitzt keine nicht.triviale Lösung
- **Beweis**
	- Angenommen, $(x,y,z)$ ist eine nicht-triviale Lösung von $x^4+y^4+z^4$
	1. Man zeigt: $(x,y,z)\in\mathbb{N}^3$ nicht-triviale Lösung von $x^4+y^4$ 