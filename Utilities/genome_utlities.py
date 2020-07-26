import pandas as pd
import time
class GenomeUtilities:

    @staticmethod
    def GenerateConstraintGraph(genome_DataFrame : pd.DataFrame) -> pd.DataFrame:
        conflict_DataFrame = pd.DataFrame(index=genome_DataFrame.index, columns=genome_DataFrame.index)
        for region_id_1 in genome_DataFrame.index:
            # conflict_DataFrame[region_id_1] = genome_DataFrame.apply(lambda row: GenomeUtilities.IsConflicted(row, genome_DataFrame.loc[region_id_1]), axis=1)
            for region_id_2 in genome_DataFrame.index:
                region_1 = genome_DataFrame.loc[region_id_1]
                region_2 = genome_DataFrame.loc[region_id_2]
                
                compatible = GenomeUtilities.IsConflicted(region_1, region_2)

                conflict_DataFrame[region_id_1][region_id_2] = compatible
        conflict_DataFrame.to_csv('bigboi.csv')
        return conflict_DataFrame

    @staticmethod   
    def IsConflicted(region_1 : pd.Series, region_2 : pd.DataFrame) -> int:
        if region_1.name == region_2.name:
            return 1
        if (region_1['end'] < region_2.start):
            return 1
        elif (region_1['start'] > region_2.end):
            return 1
        else:
            return 0

    @staticmethod
    def GenerateConstraintGraphFast(genome_DataFrame : pd.DataFrame) -> pd.DataFrame:
        left = genome_DataFrame
        right = genome_DataFrame.copy()
        left['index'] = left.index
        right['index'] = right.index
        merged = left.assign(key=1).merge(right.assign(key=1), on='key').drop('key', 1)
        
        # conflict_DataFrame = pd.DataFrame(index=genome_DataFrame.index, columns=genome_DataFrame.index)
        start = time.perf_counter()
        print("started")
        # merged.apply(lambda row: GenomeUtilities.CheckConstraint(row, conflict_DataFrame), axis=1)
        merged['constraint'] = merged.apply(lambda row: GenomeUtilities.CheckConstraintOld(row), axis=1)
        print("ended")
        end = time.perf_counter()
        print(end-start)
        merged.to_csv('bigboi.csv')
        return merged

    @staticmethod
    def CheckConstraintOld(row):
        if row.index_x == row.index_y:
            return 1
        if (row.end_x < row.start_y):
            return 1
        elif (row.start_x > row.end_y):
           return 1
        else:
           return 0

    @staticmethod
    def CheckConstraint(row, conflict_DataFrame):
        if (row.end_x < row.start_y):
            conflict_DataFrame.loc[row.index_x, row.index_y] = 1
        elif (row.start_x > row.end_y):
           conflict_DataFrame.loc[row.index_x, row.index_y] = 1
        else:
           conflict_DataFrame.loc[row.index_x, row.index_y] = 0