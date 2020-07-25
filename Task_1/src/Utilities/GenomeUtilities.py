import pandas as pd

class GenomeUtilities:

    @staticmethod
    def GenerateConstraintGraph(genome_DataFrame : pd.DataFrame) -> pd.DataFrame:
        pass
    
    @staticmethod
    def IsConflicted(region_1 : pd.DataFrame, region_2 : pd.DataFrame) -> bool:
        if (region_1.end < region_2.start):
            return False
        elif (region_1.start > region_2.end):
            return False
        else:
            return True