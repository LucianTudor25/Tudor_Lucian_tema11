"""Modul cu operatiile pe fisierul CSV: listare, adaugare, stergere.

Fisierul angajati.csv se afla in folderul radacina al proiectului
(acelasi folder cu main.py) si are header-ul:
Nume familie, Prenume, nr contract, nivel skill.
"""

import csv
import os

from module.validari import inregistreaza_eroare, cere_text, cere_intreg

# Calea fisierului CSV = folderul radacina al proiectului
# (folderul parinte al pachetului gestiune)
FOLDER_PROIECT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)
CALE_CSV = os.path.join(FOLDER_PROIECT, "angajati.csv")

HEADER = ["Nume familie", "Prenume", "nr contract", "nivel skill"]


def fisier_exista():
    """Verifica existenta fisierului CSV. Daca lipseste, afiseaza eroare."""
    if not os.path.isfile(CALE_CSV):
        print(f"  ! EROARE: fisierul nu exista la locatia: {CALE_CSV}")
        return False
    return True


def citeste_angajati():
    """Citeste randurile din CSV (fara header), ca lista."""
    with open(CALE_CSV, "r", newline="", encoding="utf-8") as f:
        cititor = csv.reader(f)
        next(cititor, None)  # sarim peste header
        return [rand for rand in cititor if rand]


def listare():
    """Afiseaza angajatii din fisierul CSV sub forma de tabel."""
    if not fisier_exista():
        return
    angajati = citeste_angajati()
    if not angajati:
        print("  Fisierul nu contine niciun angajat.")
        return
    print(
        f"\n  {'Nume familie':<15}{'Prenume':<15}"
        f"{'Nr contract':<13}{'Nivel skill':<11}"
    )
    print("  " + "-" * 54)
    for rand in angajati:
        print(f"  {rand[0]:<15}{rand[1]:<15}{rand[2]:<13}{rand[3]:<11}")
    print(f"  Total: {len(angajati)} angajati.")


def adaugare():
    """Cere datele unui angajat, le valideaza si le adauga in CSV."""
    if not fisier_exista():
        return

    nume = cere_text("Nume familie")
    if nume is None:
        return
    prenume = cere_text("Prenume")
    if prenume is None:
        return
    nr_contract = cere_intreg("Nr contract (numar intreg de la 1)", 1)
    if nr_contract is None:
        return

    # Nr contract trebuie sa fie unic in fisier
    # (set cu contractele existente)
    existente = {rand[2] for rand in citeste_angajati()}
    if str(nr_contract) in existente:
        inregistreaza_eroare(
            f"Nr contract {nr_contract} exista deja in fisier."
        )
        return

    nivel_skill = cere_intreg("Nivel skill (0-6)", 0, 6)
    if nivel_skill is None:
        return

    with open(CALE_CSV, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([nume, prenume, nr_contract, nivel_skill])
    print(f"  Angajatul {nume} {prenume} a fost adaugat.")


def stergere():
    """Sterge un angajat din CSV dupa nr contract, rescriind fisierul."""
    if not fisier_exista():
        return

    nr_contract = cere_intreg("Nr contract de sters", 1)
    if nr_contract is None:
        return

    angajati = citeste_angajati()
    ramasi = [rand for rand in angajati if rand[2] != str(nr_contract)]

    if len(ramasi) == len(angajati):
        inregistreaza_eroare(
            f"Nr contract {nr_contract} nu a fost gasit in fisier."
        )
        return

    with open(CALE_CSV, "w", newline="", encoding="utf-8") as f:
        scriitor = csv.writer(f)
        scriitor.writerow(HEADER)
        scriitor.writerows(ramasi)
    print(f"  Angajatul cu nr contract {nr_contract} a fost sters.")
