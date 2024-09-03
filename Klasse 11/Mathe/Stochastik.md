# Stochastik

## Klassische Wahrscheinlichkeit

$\text{Wahrscheinlichkeit}=\frac{\text{Anzahl günstiger Ereignisse}}{\text{Anzahl möglicher Ereignisse}}$

**Beispiel**
Idealer Würfel $P(X=6)=\frac{1}{6}$

### Pfadregeln

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

#### Pfadmultiplikatiosregel

Bei mehrstufigen Zufallsversuchen ist die Wahrscheinlichkeit eines Ereignisses gleich dem Produkt der Wahrscheinlichkeit längs des zugehörigen Pfades.

**Beispiel**
$P(X=2)=\frac{4}{12}*\frac{4}{12}$

#### Pfadadditionsregel

Setzt sich bei einem mehrstufigen Zufallsexperiment ein Ereignis aus verschiedenen Pfaden zusammen, erhält man die Wahrscheinlichkeit., durch Addition der einzelnen Pfad-Wahrscheinlichkeit

**Beispiel**
$P(X=1)=\frac{4}{12}*\frac{8}{12}+\frac{8}{12}*\frac{4}{12}=\frac{4}{9}$

#### Ziehen ohne Zurücklegen

Beim ziehen ohne Zurücklegen ändern sich in den folgenden Stufen des Zufallsexperimentes die Wahrscheinlichkeiten.

#### Komplementärregel

Ereignis + Gegenergeignis = 1 $P(A)+P(\bar{A})=1$

**Beispiel**
$P(X\geq1)\geq1-P(X=0)$
$1-P(X=0)=1-\frac{8}{12}*\frac{8}{12}=1-\frac{2}{3}*\frac{2}{3}=1-\frac{4}{9}=\frac{5}{9}$

### Fakultät

$n!=n*(n-1)*(n-2)*\dots*1$

**Beispiel**
$5!=5*4*3*2*1=120$
$4!=4*3*2*1=24$

### Abzählverfahren

**Beispiel**
Pferderennen, 12 Pferde
Einlauf  der ersten 3 Pferde soll vorausgesagt werden.

### Satz über die total Wahrscheinlichkeit

Ereignisse $A$ und $B$.
$P(B)=P(A)*P_{A}(B)+P(\bar{A})*P_{\bar{A}}(B)$

~~~mermaid
graph TB
A[*]
A-->|50%|A0[rot]
A-->|50%|A1[blau]
A0-->|50%|A00[rot]
A0-->|50%|A01[blau]
A1-->|50%|A10[rot]
A1-->|50%|A11[blau]
~~~

### Satz von Bayes

$P_B(A)=\frac{P(A\cap B)}{P(A)*P_{A}(B)+B(\bar{A})*P_{\bar{A}}(B)}$

### Darstellung bedingter Wahrscheinlichkeit mithilfe einer Vierfeldertafel

**Beispiel**
Ein Schüler fährt an $50\%$ der Schultage mit dem Bus. In $70\%$ dieser Fälle kommt er pünktlich. Durchschnittlich kommt er an $60\%$ der Tage pünktlich. Heute kommt der Bus Pünktlich. Mit welcher Wahrscheinlichkeit hat er den Bus benutzt?

|           | $B$    | $\bar{B}$ | Summe |
| --------- | ------ | --------- | ----- |
| $P$       | $0.35$ | $0.25$    | $0.6$ |
| $\bar{P}$ | $0.15$ | $0.25$    | $0.4$ |
| Summe     | $0.5$  | $0.5$     | $1$   |

$P_{P}(B)=\frac{0.35}{0.6}$

Heute fährt er nicht mit dem Bus. Mit welcher Wahrscheinlichkeit kommt er zu spät?

$P_\bar{B}(\bar{P})=\frac{0.25}{0.5}$

$P(B\cap P)=0.35\quad P(B\cap\bar{P})=0.15$

### Unabhängigkeit zufälliger Ereignisse

Zwei Ereignisse $A$ und $B$ heißen stochastich voneinander unabhängig genau dann, wenn gilt $P_{A}(B)=P(B)$ und $P_{B}(A)=P(A)$

#### Multiplikationssatz

Sind A und B stochastisch voneinander unabhängig, dann gilt: $P(A\cap B)=P(A)*P(B)$

**Beispiel**
Tankstellenbesitzer Til weiß aus Erfahrung, dass $30\%$ seiner Kunden Superbenzin tanken, wobei $40\%$ von diesen die Automarke M fahren.
Außerdem weiß er, dass $42\%$ aller seiner Kunden weder Fahrer der Automarke M sind, noch Super tanken.

|           | $S$    | $\bar{S}$ | Summe |
| --------- | ------ | --------- | ----- |
| $M$       | $0.12$ | $0.28$    | $0.4$ |
| $\bar{M}$ | $0.18$ | $0.42$    | $0.6$ |
| Summe     | $0.3$  | $0.7$     | $1$   |

$P(A\cap B)=P(M)*P(S)=0.4*0.3=0.12$

## Binomialverteilte Zufallsgröße

| Begriff                       | Erklärung                                                                                         |
| ----------------------------- | ------------------------------------------------------------------------------------------------- |
| Diskrete Zufallsgrößen        | Kann nur ganzzahlige Werte annehmen                                                               |
| Wahrscheinlichkeitsverteilung | Gibt an, wie sich die Wahrscheinlichkeit auf die möglichen Werte einer Zufalssvariable verteilen  |
| Bernoulli-Versuch             | Es gibt nur 2 mögliche Ausgänge (Erfolg, Misserfolg)                                              |
| Bernoulli-Kette               | Bernoulli-Versuch wird mehrfach hintereinander ausgeführt, die einzelnen Versuche sind unabhängig |

Die Binomialverteilung ist eine diskrete Wachscheinlichkeitsverteilung. Sie beschreibt die Anzahl der Erfolge in einer Bernoulli-Kette.

**Beispiel**
4 mal Würfeln, „6“ gilt als Erfolg, ansonsten ist es ein Misserfolg

~~~mermaid
graph LR
A[*]
A-->|1/6|A0[Erfolg]
A-->|5/6|A1[Misserfolg]
A0-->|1/6|A00[Erfolg]
A0-->|5/6|A01[Misserfolg]
A1-->|1/6|A10[Erfolg]
A1-->|5/6|A11[Misserfolg]
A00-->|1/6|A000[Erfolg]
A00-->|5/6|A001[Misserfolg]
A01-->|1/6|A010[Erfolg]
A01-->|5/6|A011[Misserfolg]
A10-->|1/6|A100[Erfolg]
A10-->|5/6|A101[Misserfolg]
A11-->|1/6|A110[Erfolg]
A11-->|5/6|A111[Misserfolg]
A000-->|1/6|A0000[Erfolg]
A000-->|5/6|A0001[Misserfolg]
A001-->|1/6|A0010[Erfolg]
A001-->|5/6|A0011[Misserfolg]
A010-->|1/6|A0100[Erfolg]
A010-->|5/6|A0101[Misserfolg]
A011-->|1/6|A0110[Erfolg]
A011-->|5/6|A0111[Misserfolg]
A100-->|1/6|A1000[Erfolg]
A100-->|5/6|A1001[Misserfolg]
A101-->|1/6|A1010[Erfolg]
A101-->|5/6|A1011[Misserfolg]
A110-->|1/6|A1100[Erfolg]
A110-->|5/6|A1101[Misserfolg]
A111-->|1/6|A1110[Erfolg]
A111-->|5/6|A1111[Misserfolg]
~~~

| Anzahl Erfolge | Anzahl Pfade | Wahrscheinlichkeit                |
| -------------- | ------------ | --------------------------------- |
| 0              | 1            | $1*\frac{1}{6}^{0}*\frac{5}{4}^{4}\approx0.4823$ |
| 1              | 4            | $4*\frac{1}{6}^{1}*\frac{5}{3}^{4}\approx0.3858$ |
| 2              | 6            | $6*\frac{1}{6}^{2}*\frac{5}{2}^{4}\approx0.1157$ |
| 3              | 4            | $4*\frac{1}{6}^{3}*\frac{5}{1}^{4}\approx0.0154$ |
| 4              | 1            | $1*\frac{1}{6}^{4}*\frac{5}{0}^{4}\approx0.0008$ |

- - -

10 mal Würfeln Wahrscheinlichkeit auf einen Pfad mit genau 6 Erfolgen: $(\frac{1}{6})^{6}*(\frac{5}{6})^{4}$

Anzahl Pfade: $\binom{10}{6}=\frac{10!}{6!(10-6)!}$

$\binom{n}{k}=\frac{n!}{k!(n-k)!}$
$n$ Durchführungszahl
$k$ Anzahl Erfolge

## Bernoulli-Formel

Gegeben ist ein $n$-stufiges Zufallsexperiment und die Erfolgswahrscheinlichkeit $p$. Die Zufallsgröße $x$ beschreibt die Anzahl der Erfolge.

$P(x=k)=\binom{n}{k}*p^{k}*(1-p)^{n-k}$

~~~js
binomCdf(count, percentage, min, max)
~~~

### Zeichnen von Histogrammen

![](Histogramm.png)

$n=10$ $p=0.8$

| $k$  | $P(x=k)$    | kumuliert   |
| ---- | ----------- | ----------- |
| $0$  | $0.0000001$ | $0.0000001$ |
| $1$  | $0.000004$  | $0.0000041$ |
| $2$  | $0.000074$  | $0.0000781$ |
| $3$  | $0.000786$  | $0.0008641$ |
| $4$  | $0.005505$  | $0.0063691$ |
|      |             |             |
| $10$ | $0.107374$  | $1.0$       |

#### Eigenschaften von Histogrammen

- Histogramme der Binominalverteilung sind nur symmetrisch für $p=0.5$
- Bei $p>0.5$ ist die rechte Säule stets größer als die linke Säule
- Bei $p<0.5$ ist die linke Säule neben der höchsten Säule stets größer als die rechte Säule neben der höchsten Säule
- Die Höchste Säule ist beim Erwartungswert
- Bei der kumulierten Binominalverteilung ist die letzte Säule stets 1
- Je weiter ein Ereigniss vom Erwartungswert entfernt ist, desto kleiner ist sein Wert.

### Summenschreibweise für Intervall-Wahrscheinlichkeiten

**Beispiel**
$n=50$
$p=0.9$

$P(0\leq x\leq45)=\sum_\limits{k=0}^{45}\binom{50}{k}p^{k}(1-p)^{50-k}$
$P(43\leq x\leq50)=\sum_\limits{k=43}^{50}\binom{50}{k}p^{k}(1-p)^{50-k}$
$P(0\leq x\leq39)=\sum_\limits{k=0}^{39}\binom{50}{k}p^{k}(1-p)^{50-k}$
$P(42\leq x\leq48)=\sum_\limits{k=42}^{48}\binom{50}{k}p^{k}(1-p)^{50-k}$

### Minimale Durchführungszahl

Wie oft muss dieser Zufallsversuch durchgeführt werden, damit mit einer Wahrscheinlichkeit von mindestens 1 Treffer dabei ist?

| Beispiel                                | Allgemein                             |
| --------------------------------------- | ------------------------------------- |
| $P(x\geq1)\geq0.98$                     | $P(x\geq1)\geq a$                     |
| $1-P(x=0)\geq0.98$                      | $1-P(x=0)\geq a$                      |
| $1-\binom{n}{0}0.8^{0}*0.2^{n}\geq0.98$ | $1-\binom{n}{0}p^{0}*(1-p)^{n}\geq a$ |
| $1-0.2^{n}\geq0.98$                     | $1-(1-p)^{n}\geq a$                   |
| $0.02\geq0.2^{n}$                       | $1-a\geq(1-p)^{n}$                    |
| $\ln{0.02}\geq\ln{0.2^n}$               | $\ln{1-a}\geq\ln{(1-p)^{n}}$          |
| $\ln{0.02}\geq n*\ln{0.2}$              | $\ln{1-a}\geq n\ln{1-p}$              |
| $\frac{\ln{0.02}}{\ln{0.2}}\geq n$      | $\frac{\ln{1-a}}{\ln{1-p}}\geq n$     |

#### Mehr als ein Treffer

~~~js
binomCtf(n, p, x, n)
~~~

### Erwartungswert, Standardabweichung, und Varianz bei binominalverteilten Zufallsgrößen

#### Erwartungswert

**Beispiel**
Ein Würfel wird 60 mal geworfen. Wie oft kann man dabei eine „6“ erwarten?
$\mu=np=60 \frac{1}{6}=10$

#### Varianz und Standartabweichung

Varianz
$V=np(1-p)$

Standartabweichung
$\sigma=\sqrt{V}=\sqrt{np(1-p)}$

Die Standartabweichung gibt an, wie stark die Werte einer Zufallsgröße vom Erwartungswert abweichen. Die Standartabweichung sit die Wurzel aus der Varianz.

### Wahrscheinlichkeitsverteilung und Erwartungswert einer Zufallsgröße

**Beispiel**
In einer Lostrommel sind 20% Gewinnlose und 80% Nieten. Jemand will solange ein Los ziehen, bis er ein Gewinnlos gezogen hat, maximal jedoch 5 mal. Ermittle, mit welcher Ausgabe er rechnen muss, wenn ein Los 2€ kostet.

x Anzahl Lose

| $x_{1}$ | $P(x=x_{1})$          |
| ------- | --------------------- |
| 1       | $0.2$                 |
| 2       | $0.8*0.2=0.16$        |
| 3       | $0.8^{2}*0.2=0.128$   |
| 4       | $0.8^{3}*0.2=0.14024$ |
| 5       | $0.8^{4}=0.4069$      |

$E(x)=1*0.2+2*0.16+3*0.128+4*0.14024+5*0.4069=3.3481$

Ausgabe: $2\text{€}*3.3481=6.7\text{€}$

**Beispiel**
Eine Urne enthält 6 Kugeln. 3 davon sind mit „1“ beschriftet, 2 mit „2“ und eine mit „3“. In einem Spiel werden 2 Kugeln ohne zurücklegen gezogen. Die Summe der Nummern kommt man in Euro ausgezahlt.

1) Ermittle, mit welcher Auszahlung langfristig pro Spiel zu rechnen ist.
2) Bestimme, wie hoch der Einsatz bei diesem Spiel sein muss, damit das Spiel fair ist.

| $x_{i}$ | Gezogen           | $P(x=x_{i})$    |
| ------- | ----------------- | --------------- |
| 2       | (1,1)             | $\frac{6}{10}$  |
| 3       | (1,2) (2,1)       | $\frac{12}{30}$ |
| 4       | (1,3) (3,1) (2,2) | $\frac{8}{30}$  |
| 5       | (2,3) (3,2)       | $\frac{4}{30}$  |

$E(x)=2 \frac{6}{30}+3 \frac{12}{30}+4 \frac{8}{30}+4 \frac{8}{30}+5 \frac{4}{30}=3.33\text{€}$

$0=(2-y) \frac{6}{30}+(3-y) \frac{12}{30}+(4-y) \frac{8}{30}+(5-y) \frac{4}{30}=3.33\text{€}$
