# Schwingungen

## Hooksches Gesetz

(Lb. S. 48)

Die wirkenden Kraft ist direkt proportional zur Auslenkung der Feder ist: $F=D\cdot s$
- $D$ Federkonstante
- $s$ Auslenkung

**Beispiel**
$D=10 \frac{N}{m}$
Man benötigt eine Kraft von $10 N$, um die um $1 m$ zu dehnen.

### Scherung

(Lb. S: 49)

![Scherung](Working%20Materials/Schwingungen/Scherung.png)

$F\sim \delta$

### Torsion

![Torsion](Working%20Materials/Schwingungen/Torsion.png)

$F\sim \varphi$

## Größe einer Schwingung

![](Working%20Materials/Schwingungen/Schwingungen.png)

$\hat{y}$ Amplitude (Maximale Auslenkung)
$y$ Elongation (Auslenkung)
$f$ Frequenz in $1Hz=1s^{-1}$
$T$ Periode $T=\frac{1}{f}$

## Harmonische Schwingung

Schwingungen, die durch eine Sinus- oder Kosinusfunktion beschrieben werden kann.

## Zeigerdiagramm

![](Working%20Materials/Schwingungen/Zeigerdiagramm.png)

Eine gleichförmige Kreisbewegung kann man gedanklich in zwei harmonische Schwingungen gleicher Frequenz und Amplitude zerlegen, die senkrecht zueinander verlaufen. Umgekehrt kann man sich auch jede harmonische Schwingung als Projektion einer Kreisbewegung denken. Deshalb wird zur Veranschaulichung von harmonischen Schwingungen oft eine Zeigerdiagramm verwendet, in dem ein Zeiger der Länge $A$ mit der Frequenz $f$ um einen festen Punkt rotiert.

## Geschwindigkeit & Beschleunigung bei Schwingungen

Auslenkung
$y(t)=\hat{y}\sin{(\omega t)}$

Geschwindigkeit
$v(t)=\frac{dy}{dt}=\hat{y}\omega\cos{(\omega t)}=\hat{v}\cos{(\omega t)}$ mit $\hat{v}=\hat{y}\omega$

Beschleunigung
$a(t)=\frac{dv}{dt}=-\hat{y}\omega^{2}\sin{(\omega t)}=-\hat{a}\sin{(\omega t)}$ mit $\hat{a}=\hat{y}\omega^{2}$

### Rückstellkraft

$y(t)=\hat{y}\sin{(\omega t)}$
$a(t)=-\hat{y}\omega^{2}\sin{(\omega t)}=-\omega\hat{y}\sin{(\omega t)}=-\omega^{2}y(t)$

$a(t)\sim y(t)\to F_{r}(t)\sim a(t)\sim y(t)$

**Beispiel Federschwinger**
$F_{r}(t)=-Dy(t)$

### Eigenfrequenz Federschwinger

$w_{0}=\sqrt{\frac{D}{m}}$
$f_{0}=\frac{1}{2\pi} \sqrt{\frac{D}{m}}$
$T_{0}=2\pi \sqrt{\frac{m}{D}}$

### Periodendauer Fadenpendel

$w_{0}=\sqrt{\frac{g}{l}}$
$f_{0}=\frac{1}{2\pi} \sqrt{\frac{g}{l}}$
$T_{0}=2\pi \sqrt{\frac{l}{g}}$

## Energieerhaltung einer harmonischen Schwingung

|                | $E_{\text{kin}}$   | $E_{{pot}}$         |
| -------------- | ------------------ | ------------------- |
| Federschwinger | $\frac{m}{2}v^{2}$ | $\frac{1}{2}Dx^{2}$ |
| Fadenpendel    | $\frac{m}{2}v^{2}$ | $mgh$               |

$E_{ges}=E_{pot}+E_{kin}=\frac{1}{2}Dx(t)^{2}+ \frac{1}{2}mv(t)^{2}=\frac{1}{2}D(\hat{x}\cos{\omega t})^{2}+ \frac{1}{2}m (-\hat{x}\omega \sin{\omega t})^{2}$
$\frac{1}{2}D\hat{x}\cos^{2}{\omega t}+ \frac{1}{2}m \hat{v}^{2}\sin{\omega t}=E_{ges}\cos^{2}{\omega t}+E_{ges}\sin^{2}{\omega t}=E_{ges}(\cos^{2}{\omega t}+\sin^{2}{\omega t})=E_{ges}$

## Gedämpfte Schwingung

$\delta=\frac{b}{2m}$
$\omega=\sqrt{\omega_{0}^{2}-\delta^{2}}$

### Reibungskraft = konst.

$W_{R}=\Delta E=F_{R}(\hat{y}_{1}+\hat{y}_{2})$
$\Delta E=\frac{1}{2} D \hat{y}^{2}_{1}- \frac{1}{2}D\hat{y}^{2}_{2}$

$F_{R}(\hat{y}_{1}+\hat{y}_{2})=\frac{1}{2}D(\hat{y}^{2}_{1}-\hat{y}^{2}_{2})$
$F_{R}(\hat{y}_{1}+ \hat{y}_{2})=\frac{1}{2}D(\hat{y}_{1}+\hat{y}_{2})(\hat{y}_{1}-\hat{y}_{2})$
$F_{R}=\frac{1}{2}D(\hat{y}_{1}-\hat{y}_{2})$
$\frac{2F_{R}}{D}=(\hat{y}_{1}-\hat{y}_{2})$
$\hat{y}_{2}=\hat{y}_{1}-\frac{2F_{R}}{D}$

Amplitude nimmt linear  über die Zeit ab.
$\hat{y}_{n+1}=\hat{y}_{n}- \frac{2F_{R}}{D}$

### Reibungskraft ~ Geschwindigkeit

Ansatz
$\vec{F_{s}}=-D\hat{y}$
$\vec{F_{R}}=-b\vec{v}$
$\vec{F_{ges}}=\vec{F_{s}}+\vec{F_{R}}$

$m\vec{a}=-D\vec{y}-b\vec{v}$
$m \frac{d^{2}\vec{y}}{dt}=-D\vec{y}-b \frac{d\vec{y}}{dt}$

Lösung
$y(t)=\hat{y}e^{-st}\cos{\omega t}\quad \text{ mit } \delta=\frac{b}{2m}$
$\omega=\sqrt{\frac{D}{m}-\delta^{2}}$
$f=\frac{1}{2\pi}\sqrt{\frac{D}{m}-\delta^{2}}$

$\hat{y}(t)=\hat{y}e^{-st}$
$y(t)=\hat{y}(t)\cos{(\omega t)}$

### Starke Dämpfung

(Aperiodischer Grenzfall: $\omega_{0}=\delta$)

(Kriechfall: $\omega_{0}<\delta$)

## Resonanz

> Anregung und schwingendes System befinden sich in Resonanz, wenn die Erregerfrequenz und die Eigenfrequenz des Systems gleich sind.

![](Working%20Materials/Schwingungen/Resonanz.gif)

### Erzwungene Schwingung


> Je mehr  sich die Eregerfreqenz einer Eigenfrequenz des Systems nähert, desto mehr Energie pro Periode wird vom Erreger auf dem Oszillator übertragen Im Resonanzfall ist die Energieübertragung maximal.

Erregerfrequenz $f$
Eigenfrequenz $f_{0}$

$f<f_{0}\quad\Delta\varphi\approx0$

![](Working%20Materials/Schwingungen/Erzwungen%200.png)

$f=f_{0}\quad\Delta\varphi=\frac{\pi}{2}$

![](Working%20Materials/Schwingungen/Erzwungen%20pi2.png)

$f>f_{0}\quad\Delta\varphi=\pi$

![](Working%20Materials/Schwingungen/Erzwungen%20pi.png)

### Elektrischer Schwingkreis

**Skizze** ohne Dämpfung

![](Working%20Materials/Schwingungen/Elektrischer%20Schwingkreis%20ohne%20Dämpfung.png)

**Skizze** mit Dämpfung

![](Working%20Materials/Schwingungen/Elektrischer%20Schingkreis%20mit%20Dämpfung.png)

### Vergleich elektrischer Schwingkreis mit Federschwinger

| Schwingkreis                                 | Federschwinger                                    |
| -------------------------------------------- | ------------------------------------------------- |
| Kondensator wird geladen (maximale Spannung) | Wird gespannt (maximale Auslenkung)               |
| Wird mit Spule verbunden (Schalter umlegen)  | Massestück wird losgelassen                       |
| Spannung nimmt ab; Stromstärke wird größer   | Auslenkung nimmt ab, Geschwindigkeit wird größer  |
| Spannung ist null; Stromstärke maximal       | Auslenkung ist null; Geschwindigkeit maximal      |
| Spannung nimmt zu; Stromstärke wird kleiner  | Auslenkung nimmt zu; Geschwindigkeit wird kleiner |
| Spannung maximal; Stromstärke ist null       | Auslenkung maximal; Geschwindigkeit ist null      |

- Energie Schwingkreis
	- $E_{el}=\frac{1}{2}CU^{2}$
	- $E_{mag}=\frac{1}{2}LI^{2}$

- Energie Federschwinger
	- $E_{pot}=\frac{2}{2}Dy^{2}$
	- $E_{kin}=\frac{1}{2}mv^{2}$

### Ohne Dämpfung


$U_{L}=-L \frac{dI}{dt}=-L \frac{d}{dt}(\frac{dQ}{dt})=-L \frac{d^{2}Q}{dt^{2}}$

$U_{L}=U_{C}$
$-L \frac{d^{2}Q}{dt^{2}}=\frac{Q}{C}$

$-\frac{d^{2}Q}{dt^{2}}=\frac{1}{LC}Q$

$w_{0}=\sqrt{\frac{1}{LC}}$
$f_{0}=\frac{1}{2\pi}\sqrt{\frac{1}{LC}}$

### Mit Dämpfung

$U_{l}=U_{R}+U_{C}$
$U=R \cdot I=R \frac{dQ}{dt}$
$-L \frac{d^{2}Q}{dt}=R \frac{dQ}{dt}+ \frac{Q}{C}$
$\omega=\sqrt{\omega_{0}^{2}-\delta^{2}}\quad\text{ mit }\delta= \frac{R}{2L}$

### Rückkopplungsschaltung nach Meißner

**Rückkopplung**: Periodische Zufuhr von Energie in einem schwingenden System.+

**Schaltplan**
![](Working%20Materials/Schwingungen/Rückkopplungsschaltung.png)

Mit dem Regelbaren Widerstand wird der Arbeitspunkt des Transistors eingestellt. Durch den Schwingkreis wird über die Spule $L_{S}$ eine Wechselspannung in $L_{R}$ induziert. Dadurch liegt auch ein Wechselstrom $I_B$ an der Basis an. Wenn $I_{B}$ maximal ist, schaltet der Transistor in Durchlassrichtung und der Kondensator im Schwingkreis wird wieder auf die maximale Spannung geladen.

**Anwendungen Schwingkreise**: Radio, Fernsehtechnik, Funktechnik

### Wechselstromkreis

**Effektivwert**

$U(t)=R \cdot i(t)$

Wechselstrom: $P=u(t)\cdot i(t)=R \cdot i(t)^{2}$

Gleichstrom: $P=UI=RI^{2}$

Welcher Gleichstrom wäre nötig, um die gleiche Leistung zu bekommen, wie im Mittel bei dem Wechselstrom?

Herleitung

$RI_{eff}^{2}=R \frac{1}{T}\displaystyle\int_{0}^{T}{\hat{I}\sin^{2}{(\omega t)}}dt=R \frac{1}{T} \frac{\hat{I}}{2}T$
$I_{eff}^{2}=\frac{\hat{I}^{2}}{2}$

$I_{eff}=\frac{\hat{I}}{\sqrt{2}}$
$U_{eff}=\frac{\hat{U}}{\sqrt{2}}$

### Zeigerdiagramme

**Widerstand**

#### Kondensator im Wechselstromkreis

**Kondensator**

Der Strom eilt der Spannung um $\frac{\pi}{2}$ voraus.
Kapazitiver Widerstand: 
$U=\hat{U}\sin{\omega t}$
$I=\frac{dQ}{dt}=C \frac{dU}{dt}$
$I=C \frac{dU}{dt}=C\hat{U}\omega\cos{(\omega t)}=\hat{I}\cos{(\omega t)}$
$U=X_{C}\cdot I\to X_{C}=\frac{U}{I}=\frac{\hat{U}}{C\hat{U}\omega}=\frac{1}{C\omega}$

#### Spule im Wechselstromkreis

![](Working%20Materials/Schwingungen/Spule%20Im%20Wechselstromkreis.png)

$U=-L \frac{dI}{dt}$
$I=\hat{I}\sin{(\omega t)}$

$U=-L \frac{d}{dt}\big(\hat{I}\sin{(\omega t)}\big)=-L \omega \hat{I}\cos{(\omega t)}$

**induktiver Widerstand**

$X_{L}=\frac{\hat{U}}{\hat{I}}=\frac{L\omega\hat{I}}{\hat{I}}=L \omega$

### Reihenschaltung von Spule, Kondensator & Widerstand

(Siebkette, Siebkreis, Bandpass)

**Zeigerdiagramm**

![](Working%20Materials/Schwingungen/Reihenkondensator.png)

$U_{R}$ ist Phasenverschoben zur Stromstärke
$U_C$ ist der Stromstärke hinterher
$U_L$ ist der Stromstärke voraus

$\hat{U}_{ges}=Z \cdot\hat{I}$
$Z=\frac{\hat{U}_{ges}}{\hat{I}}=\frac{\sqrt{\hat{U}_{R}^{2}+(\hat{U}_{L}+\hat{U}_{C})^{2}}}{\hat{I}}=\frac{\sqrt{R^{2}\hat{I}^{2}+((\omega L)+ \frac{1}{\omega C} \hat{I})^{2}}}{\hat{I}}=\frac{\sqrt{\hat{I}^{2}+(R^{2}+ (\omega L-\frac{1}{\omega C} \hat{I}))^{2}}}{\hat{I}}=\sqrt{R^{2}+(\omega L- \frac{1}{\omega C})^{2}}$

Allgemein:
$Z=\sqrt{R^2+X^{2}}$
$\text{Imdepedanz}=\sqrt{\text{ohmscher Widerstand}^{2}+\text{Reaktanz}^{2}}$

### Frequenzabhängigkeit der Impedanz

$\lim\limits_{\omega\to0}Z=\lim\limits_{\omega\to0}\sqrt{R^{2+(\omega L- \frac{1}{\omega C})^{2}}}=\infty\to I=0$
$\lim\limits_{\omega\to\infty}Z=\lim\limits_{\omega\to\infty}\sqrt{R^{2}+(\omega L- \frac{1}{\omega C})^{2}}=\infty\to I=0$

$Z$ ist minimal für: $\omega L- \frac{1}{\omega C}=0\to I=I_{\text{max}}$

### Hochpass und Tiefpass

### Leistung im Wechselstromkreis

$P_{S}=U \cdot I=\sqrt{P_{W}^{2}+P_{B}^{2}}$
$P_{W}=U \cdot I \cdot\cos{\varphi}$
$P_{B}=U \cdot I \cdot\sin{\varphi}$
