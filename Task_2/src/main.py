from Utilities import GenomeParser
import pandas as pd
import sys

def main(path=None):
    if path == None:
        path = "../../Data/Regions_Big.txt"
    
    original_regions = GenomeParser.read_genome_dataframe(path)
    segment_dictionary = create_segment_dict(original_regions)
    segment_dictionary = add_count_to_segment_dict(segment_dictionary,
                                                   original_regions)
    segment_lines = create_segment_lines(segment_dictionary)
    write_solution_to_file('../Output/solution2.txt', segment_lines)


def create_segment_dict(original_regions: pd.DataFrame) -> pd.DataFrame:

    keys = original_regions.start.tolist()
    end_keys = original_regions.end.tolist()
    keys.extend(end_keys)
    segment_dictionary = dict.fromkeys(keys, 0)
    return segment_dictionary


def add_count_to_segment_dict(segment_dictionary: dict,
                              original_regions: pd.DataFrame) -> pd.DataFrame:

    for key in segment_dictionary.keys():
        matching_regions = original_regions[original_regions.start <= key][
            original_regions.end > key]

        segment_dictionary[key] = len(matching_regions.index)
    return segment_dictionary


def write_solution_to_file(path: str, lines: list):
    with open(path, 'w+') as solution_file:
        solution_file.writelines(lines)


def create_segment_lines(segment_dictionary: dict) -> list:
    lines = []
    sorted_keys = sorted(segment_dictionary)

    for i in range(len(sorted_keys) - 1):

        current_key = sorted_keys[i]
        next_key = sorted_keys[i + 1]
        current_value = segment_dictionary[current_key]
        next_value = segment_dictionary[next_key]

        if current_value != 0:
            if next_value == 0:
                # if there is a gap between segments
                lines.append(
                    str(current_value) + '\t' + str(current_key) + '\t' +
                    str(next_key) + '\n')
            else:
                # previous segment will end at start of next -1
                lines.append(
                    str(current_value) + '\t' + str(current_key) + '\t' +
                    str(next_key - 1) + '\n')
    return lines


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
