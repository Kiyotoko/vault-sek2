# Kinematik

Lehre von der Beschreibung von Bewegungen aller Art
 
## Bewegungsarten

- geradlinig
- krummlinig
- kreisförmig
- Schwingung

## Bewegungsformen

- gleichförmig
- beschleunigt

## Modell Massepunkt

Modell eines ausgedehnten Körpers. Er beschreibt den jeweiligen Ort des Körpers. Nicht berücksichtigt werden Form und Größe. Die gesamte Masse ist gedanklich in einem Punkt vereint.

## Bezugssystem

Ein gedachtes raum-zeitliches Gebilde, das erforderlich ist, um das Verhalten ortsabhängiger Größen eindeutig und vollständig zu beschreiben. Insbesondere kann die Lage und Bewegung von physikalischen Körpern nur relativ zu einem Bezugssystem angegeben werden. 

## Ort und Weg

Beschreibt die Position eines Körpers zu einem bestimmten Zeitpunkt $t$.
- Formelzeichen $r$ bzw. $r(t)$ o. $x$ bzw. $x(t)$

Ist die zurückgelegte Strecke eines Körpers in einem bestimmten Zeitintervall $\Delta t$.
- Formelzeichen $s$ bzw. $s(\Delta t)$

## Durchschnittsgeschwindigkeit

- Formelzeichen $v$
- Einheit $1\frac{m}{s}$
- Formel $v=\frac{\Delta s}{\Delta t}$

## Relativgeschwindigkeit

- Formel $v_{KBS}=v_K-v_{BS}$
	- $v_K$ Geschwindigkeit des Körpers bezüglich der Erde
	- $v_{BS}$ Geschwindigkeit des Bezugsystemes BS bezüglich der Erde
	- $v_{KBS}$ Geschwindigkeit des Körpers K bezüglich des neuen Bezugsystems BS

## Beschleunigung

Gibt die Geschwindigkeitsveränderung eines Körpers innerhalb eines Zeitintervalls $\Delta t$ an.
- Formelzeichen $a$ bzw. $a(t)$
- Einheit $1\frac{m}{s^2}$
- Formel $a=\frac{\Delta v}{\Delta t}$

## Momentangeschwindigkeit

Die Momentangeschwindigkeit (Augenblicksgeschwindigkeit) ist die Geschwindigkeit, die ein Körper zu einem Bestimmten Zeitpunkt $t$ besitzt.
- Formelzeichen $v(t)$
- Einheit $1\frac{m}{s}$
- Formel $\lim\limits_{\Delta t\to0}\frac{\Delta s}{\Delta t}$

## Momentanbeschleunigung

Die Momentanbeschleunigung(Augenblicksbeschleunigun) ist die Beschleunigung, die ein Körper zu einem Bestimmten Zeitpunkt $t$ besitzt.
- Formelzeichen $a(t)$
- Einheit $1\frac{m}{s²}$
- Mathematisch $\lim\limits_{\Delta t\to0}\frac{\Delta v}{\Delta t}$

## Zurückgelegter Weg

Der Flächeninhalt, der von dem Graphen im $v$-$t$-Diagramm und der Zeitachse eingeschlossen wird, entspricht dem zurückgelegten Weg.
- Mathematisch $\int v(t)dt =s(t)$

## Geschwindigkeit

Der Flächeninhalt, der von dem Graphen im $a$-$t$-Diagramm und der Zeitachse eingeschlossen wird, entspricht der Momentangeschwindigkeit.
- Mathematisch $\int a(t)dt =s(t)$

## Gleichförmige Bewegung

Bei der Gleichförmigen Bewegung ist die Geschwindigkeit konstant. Die Fläche bildet unter dem Graphen im $t$-$v$-Diagramm ein Rechteck mit der Fläche $\Delta s=v*t$.
- Formeln
	- $v(t)=v=konst.$
	- $s(t)=v*t+s_0$

## Gleichmäßig Beschleunigte Bewegung

Bei der Gleichmäßig beschleunigten Bewegung ist die Beschleunigung konstant.
- Formeln
	- $a(t)=a=konst.$
	- $v(t)=a*t+v_0$
	- $s(t)=\frac{1}{2}a*t²+v_0*t+s_0$

## Freier Fall

Ein Körper fällt aufgrund der Erdanziehungskraft beschleunigt nach unten.
- Formeln
	- $s=\frac{1}{2}gt²$
	- $t=\sqrt{\frac{2s}{g}}$
	- $v=\sqrt{2sg}$

## Senkrechter Wurf

Die Bewegung startet mit einer Geschwindigkeit von $v_0$. Senkrechte Würfe sind Fallbewegungen mit der Anfangsgeschwindigkeit.
- Formeln
	- $t_s=\frac{v_0}{g}$
	- $a(t)=-g$
	- $v(t)=-g*t$

## Mehrdimensionale Bewegung

### Zusammengesetzte Bewegungen

Zwei Teilbewegungen können sich zu einer zusammengesetzten Bewegung überlagern. Die Teilbewegungen können:
1. in gleicher Richtung
1. in entgegengesetzter Richtung
1. senkrecht zueinander
1. schräg zueinander

erfolgen.

### Geschwindigkeit Als Vektorielle (gerichtete) Größe

- sie ist entlang der Bewegungsrichtung orientiert → wir als Vektor (Pfeil) dargestellt $\vec{v}$-beschreibt den Vector(-pfeil)
- Betrag des Vektors (Länge des Pfeils) gibt die Geschwindigkeit an $v$-Zahlenwert mit Einheit

### Addition Von Geschwindigkeitsvektoren

Vektoren werden addiert, indem man sie aneinander legt. Der Gesamtvektor zeigt dann von Anfang des ersten bis zum Ende des letzten Vektors.
- Formel $v_{ges}=\sqrt{v_0²+2v_0v_1\cos{\alpha}+v_1²}$

## Waagerechter Wurf

Ein waagerechter Wurf wird durch die Erdanziehungskraft nach unten beschleunigt, er bewegt sich in einer gekrümmten Bahn. Unter idealen Bedingungen wird der Körper in horizontaler Richtung weder langsamer noch schneller, senkrecht nach unten wird er hingegen gleichmäßig beschleunigt.

~~~functionplot
---
xLabel: Zeit
yLabel: Höhe
bounds: [0,10,0,10]
disableZoom: true
---
f(x)=-0.1x^2+9
~~~

- Formeln
	- $a_x=0$
	- $v_x=v_0$
	- $s_x=v_0*t$
	- $a_y=-g$
	- $v_y=-g*t$
	- $s_y=-\frac{1}{2}g*t²$
- Herleitung $y(t=\frac{x}{2v_0})=-\frac{g}{2v_0²}*x²+h_0$

## Schiefer Wurf

- Formeln
	- $x(t=v_0x*t=v_0\cos{\alpha}*t$
	- $y(t)=-\frac{g}{2}t²+v_0y*t+y_0=-\frac{g}{2}t²+v_0\sin{\alpha}*t+y_0$
- Herleitung
	- $v_x=v_0\cos{\alpha}\quad v_y=-gt+v_0\sin{\alpha}$
	- $y(t=\frac{x}{v_0\cos{\alpha}})=\frac{-g}{2}(\frac{x}{v_0\cos{\alpha}})^2+v_0\sin{\alpha}\frac{x}{\cos{\alpha}}+y_0=\frac{-g}{2v_0^2\cos{\alpha}^2}+\tan{\alpha}x+y_0$
	- $v=\sqrt{v_y^2+v_x^2}=\sqrt{(-gt+v_0\sin{\alpha})^2+(v_0\cos{\alpha})^2}$

## Kreisbewegung

|Kenngröße|Beschreibung|Formel|
|-|-|-|
|Umlaufdauer $T$|Gibt die Dauer für eine vollständige Umdrehung an.|$T=\frac{t}{N}$|
|Drehzahl $f$|Gibt die Anzahl der Umdrehungen pro Zeiteinheit an.|$f=\frac{N}{t}=\frac{1}{T}$|

### Winkel- Und Bahngeschwindigkeit

Gibt den Winkel auf einer Kreisbahn an, den ein Körper in einer bestimmten Zeit überstreicht.
- Formelzeichen $\omega$
- Einheit $s^{-1}$
- Formel $\omega=\frac{2\pi}{T}=2\pi f$

Gibt an, wie viel Weg ein Körper auf seiner Kreisbahn in einer bestimmten Zeit zurücklegt.
- Formelzeichen $v$
- Einheit $\frac{m}{s}$
- Formel $v=\frac{s}{t}=\frac{2\pi r}{T}=\omega r$

### Radialbeschleunigung

Da sich die Richtung der Geschwindigkeit ändert, wirkt auf den Körper ständig eine Beschleunigung. Sie ist stets zum Kreismittelpunkt gerichtet.
- Formelzeichen $a_r$
- Einheit $\frac{m}{s^2}$
- Formel $a_r=\frac{v^2}{r}=\omega^2r$

