from vypis import Vypis


class PridatUzivatele:

    def __init__(self):
        self.vek = None
        self.spravne = None
        self.telefon = None
        self.krestni = None
        self.prijmeni = None

    def pridat_krestni(self):
        self.krestni = input("Zadejte křestní jméno pojištěného:\n")
        data_pojistencu.append(self.krestni)

    def pridat_prijemni(self):
        self.prijmeni = input("Zadejte příjmení pojištěného:\n")
        data_pojistencu.append(self.prijmeni)

    def pridat_telefon(self):
        self.spravne = False
        while not self.spravne:
            try:
                self.telefon = int(input("Zadejte telefonní číslo pojištěného:\n"))
                self.spravne = True
            finally:
                print("Telefonní číslo může obsahovat pouze číslice!:\n")
        data_pojistencu.append(self.telefon)

    def pridat_vek(self):
        self.vek = int(input("Zadejte věk pojištěného:\n"))
        data_pojistencu.append(self.vek)
        
    @staticmethod
    def kompletni_zapis(self):
        vypis.obrazovka_hla()
        pridat_uzivatele.pridat_krestni()
        pridat_uzivatele.pridat_prijemni()
        pridat_uzivatele.pridat_telefon()
        pridat_uzivatele.pridat_vek()
        vypis.obrazovka_hla()
        print("Nový pojištěnec úspěšně přidán !\n\nPokračujte libovolnou klávesou...")
        input()

    def __str__(self):
        return data_pojistencu


pridat_uzivatele = PridatUzivatele()
vypis = Vypis()

data_pojistencu = []
