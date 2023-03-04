# values
T = linspace(0,10,10);
X = T * 8;

Y1 = - (9.81 / 2) * T.^2;
Y2 = - 9.81/(2*8^2)*X.^2;

# settings
title("Linear Graph");
xlabel("x-Achse");
ylabel("y-Achse");
set(gca, "Fontsize", 16);

plot(X,Y1,'-xr')
hold on
plot(X,Y2,'-pg')
