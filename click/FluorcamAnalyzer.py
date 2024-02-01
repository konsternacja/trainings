import click
from fc_read import combine_reports


@click.command()
@click.option("--version", "-v", is_flag=True, help="Show version")
@click.option("--help", "-h", is_flag=True, help="Show help")
@click.argument("file_paths", nargs=-1, type=click.Path(exists=True))
def main(version, help, file_paths):
    """Main script."""
    if version:
        click.echo("Fluorcam Analyzer Version 1.0")
    elif help:
        click.echo(
            "Usage: FluorcamAnalyzer.py [OPTIONS] FILE_PATH1\
            FILE_PATH2 FILE_PATH3..."
        )
    else:
        click.echo(f"Running main script with files: {', '.join(file_paths)}")
        # Wywołanie funkcji z drugiego pliku
        combine_reports(*file_paths)


if __name__ == "__main__":
    main()
