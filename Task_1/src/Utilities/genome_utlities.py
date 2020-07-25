import pandas as pd

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
        
        return conflict_DataFrame

    @staticmethod   
    def IsConflicted(region_1 : pd.Series, region_2 : pd.DataFrame) -> int:
        if region_1.equals(region_2):
            return 1
        if (region_1['end'] < region_2.start):
            return 0
        elif (region_1['start'] > region_2.end):
            return 0
        else:
            return 1