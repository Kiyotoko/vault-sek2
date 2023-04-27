array = ["Karl", "Carl", "Til", "Philip"]
array.append("Hannah")
array += ["Cora", "Wilhelm"]
array.extend(["Max", "Leni", "Mailin"])
array.sort()
print(array)

dict = {
    "alter":17,
    "vorname":"Carl",
    "nachname":"Zimmermann"
}
print(dict["vorname"])

tuple = (17, "Carl", "Zimmermann")
print(tuple.index(17))

class Bewohner:

    def __init__(self, vorname, nachname, alter) -> None:
        self.vorname = vorname
        self.nachname = nachname
        self.alter = alter

carl = Bewohner(alter=17,vorname="Carl", nachname="Zimmermann")

print(carl.alter)