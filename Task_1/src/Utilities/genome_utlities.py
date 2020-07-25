import pandas as pd

class GenomeUtilities:

    @staticmethod
    def GenerateConstraintGraph(genome_DataFrame : pd.DataFrame) -> pd.DataFrame:
        conflict_DataFrame = pd.DataFrame(index=genome_DataFrame.index, columns=genome_DataFrame.index)
        for region_id_1 in genome_DataFrame.index:
            for region_id_2 in genome_DataFrame.index:
                compatible = 1
                if region_id_1 != region_id_2:
                    region_1 = genome_DataFrame.loc[genome_DataFrame.index == region_id_1]
                    region_2 = genome_DataFrame.loc[genome_DataFrame.index == region_id_1]
                    
                    if GenomeUtilities.IsConflicted(region_1, region_2):
                        compatible = 0    

                conflict_DataFrame[region_id_1][region_id_2] = compatible
        
        return conflict_DataFrame

    @staticmethod   
    def IsConflicted(region_1 : pd.DataFrame, region_2 : pd.DataFrame) -> bool:
        if (region_1.end < region_2.start):
            return False
        elif (region_1.start > region_2.end):
            return False
        else:
            return True