
from Utilities import GenomeUtilities,GenomeParser, get_solution
from constraint import *
import pandas as pd


def main():

    original_regions = GenomeParser.ToGenomeDataFrame("./Data/Regions_Big.txt")
    constraints_dataframe = GenomeUtilities.GenerateConstraintGraphFast(original_regions)
    # constraints_dataframe = pd.read_csv('bigboi.csv', index_col=0)
    for_solver = constraints_dataframe.copy()

    order = constraints_dataframe.groupby(['index_x'])['constraint'].sum().sort_values(ascending=False)

    for_solver_order = order.copy()

    heuristic_solution = generate_heuristic(constraints_dataframe, order)

    print(heuristic_solution)


    final_solution = None
    i = max(list(heuristic_solution.keys()))

    final_solution = get_solution(for_solver_order.index, for_solver, i)

    write_solution('./Output/solution.txt', final_solution, original_regions)



def generate_heuristic(constraints_dataframe :pd.DataFrame, order_dataframe : pd.DataFrame):
    heuristic_solution={}
    count=0
    matches= False

    while order_dataframe.empty == False:
        if matches == False:
            count += 1
            heuristic_solution[count] = []

        constraints_dataframe, 
        order_dataframe, 
        matches, 
        heuristic_solution[count] = add_next_region_to_row(constraints_dataframe, 
                                                    order_dataframe, 
                                                    heuristic_solution[count])

    return heuristic_solution

def write_solution(path: string, final_solution:dict, original_regions:pd.DataFrame):
    original_regions['row'] = 0
    with open('solution.txt', 'a+') as the_file:
        for region,row in final_solution.items():
            region_start = original_regions.loc[region].start
            region_end = original_regions.loc[region].end
            original_regions.loc[region]['row'] = row
            the_file.write(str(row) + '\t' + str(region_start) + '\t' + str(region_end) +'\n') 



def add_next_region_to_row(df : pd.DataFrame, order : pd.DataFrame, existing:list):
    top_series = order.index[0]

    df_top_series = df[df.index_x == top_series]

    df_top_series = df_top_series[df_top_series.index_y != top_series]

    matches = False

    set_existing_check =set(df_top_series[df.index_y.isin(existing)].constraint.tolist())

    if  set_existing_check== {1} or set_existing_check==set():
        existing.append(top_series)
        matches = True
        order = order.drop(top_series)

    return df, order,matches,existing

if __name__ == "__main__":
    pass