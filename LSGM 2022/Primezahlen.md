# Primzahlen

$\DeclareMathOperator\rev{rev}$
* Satz: $P$ ist eine unendliche Menge
* Beweis: 
	* Angenommen, $P$ ist eine endliche Menge. 
	* Dann gilt $E$ $n$ $e$ $N$ : $P = { P1, P2, P3, ..., Pn }$ 
	* Sei $m$ $e$ $N$ : $m = (n~j=1 Pj) + 1$ 
	* Zwei Fälle;
		* 1.Fall: $m$ ist eine Primzahl
		* 2.Fall: $m$ist keine Primzahl
	* PI(x) > x / \log(x) V >= 17

# Sheldon-Primzahlen

* ### Beispiel 37:
	* 73 ist die 21 Primzahl
	* 37 ist die 12 Primzahl
	* 12 ist die Spiegeltzahl von 21
	* 21 =  7 x 3
* ### Definition:
	* Sei $n \in N$ und $Pn \in N$  die n-te Primzahl
		1. $Pn$ hat die Produkteigenschaft, wenn für all seine Ziffern $a1, a2, a3, ..., an$  ($R$ $e$ $N$ gilt: $k~j=1 aj = n$)
		1. Für $m \in N$ ist rev(m) die Zahl, deren Ziffern in umgekehrter Reihenfolge im Vergleich zu $m$ angeordnet sind. Bsp.: m = 51.792 => rev(m) = 29.715
		1. $P_n$ hat die Spiegeleigenschaft, wenn gilt: $\rev{P_n} = P*\rev{n}$
		1. $P_n$ ist eine Shelton-Primzahl, wenn sie sowohl die Produkt-, als auch die Spiegeleigenschat besitzt
* ### Satz:
	* 73 ist eine Sheldon-Primzahl
* ### Beweis:
	1. $P_n = 73 \to n = 21; k~j=1 aj = 3 * 7 = 21 = n$
	1. $\rev(73) = 37$ mit $P21 = 73; rev(21) = 12 \to P rev(21) = P12 = 37 = \rev(73)$
* ### Satz:
	* Es gibt nur endlich viele Sheldon-Primzahlen
* ### Beweis:
	* Es gibt keine Sheldon-Primzahl $P_n \to 10E45$. 
	* Wiederspruchsbeweis: Sei $P_n \in P \to 10E45$ eine Sheldon-Primzahl mit $k$ Ziffern und der Anfangsziffer $a1 \in { 1, ..., 9 }$ 
	* Nach der Produkteigenschaft gilt: $n = k~j=1 aj \gets a1 x 9^{k-1}$. Da $P_n > 10E45 > 17$,  gilt: $n = \pi(n) > P_n / \log(P_n)$ 
	* $f(x) = x / \log(x)$ ist eine streng monoton wachsende Funktion, weshalb mit $P_n > a1 x 10^a_1 * 10^{k-1}$ folgt $n > a*\frac{10^{k-1}}{\log{a1 x 10^k-1}}$ und somit $a1 x g^{k-1} > a1 x 10^{k-1} / \log(a x 10^k-1)$ <=> $g^k.1 > 10^k-1 / \log(a1 x 10^k1)$ <=> $\log(a1 x 10^k-1) > 10^k-1 / 9^k-1$ <=> $\log(a1) + \log(10^k-1) > (10 / 9)^k-1$ <=> $\log(a1) + (k-1)\log(10) > (10 / 9)^k-1$ => $k x \log(10) > (10 / 9)^k-1$ (da a1 < 10)
	* Für alle $k >= 46$ gilt aber $k x \log(10) < (10 / 9) ^ k-1$

# Vollständige Induktion

* Für alle $n \in N$:  $2^n > n²$
* ### Induktionsanfang: n0 = 5
	* $2^n0 = 2⁵ = 32 > n0² = 5² = 25$
* ### Induktionsvorraussetzung:
	* $2^n > n²$ für ein $n >= 5$
* ### Induktionsbehauptung:
	* $2^n+1 > (n+1)²$
* ### Induktionsschluss:
	* $(n+1)² = n² + 2n + 1 < 2^n + 2n + 1 < 2^n + 2^n = 2 x 2^n = 2^n+1$

# Beweis Durch Vollständige Induktion Nach $k \in \mathbb{N}$

* ### Satz:
	* $k x \log(10) > (10 / 9)^k-1$
	* $k x \log(10) < (10 / 9)^k-1$
* ### Beweis:
	* $k0 = 46 => k0 x \log(10) < 106; (10 / 9)^k0-1 > 114$
	* $k*\log(10)<(10 / 9)^{k-1} \forall k\in\mathbb{N}>=46$
	$(k+1) x \log(10) < (10 / 9)^k(k+1) x \log(10)$
	$= k x \log(10) + \log(10) < (10 / 9)^k-1 + \log(10)$
	$= (10 / 9)^k - (10 / 9)^k-1 x (1 / 9) + \log(10) < (10 / 9)^k$
	$= (10 / 9)^k + (\log(10) - (1 / 9) x (10 / 9)^k-1)$
	
* ### Satz:
	* Sein $P_n\in\mathbb{P}$ eine Shelodon-Primzahl. Dann besitzt $P_n$ als Ziffer niemals die $0$.
* ### Beweis:
	* Es gibt keine 0th Primzahl.
* ### Satz:
	* Sei $P_n\in\mathbb{P}$ eine Sheldon-Primzahl. Dann gilt für ihre Anfangsziffer $a_1$: $a_1 e {1; 3; 7; 9}$
* ### Beweis: 
	* Da nach Vorraussetzung $\rev{P_n}\in P$, muss $\rev{P_n}$ auf $1, 3, 7, 9$ enden.
	* => $a_1 \in {1; 3; 7; 9}$
* ### Satz:
	* Sei $P_n$ eine Sheldon-Primzahl mit $n\geq 10^{10}$. Dann teilt $5^4$ nicht n.
* ### Beweis:
	* Angenommen, es gibt $P_n\in P$ Sheldon-Primzahl mit $n=0\mod5⁴$ und $n>10^{10}\geq P_n$ enthält mindestens viermal die Ziffer 5. 
	* $n\leq a_1*5^4*g^{k-5}$; $P_n\geq a_1*10^{k-1}$
		* $a1 x 5⁴ x 9^k-5 > a1 x 10^k-1 / \log{a^x 10^k-1}$
		* $5^4*g^{k-5} > 10^{k-1} / \log{a_1*10^{k-1}}$
		* $\log{a_1*10^{k-1}}>10^{k-1}=\frac{10^4}{5^4}*\frac{10}{9}^{k-5}=16*\frac{10}{9}^{k-5}$
		* $\log{a_1}+(k-1) x \log(10) > 16 x (10/ 9)^k-5$
		* $k x \log(10) > 16 x (10 / 9)^k-5$ -> Wiederspruch
		* Induktion:
			* Induktionsanfang:
				* $k_0=5$
				* $5*\log(10)>16*1$
			* Induktionsvorraussetzung:
				* $k*\log(10)<16*\frac{10}{9}^{k-5}$
			* Induktionsbehauptung:
				* $(k+1)*\log{10}>16*\frac{10}{9}^{k-4}$
				* $\frac{10}{9}^k*\log{10}<\frac{10}{9}^{k-4} \to \frac{10}{9}k\geq k+1$
