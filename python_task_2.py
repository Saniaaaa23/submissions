#!/usr/bin/env python
# coding: utf-8

# # Question 1: Distance Matrix Calculation

# In[2]:


import pandas as pd
df = pd.read_csv(r"C:\Users\sania\Downloads\dataset-3.csv")


# In[10]:


df.head()


# In[11]:


def calculate_distance_matrix(df):
    matrix_df = df.pivot(index='id_start', columns='id_end', values='distance')
    matrix_df = matrix_df.fillna(0)
    for index in matrix_df.index:
        if index in matrix_df.columns:
            matrix_df.at[index, index] = 0
    return matrix_df
result_matrix = calculate_distance_matrix(df)
print(result_matrix)


# # Question 2: Unroll Distance Matrix

# In[12]:


def unroll_distance_matrix(distance_matrix):
    id_start_values = distance_matrix.index.tolist()
    id_end_values = distance_matrix.columns.tolist()
    unrolled_data = []
    for id_start in id_start_values:
        for id_end in id_end_values:
            if id_start != id_end:
                unrolled_data.append({
                    'id_start': id_start,
                    'id_end': id_end,
                    'distance': distance_matrix.at[id_start, id_end]
                })
    unrolled_df = pd.DataFrame(unrolled_data)
    return unrolled_df
unrolled_df = unroll_distance_matrix(distance_matrix)
print(unrolled_df)


# # Question 3: Finding IDs within Percentage Threshold

# In[13]:


def find_ids_within_ten_percentage_threshold(df, reference_value):
    reference_df = df[df['id_start'] == reference_value]
    avg_distance = reference_df['distance'].mean()
    threshold_range = 0.1 * avg_distance
    within_threshold_ids = df[
        (df['id_start'] != reference_value) & 
        (df['distance'] >= avg_distance - threshold_range) &
        (df['distance'] <= avg_distance + threshold_range)
    ]['id_start'].unique()
    within_threshold_ids = sorted(within_threshold_ids)
    return within_threshold_ids
reference_value = 801
result_ids = find_ids_within_ten_percentage_threshold(unrolled_df, reference_value)
print(result_ids)


# # Question 4: Calculate Toll Rate

# In[14]:


def calculate_toll_rate(df):
    df['moto'] = 0.8 * df['distance']
    df['car'] = 1.2 * df['distance']
    df['rv'] = 1.5 * df['distance']
    df['bus'] = 2.2 * df['distance']
    df['truck'] = 3.6 * df['distance']
    return df
result_df = calculate_toll_rate(unrolled_df)
print(result_df)


# # Question 5: Calculate Time-Based Toll Rates

# In[ ]:





# In[ ]:




