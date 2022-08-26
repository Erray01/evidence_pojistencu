from vypis import Vypis

vypis = Vypis()

pokracovat = True

spatne = "Špatný vstup, prosím znovu.\n"
nenalezen = "\nHledaný pojištěnec se nenachází v seznamu, pokračujte libovolnou klávesou...\n"
velikost_sloupce = 15

while pokracovat:
    vypis.obrazovka_hla_cela()
    zadano = False
    while not zadano:
        try:
            vyber = int(input())
            if vyber == 1:
                zadano = True
                from pridat import PridatUzivatele

                pridat_uzivatele = PridatUzivatele()
                pridat_uzivatele.kompletni_zapis()

            elif vyber == 2:
                pozice = -1
                vypis.obrazovka_hla()
                zadano = True
                pojistenci = pridat_uzivatele.__str__()
                while pozice != (len(pojistenci) - 1):
                    print("{0}{1}{2}{3}{4}{5}{6}".format(pojistenci[pozice + 1],
                                                         " " * (velikost_sloupce - len(pojistenci[pozice + 1])),
                                                         pojistenci[pozice + 2],
                                                         " " * (velikost_sloupce - len(pojistenci[pozice + 2])),
                                                         pojistenci[pozice + 3],
                                                         " " * (velikost_sloupce - len(str(pojistenci[pozice + 3]))),
                                                         pojistenci[pozice + 4]))

                    pozice += 4
                print("\nPokračujte libovolnou klávesou...\n")
                input()

            elif vyber == 3:
                zadano = True
                vypis.obrazovka_hla()
                jmeno = input("Zadejte jméno pojištěného:\n")
                prijmeni = input("\nZadejte příjmení pojištěného:\n")
                vypis.obrazovka_hla()
                pojistenci = pridat_uzivatele.__str__()
                if (jmeno and prijmeni) in pojistenci:
                    index_jmeno = pojistenci.index(jmeno)
                    index_prijmeni = pojistenci.index(prijmeni)
                    if (index_prijmeni - index_jmeno) == 1:
                        print("{0}{1}{2}{3}{4}{5}{6}".format(pojistenci[index_jmeno],
                                                             " " * (velikost_sloupce - len(pojistenci[index_jmeno])),
                                                             pojistenci[index_prijmeni],
                                                             " " * (velikost_sloupce - len(pojistenci[index_prijmeni])),
                                                             pojistenci[index_prijmeni + 1], " " * (
                                                                     velikost_sloupce - len(
                                                                 str(pojistenci[index_prijmeni + 1]))),
                                                             pojistenci[index_prijmeni + 2]))
                        print("\nPokračujte libovolnou klávesou...\n")
                        input()
                    else:
                        print(nenalezen)
                        input()
                else:
                    print(nenalezen)
                    input()

            elif vyber == 4:
                zadano = True
                pokracovat = False
                pass

        finally:
            print(spatne)

vypis.obrazovka_hla()
print("              KONEC - Nashledanou.\n--------------------------------------------\n")

