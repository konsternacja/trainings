"""
This script contains a function to transform an OTU (Operational Taxonomic Unit) table to fit Funguild.
The function reads an input file, performs several transformations including renaming columns,
prefixing OTU IDs, and removing spaces from the taxonomy column, and then writes the transformed data to an output file.
"""

import pandas as pd
import sys


def transform_otu_table(input_file, output_file):
    otu_table_raw = pd.read_csv(input_file, sep='\t', skiprows=1)
    otu_table_renamed = otu_table_raw.rename(
        columns={'#OTU ID': 'OTU ID'}
    )
    otu_table_renamed['OTU ID'] = otu_table_renamed[
        'OTU ID'
    ].apply(
        lambda x: 'OTU_' + str(x) if not str(x).startswith('OTU_') else str(x))
    otu_table_renamed['taxonomy'] = otu_table_renamed[
        'taxonomy'
    ].str.replace(' ', '')
    otu_table_renamed.to_csv(output_file, sep='\t', index=False)


if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    transform_otu_table(input_file, output_file)
