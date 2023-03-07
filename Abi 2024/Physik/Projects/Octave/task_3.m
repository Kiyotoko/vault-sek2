# values
X = linspace(0,20,40);

Y1 = 0.5/2 * X.^2 + 2 * X;
Y2 = 4 * X + 10;

# settings
title("Linear Graph");
xlabel("x-Achse");
ylabel("y-Achse");
set(gca, "Fontsize", 16);

plot(X,Y1,'-xr')
hold on
plot(X,Y2,'-xg')
