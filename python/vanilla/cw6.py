#!/usr/bin/env python3

# cw1
import re

pattern = "CC[GA][CT]GG"

sequence = "ATGCCACCGGAGTACCGCGGGCGTCCCGG"

matches = re.findall(pattern, sequence)
print(matches)


# cw2
def translate_codon(codon):
    codon_table = {
        "TTT": "F",
        "TTC": "F",
        "TTA": "L",
        "TTG": "L",
        "CTT": "L",
        "CTC": "L",
        "CTA": "L",
        "CTG": "L",
        "ATT": "I",
        "ATC": "I",
        "ATA": "I",
        "ATG": "M",
        "GTT": "V",
        "GTC": "V",
        "GTA": "V",
        "GTG": "V",
        "TCT": "S",
        "TCC": "S",
        "TCA": "S",
        "TCG": "S",
        "CCT": "P",
        "CCC": "P",
        "CCA": "P",
        "CCG": "P",
        "ACT": "T",
        "ACC": "T",
        "ACA": "T",
        "ACG": "T",
        "GCT": "A",
        "GCC": "A",
        "GCA": "A",
        "GCG": "A",
        "TAT": "Y",
        "TAC": "Y",
        "TAA": "*",
        "TAG": "*",
        "CAT": "H",
        "CAC": "H",
        "CAA": "Q",
        "CAG": "Q",
        "AAT": "N",
        "AAC": "N",
        "AAA": "K",
        "AAG": "K",
        "GAT": "D",
        "GAC": "D",
        "GAA": "E",
        "GAG": "E",
        "TGT": "C",
        "TGC": "C",
        "TGA": "*",
        "TGG": "W",
        "CGT": "R",
        "CGC": "R",
        "CGA": "R",
        "CGG": "R",
        "AGT": "S",
        "AGC": "S",
        "AGA": "R",
        "AGG": "R",
        "GGT": "G",
        "GGC": "G",
        "GGA": "G",
        "GGG": "G",
    }
    return codon_table.get(codon, "")


def find_orfs(dna_seq):
    orfs = []
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]

    for frame in range(3):
        frame_seq = dna_seq[frame:]

        # Find start codons
        start_positions = [m.start() for m in re.finditer(start_codon, frame_seq)]

        for start_pos in start_positions:
            for stop_codon in stop_codons:
                stop_pos = frame_seq.find(stop_codon, start_pos + 3)
                if stop_pos != -1 and (stop_pos - start_pos) % 3 == 0:
                    orf_seq = frame_seq[start_pos : stop_pos + 3]
                    orfs.append(orf_seq)

    return orfs


def reverse_complement(seq):
    complement = {"A": "T", "C": "G", "G": "C", "T": "A"}
    return "".join(complement[base] for base in reversed(seq))


def process_dna_sequence(dna_seq):
    forward_orfs = find_orfs(dna_seq)
    reverse_complement_seq = reverse_complement(dna_seq)
    reverse_orfs = find_orfs(reverse_complement_seq)

    all_orfs = forward_orfs + reverse_orfs
    translated_orfs = [
        (orf, "".join(translate_codon(orf[i : i + 3]) for i in range(0, len(orf), 3)))
        for orf in all_orfs
    ]

    return translated_orfs


dna_seq = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
result = process_dna_sequence(dna_seq)

for orf, translated_seq in result:
    print(f"ORF: {orf}, Translated: {translated_seq}")

# cw3
text = """Would to heaven that the reader, emboldened and momentarily ferocious as he reads,
finds his wild and savage path through the desolate marshes of these dark and poisonous pages,
without disorientation; for, unless he brings in his reading a rigorous logic and a tension of mind
equal at least to his distrust, the mortal emanations of this book will soak his soul, as water sugar.
It is not good for everybody to read the pages that follow; some alone will savor this bitter fruit without danger.
Therefore, timid soul, before penetrating farther into such unexplored heaths, directs your heels back and not forward.
Listen well to what I say to you: run your heels back and not forward, like the eyes of a son who,
deviates respectfully from the august contemplation of the maternal side;
or, rather, as an endless angle of chilly cranes of great meditation, which, during the winter,
flies powerfully through the silence, with all sails stretched, towards a fixed point of the horizon,
whence suddenly leaves a strange and strong wind, precursor of the storm.
""".replace(
    "\n", " "
)

m_words = re.findall(r"\bm\w*", text, re.IGNORECASE)

preceding_and = re.findall(r"\b\w*\s*and", text, re.IGNORECASE)

seven_chars = re.findall(r"\b[^fF\s]\w{6}\b", text)

ing_words = re.findall(r"\b\w{1,4}ing\b", text, re.IGNORECASE)

print(m_words, preceding_and, seven_chars, ing_words, sep="\n")
