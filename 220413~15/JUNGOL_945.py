PHJ={"Pokemon":"Pikachu",
    "Digimon":"Agumon",
    "Yugioh":"Black Magician"}
input_PHJ=input()
print(PHJ.get(input_PHJ,"I don't know"))

"""
try :
    print(PHJ[input_PHJ])
except:
    print("I don't know")
"""