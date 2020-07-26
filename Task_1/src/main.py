from Utilities import GenomeUtilities, GenomeParser, ConstraintSolver
from constraint import *
import pandas as pd


def write_solution(path: str, final_solution: dict,
                   original_regions: pd.DataFrame):
    original_regions['row'] = 0
    with open(path, 'w+') as the_file:
        for region, row in final_solution.items():
            region_start = original_regions.loc[region].start
            region_end = original_regions.loc[region].end
            original_regions.loc[region]['row'] = row
            the_file.write(
                str(row) + '\t' + str(region_start) + '\t' + str(region_end) +
                '\n')


def main():

    original_regions = GenomeParser.read_genome_dataframe(
        "../../Data/Regions_Big.txt")

    constraints_dataframe = GenomeUtilities.generate_constraint_graph(
        original_regions)

    order = constraints_dataframe.groupby(
        ['index_x'])['constraint'].sum().sort_values(ascending=False)

    for_solver = constraints_dataframe.copy()

    for_solver_order = order.copy()

    heuristic_solution = ConstraintSolver.generate_heuristic(
        constraints_dataframe, order)

    final_solution = None

    i = max(list(heuristic_solution.keys()))

    final_solution = ConstraintSolver.get_solution(for_solver_order.index,
                                                   for_solver, i)

    write_solution('../Output/solution.txt', final_solution, original_regions)


if __name__ == "__main__":
    main()
