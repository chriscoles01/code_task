import pandas as pd

class GenomeParser:
    
    @staticmethod
    def ToGenomeDataFrame(path : str) -> pd.DataFrame:
        genome_DataFrame = pd.read_csv(path, sep='\t', names=['start','end'])
        return genome_DataFrame

