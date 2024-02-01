"""
This script contains a function to transform an OTU (Operational Taxonomic Unit) table to fit mdfs.
The function reads an input file, performs several transformations and then writes the transformed data to an output file.
"""

import pandas as pd
import sys

def transform_otu_table(input_file, output_file):
    otu_table_raw = pd.read_csv(input_file, sep='\t', skiprows=1)
    otu_table_renamed = otu_table_raw.rename(
        columns={'#OTU ID': 'OTU ID'}
    ).rename(
        columns=lambda x: x.replace('_bracken_species', '')
    )
    otu_table_renamed['taxonomy'] = otu_table_renamed[
        'taxonomy'
    ].str.split('; ').apply(lambda x: [i[3:] for i in x]).apply(
        lambda x: ",".join(x)
    )
    otu_table_transposed = otu_table_renamed.drop(
        'OTU ID', axis=1
    ).T
    last_row = otu_table_transposed.iloc[-1]
    otu_table_transposed = otu_table_transposed.drop(
        otu_table_transposed.index[-1]
    )
    otu_table_transposed.columns = last_row

    otu_table_transposed.to_csv(output_file, sep='\t')

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    transform_otu_table(input_file, output_file)
