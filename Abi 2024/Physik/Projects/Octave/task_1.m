# values
X = linspace(0,100,100)

Y1 = 25 * X
Y2 = -20 * X + 1000

# settings
title("Linear Graph");
xlabel("x-Achse");
ylabel("y-Achse");
set(gca, "Fontsize", 16);

plot(X,Y1,'-xr')
hold on
plot(X,Y2,'-xg')
