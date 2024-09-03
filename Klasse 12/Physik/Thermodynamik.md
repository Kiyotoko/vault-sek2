# Thermodynamik

## Innere Energie

Innere Energie $U$: Sämtliche Energieformen, die innerhalb eines Systems $s$ vorliegen, werden in der Summe als innere Energie $U$ bezeichnet.

**Beispiele**
- potenzielle Energie der Teilchenschwingung
- kinetische Energie von Teilchen
- (chemische) Bindungsenergie

Bei Festkörpern gilt:
- $U=E_{\text{kin}}+E_{\text{pot}}$ (Teilchenschwingung)
- Innere Energie, die man benötigt um einen Körper zu Schmelzen wird als Schmelzwärme $Q_{s}$ bezeichnet: $Q_{s}=q_{s}\cdot m$, wobei $q_{s}$ die spezifische Schmelzwärme ist
- $[q_{s}]= \frac{kJ}{kg}$

Bei Flüssigkeiten gilt:
- $U=E_{\text{kin}}+E_{\text{pot}}$ ($E_{\text{pot}}$ geringer als bei Festkörpern)
- Verdampfungsprozess $U=Q_{v}=q_{v}\cdot m$ (Verdampfungswärme)

Bei Gasen gilt:
- $U=E_{\text{kin}}$ (Translation & Rotation, $E_{\text{pot}}\approx0$)

### Boltzmann Verteilung

![](Working%20Materials/Thermodynamik/Boltzmann%20Verteilung.png)

## Ideales Gas

### Druck und Temperatur

$p= \frac{F}{A}$

|         | Formelzeichen | Einheit       | Fixpunkt                              |
| ------- | ------------- | ------------- | ------------------------------------- |
| Celsius | $\vartheta$   | ${}^{\circ}C$ | 100 °C Siedepunkt und 0° Schmelzpunkt |
| Kelvin  | $T$           | $K$           | absoluter Nullpunkt                   |

$0K = -273^{\circ}C$

$T\;\text{in}\;K=\vartheta\;\text{in}^{\circ}C+273$

### Eigenschaften

- Lösen nur vollkommen elastische Stöße untereinander aus.
- Es gibt keine weiteren Anziehungs- oder Abstoßungskräfte untereinander
- Gesamtenergie der Teilchen ist ausschließlich ihre kinetische Energie ihrer Translationsbewegung
- Keine Aggregatzustandsänderung

$$p \cdot V=n \cdot R \cdot T$$

> $p$, $T$ und $V$ sind Zustandsgrößen!

## Thermodynamisches Gleichgewicht und Wärme

### Mechanisches & chemisches Gleichgewicht

Besteht bei zwei miteinander verbundenen Systemen ein Druck- oder Konzentrationsunterschied, so gleichen sich Druck und Konzentration über die Zeit aus.

### Thermisches Gleichgewicht

Besitzen zwei miteinander verbundene Systeme einen Temperaturunterschied, so gleicht sich die Temperatur der Systeme über die Zeit an.

### Wärme $Q$

Thermische Energie, die von einem System aufgenommen oder abgegeben wird, aufgrund eines Temperaturunterschiedes.

$$Q=mc\cdot \Delta T=mc\cdot (T_{\text{end}}-T_{\text{an}})$$
$\Delta T$ Temperaturunterschied
$m$ Masse
$c$ Spezifische Wärmekapazität ($c_{p}$ wenn Druck konstant, $c_{v}$, wenn Volumen konstant)

> $Q>0$ Wärmeaufnahme
> $Q<0$ Wärmeabgabe

**Beispiel**
$c_{\ce{H2O}}=4.19\frac{kJ}{kg\cdot K}$
Man benötig 4.19 kJ, um 1 kg Wasser um 1 K zu erwärmen.

> Temperaturdifferenzen sind unabhängig ob gegeben in Kelvin oder Grad Celisus.

### Mischtemperatur

$m_{1}c_{\ce{H2O}}(T_{1}-T_{m})+m_{1}c_{\ce{H2O}}(T_{2}-T_{M})=0$
$T_{M}(m_{1}c_{\ce{H2O}})+m_{2}c_{\ce{H2O}}=m_{1}c_{\ce{H2O}}T_{1}+m_{2}c_{\ce{H2O}}+T_{2}$
$T_{M}=\frac{m_{1}c_{\ce{H2O}}T_{1}+m_{2}c_{\ce{H2O}}T_{2}}{m_{1}c_{\ce{H2O}}+m_{2}c_{\ce{H2O}}}$

### Wärmestrahlung

Körper, welche wärmer sind als die Umgebung, emittieren Wärme, wobei sie Energie über Zeit an die Umgebung abgeben (Strahlung). Dies passiert solange, bis sich Körper und Umgebungstemperatur ausgeglichen haben.

### Wärmeleitung

Ist an Materie gebunden, wobei Teilchen durch Bewegung bzw. Schwingung Energie austauschen. Wärmeleitfähigkeit hängt von der Kopplung der Teilchen untereinander ab sowie der elektrischen Leitfähigkeit.

### Wärmeströmung

Wärmetransport durch Stofftransport.

## Erster Hauptsatz der Thermodynamik

Die innere Energie $U$ eines Systems kann durch Zufuhr oder Entzug von mechanischer Arbeit $W$ oder Wärmemenge $Q$ erhöht oder verringert werden:
$$\Delta U=Q+W$$
$\Delta U$ Änderung der inneren Energie
$Q$ Wärme
$W$ Arbeit

$\Delta U>0$ Energieaufnahme
$\Delta U<0$ Energieabgabe

$$Q_{p}=mc_{p}\Delta T=\Delta U$$

### Isochore Zustandsänderung

$V=\text{konst.}\to \mathrm{d}V=0\to W=0$
$\Delta U=Q+W=Q+0=Q=m\cdot c_{V}\cdot\Delta T$

### Isobare Zustandsänderung

$p=\text{konst.}\to W=\int p\mathrm{d}V=p\int\mathrm{d}V$
$\Delta U=Q+W=mc_{p}\Delta T+p\int_{V_{0}}^{V_{1}}\mathrm{d}V=mc_{p}\Delta T+p(V_{0}-V_{1})$

### Isotherme Zustandsänderung

$T=\text{konst.}\to \Delta U=0$
$0=Q+W\to Q=-W$

Erfolgt so langsam, dass sich die Temperatur des Systems mit der Umgebungstemperatur immer ausgleicht.

### Adiabatische Zustandsänderung

Erfolgt so schnell oder gut isoliert, dass kein Wärmeaustausch mit der Umgebung stattfindet

$Q=0\to \Delta U=W=mc_{V}(T_{2}-T_{1})$

## Carnot-Prozess

### Zustandsänderung von 1 zu 2

isotherm -> $\Delta U=0$

$\displaystyle\begin{split} W_{1,2}&=\int_{V_{1}}^{V_{2}}p\;\mathrm{d}V=\int_{V_{1}}^{V_{2}} \frac{nRT}{V}\mathrm{d}V \\ &=\frac{nRT}{V}\int_{V_{1}}^{V_{2}}\mathrm{d}V=nRT[\ln{|V|}]_{V_{1}}^{V_{2}}\\ &=nRT\ln{\frac{V_{2}}{V_{1}}}\end{split}$

$W_{1,2}>0$ Arbeit wird am System verrichtet
isotherm: System gibt Wärme ab, da $T=\text{konst.}$ und $Q_{1,2}<0$

### Zustandsänderung von 2 zu 3

adiabatisch $Q_{2,3}=0$

$k=pV^{\gamma}=\text{konst.}$
$\gamma>1$ adiabatischer Koeffizient

$\frac{nRT}{V} V^{\gamma}=\text{konst.}$
$TV^{\gamma-1}= \text{konst.}$
$T_{2}V_{2}^{\gamma-1}=T_{3}V_{3}^{\gamma-1}$
$\frac{V_{2}^{\gamma-1}}{V_{3}^{\gamma-1}}=\frac{T_{3}}{T_{2}}$

$\displaystyle\begin{split}W_{2,3}&=\int_{V_{2}}^{V_{3}}p\;\mathrm{d}V=\int_{V_{2}}^{V_{3}}\frac{k}{V^{\gamma}} \;\mathrm{d}V\\ &=k\int_{V_{2}}^{V_{3}}V^{-\gamma}\;\mathrm{d}V=k\Big[\frac{V^{-\gamma+1}}{-\gamma+1}\Big]_{V_{2}}^{V_{3}}\\ &=\frac{k}{-\gamma+1}(V_{3}^{-\gamma+1}- V_{2}^{-\gamma+1})=\frac{p_{2}V_{2}^{\gamma}}{-\gamma+1}(V_{3}^{-\gamma+1}- V_{2}^{-\gamma+1})\\ &=\frac{p_{2}}{-\gamma+1}(V_{2}^{\gamma}V_{3}^{-\gamma+1}- V_{2}^{\gamma}V_{2}^{-\gamma+1})=\frac{p_{2}}{-\gamma+1}(V_{2}^{\gamma}V_{3}^{-\gamma+1}- V_{2})\\ &=\frac{p_{2}V_{2}}{-\gamma+1}(V_{2}^{\gamma-1}V_{3}^{-(\gamma-1)}-1)=\frac{p_{2}V_{2}}{-\gamma+1}\Big(\frac{V_{2}^{\gamma-1}}{V_{3}^{\gamma-1}}-1\Big)\\ &=\frac{nRT_{2}}{-\gamma+1}\Big(\frac{T_{3}}{T_{2}}-1\Big)= n \frac{R}{-\gamma+1}(T_{3}-T_{2})=n\cdot c_{V} \Delta T=Q_{V}\end{split}$

### Zustandsänderung von 3 zu 4

isotherm $\Delta U=0$
$W_{3,4}=-Q_{3,4}$
$W_{3,4}=nRT_{3} \ln{\frac{V_{4}}{V_{3}}}$

### Zustandsänderung von 4 zu 1

adiabatisch $Q=0$

$\Delta U=W=Q_{V}$
$W_{2,3}=n \frac{R}{-\gamma+1} (T_{3}-T_{2})=n \frac{T}{-\gamma+1} (T_{3}-T_{1})$

$W_{4,1}=n \frac{R}{-\gamma+1}(T_{1}-T_{3})=-n \frac{R}{\gamma+1}(T_{3}-T_{1})=-W_{2,3}$

### Übersicht

$T_{1}=T_{2}=\text{konst.}$
$T_{3}=T_{4}=\text{konst.}$

$W_{1,2}>0$
$Q_{1,2}<0$

$W_{2,3}>0$
$Q_{2,3}=0$

$W_{1,2}<0$
$Q_{1,2}>0$

$W_{4,1}<0$
$Q_{4,1}=0$

### Wirkungsgrad

$TV^{\gamma-1}=\text{konst.}$
$T_{2}V_{2}^{\gamma-1}=T_{1}V_{2}^{\gamma-1}=T_{3}V_{3}^{\gamma-1}$
$\ce{T2->[isotherm]T1}$
$T_{4}V_{4}^{\gamma-1}=T_{3}V_{4}^{\gamma-1}=T_{1}V_{1}^{\gamma-1}$
$\frac{T_{1}}{T_{3}}=(\frac{V_{3}}{V_{2}})^{\gamma-1}=(\frac{V_{4}}{V_{1}})^{\gamma-1}$
$(\frac{V_{1}}{V_{2}})^{\gamma-1}=(\frac{V_{4}}{V_{3}})^{\gamma-1}\to \frac{V_1}{V_2}=\frac{V_{4}}{V_{3}}\to \frac{V_{2}}{V_{1}}= \frac{V_{4}}{V_{3}}^{-1}$

$\displaystyle\begin{split}\eta&= \frac{E_{\text{nutz}}}{E_{\text{zu}}}=\frac{W_{\text{nutz}}}{Q_{\text{zu}}}=\frac{W_{1,2}+W_{2,3}+W_{3,4}+W_{4,1}}{Q_{3,4}}\\&=\frac{W_{1,2}+W_{2,3}+W_{3,4}-W_{2,3}}{Q_{3,4}}=\frac{W_{1,2}+W_{3,4}}{Q_{3,4}}\\ &=\frac{nR(T_{1}\ln{\frac{V_{2}}{V_{1}}}+T_{3}\ln{\frac{V_{4}}{V_{3}}})}{nRT_{3}\ln{\frac{V_{4}}{V_{3}}}}=\frac{(T_{1}\ln{(\frac{V_{4}}{V_{3}})^{-1}}+T_{3}\ln{\frac{V_{4}}{V_{3}}})}{T_{3}\ln{\frac{V_{4}}{V_{3}}}}\\ &=\frac{-T_{1}\ln{\frac{V_{4}}{V_{3}}}}{T_{3}\ln{\frac{V_{4}}{V_{3}}}}+1=1 - \frac{T_{1}}{T_{3}}\end{split}$

## Stirling-Motor (Heisluftmotor)

Kreisprozess im p(V)-Diagramm

### Zustandsänderung von 1 bis 2

Isotherm $T_{1}=T_{1}$
$\Delta U=0\to Q_{1,2}=-W_{1,2}$

$W_{1,2}=\int_{V_{1}}^{V_{2}}p\;\mathrm{d}V=-nRT_{1}\int_{V_{1}}^{V_{2}} \frac{1}{V}\;\mathrm{d}V=-nRT_{1}[\ln{V}]_{V_{1}}^{V_{2}}=-nRT_{1}\ln{\frac{V_{2}}{V_{1}}}$

$Q_{1,2}=-W_{1,2}=nRT_{1}\ln{\frac{V_{2}}{V_{1}}}$

### Zustandsänderung von 2 bis 3

Isochor $V=\text{konst.}$
$\mathrm{d}V=0$

$W_{2,3}=0$
$Q_{2,3}=mv_{V}(T_{3}-T_{1})$

### Zustandsänderung von 3 bis 4

Isotherm $T_{3}=T_{4}$

$W_{3,4}=-\int_{V_{3}}^{V_{4}}p\;\mathrm{d}V=\dots=-nRT_{3}\ln{\frac{V_{4}}{V_{3}}}$

$Q_{3,4}=-W_{3,4}=nRT_{3}\ln{\frac{V_{4}}{V_{3}}}$

Da $V_{2}=V_{3}$ und $V_{4}=V_{1}$:
$Q_{3,4}=nRT_{3}\ln{\frac{V_{1}}{V_{2}}}$

### Zustandsänderung von 4 bis 1

Isochor $V_{4}=V_{1}$

$W_{4,1}=0$

$Q_{4,1}=mc_{V}(T_{1}-T_{3})=-mc_{V}(T_{3}-T_{1})=-Q_{2,3}$

### Wirkungsgrad

$\eta=\frac{W_\text{ges}}{Q_{zu}}=\frac{W_{1,2}+W_{3,4}}{Q_{2,3}+Q_{3,4}}$

Regenerator speichert $Q_{4,1}$ und gibt diese Wärme als $Q_{2,3}$ wieder ab.
$\eta=\frac{W_{1,2}+W_{3,4}}{Q_{3,4}}=\frac{-nRT_{1}\ln{\frac{V_{2}}{V_{1}}}-nRT_{3}\ln{\frac{V_{1}}{V_{2}}}}{nRT_{3}\ln{\frac{V_{1}}{V_{2}}}}=\frac{nRT_{1}\ln{\Big(\big(\frac{V_{2}}{V_{1}}\big)^{-1}\Big)}-nRT_{3}\ln{\frac{V_{1}}{V_{2}}}}{nRT_{3}\ln{\frac{V_{1}}{V_{2}}}}=\frac{nRT_{1}\ln{\frac{V_{1}}{V_{2}}}-nRT_{3}\ln{\frac{V_{1}}{V_{2}}}}{nRT_{3}\ln{\frac{V_{1}}{V_{2}}}}=\frac{T_{1}-T_{3}}{T_{3}}=\frac{T_{1}}{T_{3}}-1$

$\eta=\frac{|T_{1}}{T_{3}}-1|=1-\frac{T_{1}}{T_{3}}=1- \frac{T_{N}}{T_{H}}$

### Regenerator

Dieser Speichert die bei der isochoren Abkühlung die abgegebene Wärmemenge $Q_{4,1}$. Bei der isochoren Erwärmung gibt der Generator die zuvor aufgenommene Wärmemenge als $Q_{2,3}$ in das System ab. 

Regeneratoren können nicht 100% der Wärme speichern, abgeben oder aufnehmen. Somit ist der Wirkungsgrad in der Realität des Sirling-Prozesses kleiner als der des Carnot-Prozesses.

### Einsatzgebiete

(Lb. S. 299)

Gebieten Afrikas zum Pumpen von Wasser. Geringe Temperaturunterschied von 20K sind ausreichend für de Betrieb des Motors, weshalb er bereits mit Sonnenenergie betrieben werden kann (Solar-Stirling).

Blockheizkraftwerken, Motor versorgt Gebäude mit Strom und Wärme, wobei die Abwärme des Motors zu Beheizung des Gebäudes genutzt wird.

Verwendung bei Nasa für Radioisotopengeneratoren, da diese einen höheren Wirkungsgrad haben und weniger Plutonium benötigt.

## Wärmepumpe und Kältemaschine

Es handelt sich hierbei um einen "rückwärtsablaufenden" Carnot-Prozess. Dem System wird Arbeit zugeführt, damit Wärme transportiert werden kann.

1. Arbeitsmedium wird verdichtet (komprimiert) und erwärmt sicht (adiabatische Kompression).
2. Über Kondensator gibt Arbeitsmedium Wärme an Umgebung ab (isotherme Kompression).
3. Über die Drossel gelangt nur wenig vom Arbeitsmedium in den Verdampfer (adiabatische Expansion). Das Arbeitsmedium kühlt sich ab.
4. Über den Verdampfer nimmt das Arbeitsmedium Wärme von der Umgebung auf (isotherme Expansion).

### Leistungszahl

Das Verhältnis von transportierter Wärme zu zugeführter Arbeit ist die Leistungszahl:

Kältemaschine
$\epsilon=\frac{|Q_{N}|}{W}=\frac{T_{N}}{T_{H}-T_{N}}\ge1$

Wärmepumpe
$\epsilon=\frac{|Q_{H}|}{W}=\frac{T_{H}}{T_{H}-T_{N}}\ge1$

## Entropie

Die Entropie $S$ ist ein Maß für die Unordnung eines Systems. Je größer die Entropie $S$ ist, desto größer ist die Unordnung

### Irreversible Prozesse

Prozesse für deren Umkehrung Energie von außen dem System  zugeführt werden muss (Umkehrung erfolgt nicht von alleine).

**Beispiele**
- Ein Glas, welches zerspringt
- Alle Prozesse bei denen Reibung stattfindet
- Durchmischung von Gasen bzw. Flüssigkeiten

### Reversible Prozesse

Prozesse, für deren Umkehrung keine Energie zugeführt werden muss (Umkehrung erfolgt von alleine).

**Beispiele**
- Elastische Verformung
- Kompression eines Gases in einem abgeschlossenen Zylinder mit Kolben

## Zweiter Hauptsatz der Thermodynamik

In einem abgeschlossenen System ist die Entropieänderung $\Delta S\ge0$.

**Formel**
$\Delta S\approx \frac{Q_{rev}}{T}$
- Gilt für annähernd konstanter Temperatur $T$
- $Q_{rev}$ Wärmeänderung für reversible Prozesse

$\Delta S=\int_{1}^{2} \frac{1}{T}\;\mathrm{d}Q$ (allgemein)

## Dritter Hauptsatz der Thermodynamik

Der absolute Nullpunkt ($T=0\pu{K}$) der Temperatur ist nicht zu erreichen.
