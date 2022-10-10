import numpy as np
import pandas as pd

import os
# -------------------------------

mynumarr = np.random.rand(4)

type(mynumarr)

myseries = pd.Series(mynumarr, index=["First","Second","Third","Fourth"])

myseries["Fourth"]

my2darr = np.random.rand(3,2)

myframes=pd.DataFrame(my2darr)

myframes.columns=["First","Second"]

myframes["Second"]

############################

CSV_PATH= os.path.join("D:\Downloads\Programming\Python\Pandas Fundamental PluralSight\pandas-fundamentals\demos\collection-master","artwork_data.csv")

df = pd.read_csv(CSV_PATH,nrows=5)

df = pd.read_csv(CSV_PATH,nrows=5,index_col='id')

df = pd.read_csv(CSV_PATH, nrows=5, index_col='id',usecols=['id','artist'])

COLS_TO_USE = ['id','artist','title','medium','year','acquisitionYear','height','width','units']

df = pd.read_csv(CSV_PATH, nrows=5, index_col='id',usecols=COLS_TO_USE)

df.to_pickle(os.path.join("D:\Downloads\Programming\Python\Pandas Fundamental PluralSight\pandas-fundamentals\demos\collection-master",'data_frame.pickle'))
