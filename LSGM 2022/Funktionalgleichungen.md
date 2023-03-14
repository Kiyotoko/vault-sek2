---
author: karlz
tags:
- topic/math
---

# Funktionalgleichungen

Finde alle Funktionen $f: R\in\mathbb{R}$ mit $a*f(ab)= f(b)$
- $b=1$
- $a - f(a) = f(1)$
- $f(a) = \frac{f(1)}{a} = \frac{c}{a}$

Probe: 
- $a*f(a)=a*\frac{c}{a*b}=\frac{c}{b}$
- $f(b)=\frac{c}{b}$

Lösungen:
- $f(a) = \frac{c}{a}$ mit einer Konstanten $c$
- - -
Finde alle Funktionen $f: R \in\mathbb{R}$ mit $2a - f(a) +\frac{1}{2}a - f(\frac{1}{a}) = 10$
- a = $\frac{1}{a}$
- $\frac{2}{a} - f(\frac{1}{a}) + \frac{2}{a} - f(a) = 10$

1. $8a*f(a)+\frac{2}{a}*f(\frac{1}{a})=40$
1. $\frac{a}{2}*f(a)+\frac{2}{a}*f(\frac{1}{a})=10$

- $I - II$
- $(8a-\frac{a}{2})*f(a)=30$
- $\frac{15}{2}*a*f(a)=30$
- $f(a)=\frac{4}{x}$
- - -
Finde alle Funktionen $f: R \in\mathbb{R}$ mit $a+2f(a)+f(f(b)-a)=b$
- $a=f(b)$
- $f(b)+2f(f(b))+f(f(b)-f(b))=b$
- $f(b)+2f(f(b))+f(0)=b$
- $f(b)+2b+0=b$
- $f(b)=-b$

Probe:
- $a+2(-a)+-(-b-a)=b$
- $a-2a+b+a=b$
- $b=b$

## Involutionen

<pre class="vault" style="background-color:#3CB371;"><code class="vault" style="color:white;">Funktionen mit $g(g(x)) = x$ heißen Involutionen</code></pre>

|Beispiele|
|-|
|$g(x)=\frac{1}{x}$|
|$g(x)=-x+c$|
|$g(x)=x$|
|$g(x)=c/x$|

Wenn $g$ Involution ist und $g(x)$ und $x$ als Argument in einer Funktionalgleichung vorkommen, kann man $x$ durch $g(x)$ ersetzen und erhält wie im letzten Beispiel ein Gleichungssysten mit 2 unbekannten $( f(x), f(g(x)) )$
- - -
Finde alle Funktionen $f: [0, 2] \in \mathbb{R}$ mit $f(a) + 2f(\sqrt(4 - a^2)) = 3a$
- $a=\sqrt{4-a^2}$
- $f(\sqrt{4-a^2})+2f(\sqrt{4-\sqrt{4-a^2}^2})=3(\sqrt{4 - a^2})$
- $f(\sqrt{4-a^2})+2f(\sqrt{4-(4-a^2)})=3(4-a^2)$
- $f(\sqrt{4-a^2})+2f(\sqrt{a^2}) = 3(\sqrt{4 - a^2})$
- $f(\sqrt{4-a^2})+2f(a) = 3(\sqrt{4 - a^2})$

1. $2f(\sqrt{4-a^2}) + 4f(a) = 6(\sqrt{4 - a^2})$
1. $f(a)+2f(\sqrt{4-a^2})=3a$

- $I-II$
- $3f(a) = 6(\sqrt{4 - a²}) - 3a$
- $f(a) = 2(\sqrt{4 - a²}) - a$
- - -
Finde alle Funktionen $f: [0, 1] \in R$ mit $f(a) + f(\frac{1}{1-a})=1+\frac{1}{a}+\frac{1}{1-a}$
- $a=\frac{1}{2}$
- $f(\frac{1}{2}) + f(1 / (1 - \frac{1}{2})) = 1 + \frac{1}{\frac{1}{2}} + \frac{1}{1-\frac{1}{2}}$
- $f(\frac{1}{2}) + f(2) = 1 + 2 + 2$
- $f(\frac{1}{2}) + f(2) = 5$
