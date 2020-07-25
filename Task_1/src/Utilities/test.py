from genome_utlities import GenomeUtilities
from genome_parser import GenomeParser
from constraint import *
def get_next(df):
    df = df.drop(df.index[0],axis=1)

    top_series = df.iloc[0]
    df = df.drop(df.index[0])
    matches = [region for region in top_series.index if top_series[region] == 1]
    return df, matches

    
df = GenomeParser.ToGenomeDataFrame("./Data/Regions_Small.txt")
cons = GenomeUtilities.GenerateConstraintGraph(df)

cons['total']  = cons.apply(lambda row : sum(row), axis=1)
cons = cons.sort_values(by=['total'], ascending=False)
print(cons)
cons = cons.drop('total', axis=1)
problem_dataset = cons.copy()
levels={}
count = 0
matching_regions = []
while cons.empty == False:
    if matching_regions == []:
        count += 1
        levels[count] = []
    levels[count].append(cons.index[0])
    cons, matching_regions = get_next(cons)
    

print(levels)

problem = Problem()
problem.addVariables(list(problem_dataset.index), range(1, max(list(levels.keys())) +1))

for index, row in problem_dataset.iterrows():
    for i in problem_dataset.index:
        if(row[i] == 0):
            problem.addConstraint(lambda row1, row2: row1 != row2, (index, i))

solutions = problem.getSolution()
print(solutions)
