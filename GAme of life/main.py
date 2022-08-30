from spillbrett import Spillbrett


def main():
    # Spør bruker om input og deler opp i to int verdier som puttes inn i spillbrettobjektet
    brett = input("Hvor stort rutenett ønsker du? (Rad, Kolonne): ")
    rad, kolonne = brett.split(",")
    rad = int(rad)
    kolonne = int(kolonne)
    spillbrett = Spillbrett(rad, kolonne)
    print(" ")
    print("For å se neste generasjon trykk 'ENTER'.")
    print("For å avslutte, skriv inn 'q'.")
    # spør etter input fra bruker
    x = input("Skriv inn her: ")
    # oppdaterer dersom verdien er blank
    if x == "":
        spillbrett.oppdatering()
    # avslutter om x er q og oppdaterer om x er blank
    while x != "q":
        x = input("Skriv inn her: ")
        if x == "":
            spillbrett.oppdatering()


        # starte hovedprogrammet
main()
