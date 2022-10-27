from time import localtime # import för funktion


timme = localtime().tm_hour # skapar variabel timme för timme nu i verkliga livet

if timme >= 16: 
    print("skoldagen är slut") # om lokala tiden timmar är mer än eller lika med 16 kommer den printa skoldagen är slut
elif timme < 16:
    print("skoldagen pågår")
elif timme < 8:
    print("skoldagen har inte börjat")


namn = input("vad heter du")

namn = namn.strip()

age = input("hur gammal är du")

age = age.strip()

age = int(age)

if age >= 18:
    print("den första bokstaven i ditt namn är".format(namn), namn[0], "och du är myndig")




