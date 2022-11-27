wygrane1 = 2
wygrane2 = 2


runda = 1

while wygrane1 != 3 or wygrane2 != 3:
    
    player1_choose = str(input("\nPodaj wybór Gracz1: "))
    player2_choose = str(input("Podaj wybór Gracz2: "))

    if player1_choose != player2_choose:

        if player1_choose == "kamien" and player2_choose == "nozyce":
            wygrane1 += 1
            print(f"Gracz1 wygrał, Runda {runda}\n\
            Wygrane: Gracz1 {wygrane1}, Gracz2 {wygrane2}")
            runda += 1

        elif player1_choose == "papier" and player2_choose == "kamien":
            wygrane1 += 1
            print(f"Gracz1 wygrał, Runda {runda}\n\
            Wygrane: Gracz1 {wygrane1}, Gracz2 {wygrane2}")
            runda += 1

        elif player1_choose == "nozyce" and player2_choose == "papier":
            wygrane1 += 1
            print(f"Gracz1 wygrał, Runda {runda}\n\
            Wygrane: Gracz1 {wygrane1}, Gracz2 {wygrane2}")
            runda += 1
        
        else:
            wygrane2 += 1
            print(f"Gracz2 wygrał, Runda {runda}\n\
            Wygrane: Gracz1 {wygrane1}, Gracz2 {wygrane2}")

    else:
        print("Remis")

else:
    if wygrane1 == 3:
        print("Wygrał Gracz1")
    else:
        print("Wygrał Gracz2")