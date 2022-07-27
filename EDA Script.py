#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)


# In[ ]:


def eda (path):
  if 'csv' in path :
    path=pd.read_csv(path)
  elif 'xls' in path :
    data=pd.read_excel(path)
  
  else :
    print("invalid extenstion")


  #cleaning data
  type(path)

  path.head()

  path.info()

  path.tail()

  shape_of_data=path.shape

  print(shape_of_data)
  #rows
  name_of_rows=path.index
  print(list(name_of_rows))
  #columns
  name_of_colums =path.columns  
  display(name_of_colums)
  #null
  check_null= path.isnull()  

  display(check_null)

  path.isnull().sum()
  for check_null in name_of_colums:

    if check_null ==0:

      print(path.drop(check_null, inplace =True, axis =1))

    else:
      ("every thing it's ok")

  path[check_null] = path[check_null].fillna('data completed')
  check_duplicated=path.duplicated()

  display(check_duplicated)

  path.describe()

  for i in name_of_colums:

    display(i.lower())
#visualize_data
  for col in path.columns :

    print(col)

    path[col].hist()

  plt.figure(figsize = (30,15))

  for index,col in enumerate(path.columns):

    plt.subplot(1,3,index+1)

    path[col].hist()

  plt.figure(figsize = (30,15))

  for index,col in enumerate(path.columns):

    plt.subplot(1,3,index+1)

    path[col].hist()


  data_numerical=[]

  data_cat=[]

  for col in path.columns :

    if path[col].dtype == np.int64 or path[col].dtype == np.int32 or path[col].dtype == np.float64 or path[col].dtype == np.float32 :

      data_numerical.append(col)

    else :

      data_cat.append(col)  

  plt.figure(figsize = (30,15))

  for index,col in enumerate(data_numerical):

    plt.subplot(1,3,index+1)

    path[col].hist()

  plt.figure(figsize = (30,15))

  for index,col in enumerate(data_cat):

    plt.subplot(1,3,index+1)

    path[col].hist()

  plt.figure(figsize = (30,15))

  fig, axes = plt.subplots(2, 2)

  for index,col in enumerate(data_numerical):

    sns.histplot(data=path,x=col,ax=axes[0,index])

  plt.figure(figsize = (30,15))

  fig, axes = plt.subplots(2, 2)

  for index,col in enumerate(data_cat):

    sns.histplot(data=path,x=col,ax=axes[0,index])

  print(data_numerical)

  print(data_cat)

script_eda= eda()  

display(eda)
  

