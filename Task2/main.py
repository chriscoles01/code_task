



original_regions = GenomeParser.ToGenomeDataFrame("./Data/Regions_Big.txt")




keys = original_regions.start.tolist()
end_keys = original_regions.end.tolist()
keys.extend(end_keys)
segment_dictionary = dict.fromkeys(keys, 0)

for key in segment_dictionary.keys():
    matching_regions = original_regions[original_regions.start <= key][original_regions.end > key]
    
    segment_dictionary[key] = len(matching_regions.index)

sorted_keys = sorted(segment_dictionary)
with open('solution2.txt', 'a+') as the_file:
    for i in range(len(sorted_keys)-1):
        current_key =sorted_keys[i]
        next_key = sorted_keys[i+1]
        current_value = segment_dictionary[current_key]
        next_value = segment_dictionary[next_key]
        if current_value != 0:
            if next_value == 0:
                the_file.write(str(current_value) + '\t' + str(current_key) + '\t' + str(next_key) +'\n')
            else:
                 the_file.write(str(current_value) + '\t' + str(current_key) + '\t' + str(next_key -1 ) +'\n')
print(segment_dictionary)


if __name__ == "__main__":
    pass