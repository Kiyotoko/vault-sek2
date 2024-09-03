# Tensoren

- Multidimensionale Arrays

## Vektoren

$$\vec{v}=\begin{pmatrix}a_1\\ a_2\\a_3\end{pmatrix}$$

- Rechenoperatoren:
	- Addition und Subtraktion
	- Skalarmultiplikation
	- Skalarprodukt

## Matrix

$$M_{m,n}=\begin{pmatrix}a_{1,1}&a_{1,2}&\cdots&a_{1,n}\\a_{2,1}&a_{2,2}&\cdots&a_{1,n}\\ \vdots&\vdots&\ddots&\vdots \\ a_{m,1}&a_{m,2}&\cdots&a_{m,n}\end{pmatrix}$$

- Rechenoperation:
	- Addition zweier gleich großer $mn$-Matrizen
	- Skalarmultiplikation einer Matrix mit einem Skalar
	- Matrizenmultiplikation zweier Matrizen, wobei die Spaltenanzahl der linken Matrix mit denen der Zeilenanzahl der rechten Matrix übereinstimmt

### Gauß-Verfahren

Das gaußsche Eliminationsverfahren oder einfach Gauß-Verfahren ist ein Algorithmus aus den mathematischen Teilgebieten der linearen Algebra und der Numerik. Es ist ein wichtiges Verfahren zum Lösen von linearen Gleichungssystemen und beruht darauf, dass Äquivalenztransformationen zwar das Gleichungssystem ändern, aber die Lösung erhalten. Dies erlaubt es, jedes eindeutig lösbare Gleichungssystem auf Stufenform zu bringen, an der die Lösung durch sukzessive Elimination der Unbekannten leicht ermittelt oder die Lösungsmenge abgelesen werden kann. 

**Beispiel**
$\begin{matrix}a+b+c=x & a+b+c=x\\ a+b+c=x & b+c=x\\ a+b+c=x & c=x\end{matrix}$

# Differenzialrechnung

Die Differential- oder Differenzialrechnung ist ein wesentlicher Bestandteil der Analysis und damit ein Gebiet der Mathematik. Zentrales Thema der Differentialrechnung ist die Berechnung lokaler Veränderungen von Funktionen. Während eine Funktion ihren Eingabewerten nach tabellarischem Prinzip gewisse Ausgangswerte zuordnet, wird durch die Differentialrechnung ermittelt, wie stark sich die Ausgabewerte nach sehr kleinen Veränderungen der Eingabewerte ändern. Sie ist eng verwandt mit der Integralrechnung, mit der sie gemeinsam unter der Bezeichnung Infinitesimalrechnung zusammengefasst wird. 

**Beispiel**
$f(x)=x^2$
$\begin{split}f'(x)&=\lim\limits_{h\to0}\frac{f(x+h)-f(x)}{h}\\ &=\lim\limits_{h\to 0}\frac{(x+h)^{2}-x^{2}}{h}\\ &=\lim\limits_{h\to0}\frac{x^{2}+2xh+h^{2}-x^{2}}{h}\\ &=\lim\limits_{h\to 0}\; 2x+h\end{split}$
