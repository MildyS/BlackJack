import random
bkarty = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,"J","J","J","J","Q","Q","Q","Q","K","K","K","K","A","A","A","A"]
sucet1 = 0
sucet2 = 0
sucet = 0
x = 0
hrac = 1
vzdal1 = False
vzdal2 = False
def kontrolak(otazka):
    sucet = 0
    if otazka == "z":
        karta = random.choice(bkarty)
        for i in range(0,len(bkarty)):
            if bkarty[i] == karta:
                del bkarty[i]
                break
        if karta == "J" or karta == "Q" or karta == "K":
            x = 10
            sucet += x
        elif karta == "A":
            x = 11
            sucet += x
        else:
            sucet += karta
        print("Vytiahnutá karta: " + str(karta))
    elif otazka == "n":
        pass
    else:
        print("Zle zadané písmeno, vyber znova")
        otazka = input("Pre zobranie karty slač Z, pre ukončenie ťahu slač N: ")
        kontrolak(otazka)
    return sucet

print("Hra sa začína !!!")
while True:
    print("Hráč "+ str(hrac) )
    otazka = input("Pre zobranie karty slač Z, pre ukončenie ťahu slač N: ")


    if hrac == 1:
        sucet1 += kontrolak(otazka)
        print("Váš súčet je: " + str(sucet1))
        hrac += 1
    else:
        sucet2 += kontrolak(otazka)
        print("Váš súčet je: " + str(sucet2))
        hrac -= 1

    if sucet1 == 21:
        print("Hráč 1 má BLACKJACK!!!")
        print("Hráč 2 prehrali ste !!!")
        break
    if sucet2 == 21:
        print("Hráč 2 má BLACKJACK!!!")
        print("Hráč 1 prehrali ste !!!")
        break
    if sucet1 > 21:
        print("Hráč 1 prehrali ste !!!")
        print("Hráč 2 vyhral !!!")
        break
    if sucet2 > 21:
        print("Hráč 2 prehrali ste !!!")
        print("Hráč 1 vyhral !!!")
        break

