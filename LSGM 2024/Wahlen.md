## Wahlsysteme

**Definition**
$A=\{a_{0},a_{1},\dots,a_{x}\}$ Kandidaten
$N=\{1,\dots,N\}$ Wahlberechtigte
Jeder hat Reihenfolge $R$ under Kandidaten, z.B. $R_{1}: a_{1}>a_{2}>a_{k}$ am besten

Wahlsystem Funktion: $\{(R_{1},R_{2},\dots,R_{i}),\dots\}\to A$

**Beispiel**
1. Meiste erste Stimmen gewinnt (UK)
	- Tie-Break: $a_{1}>a_{2}>\dots>a_{k}$
2. Bordacount:

| Listenplatz | Punkte |
| ----------- | ------ |
| 1           | k-1    |
| 2           | k-2    |
| ...         | ...    |
| k           | 0      |

3. Integrierte Stichwahl/Ranked Choice (Australien)
	- wenigsten Erststimmen raus
	- 
4. Stichwahl zwischen Top 2 (Fra)
5. Eliminierung: meiste letzte Stimmen raus
	- dann neu abstimmen

---

**Beispiel**
$k=5\quad N=100$

| Personen | Reihenfolge |
| -------- | ----------- |
| 31       | A>B>D>E>B   |
| 20       | B>D>C>E>A   |
| 19       | D>C>E>B>A   |
| 16       | E>C>B>A>D   |
| 14       | C>E>D>B>A   |

Beim ersten System: A Gewinnt
Beim zweiten System: C Gewinnt
Beim dritten System: C fliegt raus, D fliegt raus, B fliegt raus, A fliegt raus, E gewinnt
Beim vierten System: B gewinnt
Beim fünften System: D gewinnt

## Kriterien

a) Majorität: Ein Kandidat mit > 50% Erststimmen gewinnt
b) Autiz-Majorität: Ein Kandidat mit > 50% Letztstimmen gewinnt nicht
c) Pareto: Wenn jeder $X$ vor $Y$ sieht, soll $Y$ nicht gewinnen
d) Condoret: Wenn $X$ jede Stichwahl gewinnt, soll $X$ gewinnen
e) Eine Erststimme muss relevant sein/bleiben

|     | 1   | 2   | 3   | 4   | 5   |
| --- | --- | --- | --- | --- | --- |
| a   | ✅   | ❌   | ✅   | ✅   | ❌   |
| b   | ❌   | ✅   | ✅   | ✅   | ✅   |
| c   | ✅   | ✅   | ✅   | ✅   | ✅   |
| d   | ❌   |     | ❌   | ❌   |     |
| e   | ✅   | ✅   | ✅   | ✅   | ❌   |
