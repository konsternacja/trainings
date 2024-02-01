# cw1
def fasta_reader(fasta_file):
    seqs = open(fasta_file, 'r').read()
    seqs = seqs.split('\n')[:-1]

    fasta = {}
    for line in seqs:
        if line.startswith('>'):
            sequence_name = line.lstrip('>').split()[0]
        else:
            fasta[sequence_name] = fasta.get(sequence_name, '')\
                + line if sequence_name else None
    new_fasta = {key: len(value) for key, value in fasta.items()}
    return new_fasta


print(fasta_reader('data.fasta'))

# cw2


def bin2dec(nhood_list):
    return sum([b * 2**(2 - i) for i, b in enumerate(nhood_list)])


rule_table = {7: 0, 6: 1, 5: 1, 4: 0, 3: 1, 2: 1, 1: 1, 0: 0}

WIDTH, HEIGHT = 100, 100

grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

grid[0][WIDTH//2] = 1

for i in range(HEIGHT - 1):
    for j in range(1, WIDTH - 1):
        neighborhood = grid[i][j-1:j+2]
        decimal_val = bin2dec(neighborhood)
        grid[i+1][j] = rule_table[decimal_val]


with open("automat_komorkowy.ppm", "w") as ppm_file:
    ppm_file.write(f"P3\n{WIDTH} {HEIGHT}\n1\n")

    for row in grid:
        for val in row:
            ppm_file.write(f"{val} 0 0\n")


# cw3
def fasta_reader2(fasta_file):
    seqs = open(fasta_file, 'r').read()
    seqs = seqs.split('\n')[:-1]

    fasta = {}
    error_ids = []
    for line in seqs:
        try:
            if line.startswith('>'):
                sequence_name = line.lstrip('>').split()[0]
            else:
                sequence = fasta.get(sequence_name, {'A': 0, 'C': 0, 'T': 0, 'G': 0})
                for base in ['A', 'C', 'T', 'G']:
                    sequence[base] += line.count(base)
                fasta[sequence_name] = sequence
        except Exception as e:
            error_ids.append(sequence_name)

    # Write error IDs to a new file
    with open('error_ids.txt', 'w') as f:
        for id in error_ids:
            f.write(f"{id}\n")

    return fasta


print(fasta_reader2('data.fasta'))
