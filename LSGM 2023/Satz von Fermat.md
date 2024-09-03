# Der binomische Satz von Fermat

$(a+b)^2=\sum^n_\limits{i=0}\binom{n}{i}a^{i}b^{n-i}$

## Grundwissen

### Binomische Formeln

1. $(a+b)^2=a^2+2ab+b^2$
2. $(a-b)^2=a^2-2ab+b^2$
3. $(a+b)(a-b)=a^2-b^2$

### Binomialkoeffizienten

$\binom{n}{k}$ sprich: $n$ über $k$
$\binom{n}{k}$ Anzahl der Möglichkeiten aus einer $n$-elementigen Mengen einer Teilmenge aus $k$ Elementen auszuwählen, entspricht $\frac{n!}{k!(n-k)!}$.

# Der kleine Satz von Fermat

Für jede Primzahl $p$ und jede natürliche Zahl $a$ gilt: $a^p=a\mod p$

**Beweis**
Über Kombinatorik.
$p|a^p-a$

$\frac{a^p-a}{p}$ Möglichkeiten, das alle Farben verschieden rotierbar sind.
$a$ Möglichkeiten, das alle die selbe Farbe haben.
$\frac{a^p-a}{p}+a\in\mathbb{N}$, ist Teil der Menge der natürlichen Zahlen, weil es Kombinatorik ist. Da $a$ eine natürliche Zahl ist, muss $\frac{a^p-a}{p}$ auch eine natürliche Zahl sein und somit durch $p$ teilbar sein.

**Beweis**
Über vollständige Induktion.

$IA: a=1$ für $a^p=a\mod p$
$IV: p|a^p-a$
$IB: p|(a+1)^p-(a+1)$
$IS: 0=0\mod p$
$\sum^{p-1}_\limits{i=1}\frac{p!}{i!(p-i)!}*a^i=0\mod p$
$\sum^{p-1}_\limits{i=1}\binom{p}{i}*a^i=0\mod p$
$p|(a+1)^p-a^p-1$
$p|(a+1)^p-a^p-1+a-a$
$p|(a+1)^p-a-1-(a^p-a)$
$p|(a+1)^p-a-1$

# Die Propabilistische Methode

- $S$ Die Menge aller Ergebnis
- $\mathbb{P}$ Wahrscheinlichkeit mit $\mathbb{P}:S\to[0,1]$
- Eine Zufallsvariable: $X:S\to\mathbb{R}$
- Erwartungswert $E(x)=\sum_\limits{s\in\mathbb{S}}\mathbb{P}(s)*X(s)$

**Beispiel**
Eine faire Münze wird 3x geworfen.
$X$ Anzahl der geworfenen Zahlen
$E(x)=0*\frac{1}{8}+1*\frac{3}{8}+2*\frac{3}{8}+3*\frac{1}{8}=\frac{12}{8}=1.5$

**Beispiel**
$x_1,x_2$ Zufallsgrößen

$\mathbb{E}(x_1+x_2)=\mathbb{E}(x_1)+\mathbb{E}(x_2)$
In unserem Beispiel: $x_i\Bigg\{\begin{matrix}1\quad\text{ falls im i-ten Wurf Zahl geworfen wurde}\\0\quad\text{ falls im i-ten Wurf Kopf geworfen wurde}\end{matrix}$
$X=x_1+x_2+x_3$
$\mathbb{E}(x)=\mathbb{E}(x_1)+\mathbb{E}(x_2)+\mathbb{E}(x_3)$

Sei $z\in\mathbb{R}$.
- $\mathbb{E}(x)>z$ bedeutet u a, dass ein ein $s\in S$ git mit $X(s)\ge z$.
- $\mathbb{E}(x)\le z$ bedeutet u. a., dass es ein $s\in S$ gibt mit $X(s)\le z$

**Aufgabe**
In jeder Klasse ist jeder Junge mit mindestens einem Mädchen befreundet. Zeige, dass es eine Gruppe von Schülern, in der mindestens die Hälfte der Schüler enthalten ist, und in der jeder Junge mit einer ungeraden Anzahl von Mädchen innerhalb der Gruppe befreundet ist.

**Beweis**
Wähle eine zufällige Gruppe von Mädchen aus. Jedes Mädchen ist mit Wahrscheinlichkeit $\frac{1}{2}$ in der Gruppe (unabhängig voneinander). Dazu kommen alle Jungs, die mit einer ungeraden Anzahl von Mädchen in der gerade ausgewählten Mädchengruppe befreundet sind.
$X$ Anzahl der Schüler in der ausgewählten Gruppe.

$x_i\Bigg\{\begin{matrix}1\quad\text{ wenn i-te Schüler in der Gruppe}\\0\quad\text{ sonst}\end{matrix}$
$y_i\Bigg\{\begin{matrix}1\quad\text{ wenn i-te Schüler in der Gruppe}\\0\quad\text{ sonst}\end{matrix}$
$X=x_i+y_i$

$\mathbb{E}(x_i)=0\frac{1}{2}+1\frac{1}{2}=\frac{1}{2}$
i-ter Junge ist mit Mädchen A befreundet. Es gibt genau so viele Mädchengruppen, bei denen er mit einer geraden Anzahl befreundet ist und bei denen er mit einer ungeraden Anzahl befreundet ist (Zuordnung, indem man $A$ dazu tut oder $A$ wegnimmt).
$\mathbb{E}(y_i)=0\frac{1}{2}+1\frac{1}{2}=\frac{1}{2}$
$\mathbb{E}(X)$ Summe der Erwartungswerte $\mathbb{E}(x_i)$ und $\mathbb{E}(y_i)$. Somit ist $\mathbb{E}(X)=n\frac{1}{2}$, wobei $n$ gleich der Anzahl an Schülern entspricht. Es existier eine Gruppe mit mindestens $\frac{n}{2}$ Schülern, womit die Bedingung erfüllt ist.