'''
This script is made to run bracken and create empty file if the abundance of the given phyla is 0.
'''

import subprocess
from sys import argv


try:
    cmd = "python3 /path/to/est_abundance.py -i {input} -k {kmer_distrib} -l S -t 10 -o {output_bracken} --out-report {output_bracken_species}".format(
        input = argv[1],
        kmer_distrib = argv[2],
        output_bracken = argv[3],
        output_bracken_species = argv[4]
    )
    subprocess.run(cmd.split())
    
except Exception as e:
    print(e)
