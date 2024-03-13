import glob
import os

import click
import pandas as pd


def flatten_sum(matrix):
    return sum(matrix, [])


def combine_reports(*directory_paths):
    """
    Combine reports from multiple directories into a single DataFrame.
    It is important to remember that the file must be ended with /
    """
    for directory_path in directory_paths:
        if not os.path.isdir(directory_path):
            click.echo("Directory path does not exist: {}".format(directory_path))
            return
        else:
            click.echo("Directory path exists: {}".format(directory_path))
        files = glob.glob(directory_path + "*.TXT")

        # Print the contents of the 'files' list
        print("Files found: ", files)

        if not files:
            click.echo("No .TXT files found in: {}".format(directory_path))

        for file in files:
            base_name = os.path.splitext(os.path.basename(file))[0]
            print(base_name)

            # Read the file into a DataFrame
            df = pd.read_csv(file, sep="\t", skiprows=2, index_col=0)

            print(df)


if __name__ == "__main__":
    combine_reports()
