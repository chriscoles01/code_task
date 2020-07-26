from constraint import *
import pandas as pd


def GetSolution(genome_index:pd.Index, genome_constraints:pd.DataFrame, i:int) -> dict:
    solutions = {}
    while solutions is not None:

        problem = Problem(MinConflictsSolver())
        problem.addVariables(list(genome_index), range(1,i))

        unmatched_regions = genome_constraints[genome_constraints.constraint == 0]
        # todo extract to method
        unmatched_regions.apply(lambda row: problem.addConstraint(lambda row1, row2: row1 != row2, (row['index_x'], row['index_y'])),axis=1)

        print("before solution")
        solutions = problem.getSolution()
        print("after solution", i-1)

        if solutions is not None:
            i -=1
            final_solution = solutions

    return final_solution
