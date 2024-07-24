import pandas as pd

# Creating 2 sample dataframes
data1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
                      'value1': [1, 2, 3, 4, 5, 6, 7]})
data2 = pd.DataFrame({'key': ['C', 'D', 'E', 'F', 'G', 'H'],
                      'value2': [8, 9, 10, 11, 12, 13]})

print(data1)
print(data2)

# Inner Join = Common keys of the two data frames
merge_inner_join = pd.merge(data1, data2, on='key', how='inner')
print("\n", merge_inner_join)

# Left Join = All the values in the left table and the common values of right as well
merge_left_join = pd.merge(data1, data2, on='key', how='left')
print("\n", merge_left_join)

# Right Join = All the values in the right table and the common values of left as well
merge_right_join = pd.merge(data1, data2, on='key', how='right')
print("\n", merge_right_join)

# Left Anti Join = Only the unique values of left table
merge_left = pd.merge(data1, data2, on='key', how='left', indicator = True)
merge_left_anti_join = merge_left[merge_left['_merge'] == 'left_only']
merge_left_anti_join = merge_left_anti_join.drop('_merge', axis=1)
print("\n", merge_left_anti_join)