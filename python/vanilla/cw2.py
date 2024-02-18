#!/usr/bin/env python3
# cw1
import random
import requests as rq


def game():
    n = int(input("Zgadnij liczbę od 1 do 20: "))
    target = random.randint(1, 20)
    tries = 0
    while n != target:
        if n > target:
            print("Liczba jest za wysoka.")
        elif n < target:
            print("Liczba jest zbyt niska.")
        tries += 1
        n = int(input("Zgaduj dalej: "))
    print("Udało Ci się, ta liczba to", target)
    print("Zajęło Ci to", tries, "prób!\n")


game()


# cw2,3

uniprot_id = "Q9NR28"


def get_best_resolution(uniprot_id):
    response = rq.get(
        f"https://www.ebi.ac.uk/pdbe/graph-api/mappings/best_structures/{uniprot_id}"
    ).json()[uniprot_id]
    temp = {}
    for idx, r in enumerate(response):
        if r["resolution"] != None:
            temp[r["pdb_id"]] = r["resolution"], idx
    temp = sorted(temp.items(), key=lambda x: x[1])
    best_structure_idx = temp[0][1][1]
    best_structure = response[best_structure_idx]
    result = {
        best_structure["pdb_id"]: {
            "chain_id": best_structure["chain_id"],
            "unp_start": best_structure["unp_start"],
            "unp_end": best_structure["unp_end"],
        }
    }
    return result


best_structure = get_best_resolution(uniprot_id)
print(best_structure)

best_pdb_id = list(best_structure.keys())[0]


def get_molecule_data_from_pdbe(pdb_id):
    entities = rq.get(
        f"https://www.ebi.ac.uk/pdbe/api/pdb/entry/molecules/{pdb_id}"
    ).json()[pdb_id]
    for entity in entities:
        chain_id = get_best_resolution(uniprot_id)[pdb_id]["chain_id"]
        if (
            entity["molecule_type"] == "polypeptide(L)"
            and chain_id in entity["in_chains"]
        ):
            if entity is not None:
                print()
                return entity["sequence"][
                    int(
                        entity["source"][0]["mappings"][0]["start"]["residue_number"]
                        - 1
                    ): int(entity["source"][0]["mappings"][0]["end"]["residue_number"])
                ]


print(get_molecule_data_from_pdbe(best_pdb_id))
