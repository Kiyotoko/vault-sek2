Eine ganzzahlige Lösung der Gleichung $x^n+y^n=z^n$ ist ein Tripel $(x,y,z)\in\mathbb{Z}^3$, für das $x^n+y^n=z^n$ gilt.

# Pythagoreische Tripel

- Eine Lösung $(x,y,z)\in\mathbb{N}^3$ von $x^2+y^2=z^2$ wird pythagoreisches Tripel genannt.
- Wie viele ganzzahlige Lösungen besitzt die Gleichung $x^2+y^2=25$?
- **Bemerkung** Die ganzzahligen Lösungen von $x^2+y^2=z^2$ sind:
	- $(0,0,0)$
	- $(\pm a,0,\pm a)$ und $(0,\pm a, \pm a)\forall a\in\mathbb{N}$
	- $(x,y,z)$, wenn $(|x|,|y|,|z|)$ ein pythagoreisches Tripel ist.
- **Lemma** Sei $(x,y,z)$ ein pythagoreisches Tripel von $d=ggT{x,y}$. Dann gilt:
	1. $(\frac{x}{d},\frac{y}{d},\frac{z}{d})$ ist ein pythagoreisches Tripel
	1. $ggt(\frac{x}{d}\frac{y}{d})=1$
- **Beweis**
	1. Es gilt $x^2+y^2=z^2$ sowie $d|x  d|y$
		- → $d|(x^2+y^2)$ → $d|z^2$ → $d|z$
		- Offensichtlich folgt aus $x^2+y^2=z^2$: $\frac{x^2+y^2}{d}=\frac{z^2}{d}$ → $(\frac{x^2}{d})+(\frac{y^2}{d})=(\frac{z^2}{d})$
	1. Angenommen,  $ggt(\frac{x}{d}\frac{y}{d})>1, k\in\mathbb{N}_{>1}$: 
		- $k|\frac{x}{d}$ und $k|\frac{y}{d}$ → $k|\frac{x}{ggT(x,y)}$ und $k|\frac{y}{ggT(x,y)}$
		- $x=n_1k ggT(x,y)$ und $y=n_2k ggT(x,y)$
- **Definition** Ein pythagoreisches Tripel $(x,y,z)\in\mathbb{N}^3$ heißt primitiv, wenn gilt $ggT(x,y)=1$.
- **Lemma** Sei $(x,y,z)$ ein primitives pythagoreisches Tripel, dann ist entweder $x$ oder $y$ eine gerade Zahl
- **Beweis** 
	1. Wenn $ggT(x,y)=1$ können x und y nicht beide durch 2 teilbar sein.
		- Angenommen, $x=1\mod2$ und $y=1\mod2$. Dann $n_1,n_2\in\mathbb{N}$: $x=2n_1+1$ und $y=2n_1+1$
		- $z^2=x^2+y^2=(2n_1+1)^2+(2n_2+1)^2=4n_1^2+4n_2^2+4n_1+4n_2+2=4(n_1^2+n_2^2+n_1+n_2)$

# Euklids Klassifikationssatz

- **Satz** Die folgenden Aussagen sind äquivalent:
	1. $(x,y,z)\in\mathbb{N^3}$ ist ein primitives pythagoreisches Tripel mit $x=0\mod2$
	1. mit $m>n,ggT(m,n)=1$ und $m\neq n\mod2$, sodass $x=2mn$ und $y=m^2-n^2$ und $z=m^2+n^2$
- **Beweis**
	- Zunächst zeigt man $(ii)\to(i)$
	- $x^2+y^2=(2mn)^2+(m^2-n^2)^2=4m^2n^2-2m^2n^2$
	- Angenommen, $ggT(x,y)>1$ $d:=ggT(x,y)$ → $p\in\mathbb{N}$ mit $p\text{ prim}$ und $p|d$
		1. $p=2\to p=2$ und $p|x$
		1. $p\neq 2\to p=1\mod2$ und $p|y$ und $p|x$ → $p|x^2+y^2$ → $p|z^2$ → $p|z$
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
	- Die Gleichung $x^4+y^4=z^2$ besitzt keine nicht-triviale Lösung
- **Beweis**
	- Angenommen, $(x,y,z)$ ist eine nicht-triviale Lösung von $x^4+y^4=z^2$
	1. Man zeigt: $(x,y,z)\in\mathbb{N}^3$ nicht-triviale Lösung von $x^4+y^4=z^2$ mit $ggT(x,y)=1$
		- Es gilt: $x',y',z'\neq0$ und $(|x'|,|y'|,|z'|)$ ist ebenfalls eine nicht-triviale Lösung. Deshalb reicht es anzunehmen, dass $x',y',z'\in\mathbb{N}$
		- Sei $d=ggT(x',y')$. Dann folgt aus $d|x^2$
		- Mit $x=\frac{x'}{d}$, $y=\frac{y'}{d}$ und $z=\frac{z'}{d}$ ist $(x,y,z)\in\mathbb{Z}^3$ eine nicht-triviale Lösung und wegen $z=\frac{z'}{d}\leq z'$ gilt $z^2\leq z'^2$. 
		- $ggT(x,y)=ggT(\frac{x'}{d},\frac{y'}{d})=1$ folgt logisch.
		- Schlussfolgerung: man kann annehmen, dass $(x,y,z)\in\mathbb{N}^3$ eine nicht-triviale Lösung ist mit $ggT(x,y)=1$
	1. Man zeigt: Entweder $x$ oder $y$ ist gerade.
		- Angenommen, $x=y=0\mod2$.
		- $ggT(x,y)\geq2\neg ggT(x,y)=1$
		- Angenommen, $x=y=1\mod2$
		- $x^2=y^2=1\mod2$ → $1\mod2$.
		- $x^2=2a+1$ oder $y^2=2b+1$
		- $x^4+y^4=(2a+1)^2+(2b+1)^2=4(a^2+a+b^2+b)$
	1. Man zeigt: $m,n\in\mathbb{N}$ mit $m>n$, $ggT(m,n)=1$ und $m\neq n\mod2$, sodass gilt: $x^2=2mn$, $y^2m^2-n^2$ und $z=m^2+n^2$
		- Beweis: Wegen $(x^2)^2+(y^2)^2=z^2$ ist $(x^2,y^2,z)$ ein pythagoreisches Tripel, das wegen $ggT(x,y)=ggT(x^2,y^2)=1$ primitiv ist. Dann folgt die Behauptung aus Euklids Klassifikationssatz.
	1. Man zeigt: $m=1\mod2$ und $n=0\mod2$
		- Beweis: Angenommen; $n=1\mod2$ → $a\in\mathbb{N}$: $n=2a+1$ und $m=0\mod2$ → $b\in\mathbb{N}:m=2b$
		- Da $y^2=1\mod2$, $c\in\mathbb{N}: y=2c+1$ und es folgt $y^2=(2x+1)^2=4c^2+4c+1$ → $4c^2+4c+2$ → $y^2=1\mod4$
		- Aber $y^2=m^2-n^2=0-1=3\mod4$
		- Schlussfolgerung: $r\in\mathbb{N}: n=2r$ → $x^2=2mn=4mr$ → $(\frac{x}{2})^2=mr$
	1. Man zeigt: $m$ und $r$ sind Quadratzahlen.
		- Beweis: $x=0\mod2\to(\frac{x}{2})^2$ eine Quadratzahlen in $\mathbb{N}$. Es reicht zu zeigen, dass $ggT(m,r)=1$. Angenommen, $d=ggT(m,r)>1$. Dann gilt: $d|m$ und $d|r$ → $d|2t=n$.
		→ $ggT(m,n)\geq d\geq1\neq ggT(m,n)=1$
		- Schlussfolgerung: $t,v\in\mathbb{N}: m=t^2$ und $r=v^2$
	1. Man zeigt: $(2v^2)^2+y^2=(t^2)^2$.
		- Beweis: $r=v^2$ → $n=2r=2v^2$
		- $y^2=m^2-n^2$ und $t^2=m$
		→ $(2v^2)^2+y^2=m^2+n^2-n^2=m^2=(t^2)^2$
	1. Man zeigt: $(2v^2,y,t^2)$ ist ein primitives pythagoreisches Tripel.
		- Beweis: Aus Schritt 6 folgt, dass $(2v^2,y,t^2)$ ein primitives  pythagoreisches Tripel ist. Bleibt für die Primitivität noch $ggT(2v^2,y)=1$ zu zeigen.
		- Angenommen: $d>1$. Dann sei $p|d\text{prim.}$ Es folgt: $p|2v^2=n$ und $p|y$ → $p|n^2$ und $p|y^2$ → $p|n^2+y^2$ $(n^2+y^2=n^2+m^2-n^2=m^2)$ → $p|m^2$ → $p|m$ und $p|n$
	1. Man zeigt: es gibt eine nicht-triviale Lösung $(u,w,t)$ von $(x^4+y^4=z^2)$ mit $t^2<z^2$.
		- Nach Schritt 7 ist $(2v^2,y,t^2)$ ein primitives pythagoreisches Tripel mit $2v^2=0\mod2$.
		- $M,N\in\mathbb{N}$ mit $ggT(M,N)=1,M>N$, sodass gilt: $2v^2=2MN$, $y=M^2-N^2$ und $t^2=M^2+N^2$
		→ $v^2=MN$ → $M$ und $N$ sind Quadratzahlen.
		$u,w\in\mathbb{N}: M=u^2$ und $N=w^2$
		- Es folgt aus $t^2=M^2+N^2$: $t^2=u^4+w^4$
		→ $(u,w,t)$ ist eine nicht-triviale Lösung von $x^4+y^4=z^2$
		- Weiter gilt $t^2=m\leq m^2<m^2+n^2=z\leq z^2\leq z'^2$

# Großer Satz Von Fermat

Ist $n=0\mod4$, dann hat die Gleichung $x^n+y^n=z^n$ keine nicht-trivialen Lösungen.
 - **Beweis**
	- $x^4+y^4=z^4$ besitzt keine Lösungen
	- Beweis: Angenommen, $(x,y,z)\in\mathbb{Z}^3$ ist eine nicht-triviale Lösung von $x^4+y^4=z^4$. → $(x,y,z^2)\in\mathbb{Z}^3$ ist eine nicht triviale Lösung von $x^4+y^4=z^2$. → $n=0\mod4$ → $s\in\mathbb{N}: n=4s$
	- Angenommen, $(x,y,z)\in\mathbb{Z}^2$ ist eine nicht triviale Lösung von $x^4+y^4=z^4$
- **Satz**
	- Für $n>2$ hat die Gleichung $x^n+y^n=z^n$  keine nicht-trivialen Lösungen.
- Beweisidee; Sei $p>2 prim$. Wenn $x^P+y^P=z^P$ keine nicht-trivialen Lösungen besitzt, dann hat $x^n+y^n=z^n\forall n\in\mathbb{N}_{>z}$ auch keine nicht-trivialen Lösungen.

# Pell'sche Gleichung

1. Sei $d\in\mathbb{N}$ keine Quadratzahl. Die Gleichung $X^2-dY^2=1$  wird Pell'sche Gleichung genannt.
1. $(x,y)\in\mathbb{Z}^2$ mit $(x,y)\neq(\pm1,0)$ wird eine nicht-triviale Lösung der Pell'schen Gleichung genannt, wenn $x^2-dy^2=1$
- Aufgabe
	1. $x^2-2y^2=1$ 3 und 2
	1. $x^2-3y^2=1$ 2 und 1
	1. $x^2-7y^2=1$ 8 und 3
- Aufgabe
	- $x^2+y^2+z^2\geq12\forall x,y,z\in\mathbb{R}^+: x+y+z=6$
