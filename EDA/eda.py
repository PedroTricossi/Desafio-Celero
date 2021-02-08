import os
import pandas as pd
import numpy as np

reviews_train = []
for line in open('../aclImdb_v1/aclImdb/movie_data/full_train.txt', 'r'):
    reviews_train.append(line.strip())

reviews_test = []
for line in open('../aclImdb_v1/aclImdb/movie_data/full_test.txt', 'r'):
    reviews_test.append(line.strip())

df_train = pd.DataFrame(reviews_train, columns=['Text'])
df_test = pd.DataFrame(reviews_test, columns=['Text'])
