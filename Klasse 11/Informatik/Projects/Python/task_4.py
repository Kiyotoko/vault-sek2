quiz = [
    ("Was ist die Hauptstadt von Deutschland? ", "Berlin"),
    ("Was ist die Hauptstadt von England? ", "London"),
    ("Was ist die Hauptstadt von Italien? ", "Rom"),
    ("Was ist die Hauptstadt von Frankreich? ", "Paris"),
    ("Was ist die Hauptstadt von Niederlande? ", "Amsterdam"),
    ("Was ist die Hauptstadt von Belgien? ", "Brüssel"),
    ("Was ist die Hauptstadt von Spanien? ", "Madrid")
]

global score
score=0


def ask(index):
    tup = quiz[index]
    if(input(tup[0]).lower() == tup[1].lower()):
        global score
        score+=1
        print("Richtig!")
    else:
        print("Falsch!")


print("Kennst du die europäischen Hauptstädte?")
questions=len(quiz)
for i in range(questions):
    ask(i)
print("Fertig!")
print("Du hattes", score/questions*100, "Prozent der Fragen fertig.")