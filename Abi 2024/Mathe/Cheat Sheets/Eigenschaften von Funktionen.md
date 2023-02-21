# Nullstellen
Funktion $0$ setzen.
$0=f(x)$
## Vielfachheit von NSt
Anzahl der Nullstellen.
# Schnittpunkt mit der $y$-Achse
Bei der Funktion $0$ einsetzen.
$y=f(0)$
# Definitionsbereich
Teilen durch $0$.
$f(x)=\frac{n}{x}$
Wurzeln mit Werten unter $0$.
$f(x)=\sqrt{x}$
Logarithmus mit Werten unter $0$
$f(x)=\log{x}$
Einschränkungen durch die Aufgabenstellung
$i=[\dots]$
# Asymptoten
## Waagerechte Asymptoten
Berechnung über den Grenzwert im Unendlichen.

$f(x)=\frac{2x^2-1}{x-x^2}$
$\lim\limits_{x\to\pm\infty}f(x)=-2$
## Senkrechte Asymptoten
<pre style="background-color:#3CB371;"><code style="color:white;">Senkrechte Asymptoten sind Polstellen. Polstellen sind die Definitionslücken gebrochen-rationaler Funktionen. 
Man ermittelt sie, indem man den Nenner gleich <span class="math inline">0</span> setzt.</code></pre>

<pre style="background-color:#8800ff;"><code style="color:white;"><span class="math inline">f(x)=\frac{2x^2-1}{x-1}</span>
<span class="math inline">0=x-1\quad x=1</span></code></pre>

~~~functionplot
f(x)=(4+x)/(2x)
~~~
# Symmetrie
## Achsensymmetrie
<pre style="background-color:#3CB371;"><code style="color:white;">Achsensymmetrie zur <span class="math inline">y</span>-Achse: <span class="math inline">f(x)=f(-x)</span>
<span class="math inline">f(x)=x^4+x^2+4</span></code></pre>

~~~functionplot
f(x)=x^4+x^2+4
~~~
## Punktsymmetrie
<pre style="background-color:#3CB371;"><code style="color:white;">Punktsymmetrie zu einem Punkt, meist Koordinatenursprung.
<span class="math inline">f(x)=-f(-x)</span>
<span class="math inline">-f(x)=f(-x)</span>
</code></pre>

~~~functionplot
f(x)=x^5+x^3+x
~~~
# Extrempunkte / Extremstellen
<pre style="background-color:#3CB371;"><code style="color:white;">An Extremstellen gilt:<li><span class="math inline">f'(x)=0</span><em> (notwendig)</em><li><span class="math inline">f''(x)\neq0</span><em> (hinreichend)</em></code></pre>

<pre style="background-color:#8800ff;"><code style="color:white;"><span class="math inline">f(x)=x^2-2x+1</span>
<span class="math inline">f'(x)=2x-2</span>
<span class="math inline">f''(x)=2</span>

<span class="math inline">0=2x-2\to x=1</span>
<span class="math inline">0\neq2</span>
</code></pre>
## Nachweis der Art des Extrems
<pre style="background-color:#3CB371;"><code style="color:white;"><li>Minimum: <span class="math inline">f''(x_E)>0</span></li><li>Maximum: <span class="math inline">f''(x_E)<0</span></li>oder
<li>Minimum: <span class="math inline">f'(x)=-\to f'(x)=+</span></li><li>Maximum: <span class="math inline">f'(x)=+\to f'(x)=-</span></li></code></pre>

~~~functionplot
---
disableZoom: true
---
f(x)=x^2
f'(x)=2x
~~~

<pre style="background-color:#8800ff;"><code style="color:white;"><span class="math inline">f(x)=x^2</span>
<span class="math inline">f'(x)=2x</span>
<span class="math inline">f''(x)=2</span>

<span class="math inline">0=2x_E\quad x_E=0</span>

Sattelpunkt, da:
<li><span class="math inline">f'(0)=0</span></li><li><span class="math inline">f''(0)=0</span></li><li><span class="math inline">f(0)=0</span></li></code></pre>
## Absolute Extrema
<pre style="background-color:#3CB371;"><code style="color:white;">Ist <span class="math inline">f</span> in einem abgeschlossenen Intervall <span class="math inline">[a, b]</span> definiert, so ergeben sich die absoluten Extrema, indem man die relativen Extrema bestimmt und mit den Funktionswerten am Rand vergleicht (Randwerte).
</code></pre>
# Wendepunkte / Wendestellen
<pre style="background-color:#3CB371;"><code style="color:white;">Ist <span class="math inline">f</span> im Intervall <span class="math inline">]a,b[</span> differenzierbar und geht der Graph <span class="math inline">f</span> beim Durchlaufen eines Punktes <span class="math inline">W(x_W|y_W)</span> von einer Rechtskurve in eine Linkskurve (oder umgekehrt) über, so heißt <span class="math inline">W</span> ein Wendepunkt und die Stelle <span class="math inline">x_W</span> eine Wendestelle von <span class="math inline">f</span>.

Die Tangent in <span class="math inline">W</span> heißt Wendetangente. Ein Wendepunkt mit horizontaler Tangente heißt Sattelpunkt (Terassenpunkt).
</code></pre>

<pre style="background-color:#1E90FF;"><code style="color:white;">An Wendepunkten gilt:
<li><span class="math inline">f''(x)=0</span><em> (notwendig)</em>
<li><span class="math inline">f'''(x)\neq0</span><em> (hinreichend)</em>
</code></pre>