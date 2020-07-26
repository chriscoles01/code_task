
from genome_utlities import GenomeUtilities
from genome_parser import GenomeParser
from constraint import *
import pandas as pd
import time


def main():
    pass

original_regions = GenomeParser.ToGenomeDataFrame("./Data/Regions_Big.txt")
cons = GenomeUtilities.GenerateConstraintGraphFast(original_regions)
# cons = pd.read_csv('bigboi.csv', index_col=0)
for_solver = cons.copy()
order = cons.groupby(['index_x'])['constraint'].sum().sort_values(ascending=False)
for_solver_order = order.copy()
levels={}
count = 0

start = time.perf_counter()
matches= False
while order.empty == False:
    if matches == False:
        count += 1
        levels[count] = []

    cons, order, matches, levels[count] = get_next_faster(cons,order,levels[count])


end = time.perf_counter()
print(end-start)
print(levels)


final_solution = None
i = max(list(levels.keys()))
while True:
    problem = Problem(MinConflictsSolver())
    problem.addVariables(list(for_solver_order.index), range(1,i))

    for_solver[for_solver.constraint == 0].apply(lambda row: problem.addConstraint(lambda row1, row2: row1 != row2, (row['index_x'], row['index_y'])),axis=1)

    print("before solution")
    solutions = problem.getSolution()
    print("after solution", i-1)

    if solutions is not None:
        i -=1
        final_solution = solutions
    if solutions == None:
        break
original_regions['row'] = 0


print(final_solution)
if final_solution is not None:
    with open('solution.txt', 'a+') as the_file:
        for region,row in final_solution.items():
            region_start = original_regions.loc[region].start
            region_end = original_regions.loc[region].end
            original_regions.loc[region]['row'] = row
            the_file.write(str(row) + '\t' + str(region_start) + '\t' + str(region_end) +'\n') 



def get_next_faster(df, order, existing):
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