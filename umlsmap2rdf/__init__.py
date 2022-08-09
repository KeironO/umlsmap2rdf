
import click
from . import mrconsordf

@click.command()
@click.option('--input_fp', help='The File Path of MRCONSO.RRF', required=True)
@click.option('--output_fp', help='Number of greetings.', required=True)          
def cli(input_fp, output_fp):
    """
--    _   _ __  __ _     ____    __  __    _    ____  ____ ___ _   _  ____ 
--   | | | |  \/  | |   / ___|  |  \/  |  / \  |  _ \|  _ \_ _| \ | |/ ___|
--   | | | | |\/| | |   \___ \  | |\/| | / _ \ | |_) | |_) | ||  \| | |  _ 
--   | |_| | |  | | |___ ___) | | |  | |/ ___ \|  __/|  __/| || |\  | |_| |
--    \___/|_|  |_|_____|____/  |_|  |_/_/   \_\_|   |_|  |___|_| \_|\____|
--                  
    

This python scripts collates the Unified Medical Language System (UMLS) maps into RDF/OWL files.

If you have any issues, feel free to submit a bug report at: https://github.com/KeironO/umlsmap2rdf

    Thanks!    
    """
    conv = mrconsordf.MRCCONSORDF(input_fp, output_fp)
    conv.do()
    

if __name__ == '__main__':
    cli()