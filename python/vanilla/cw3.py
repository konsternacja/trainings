# cw1
table_data = """
UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G
"""

ordered = sum([i.split() for i in table_data.split("\n")[1:-1]], [])
codon_dict = {ordered[i]: ordered[i + 1] for i in range(0, len(ordered), 2)}

# cw2
bo_tak = [
    [j + 1 if j % 2 == 0 else 69 for j in range(4)] if i % 2 != 0 else 420
    for i in range(4)
]

# cw3
hamming = lambda a, b: sum(1 for i, e in enumerate(a) if e != b[i])


# cw4
def translator(seq, codon_dict=codon_dict):
    for i in range(0, len(seq), 3):
        codon = seq[i : i + 3]
        yield codon_dict[str(codon)]


translator_generator = translator("AUGGGGUUAAUA")

print(next(translator_generator))
print(next(translator_generator))

# cw5
lista1 = [x ** (1 / 2) for x in range(0, 21) if x % 2 != 0]
lista2 = list(map(lambda x: x ** (1 / 2) if x % 2 != 0 else None, range(0, 21)))
lista2 = list(filter(lambda x: x is not None, lista2))
