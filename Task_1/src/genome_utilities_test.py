
from Utilities import GenomeUtilities
import pandas as pd


def test_generate_constraint_graph():
    test_df = pd.DataFrame({'start': [1, 2], 'end': [3, 4]})
    expected_constraint_dict = {'start_x':[1,1,2,2], 'end_x':[3,3,4,4],
                                'index_x':[0,0,1,1], 'start_y':[1,2,1,2],
                                'end_y':[3,4,3,4], 'index_y':[0,1,0,1],
                                'constraint':[1,0,0,1]}
    expected_constraint_df = pd.DataFrame(expected_constraint_dict)
    actual_constraint_df = GenomeUtilities.generate_constraint_graph(test_df)
    assert expected_constraint_df.equals(actual_constraint_df)


def test_is_matched():
    expected_constraint_dict = {'start_x':[1,1,2,2], 'end_x':[3,3,4,4],
                                'index_x':[0,0,1,1], 'start_y':[1,2,1,2],
                                'end_y':[3,4,3,4], 'index_y':[0,1,0,1],
                                'constraint':[1,0,0,1]}
    expected_constraint_df = pd.DataFrame(expected_constraint_dict)

    row_same_index = expected_constraint_df.iloc[0]
    row_different_index = expected_constraint_df.iloc[1]
    actual_match_same = GenomeUtilities.is_matched(row_same_index)
    assert actual_match_same == 1
    actual_match_different = GenomeUtilities.is_matched(row_different_index)
    assert actual_match_different == 0