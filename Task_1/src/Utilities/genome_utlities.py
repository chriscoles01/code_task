import pandas as pd
import time
class GenomeUtilities:

    @staticmethod
    def generate_constraint_graph(genome_DataFrame : pd.DataFrame) -> pd.DataFrame:
        print("Generating constraint graph")

        left = genome_DataFrame
        right = genome_DataFrame.copy()
        left['index'] = left.index
        right['index'] = right.index
        merged = left.assign(key=1).merge(right.assign(key=1), on='key').drop('key', 1)
        
        merged['constraint'] = merged.apply(lambda row: GenomeUtilities.is_matched(row), axis=1)

        return merged

    @staticmethod
    def is_matched(row) -> int:
        if row.index_x == row.index_y:
            return 1
        if (row.end_x < row.start_y):
            return 1
        elif (row.start_x > row.end_y):
           return 1
        else:
           return 0

