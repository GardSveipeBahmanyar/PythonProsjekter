import random
from cell import Celle


class Spillbrett:

    # Oppretter konstruktær og rutenett med celleobjekter. Kaller også på funksjonene for spillbrettet.
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._genNum = 0
        self._rutenett = []

        for i in range(rader):
            self._rutenett.append([])
            for j in range(kolonner):
                self._rutenett[i].append(Celle())

        self._generer()
        self.tegnBrett()
        self.finnAntallLevende()

    # traverserer gjennom rutenettet og oppretter et levende celleobjekt dersom randomint er 1.
    def _generer(self):
        for rad in range(self._rader):
            for kolonne in range(self._kolonner):
                if random.randint(0, 2) == 1:
                    self._rutenett[rad][kolonne].settLevende()

    def tegnBrett(self):  # Tegner spillbrett ved å traversere gjennom rutenettet og skrive ut O eller . avhengig av celleklasse-metoden
        for rad in self._rutenett:
            print("\n")
            for celler in rad:
                print(celler.tegnrepresentasjon(), end=" ")
        print(" ")
        print("Generasjon", self._genNum)

    def finnNabo(self, rad, kolonne):
        naboListe = []

        # traverserer gjennom naboene
        for i in range(-1, 2):
            for j in range(-1, 2):
                naboRad = rad + i
                naboKolonne = kolonne + j

                gyldig = True

                # sjekker om vi befinner oss i cellen vi sjekker
                if i == 0 and j == 0:
                    gyldig = False

                # naboRad er uten for indeksene sine
                if naboRad < 0 or naboRad >= self._rader:
                    gyldig = False

                # naboKolonne er utenfor indeksene sine
                if naboKolonne < 0 or naboKolonne >= self._kolonner:
                    gyldig = False

                if gyldig:  # dersom ingen av iftesten slår til over vil cellen ha naboer. Disse naboene vil bli lagt til i en naboliste
                    naboListe.append(
                        self._rutenett[naboRad][naboKolonne])

        return naboListe

    def oppdatering(self):
        dToA = []
        aToD = []
        # traverserer gjennom rutenettet
        for rad in range(self._rader):
            for kolonne in range(self._kolonner):
                # sjekker hver celle om den har en nabo
                naboListe = self.finnNabo(rad, kolonne)
                i = 0
                for nabo in naboListe:  # sjekker naboene og plusser 1 til i dersom den har en eller flere levende nabo
                    if nabo.erLevende():
                        i += 1
                # Sjekker levende Celler
                # hvis cellen er levende sjekker vi med to if tester
                if self._rutenett[rad][kolonne].erLevende() == True:
                    if i < 2:
                        aToD.append(self._rutenett[rad][kolonne])
                    elif i > 3:
                        aToD.append(self._rutenett[rad][kolonne])
                # Sjekker døde Celler
                # hvis cellen er død sjekker vi med 1 if test
                if self._rutenett[rad][kolonne].erLevende() == False:
                    if i == 3:
                        dToA.append(self._rutenett[rad][kolonne])

        print(" ")
        print(" ")
        print(" ")

        self._genNum += 1

        for celler in aToD:  # traverserer gjennom aliveToDead array og setter levende celler til døde
            celler.settDoed()
        for celler in dToA:  # traverserer gjennom deadToAlive array og setter døde celler til levene
            celler.settLevende()
        # genererer nytt brett med oppdaterte celler
        Spillbrett.tegnBrett(self)
        Spillbrett.finnAntallLevende(self)

    # travererserer gjennom rutenettet og sjekker om celler er levende. Dersom de er det, plusses i med 1
    def finnAntallLevende(self):
        i = 0
        for rad in range(self._rader):
            for kolonne in range(self._kolonner):
                if self._rutenett[rad][kolonne].erLevende():
                    i += 1
        print("Antall levende Celler: {}".format(i))
