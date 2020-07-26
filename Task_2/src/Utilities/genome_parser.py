import pandas as pd


class GenomeParser:
    @staticmethod
    def read_genome_dataframe(path: str) -> pd.DataFrame:
        genome_DataFrame = pd.read_csv(path, sep='\t', names=['start', 'end'])
        return genome_DataFrame
