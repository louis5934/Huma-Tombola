import os
os.chdir(r"C:\Users\kimvy\Documents\Huma_CS\JDS")

import pandas as pd

def load_participants_cs():
    # Charger le fichier Excel
    df = pd.read_excel("particpants_jds_test.xlsx")
    # Ne garder que les lignes où la 3ème colonne vaut "CS" 
    df = df[df.iloc[:, 2].astype(str).str.strip().str.upper() == "CS"]
    # Transformer en dictionnaire en utilisant la première colonne comme clé
    participants_cs_dico = df.set_index(df.columns[0]).iloc[:, 0].to_dict()

    return participants_cs_dico


def load_participants_exte():
    # Charger le fichier Excel
    df = pd.read_excel("particpants_jds_test.xlsx")
    # Ne garder que les lignes où la 3ème colonne vaut "exte" 
    df = df[df.iloc[:, 2].astype(str).str.strip().str.upper() == "EXTE"] 
    # Transformer en dictionnaire en utilisant la première colonne comme clé
    participants_exte_dico = df.set_index(df.columns[0]).iloc[:, 0].to_dict()

    return participants_exte_dico


def load_lots():
    # Charger le fichier Excel
    df = pd.read_excel("lots_tombola_test.xlsx")

    # Transformer en liste
    lots = df["Lots"].tolist()

    return lots

