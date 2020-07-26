from constraint import Problem, MinConflictsSolver
import pandas as pd


class ConstraintSolver:
    @staticmethod
    def get_solution(genome_index: pd.Index, genome_constraints: pd.DataFrame,
                     i: int) -> dict:
        solutions = {}
        final_solution = {}

        while solutions is not None:

            problem = Problem(MinConflictsSolver())
            problem.addVariables(list(genome_index), range(1, i))

            unmatched_regions = genome_constraints[
                genome_constraints.constraint == 0]
            # todo extract to method
            unmatched_regions.apply(lambda row: problem.addConstraint(
                lambda row1, row2: row1 != row2,
                (row['index_x'], row['index_y'])),
                                    axis=1)

            print("generating a solution for", i - 1, "groups")
            solutions = problem.getSolution()

            if solutions is not None:
                print("solution found for", i - 1, "groups")
                i -= 1
                final_solution = solutions
            else:
                print("no solution for", i - 1,
                      "groups, therefore optimal solution is", i, "groups")
        return final_solution

    @staticmethod
    def generate_heuristic(constraints_dataframe: pd.DataFrame,
                           order_dataframe: pd.DataFrame):
        print("generating heuristic...")
        heuristic_solution = {}
        count = 0
        matches = False

        while order_dataframe.empty == False:
            if matches == False:
                count += 1
                heuristic_solution[count] = []

            constraints_dataframe, order_dataframe, matches, heuristic_solution[
                count] = ConstraintSolver._add_next_region_to_row(
                    constraints_dataframe, order_dataframe,
                    heuristic_solution[count])
        print("generated heuristic solution with",
              len(heuristic_solution.keys()), "groups")
        return heuristic_solution

    @staticmethod
    def _add_next_region_to_row(df: pd.DataFrame, order: pd.DataFrame,
                                existing: list):
        top_series = order.index[0]

        df_top_series = df[df.index_x == top_series]

        df_top_series = df_top_series[df_top_series.index_y != top_series]

        matches = False

        df_existing = df_top_series[df.index_y.isin(existing)]

        set_existing_check = set(df_existing.constraint.tolist())

        if set_existing_check == {1} or set_existing_check == set():
            existing.append(top_series)
            matches = True
            order = order.drop(top_series)

        return df, order, matches, existing
