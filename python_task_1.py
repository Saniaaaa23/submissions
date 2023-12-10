#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np


# In[7]:


cardata = pd.read_csv(r"C:\Users\sania\Downloads\dataset-1.csv")


# In[8]:


cardata.head()


# # Question 1: Car Matrix Generation

# In[11]:


def generate_car_matrix(df):
    matrix_df = df.pivot(index='id_1', columns='id_2', values='car')
    matrix_df = matrix_df.fillna(0)
    for index in matrix_df.index:
        if index in matrix_df.columns:
            matrix_df.at[index, index] = 0
    return matrix_df
result_matrix = generate_car_matrix(df)
print(result_matrix)


# # Question 2: Car Type Count Calculation

# In[14]:


def get_type_count(df):
    conditions = [
        (df['car'] <= 15),
        (df['car'] > 15) & (df['car'] <= 25),
        (df['car'] > 25)
    ]
    choices = ['low', 'medium', 'high']
    df['car_type'] = np.select(conditions, choices, default='unknown')
    type_counts = df['car_type'].value_counts().to_dict()
    type_counts = dict(sorted(type_counts.items()))
    return type_counts
result_type_count = get_type_count(df)
print(result_type_count)


# # Question 3: Bus Count Index Retrieval

# In[15]:


def get_bus_indexes(df):
    bus_mean = df['bus'].mean()
    bus_indexes = df[df['bus'] > 2 * bus_mean].index.tolist()
    bus_indexes.sort()
    return bus_indexes
result_bus_indexes = get_bus_indexes(df)
print(result_bus_indexes)


# # Question 4: Route Filtering

# In[16]:


def filter_routes(df):
    route_avg_truck = df.groupby('route')['truck'].mean()
    selected_routes = route_avg_truck[route_avg_truck > 7].index.tolist()
    selected_routes.sort()
    return selected_routes
result_filtered_routes = filter_routes(df)
print(result_filtered_routes)


# # Question 5: Matrix Value Modification

# In[20]:


def multiply_matrix(result_matrix):
    modified_matrix = result_matrix.copy()
    modified_matrix = modified_matrix.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)
    modified_matrix = modified_matrix.round(1)
    return modified_matrix
result_multiplied_matrix = multiply_matrix(result_matrix)
print(result_multiplied_matrix)


# # Question 6: Time Check

# In[21]:


df1 = pd.read_csv(r"C:\Users\sania\Downloads\dataset-2.csv")


# In[22]:


df1.head()

