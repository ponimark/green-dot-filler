import pandas as pd
import numpy as np
d={"name" :['harry', 'rohan', 'skillf', 'shubh'],
   "marks":[92, 34, 24, 17],
   "city":['rampur', 'kolkata', 'bariely', 'antartica']}
df=pd.DataFrame(d)

r=pd.read_csv('test.csv') #,index_col=0 if don't want indexing while reading
r.index=['first', 'second', 'third', 'fourth']  # will change indexing to this
print(r)