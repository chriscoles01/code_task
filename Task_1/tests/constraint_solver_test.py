import sys
# to avoid editing your PYTHONPATH
sys.path.append("../src/")
from Utilities import  ConstraintSolver
import pandas as pd

# stochastic solution finder, therefore 4 possible ordered solutions
def test_get_solution():
    constraint_dict = {'start_x':[1,1,2,2], 'end_x':[3,3,4,4],
                                'index_x':[0,0,1,1], 'start_y':[1,2,1,2],
                                'end_y':[3,4,3,4], 'index_y':[0,1,0,1],
                                'constraint':[1,0,0,1]}
    constraint_df = pd.DataFrame(constraint_dict)
    order_df = constraint_df.groupby(['index_x'])['constraint'].sum().sort_values(ascending=False)
    expected_constraint_solution_1 = {1:1, 0:2}
    expected_constraint_solution_2 = {1:2, 0:1}
    expected_constraint_solution_3 = {0:2, 1:1}
    expected_constraint_solution_4 = {0:1, 1:2}
    actual_constraint_solution = ConstraintSolver.get_solution(order_df.index, constraint_df, 3)
    assert (actual_constraint_solution == expected_constraint_solution_1 
     or actual_constraint_solution ==expected_constraint_solution_2 
     or actual_constraint_solution ==expected_constraint_solution_3 
     or actual_constraint_solution ==expected_constraint_solution_4)

def test_generate_heuristic():
    constraint_dict = {'start_x':[1,1,2,2], 'end_x':[3,3,4,4],
                                'index_x':[0,0,1,1], 'start_y':[1,2,1,2],
                                'end_y':[3,4,3,4], 'index_y':[0,1,0,1],
                                'constraint':[1,0,0,1]}
    constraint_df = pd.DataFrame(constraint_dict)
    order_df = constraint_df.groupby(['index_x'])['constraint'].sum().sort_values(ascending=False)
    expected_heuristic_solution = {1: [1], 2: [0]}
    actual_heuristic_solution = ConstraintSolver.generate_heuristic(constraint_df, order_df)
    assert expected_heuristic_solution == actual_heuristic_solution