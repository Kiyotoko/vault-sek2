## Das Josephus-Problem

- $n$ nummerierte Objekte werden im Kreis angeordnet.
- Jedes $k$-te Objekt wird entfernt (beginnend mit Objekt $k$)
- Nach jeder Runde wird der Kreis neu geschlossen
- Bei gegebenen $n,k\in\mathbb{N} (n\ge k)$ soll das letzte Objekt der Josephus-Permutation bestimmt werden

### Josephus-Permutation

Die Reihenfolg der entfernten Objekte wird als Josephus-Permutationbezeichnet.

**Beispiel**
$n=13,k=3$
$JP=[3,6,9,12,2,7,11,4,10,5,1,8,13]$

**Aufgabe**
Bestimme die Josephus-Permutation für $n=10,k=4$
$JP=[4,8,2,7,3,10,9,1,6,5]$

### Permutation für $k=2$

$f:\mathbb{N}\to\mathbb{N}$, wobei $f(n)$ das letzte Objekt der Josephus-Permutation für n

**Aufgabe**
Bestimme für $f(n)\forall n\in[1,\dots8]$

| n    | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| f(n) | 1   | 1   | 3   | 1   | 3   | 5   | 7   | 1   |

#### Rekursion

**Satz**
Im ersten Durchlauf werden alle Objekte mit gerader Zahl eliminiert.

**Beweis**
Nach der ersten Runde sind nach die Objektnummern $1,3,\dots2n-3,2n-1$ im Kreis. Die 3 eröffnet nun die nächste Runde, $\forall j\in[1,3,\dots,2n-3,2n-1]$ sei $i=\frac{j+1}{2}\in\mathbb{N}$, d. h. $1\to1,3\to2,5\to3,\dots,2n-1\to n$. Nun startet man das Problem für n. Das letzte Objekt der Josephus-Permutation bleibt dabei offensichtlich gleich. Es gilt also umgekehrt $jP2i-1$.
$f(2n)=2f(n)-1$

**Hinweis**
Die Rekursionen
1. $f(1)=1$
2. $f(2n)=2f(n)-1$
3. $f(2n+1)=2f(n)+1$

beschreiben $f(n)$ vollständig.

**Aufgabe**
$f(11)=2f(5)+1=2(2f(2)+1)+1=2(2(2f(1)-1)+1)+1=2*3+1$

**Beweis**
$f(2^n)=1\forall n\in\mathbb{N}$
$IA: n_0\to f(2^{n_0})$
$IV: f(2^n)=1\forall n\in\mathbb{N}$
$IB: f(2^{n+1})=1$
$IS: f(2^{n+1})=f(2*2^n)=2f(2^n)-1$

Induktionsvorraussetzung: $2-1=1$

**Satz**
$f(2^n+k)=2k+1\forall k\in\mathbb{N_0}:0\le k<2^n$

**Beweis**
Vollständige Induktion nach $n\in\mathbb{N_0}$

$IA: n_0$ wegen $k_0<2^{n_0}=1$ folgt $k_0=0$ und es gilt: $f(2^{n_0})=f(1)=1=2k_0+1$
$IN: f(2^n+k)=2k+1\forall k\in\mathbb{N_0}: 0\le k<2^n$ für ein $n\in\mathbb{N}_0$
$IB: f(2^{n+1}+k)=2k+1\forall k\in\mathbb{N}_0: 0\le k\le2^{n+1}$
$IS:$
1. $k=0\mod2\to\frac{k}{2}\in\mathbb{k}{2}\in\mathbb{N}_0$. Es folgt: $f(2^{n+1}+k)=f(2(2^n+\frac{k}{2}))=2f(2^{n}+\frac{k}{2})-1$
2. $k=1\mod2$ Die Rekursionsforschrift ergibt $\forall m\in\mathbb{N}: f(2m+1)=2f(m)+1=2f(m)-1+2=f(2m)+2$. Angewandt folgt: $f(2^{n+1}+k)=f(2^{n+1}+k-1)=2(k-1)+1+2=2k+1$

**Aufgabe**
Berechne
$f(1000)=977$
$f(2600)=1105$

#### 1-Bit-Linksrotation

Sei $n\in\mathbb{N}$ in Binärdarstellung $n=\sum^m_\limits{j=0}b_j2^{j+1} (b_j\in[0,1]\forall j\le m)$. Dann ist $r: \mathbb{N}\to\mathbb{N}$ mit $n\to b_m+\sum^{m-1}_\limits{j=0}b_j2^{j+1}$ die 1-Bit-Linksrotation.

**Beispiele**
$n=10=(1010)_2\to r(n)=(0101)_2=5$
$n=14=(1110)_2\to r(n)=(1101)_2=13$

**Satz**
$f(n)=r(n)\forall n\in\mathbb{N}$

**Beweis**
Seien $m,k\in\mathbb{N}$ so gegeben, dass $n=2^m+k$ mit $0\le k<2^m$. Dann gilt: $2^m=(10\dots0)_2$ und $k=(0b_{m_1}b_{m-2}\dots b_0)$ mit $b_j\in[0,1]\to2^m+k=(1b_{m_1}b_{m-2}\dots b_0)$.
Wegen $f(n)0f(2^m+k)=2k+1$, folgt: $f(n)=2(0b_{m_1}b_{m-2}\dots b_0)_2+1=(b_{m_1}b_{m-2}\dots b_00)_2+1=(0b_{m_1}b_{m-2}\dots b_01)_2=r(2^m+k)=r(n)$

**Satz**
Sei $f$ die Josephus-Funktion, dann gilt $\forall n\in\mathbb{N}$: $f(n)=1+2n-2^{1+\log_{2}n}$

**Hinweis**
Gaußsche Klammern: $[x]=\max{k\in\mathbb{Z}|k\le x}$

**Beweis**
Es gilt: $f(n)=f(2^{\log_{2}n}+n-2^{\log_{2}n})$
Offensichtlich ist $n<2^{1+\log_{2}n}\forall n\in\mathbb{N}$. Daraus folgt $2n<2*2^{\log_{2}n}\to n-2^{\log_{2}n}=2^{\log_{2}n}$. Daraus folgt: $f(n)=1+2n-2^{1+\log_{2}n}$

### Permutation für $k=3$

| n      | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| f_3(n) | 1   | 2   | 2   | 1   | 4   | 1   | 4   | 7   | 1   | 4   |

**Hinweise**
Aufrundungsfunktion $[x]=\min{k\in\mathbb{Z}|k\ge x}$
Rundungsfunktion $\text{round}(x)=[x+\frac{1}{2}]\forall x\in\mathbb{R}^+$

Sei im Folgenden $\alpha\in\mathbb{R}$ eine Konstante mit $\alpha\approx0.8111$

$\forall n\in\mathbb{N}$ sei $m(n)$ die größte ganze Zahl, für die gilt: $\text{round}(\alpha\frac{3}{2}^{m(n)})\le n$

**Satz**
Es gilt: $m(n)=\text{round}(\log_{\frac{3}{2}}\frac{n}{\alpha})$ und $m(n)=\text{round}(\log_{\frac{3}{2}}\frac{n}{\alpha})-1$

**Beweis**
Es gilt $\frac{n}{\alpha}=\frac{3}{2}^{\log_{\frac{3}{2}}\frac{n}{\alpha}}$ und somit $n=\alpha\frac{3}{2}^{\log_{\frac{3}{2}}\frac{n}{\alpha}}$. Ist $[\log_{\frac{3}{2}}\frac{n}{\alpha}]=\text{round}(\log_{\frac{3}{2}}\frac{n}{\alpha})$, dann gilt $n=\alpha(\frac{3}{2})^{\log_{\frac{3}{2}}\frac{n}{\alpha}}\ge\alpha(\frac{3}{2})^{[\log_{\frac{3}{2}}\frac{n}{\alpha}]}=\alpha(\frac{3}{2})^{\text{round}(\log_{\frac{3}{2}}\frac{n}{\alpha})}$.

**Satz**
$f_3(n)=3(n-\text{round}(\alpha\frac{3}{2})^{m(n)})+\Bigg\{\begin{matrix}2\quad\text{ wenn }\alpha(\frac{3}{2})^{m(n)}<\text{round}(\alpha(\frac{3}{2})^{m(n)})\\1\quad\text{ wenn }\alpha(\frac{3}{2})^{m(n)}>\text{round}(\alpha(\frac{3}{2})^{m(n)})\end{matrix}$

**Beispiel**
$n=41$
1. $\text{round}(\log_{\frac{3}{2}}\frac{n}{\alpha})=\text{round}(\log_{\frac{3}{2}}\frac{41}{0.8111})=\text{round}(9.81)=10=m'$
2. $\text{round}(\alpha(\frac{3}{2})^{m'})=\text{round}(\alpha(\frac{3}{2})^{10})=47>n\to m(41)=m'-1=9$
3. $\text{round}(0.8111(\frac{3}{2}^9))=\text{round}(31.18)=31$, es wird abgerundet, daher: $f_3(41)=3(41-31)+1=31$

**Beispiel**
$n=50$
1. $\text{round}(\log_{\frac{3}{2}}\frac{n}{\alpha})=\text{round}(\log_{\frac{3}{2}}\frac{50}{0.8111})=\text{round}(10.1646)=10=m'$
2. $\text{round}(\alpha(\frac{3}{2})^{m'})=\text{round}(\alpha(\frac{3}{2})^{10})=47<n\to m(50)=m'=10$
3. $\text{round}(0.8111(\frac{3}{2}^{10}))=\text{round}(46.7721)=47$, es wird aufgerundet, daher: $f_3(50)=3(50-47)+2=11$

**Beispiel**
$n=35$
1. $\text{round}(\log_{\frac{3}{2}}\frac{n}{\alpha})=\text{round}(\log_{\frac{3}{2}}\frac{35}{0.8111})=\text{round}(9.28492)=9=m'$
2. $\text{round}(\alpha(\frac{3}{2})^{m'})=\text{round}(\alpha(\frac{3}{2})^{9})=31<n\to m(31)=m'=9$
3. $\text{round}(0.8111(\frac{3}{2}^{9}))=\text{round}(31.1814)=31$, es wird abgerundet, daher: $f_3(50)=3(35-31)+1=13$

## Permutation für $k\ge4$

**Satz**
Es gilt $\forall n,k\in\mathbb{N}_{\ge2} f_k(n)=((f_k(n-1)+k-1)\mod n)+1$ mit $f_k(1)=1$

**Beispiel**
$f_3(7)=4$
$f_5(17)$, wenn $f_5(15)=2$
$f_5(16)=2+5-1+1=7$
$f_5(17)=7+5-1+1=12$