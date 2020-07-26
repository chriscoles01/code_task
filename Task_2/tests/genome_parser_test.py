import sys
# to avoid editing your PYTHONPATH
sys.path.append("../src/")
from Utilities import  GenomeParser
import pandas as pd


def test_read_genome_dataframe(tmpdir):
    test_df = pd.DataFrame({'start': [1, 2], 'end': [3, 4]})
    test_file = tmpdir / 'test_genome.csv'
    test_df.to_csv(test_file, sep='\t', header=False, index=False)

    genome_parser_df = GenomeParser.read_genome_dataframe(test_file)

    assert test_df.equals(genome_parser_df)

