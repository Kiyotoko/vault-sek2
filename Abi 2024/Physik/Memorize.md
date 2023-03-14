---
author: karlz
tags:
- topic/science
---

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

## Ort Und Weg

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

# Dynamik

## Die Newton'schen Axiome

### 1. Axiom (Trägheitsprinzip)

Jeder Körper verharrt in Ruhe oder behält seine gleichförmig geradlinige Bewegung bei, solange von außen keine Kragt auf ihn ausgeübt wird.

### 2. Axiom (Aktionsprinzip)

Die Beschleunigung eines Körpers ist direkt proportional zur auf ihn ausgeübten Kraft und indirekt proportional zu seiner Masse:
- $\vec{F}=m*\vec{a}$

### 3. Axiom (Wechselwirkungsprinzip)

Wenn ein Körper auf einen zweiten eine Kraft ausübt, so übt auch der zweite Körper eine Kraft auf den ersten aus. Beide Kräfte sind betragsmäßig gleich groß, aber entgegengesetzt gerichtet.
- $-m_1\Delta v_1=m_2\Delta v_2$
- $-m_1\frac{\Delta v_1}{\Delta t}=m_2\frac{\Delta v_2}{\Delta t}$
- $-m_1a_1=m_2a_2$
- $\vec{F}_{1\to 2}=-\vec{F}_{2\to 1}$

## Impuls & Impulserhaltungsgesetzt

### Trägheit

Um einen Körper zu beschleunigen - ihn also aus der Ruhelage in Bewegung zu versetzen, ihn abzubremsen oder seine  Bewegungsrichtung zu ändern -, ist ein bestimmter Aufwand nötig: Jeder Körper ist träge. Die Trägheit eines Körpers wird durch die Masse $m$ beschrieben: Je größer die Trägheit eines Körpers ist, desto größer ist die Masse.

### Schwere

Jeder Körper wird von einem anderen angezogen, beispielsweise ein Apfel von der Erde: Jeder Körper ist schwer. Auch die Eigenschaft der Schwere wird durch die Masse $m$ beschrieben. Je stärker ein Körper von einem anderen Körper angezogen wird, desto größer ist seine Masse.

### Impuls

Der Impuls eines Körpers ist definiert als $\vec{p}=m\vec{v}$. Es gilt der Trägheitssatz: Der Impuls ändert sich nicht, solange der Körper keinem äußeren Einfluss unterliegt.
- $p=mv$
- $p'=mv'+m'v$

### Impulserhaltungssatz

Die Vektorsumme der Impulse eines geschlossenen Systems bleibt bei allen Stößen und Wechselwirkungen innerhalb des Systems erhalten.
- $\vec{v_1}=\vec{v_2}\to\vec{v_2}=\vec{v_1}$

## Stöße

### Zentraler Elastischer Stoß

Beim zentral elastischen Stoß treffe zwei Körper auf einer Geraden aufeinander. Für die Berechnung der Geschwindigkeiten der Körper vor dem Stoß $v_1$ und nach dem Stoß $v_1'$ und $v_2'$ gilt die Energieerhaltung:
- $\frac{1}{2}m_1*v_1^2+\frac{1}{2}m_2*v_2^2=\frac{1}{2}m_1*v_1'^2+\frac{1}{2}m_2*v_2'^2$
Außerdem bleibt die Summe der Impulse erhalten:
- $m_1*v_1+m_2*v_2=m_1*v_1'+m_2*v_2'$
Bei gleichen Massen gilt:
- $v_1'=v_2$ und $v_2'=v_1$
Berechnung der Geschwindigkeiten:
- $v_1'=\frac{(m_1-m_2)*v_1+2m_2*v_2}{m_1+m_2}$
- $v_2'=\frac{(m_2-m_1)*v_2+2m_1*v_1}{m_1+m_2}$

### Vollkommen Unelastischer Stoß

Ein vollkommen unelastischer Stoß liegt vor, wenn beide Körper nach dem Stoß aneinander haften bleiben, also dann die gleiche Geschwindigkeit $v'$ haben:
- $m_1*v_1+m_2*v_2=(m_1+m_2)*v'$
Berechnung der Geschwindigkeit:
- $v'=\frac{m_1*v_1+m_2*v_2}{m_1+m_2}$

## Schiefe Ebene

$F_H=mg\cos{\alpha}$
$F_N=mg\sin{\alpha}$

Normalkraft $F_N$ und Hangabtriebskraft $F_g$ sind keine neuen Kräfte, sondern $F_N$ ist der Anteil von $F_g$, der senkrecht zur schiefen Ebene wirkt und $F_H$ ist der Anteil von $F_g$, der parrallel zur schiefen Ebene wirkt.

## Reibungskraft

$F_R=\mu*F_N$

### Haftreibung

Wenn zwei Körper aneinander haften und sich nicht zueinander bewegen (angezogene Bremse bei einem parkendem Auto).

### Gleitreibung

Wenn ein Körper auf einem anderen Körper gleitet (Schlittschuhlaufen auf dem Eis). 

### Rollreibung

Die bewegungshemmende Kraft, die zwischen Rädern und der Straße auftritt, wird als Rollreibung bezeichnet. Sie ist der Drehbewegung der Räder entgegengerichtet.

## Kraft

Kraft ist eine vektorielle Größe mit Stärke und Richtung.

### Normalkraft

Die Normalkraft $\vec{F}_N$ ist die Kraft, mit der ein Körper auf seine Unterlage wirkt.

### Radialkraft Und Radialbeschleunigung

Da sich die Richtung der Geschwindigkeit ändert, wirt auf den Körper ständig eine Kraft (Radialkraft). Diese Kraft hält den Körper auf seiner Kreisbahn. Sie ist stets zum Kreismittelpunkt gerichtet.
$a=\frac{v^2}{r}$
$F=m*r=m=\frac{v^2}{r}$

### Reibungskräfte

Reibungskräfte sind bewegungshemmende Kräfte, die an den Grenzflächen zweier Körper auftreten.
- Haftreibung
- Gleitreibung
- Rollreibung

#### Zusammenhang Zwischen Haft- Und Gleitreibung

- die Haftreibung hindert einen Körper daran sich in Bewegung zu versetzen
- die Haftreibungskraft 𝐹Ԧ hr ist immer so groß wie die Zugkraft 𝐹Ԧ Z mit der an einem Körper gezogen wird
- die Haftreibungskraft besitzt einen
maximalen Wert 𝐹HR
- wird dieser maximale Wert überschritten, setzt sich der Körper in Bewegung und fängt an zu gleiten
- $F_R=\mu*F_N$

## Energie

- Formelzeichen $E$
- Einheit $1J$

### Systeme

|Art des Systems|Kennzeichen für das System|Beispiele|
|-|-|-|
|offenes System|Systemgrenze ist durchlässig für Energie und Stoff|Motor eines Pkw, Mensch|
|geschlossenes System|Systemgrenze ist durchlässig für Energie und undurchlässig für Stoff|Kühlschrank, Wärmepumpe, Sonnenkollektor|
|abgeschlossenes System|Systemgrenze ist undurchlässig für Energie und Stoff|gut isoliertes, verschlossenes Themosgefäß|

### Energieerhaltungssatz

Energie kann weder erzeugt noch verbraucht werden. Es ist lediglich möglich, verschiedene Energieformen ineinander umzuwandeln. Die Summe aus potentieller und kinetischer Energie ist in abgeschlossenen Systemen konstant.
- Energieerhaltung $\sum{W_{kin}}+\sum{W_{pot}}=kons.$

### Energieformen

- Lageenergie
- Bewegungsenergie
- Rotationsenergie
- Thermische Energie
- Chemische Energie
- Strahlungsenergie
- Elektrische Energie
- Magnetische Energerie
- Kernenergie
---
- **Potenzielle Energie**
	- Ist die Energie eines Körpers, die er durch die Fallbeschleunigung hat.
	- Potenzielle Energie $E_{pot}=m*g*h$
- **Kinetische Energie**
	- Ist die Energie, mit der ein Körper beschleunigt wird.
	- Kinetische Energie $E_{kin}=F*s=\frac{m}{2}v^2$
- **Spannenergie**
	- Ist die in den Feldern gespeicherte Energie.
	- Spannkraft $F=D*s$
	- Spannenergie $E_{spann}=\frac{1}{2}D*s^2$
- - -
- **Fadenpendel**
	- Die potenzielle Energie wird in kinetische Energie beim loslassen des Pendels umgewandelt.
	- Die potenzielle Energie entspricht der Höhe des Pendels beim loslassen.

### Energieübertragung

Die Übertragung von Energie von einem System auf ein anderes kann in verschiedener Weiser erfolgen. Energie kann in Form von Wärme übertragen werden, Dabei ist zwischen Wärmeleitung, Wärmeströmung und Wärmestrahlung zu unterscheiden.

### Energieumwandlung

Die Umwandlung von Energie von einer Form in andere Formen finden wir in Natur und Technik in vielfältiger Weise. Nutzt man den Begriff Energieträger, sol lässt sich das wie folgt formulieren: Energie wird von einem Energieträger übertragen.
- Wirkungsgrad $\eta=\frac{E_{nutz}}{E_{zu}}$

## Arbeit

$W=E_{End}-E_{Anfang}=\Delta E$
- $\Delta E=W>0$ am Körper wird Arbeit verrichtet
- $\Delta E=W<0$ Körper verrichtet Arbeit
- Formel $W=E_{End}-E_{Anfang}=\Delta E$

## Leistung

- **Definition:** Die Leistung ist die Änderungsrate der Energie, sie gibt also an, wie viel Energie $\Delta E$ in einer bestimmten Zeit $\Delta t$ umgewandelt bzw. übertragen wird.
- **Formelzeichen:** P
- **Einheit:** Watt, $PS = 735 W$
- **Formel:** $P=\frac{\Delta E}{\Delta t}$ oder $P=\frac{W}{\Delta t}$
Im Alltag wird die Energie of tin Leistungseinheitenausgedrückt: $1kWh$

## Wirkungsgrad

- **Definition:** Der Wirkungsgrad gibt den Anteil an zugeführter Energie $E_{zu}$
an, der in nutzbare Energie $E_{nutz}$umgewandelt bzw. übertragen wurde.
- **Formelzeichen:** $\eta$
- **Einheit:** \%
- **Formel:** $\eta=\frac{E_{nutz}}{E_{zu}}$ oder $\eta=\frac{E_{nutz}}{E_{zu}}$
Nicht nutzbare Energie wird als entwertete Energie bezeichnet.

# Modellierung

# Elektrostatik Und Elektrodynamik

## Die Größe Der Elektrischen Ladung

Die elektrische Ladung eines Körpers gibt an, wie groß seine negative (Elektronenüberschuss) oder positive (Elektronenmangel) Ladung ist.

- Formelzeichen $Q$
- Einheit $[Q] = 1 C$ (ein Coulomb)
- Formel $Q=N*e$

Jede elektrische Ladung ist ein vielfaches der Ladung eines Elektrons. Sie wird auch als Elementarladung $e=1.602*10^{-19}C$ bezeichnet.

### Kräfte Zwischen Elektrostatisch Geladenen Körpern

Ungleichnamig geladene Körper ziehen einander an und gleichnamig geladene Körper stoßen sich ab.

### Nachweis Elektrostatischer Ladungen

Elektrometer: Wenn die Elektrode mit einem geladenen Körper berührt wird, überträgt sich ein Teil der Ladung auf den Zeiger und den Metallträger. Da Zeiger und Metallträger gleich geladen sind, wirken abstoßende Kräfte (Zeiger schlägt aus).
![Elektrometer](Working%20Materials/Elektrisches%20Feld/Elektrometer.png)

### Ladungsausgleich

Beim Ladungsausgleich fließen zuvor getrennt Ladungen zurück.

#### Influenz

Ist ein geladener Körper in der Nähe eines leitenden, ladungsneutralen Körpers, so tritt bei dem leitenden Körper eine Ladungsverschiebung und somit eine Ladungstrennung auf. Diese wird als Influenz bezeichnet.

#### Polarisation

Ist ein geladener Körper in der Nähe eines Isolators erfolgt eine Verschiebung von elektrischen Ladungen über kurze Distanzen (Größenordnung eines Atomabstandes). Moleküle oder kleinste Teilchen werden zu elektrischen Dipolen.

### Kunststoffstab Am Elektroskop

 Kommt der geladene Körper in die Nähe des Elektroskops, dann werden Elektronen im Elektroskop abgestoßen. Diese wandern im „unteren“ Teil des Zeigers des Metallstabes. Es erfolgt eine Ladungstrennung durch Influenz. Da sich gleiche Ladungen abstoßen, schlägt der Zeiger aus.

### Möglichkeiten Der Ladungstrennung

- Reibung
- Dissoziation
- Influenz
- Polarisation
- magnetische Induktion
- thermoelektronische Vorgänge

### Strom Als Bewegte Ladung

Die elektrische Stromstärke I gibt an, wie viel Ladung $Q$ in einer bestimmten Zeit $t$ durch den Querschnitt eines Leiters fließt
$I=\frac{\Delta Q}{\Delta t}$

### Erhaltungssatz Der Ladung

In einem abgeschlossenen System bleibt die Gesamtladung Q erhalten
$Q=Q_1$

## Nah- Und Fernwirkungstheorie

- **Fernwirkungstheorie**: Die Wirkung zwischen Körpern erfolgt unmittelbar (instantan) und ohne „Vermittler“.
- **Nahwirkungstheorie**: Die Wirkung zwischen Körpern erfolgt nach einer gewissen Zeit (besitzt also eine Ausbreitungsgeschwindigkeit) und durch einen „Vermittler“.

## Elektrostatisches Feld

In dem Raum (Wirkungsbereich) um einen elektrostatisch geladenen Körper werden Kräfte auf andere geladene Körper ausgeübt. Das elektrostatische Feld beschreibt diesen Raum. 

### Das Feldlinienbild Des Elektrischen Feldes

### Homogenes Feld

Die Feldlinien verlaufen parallel und im gleichen Abstand zueinander.

### Faradayscher Käfig

## Die Elektrische Feldstärke

Die elektrische Feldstärke  gibt an, wie groß die Kraft  pro Ladung  an einem bestimmten Ort ist.
- Formelzeichen $E$
- Einheit $N$
- Formel $\vec{E}=\frac{\vec{F}}{q}$

![Polarisation](Working%20Materials/Elektrisches%20Feld/Polarisation.png)
![Potenzial](Working%20Materials/Elektrisches%20Feld/Potenzial.png)

## Coulombsches Gesetz

### Relative Permittivität

Die relative Permittivität ist ein Maß für die Feldabschwächung des elektrischen Feldes durch Polarisation eines Mediums.

![Relative Permittivität](Working%20Materials/Elektrisches%20Feld/Relative%20Permittivität.png)

Befindet sich innerhalb der Spule ein ferro-magnetischer Stoff, dann vergrößert sich die magnetische Flussdichte der Spule:

Die relative Permeabilitätszahl  ist eine Stoffkonstante. Sie gibt an, um wie viel sich die magnetisch Flussdichte im Vergleich zum Vakuum (näherungsweise auch Luft) vergrößert.

## Elektrisches Potential

Das elektrische Potential in einem Punkt  des elektrischen Feldes bezieht sich auf die Arbeit , die benötigt wird, um eine Probeladung  von einem festen Bezugspunkt  zu einem Punkt  zu verschieben.
- Formelzeichen $\varphi$
- Einheit $V$
- Formel

### Äuipotentialflächen

Die Flächen, die das gleiche Potential besitzen, heißen Äquipotentialflächen

## Elektrische Spannung

Wir eine Probeladung  von einem Anfangspunkt zu einem Endpunkt innerhalb eines elektrischen Feldes verschoben, ändert sich das Potential  für die Ladung . Diese Änderung des Potentials  wird als Spannung bezeichnet.
- Formelzeichen $U$
- Einheit $V$
- Formel $U=E*d$ 

## Kondensatoren

Ein Kondensator ist ein Bauelement zur Speicherung von elektrischer Ladung und somit elektrischer Energie. Er besteht aus sich gegenüberliegenden leitenden Schichten, die durch einen Isolator (Di-elektrikum) getrennt sind. 
![Plattenkondensator](Working%20Materials/Elektrisches%20Feld/Plattenkondensator.png)

### Kapazität

Die Kapazität eines Kondensators gibt an, wie viel elektrische Ladung der Kondensator bei einer Spannung von $1 V$ speichern kann.
- Formelzeichen $C$
- Einheit $F=\frac{C}{V}$
- Formel $C=\frac{Q}{U}$
- Idealer Plattenkondensator $C=\varepsilon_0*\varepsilon_r*\frac{A}{d}$

### Speicherung Elektrischer Energie

Die elektrische Energie lässt sich auch mithilfe der Feldstärke $E=\frac{U}{d}$ ausdrücken.

$W=\frac{1}{2}\varepsilon_0*\varepsilon_r*A*d*E^2$

Die Kapazität und damit das Speichervermögen eines Kondensators ist umso größer,
- je größer die Flächen der Platten ist,
- je kleiner der Abstand der Platten ist,
- je größer die Permittivität des Dialektrikums ist.

#### Parallelschaltung

$C_{ges}=C_1+C_2+C_3+\dots+C_n$

#### Reihenschaltung

$\frac{1}{C_{ges}}=\frac{1}{C_1}+\frac{1}{C_2}+\frac{1}{C_3}+\dots+\frac{1}{C_n}$

### Auf Und Entladen Eines Kondensators

#### Aufladungsvorgang

$U_0=U_R+U_C=R*I+\frac{Q}{C}$

#### Entladungsvorgang

$I(t)=\frac{\Delta Q}{\Delta t}$

## Magnete Und Magnetische Felder

### Magnetische Körper

Zwischen einem Magneten und Körpern aus Eisen, Nickel, Cobalt Neodym-Eisen-Bor und bestimmten keramischen Werkstoffen (so genannte Ferrite) oder stromdurchflossenen Leitern wirken magnetische Kräfte
![](Working%20Materials/Elektrisches%20Feld/Cobalt.png)
![](Working%20Materials/Elektrisches%20Feld/Eisen.png)
![](Working%20Materials/Elektrisches%20Feld/Ferrit.png)

### Permanentmagnet

Permanentmagneten besitzen einen dauerhaften Magnetismus. Sie werden auch als Dauermagneten bezeichnet.

### Kräfte Zwischen Magneten

Zwischen zwei Magnetpolen können anziehende und abstoßende Kräfte auftreten. Ungleichnahmige Pole ziehen sich an, gleichnamige Polen stoßen sich ab.

### Elektromagnete

- je größer die Stromstärke des durch die Spule fließenden Stromes ist, desto größer ist die magnetische Kraftwirkung

## $U(t)$ Und $I(t)$ Diagramme: Kondensator

![Kondensator](Working%20Materials/Elektrisches%20Feld/Kondensator.png)

### Aufladungsvorgang

Die obere Platte wurde positiv, und die untere negativ aufgeladen.
~~~functionplot
---
disableZoom: true
bounds: [0,10,0,10]
ylabel: U(t)
---
U(x)=(x/10)^2*10
~~~

~~~functionplot
---
disableZoom: true
bounds: [0,10,0,10]
---
I(x)=-(x/10)^2*10+10
~~~

### Endladungsvorgang

Der Kondensator wird entladen. Der Strom fließt nun entgegengesetzt.

~~~functionplot
---
disableZoom: true
bounds: [0,10,0,10]
---
U(x)=-(x/10)^2*10+10
~~~

~~~functionplot
---
disableZoom: true
bounds: [0,10,-10,0]
---
I(x)=(x/10)^2*10-10
~~~

## Hysterese Von Ferromagnetischen Stoffen

Fläche, die von der Hysteresekurve eingeschlossen wird, ist ein Maß für die Energie, die Für das Ummagnetisieren benötigt wird.

## Magnetfeld Von Elektromagneten

![](Working%20Materials/Elektrisches%20Feld/Magnetfeld%20von%20Elektromagneten.png)

Das Magnetfeld einer stromdurchflossenen Spule gleicht dem eines Stabmagneten. Im Inneren der Spule herrscht annähernd ein homogenes Magnetfeld.

## Magnetische Flussdichte

Die magnetische Flussdichte einer Spule ist direkt proportional zur fließenden Stromstärke und der Windungszahl.
- Formelzeichen $B$
- Einheit $T=\frac{N}{Am}$

Zusammenhang zwischen magnetischer Feldstärke $H$ und magnetischer Flussdichte $B=\mu_0\mu_rH$

Die magnetische Flussdichte einer Spule ist indirekt proportional zur Länge der Spule.

$B\sim\frac{1}{B}$

Für die magnetische Flussdichte im Inneren einer langen, dünnen Spule gilt:

$B=\mu_0\mu_r\frac{N*I}{l}$
- $N$ Windungszahl
- $I$ Stromstärke
- $l$ Spulenlänge
- $\mu_r$ relative Permeabilität
- $\mu_0$ magnetische Feldkonstante 

$\mu_0\approx1.257*10^{-6}\frac{Vs}{Am}=4\pi*10^{-7}\frac{Vs}{Am}$

## Helmholtz-Spulen-Paar

Helmholtz-Spulen-Paar: Zwei kurze Spulen mit dem Radius R werden parallel und im Abstand vom Radius R der Spulen aufgestellt. Die beiden Magnetfelder überlagern sich und ergeben im Bereich zwischen den Spulen ein annähernd homogenes Magnetfeld.

![](Working%20Materials/Elektrisches%20Feld/Helmholtz-Spulen-Paar.png)
