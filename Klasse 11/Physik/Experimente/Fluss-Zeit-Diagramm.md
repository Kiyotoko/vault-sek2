---
author: karlz
tags:
  - Physik
  - FGN
---


## Aufgabenstellung

Leite das magnetische Fluss-Zeit-Diagramm für das Innere einer Spule aus dem $U_{ind}(t)$-Diagramm ab. Dabei wird ein Magnet durch die Spule ($N=1200$) fallen gelassen. Das $\Phi(t)$-Diagramm soll 10 Punkte besitzen.

## Herleitung

$A=\frac{U_{ind_1}+U_{ind_2}}{2}*\Delta t$
$U_{ind}=-N\frac{\Delta\Phi}{\Delta t}$
$\Delta\Phi=-\frac{U_{ind}*\Delta t}{N}$
$\Delta\Phi=-\frac{\frac{U_{ind_1}+U_{ind_2}}{2}*\Delta t}{N}$
$\Phi_j=\sum_\limits{k=0}^{j}-\frac{\frac{U_{ind_{k}}+U_{ind_{k+1}}}{2}*\Delta t_{k\to k+1}}{N}$

## Messwerte

|     | u1    | u2    | dt   | phi             | sum             |
| --- | ----- | ----- | ---- | --------------- | --------------- |
| 1   | -0.01 | -0.03 | 0.02 | $3.33*10^{-7}$  | $3.33*10^{-7}$  |
| 2   | -0.03 | -0.11 | 0.02 | $1.166*10^{-6}$ | $1.5*10^{-6}$   |
| 3   | -0.11 | -0.23 | 0.02 | $5.666*10^{-6}$ | $7.166*10^{-6}$ |
| 4   | -0.25 | -0.30 | 0.02 | $3.43*10^{-6}$  | $4.58*10^{-6}$  |
| 5   | -0.30 | -0.02 | 0.02 |                 |                 |
| 6   | -0.01 | 0.51  | 0.02 |                 |                 |
| 7   | 0.52  | 0.36  | 0.02 |                 |                 |
| 8   | 0.32  | 0.03  | 0.02 |                 |                 |
| 9   | 0.03  | 0.02  | 0.02 |                 |                 |
| 10  | 0.02  | -0.02 | 0.02 |                 |                 |