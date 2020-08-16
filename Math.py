import seaborn as sb 
import pandas as pd


for x in range(3):
  print("hello")

u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
y = pd.read_csv("http://files.grouplens.org/datasets/movielens/ml-100k/u.user", 
    sep='|', names=u_cols)

