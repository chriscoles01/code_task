import pandas as pd

class GenomeParser:
    
    @staticmethod
    def ToGenomeDataFrame(path : str):
        genome_DataFrame = pd.read_csv(path, sep='\t', names=['start','end'])
        return genome_DataFrame

