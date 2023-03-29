---
author: karlz
tags:
- Mathe
---

# Zahlenbereiche

## Natürliche Zahlen

- Beinhaltet alle positiv ganzen Zahlen
- Symbol $\mathbb{N}$

## Gebrochene Zahlen

- Erweiterung der natürlichen Zahlen, erweitert durch Brüche
- Symbol $\mathbb{Q^+}$

## Reelle Zahlen

- Beinhalten auch $\sqrt{2}$ und $\pi$
- Symbol $\mathbb{R}$

## Komplexe Zahlen

- Erweiterung der reellen Zahlen um eine imaginäre Einheit $i$ mit $i^2=-1$
- Symbol $\mathbb{C}$

# Tensoren

- Multidimensionale Arrays

## Vektoren

- $\vec a$ Vektor $\begin{pmatrix}a_1\\ a_2\\a_3\end{pmatrix}$
- Rechenoperatoren:
	- Addition und Subtraktion
	- Skalarmultiplikation
	- Skalarprodukt

## Matrix

- $m,n$-Matrix $\begin{pmatrix}a_{1,1}&a_{1,2}&\cdots&a_{1,n}\\a_{2,1}&a_{2,2}&\cdots&a_{1,n}\\ \vdots&\vdots&\ddots&\vdots \\ a_{m,1}&a_{m,2}&\cdots&a_{m,n}\end{pmatrix}$
- Rechenoperation:
	- Addition zweier gleich großer $mn$-Matrizen
	- Skalarmultiplikation einer Matrix mit einem Skalar
	- Matrizenmultiplikation zweier Matrizen, wobei die Spaltenanzahl der linken Matrix mit denen der Zeilenanzahl der rechten Matrix übereinstimmt

### Gauß-Verfahren

Das gaußsche Eliminationsverfahren oder einfach Gauß-Verfahren ist ein Algorithmus aus den mathematischen Teilgebieten der linearen Algebra und der Numerik. Es ist ein wichtiges Verfahren zum Lösen von linearen Gleichungssystemen und beruht darauf, dass Äquivalenztransformationen zwar das Gleichungssystem ändern, aber die Lösung erhalten. Dies erlaubt es, jedes eindeutig lösbare Gleichungssystem auf Stufenform zu bringen, an der die Lösung durch sukzessive Elimination der Unbekannten leicht ermittelt oder die Lösungsmenge abgelesen werden kann. 

- **Beispiel**
	- $a+b+c=x\quad a+b+c=x$
	- $a+b+c=x\quad b+c=x$
	- $a+b+c=x\quad c=x$

# Differenzialrechnung

Die Differential- oder Differenzialrechnung ist ein wesentlicher Bestandteil der Analysis und damit ein Gebiet der Mathematik. Zentrales Thema der Differentialrechnung ist die Berechnung lokaler Veränderungen von Funktionen. Während eine Funktion ihren Eingabewerten nach tabellarischem Prinzip gewisse Ausgangswerte zuordnet, wird durch die Differentialrechnung ermittelt, wie stark sich die Ausgabewerte nach sehr kleinen Veränderungen der Eingabewerte ändern. Sie ist eng verwandt mit der Integralrechnung, mit der sie gemeinsam unter der Bezeichnung Infinitesimalrechnung zusammengefasst wird. 

- **Beispiel**
	- $f(x)=x^2$
	- $f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}=\lim_{h\to 0}\frac{(x+h)^2-x^2}{h}=\lim_{h\to0}\frac{x^2+2xh+h^2-x^2}{h}=\lim_{h\to 0}(2x+h)$

# Beweise

Ein Beweis ist in der Mathematik die als fehlerfrei anerkannte Herleitung der Richtigkeit bzw. der Unrichtigkeit einer Aussage aus einer Menge von Axiomen, die als wahr vorausgesetzt werden, und anderen Aussagen, die bereits bewiesen sind. Man spricht daher auch von axiomatischen Beweisen.

## Beweismethoden

Einige mathematische Sätze oder logische Schlussregeln lassen sich für eine Vielzahl von Beweisen einsetzen und beeinflussen die Struktur des Beweises besonders stark.

### Direkter Beweis

Für einen direkten Beweis (direkter Schluss) nimmt man einen bereits als richtig bewiesenen Satz (Prämisse) und leitet, durch logische Schlussfolgerungen, daraus den zu beweisenden Satz (Konklusion) ab.

### Indirekter Beweis

Bei einem indirekten Beweis (Reductio ad absurdum, Widerspruchsbeweis) zeigt man, dass ein Widerspruch entsteht, wenn die zu beweisende Behauptung falsch wäre. Dazu nimmt man an, dass die Behauptung falsch ist, und wendet dann die gleichen Methoden wie beim direkten Beweis an. Wenn daraus ein Widerspruch entsteht, dann kann die Behauptung nicht falsch sein, also muss sie richtig sein.

### Vollständige Induktion

Der Beweis durch vollständige Induktion ist ein oft angewendetes Verfahren zum Beweis von Sätzen der Form „Für jede natürliche Zahl n n gilt …“. Dazu zeigt man zuerst, dass die Aussage für $n=0$ (oder auch einen anderen Anfangswert $n_{0}$) gilt, und danach, dass sie immer auch für $n+1$ gilt, wenn sie für ein $n$ gilt.

### Vollständige Fallunterscheidung

Bei einem Beweis durch vollständige Fallunterscheidung (engl. proof by exhaustion „durch Ausschöpfung“) wird jeder der möglichen Fälle einzeln betrachtet. Die Zahl der möglichen Fälle muss daher endlich sein.

### Diagonalverfahren

Die Diagonalverfahren wurden von Georg Cantor zum Beweis zweier spezieller Aussagen entwickelt. Sie haben sich seitdem als allgemeine Beweismethoden bewährt.

Das erste Cantorsche Diagonalverfahren ist ein direkter Beweis für die Abzählbarkeit einer Menge. Es wird gezeigt, dass man jedem Element der zu untersuchenden Menge eine natürliche Zahl zuordnen kann.

Das zweite Cantorsche Diagonalverfahren ist ein indirekter Beweis für die Überabzählbarkeit einer Menge. Es wird also das Gegenteil angenommen, nämlich dass die Menge abzählbar wäre. Dann wird aus dieser Annahme ein Widerspruch hergeleitet, sodass sie fallen gelassen werden muss. 

# Ungleichungen

## Formen Von Ungleichungen

$T_1<T_2$
$T_2\leq T_2$
$T_1>T_2$
$T_1\geq T_2$
$T_1\neq T_2$

## Umformung Von Ungleichungen

### Umkehrbarkeit

Ungleichungen können umgekehrt werden $(T_1\leq T_2)\Leftrightarrow(T_2\geq T_1)$

### Monotoniegesetz

#### Addition Und Subtraktion

- Es ist $T_1 < T_2$ genau dann, wenn $T_1+T_3 < T_2+T_3$.
- Es ist $T_1 < T_2$ genau dann, wenn $T_1-T_3 < T_2-T_3$.

#### Multiplikation Und Division

- Aus $T_1<T_2$ folgt $-T_1>-T_2$.
- Aus $0<T_1<T_2$ folgt $0<1/T_2<1/T_1$.
- Aus $T_3 > 0$ und $T_1<T_2$ folgt $T_1 T_3 < T_2 T_3$ und $T_1/T_3 < T_2/T_3$.
- Aus $T_3 < 0$ und $T_1<T_2$ folgt $T_1 T_3 > T_2 T_3$ und $T_1 / T_3 > T_2/T_3$.
