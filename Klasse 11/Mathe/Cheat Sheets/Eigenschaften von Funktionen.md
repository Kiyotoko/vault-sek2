---
author: karlz
tags:
- Mathe
- FGB
---

# Nullstellen

Funktion $0$ setzen. Synonym zum Schnittpunkt mit der $x$-Achse.
$0=f(x)$

```js
solve(f(x) = 0, x)
```

```js
zeros(f(x), x)
```

## PQ-Formel

Für quadratische Funktionen der Form $x^{2}+px+q=0$ gilt:
$x=- \frac{p}{2}\pm\sqrt{(\frac{p}{2})^{2}-q}$

## Vielfachheit von NSt

Anzahl der Nullstellen.

# Schnittpunkt mit der $y$-Achse

Bei der Funktion $0$ einsetzen.
$y=f(0)$

# Bereiche

## Definitionsbereich

$$\mathbb{D}=x\in\mathbb{R}$$

Teilen durch $0$.
$f(x)=\frac{n}{x}$
Wurzeln mit Werten unter $0$.
$f(x)=\sqrt{x}$
Logarithmus mit Werten unter $0$
$f(x)=\log{x}$
Einschränkungen durch die Aufgabenstellung
$i=[\dots]$

## Wertebereich

$$\mathbb{W}=y\in\mathbb{R}$$

Asymptoten bzw. Limes
$\lim\limits_{x\to\infty}\sum\limits_{n=1}^{x} \frac{1}{2^{n}}=1$
Wurzel hat keine Werte unter $0$
$\sqrt{x}\ge0$
Logarithmus hat keine Werte unter $0$
$\log{x}\ge0$
EInschränkung durch die Aufgabenstellung
$i=[\cdots]$

# Asymptoten

## Waagerechte Asymptoten

Berechnung über den Grenzwert im Unendlichen.

$f(x)=\frac{2x^2-1}{x-x^2}$
$\lim\limits_{x\to\pm\infty}f(x)=-2$

## Senkrechte Asymptoten

Senkrechte Asymptoten sind Polstellen. Polstellen sind die Definitionslücken gebrochen-rationaler Funktionen.
Man ermittelt sie, indem man den Nenner gleich $0$ setzt.

$f(x)=\frac{2x^2-1}{x-1}$
$0=x-1\quad x=1$

# Symmetrie

## Achsensymmetrie

Achsensymmetrie zur $y$-Achse: $f(x)=f(-x)$
$f(x)=x^4+x^2+4$

## Punktsymmetrie

Punktsymmetrie zu einem Punkt, meist Koordinatenursprung.
$f(x)=-f(-x)$
$-f(x)=f(-x)$

# Extrempunkte / Extremstellen

An Extremstellen gilt:
- $f'(x)=0$ (notwendig)
- $f''(x)\neq0$ (hinreichend)

**Beispiel**
$f(x)=x^2-2x+1$
$f'(x)=2x-2$
$f''(x)=2$

$0=2x-2\to x=1$
$0\neq2$

## Nachweis der Art des Extrems

Minimum: $f''(x_{E})>0$
Maximum: $f''(x_{E})<0$
Sattelpunkt: $f''(x_{E})=0$

  **Beispiel**
$f(x)=x^2$
$f'(x)=2x$
$f''(x)=2$

$0=2x_E\quad x_E=0$

Sattelpunkt, da:
$f(0)=0$
$f'(0)=0$
$f''(0)=0$

## Absolute Extrema

Ist $f$ in einem abgeschlossenen Intervall $[a, b]$ definiert, so ergeben sich die absoluten Extrema, indem man die relativen Extrema bestimmt und mit den Funktionswerten am Rand vergleicht (Randwerte).

# Wendepunkte / Wendestellen

Ist $f$ im Intervall $]a,b[$ differenzierbar und geht der Graph $f$ beim Durchlaufen eines Punktes $W(x_W|y_W)$ von einer Rechtskurve in eine Linkskurve (oder umgekehrt) über, so heißt $W$ ein Wendepunkt und die Stelle $x_W$ eine Wendestelle von $f$.

Die Tangent in $W$ heißt Wendetangente. Ein Wendepunkt mit horizontaler Tangente heißt Sattelpunkt (Terassenpunkt).

An Wendepunkten gilt:
- $f''(x)=0$ (notwendig)
- $f'''(x)\neq0$ (hinreichend)
