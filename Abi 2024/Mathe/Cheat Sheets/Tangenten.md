# Änderungsrate
~~~ad-important
- Durchschnittliche Änderungsrate: Differenzenquotient
- Momentane Änderungsrate: Differentialquotient (Ableitung)
~~~
# Tangenten
~~~ad-help
1. Die Tangente ist eine Gerade ($y=mx+n$).
2. Die Tangente hat mit dem Funktionsgrahen den Berührungspunkt gemeinsam.
3. Im Berührungspunkt ist der Anstig der Tangente gleich dem Anstieg des Funktionsgraphen.
~~~
## Zu Punkten und Parallelen
~~~ad-important
1. Ableitung bilden
2. Berührungspunkt bilden
3. $m$ berechnen
4. $n$ berechnen
5. Tangentengleichung angeben
~~~

~~~ad-example
$$f(x)=x^2\quad x_0=2$$
- $f'(x)=2x$
- $P(2|f(2))=P(2|4)$
- $m=f'(2)=4$
- $4=4*2+n\to n=-4$
- $t(x)=4x-4$
~~~
## Von externen Punkten
~~~ad-important
1. Ableitung bilden
2. Gedachter Berührungspunkt $A$ bilden
3. Schnittpunkte $s$ bilden
4. Tangentengleichung angeben
~~~

~~~ad-help
$f(x)=...$
$f'(x)=...$

$Q(x_Q|y_Q)$
$A(x_A|f(x_A))$

$m=\frac{x_Q-f(x_A)}{y_Q-x_A}$
$m=f'(x_A)$

$s=solve(\frac{y_Q-f(x_A)}{x_Q-x_A}=f'(x_A),x_A)$
$t(x)=tangentline(f(x),x,s)$
~~~
# Normale
~~~ad-important
Die Normale steht senkrecht auf der Tangente.
~~~

~~~ad-info
Normale: $m=-\frac{1}{f'(x)}$
~~~

~~~ad-help
$normalline(f(x),x,s)$
~~~

$f(x):=x^2$
$f1(x):=\frac{d}{dx}f(x)$
$solve(f1(x)=\frac{f(x)-0}{x--2},x)$
→ -4 → 0

$tangentline(f(x), x, -4)$

$y=mx+n$
$y=-8x-16$


$\sqrt{x^2+y^2}=\sqrt{(-6-0)^2+(0-f(0))^2}$
~~~functionplot
f(x)=9*(x+3)/(x+6)
t(x)=.75x+4.5
~~~