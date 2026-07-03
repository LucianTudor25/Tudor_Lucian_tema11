"""Program de gestiune a angajatilor intr-un fisier CSV - punct de intrare.

Optiuni: listare, adaugare, stergere, iesire.
Dupa 10 date gresite introduse de la tastatura, programul se opreste.
"""

from module.operatii import listare, adaugare, stergere
from module1git.validari import inregistreaza_eroare


def meniu():
    """Bucla principala: afiseaza meniul si executa optiunea aleasa."""
    while True:
        print("\n===== GESTIUNE ANGAJATI =====")
        print("  1. Listare")
        print("  2. Adaugare")
        print("  3. Stergere")
        print("  4. Iesire")
        optiune = input("Alegeti optiunea (1-4): ").strip()

        if optiune == "1":
            listare()
        elif optiune == "2":
            adaugare()
        elif optiune == "3":
            stergere()
        elif optiune == "4":
            print("La revedere!")
            break
        else:
            inregistreaza_eroare("Optiune invalida: alegeti 1, 2, 3 sau 4.")


if __name__ == "__main__":
    meniu()
