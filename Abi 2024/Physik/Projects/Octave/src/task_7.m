# values
T = linspace(0, 5, 10^2);
X = 8 * T * cos(35 / 180 * pi);

Y1 = -9.81/2 * T.^2 + 8 * T * sin(35 / 180 * pi);
Y2 = -9.81/(2 * 8^2 * cos(35 / 180 * pi)^2) * X.^2 + X * tan(35 / 180 * pi);

# settings
title("Throw Graph");
xlabel("x-Achse");
ylabel("y-Achse");
set(gca, "Fontsize", 16);

plot(X,Y1,'-xr')
hold on
plot(X,Y2,'-cg')
