# values
X = linspace(0,10,10^2)

Y1 = 30 * X;
Y2 = 10 * X.^2 + 30;
Y3 = -2 * X.^3 + X -1;

plot(X,Y1,'-xr')
hold on
plot(X,Y2,'-xg')
plot(X,Y3,'-xb')
