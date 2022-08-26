class Vypis:

    @staticmethod
    def vypis_menu():
        return "--------------------------------------------\n" \
               "              Evidence pojištěnců\n" \
               "--------------------------------------------\n"

    @staticmethod
    def vyber_akci():
        return "Vyberte si akci:\n" \
               "1  -  Přidat nového pojistného\n" \
               "2  -  Vypsat všechny pojištěné\n" \
               "3  -  Vyhledat pojištěného\n" \
               "4  -  Konec\n"

    @staticmethod
    def _vycisti_obrazovku():
        import sys as _sys
        import subprocess as _subprocess
        if _sys.platform.startswith("win"):
            _subprocess.call(["cmd.exe", "/C", "cls"])
        else:
            _subprocess.call(["clear"])

    @staticmethod
    def obrazovka_hla_cela():
        vypis._vycisti_obrazovku()
        print(vypis.vypis_menu())
        print(vypis.vyber_akci())

    @staticmethod
    def obrazovka_hla():
        vypis._vycisti_obrazovku()
        print(vypis.vypis_menu())


vypis = Vypis()
