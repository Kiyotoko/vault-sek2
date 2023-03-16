body_mass = [
    (0, 18.5, "Untergewicht"),
    (18.5, 24.9, "Normalgewicht"),
    (24.9, 29.9, "Übergewicht"),
    (29.9, 34.9, "Adipositas I"),
    (34.9, 39.9, "Adipositas II"),
    (40, 1_000, "Adipositas III"),
]


weigth=float(input("Gewicht (kg): "))
height=float(input("Größe (m): "))
bmi=weigth/height**2

for clazz in body_mass:
    if(clazz[0] <= clazz[1] < bmi):
        print(clazz[2])