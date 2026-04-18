# Stochează datele unor elevi într-o listă de dicționare. Fiecare elev are:

# nume (string)
# note (listă de numere)
# prezenta (procent, float)
# 
# Calculează media fiecărui elev și adaug-o în dicționar (medie).
# Selectează elevii cu media ≥ 7 și prezență ≥ 85% și pune-i într-o listă separată.

# Afișează doar numele elevilor selectați, fiecare cu mesajul:

# Felicitări, [Nume]! Ai trecut cu media [medie] și prezența [prezenta]%.
# Extra challenge cu list comprehension:
# Creează o listă cu toate notele > 9 din toți elevii.




elevi = {
"Ana" : {"nume": "Ana", "note": [10,8,9], "prezenta": 95.0},
"Sandu" : {'nume': "Sandu", "Note": [10,10,10], "prezenta": 100.0},
"Andrei" : {"nume": "Andrei", "Note": [8,6,9], "prezenta": 80.2},
"Media" : {"Andrei": None, "Sandu": 0, "Ana": "..."} }
# def media(elevi["note"]):
#     elevi/elevi[note].count()

# print(elevi["Ana"]["note"])

elevi["Media"]["Andrei"] = ((elevi["Andrei"]["Note"][0] + elevi["Andrei"]["Note"][1] + elevi["Andrei"]["Note"][2])  / len(elevi["Andrei"]["Note"]))

media_andrei = round(elevi["Media"]["Andrei"], 2)

# print(elevi["Andrei"]["Note"][0] + elevi["Andrei"]["Note"][1] + elevi["Andrei"]["Note"][2]  / len(elevi["Andrei"]["Note"]))




print(f"Media lui Andrei: {media_andrei}")

# elevi["Media"]["Andrei"] = elevi["Media"]["Andrei"] = (elevi["Andrei"]["Note"][0] + elevi["Andrei"]["Note"][1] + elevi["Andrei"]["Note"][2])  / len(elevi["Andrei"]["Note"])

note_sandu = elevi["Sandu"]["Note"]
media_sandu = 0 
for x in note_sandu:
    media_sandu += x  
    


elevi["Media"]["Sandu"] = media_sandu / len(elevi["Sandu"]["Note"])
print(f"Media lui Sandu: {elevi["Media"]['Sandu']}")

