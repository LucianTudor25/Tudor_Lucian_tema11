"""Modul cu validarile datelor introduse de la tastatura.

Tine si contorul global de erori: dupa 10 date gresite,
programul afiseaza mesaj de eroare si se opreste.
"""

import sys

LIMITA_ERORI = 10

# Contor global pentru datele gresite introduse de la tastatura
erori = 0


def inregistreaza_eroare(mesaj):
    """Afiseaza mesajul de eroare, incrementeaza contorul global
    si opreste programul daca s-a atins limita de erori."""
    global erori
    erori += 1
    print(f"  ! {mesaj} (eroare {erori}/{LIMITA_ERORI})")
    if erori >= LIMITA_ERORI:
        print(
            "\nEROARE FORMAT DATE: "
            "ati introdus 10 date gresite. Program oprit."
        )
        sys.exit(1)


def cere_text(eticheta):
    """Cere un text nevid (nume/prenume).

    Returneaza textul introdus sau None la eroare.
    """
    valoare = input(f"  {eticheta}: ").strip()
    if valoare == "" or any(caracter.isdigit() for caracter in valoare):
        inregistreaza_eroare(
            f"{eticheta} invalid: nu poate fi gol sau cu cifre."
        )
        return None
    return valoare


def cere_intreg(eticheta, minim, maxim=None):
    """Cere un numar intreg intre minim si maxim.

    Returneaza numarul (int) sau None la eroare.
    """
    text = input(f"  {eticheta}: ").strip()
    if not text.isdigit():
        inregistreaza_eroare(
            f"{eticheta} invalid: trebuie sa fie numar intreg."
        )
        return None
    numar = int(text)
    if numar < minim or (maxim is not None and numar > maxim):
        if maxim is None:
            limite = f"minim {minim}"
        else:
            limite = f"intre {minim} si {maxim}"
        inregistreaza_eroare(f"{eticheta} invalid: trebuie sa fie {limite}.")
        return None
    return numar
