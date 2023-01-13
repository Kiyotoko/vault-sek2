# Memorize
## Zahlenbereiche
### Natürliche Zahlen 
* beinhaltet alle positiv ganzen Zahlen
* Symbol $\mathbb{N}$
### Gebrochene Zahlen
* erweiterung der natürlichen Zahlen, erweitert durch Brüche
* Symbol $\mathbb{Q^+}$
### Reelle Zahlen
* beinhalten auch $\sqrt{2}$ und $\pi$
* Symbol $\mathbb{R}$
### Komplexe Zahlen
* Erweiterung der reellen Zahlen um eine imaginäre Einheit $i$ mit $i²=-1$
* Symbol $\mathbb{C}$
## Tensoren
* multidimensionale Arrays
### Vektoren
* $\vec a$ Vektor $\begin{pmatrix}a_1\\ a_2\\a_3\end{pmatrix}$
* Rechenoperatoren:
	* Addition und Subtraktion
	* Skalarmultiplikation
	* Skalarprodukt
### Matrix
* $m,n$-Matrix $\begin{pmatrix}a_{1,1}&a_{1,2}&\cdots&a_{1,n}\\a_{2,1}&a_{2,2}&\cdots&a_{1,n}\\ \vdots&\vdots&\ddots&\vdots \\ a_{m,1}&a_{m,2}&\cdots&a_{m,n}\end{pmatrix}$
* Rechenoperation:
	* Addition zweier gleich großer $mn$-Matrizen
	* Skalarmultiplikation einer Matrix mit einem Skalar
	* Matrizenmultiplikation zweier Matrizen, wobei die Spaltenanzahl der linken Matrix mit denen der Zeilenanzahl der rechten Matrix übereinstimmt
# Gleichungssysteme
### Gauß-Verfahren
Das gaußsche Eliminationsverfahren oder einfach Gauß-Verfahren ist ein Algorithmus aus den mathematischen Teilgebieten der linearen Algebra und der Numerik. Es ist ein wichtiges Verfahren zum Lösen von linearen Gleichungssystemen und beruht darauf, dass Äquivalenztransformationen zwar das Gleichungssystem ändern, aber die Lösung erhalten. Dies erlaubt es, jedes eindeutig lösbare Gleichungssystem auf Stufenform zu bringen, an der die Lösung durch sukzessive Elimination der Unbekannten leicht ermittelt oder die Lösungsmenge abgelesen werden kann. 

Beispiel:
$a+b+c=x\quad a+b+c=x$
$a+b+c=x\quad b+c=x$
$a+b+c=x\quad c=x$
## Differenzialrechnung
Die Differential- oder Differenzialrechnung ist ein wesentlicher Bestandteil der Analysis und damit ein Gebiet der Mathematik. Zentrales Thema der Differentialrechnung ist die Berechnung lokaler Veränderungen von Funktionen. Während eine Funktion ihren Eingabewerten nach tabellarischem Prinzip gewisse Ausgangswerte zuordnet, wird durch die Differentialrechnung ermittelt, wie stark sich die Ausgabewerte nach sehr kleinen Veränderungen der Eingabewerte ändern. Sie ist eng verwandt mit der Integralrechnung, mit der sie gemeinsam unter der Bezeichnung Infinitesimalrechnung zusammengefasst wird. 

* __Beispiel:__
	* $f(x)=x²$
	* $f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}=\lim_{h\to 0}\frac{(x+h)^2-x^2}{h}=\lim_{h\to0}\frac{x^2+2xh+h^2-x^2}{h}=\lim_{h\to 0}(2x+h)$

# Tasks
## 13.09.2022
$\frac{\Delta r}{\Delta t}=\frac{9-3}{8-2}=\frac{6}{6}=1\frac{m}{s}\quad3m-1\frac{m}{s}*2s=1m$
$\frac{\Delta r}{\Delta t}=\frac{8-2}{7-3}=\frac{6}{4}=1.5\frac{m}{s}=2m-1.5\frac{m}{s}*3s=-2.5m$
$t+1=1.5t-2.5\quad -.5t=-3.5\quad t=7\quad r=8$
$X_A(8)=1.5*8+1=13$