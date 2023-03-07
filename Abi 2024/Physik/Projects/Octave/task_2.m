# values
X1 = linspace(-5, 5, 5^2);
Y1 = sin(X1) * 5;
X2 = linspace(-5, 5, 5^2);
Y2 = X2.^2;

# settings
title("Linear Graph");
xlabel("x-Achse");
ylabel("y-Achse");
set(gca, "Fontsize", 16);

plot(X1, Y1, '-ob')
hold on
plot(X2, Y2, '-xr')
grid on
