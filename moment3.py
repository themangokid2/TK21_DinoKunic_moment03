from time import localtime # import för funktion


timme = localtime().tm_hour # skapar variabel timme för timme nu i verkliga livet

for i in range(1, 25)
 timme += 1
    if timme >= 8 and timme <= 17:
        print('skolan pågår')
    if timme >= 17 and timme <=24:
        print('skolan är slut')


namn = input("vad heter du")

namn = namn.strip()

age = input("hur gammal är du")

age = age.strip()

age = int(age)

if age >= 18:
    print("den första bokstaven i ditt namn är".format(namn), namn[0], "och du är myndig")




