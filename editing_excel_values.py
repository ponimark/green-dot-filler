import pandas as pd
import numpy as np
d={"name" :['harry', 'rohan', 'skillf', 'shubh'],
   "marks":[92, 34, 24, 17],
   "city":['rampur', 'kolkata', 'bariely', 'antartica']}
df=pd.DataFrame(d)

r=pd.read_csv('test.csv')
r['marks'][0] = 45  #will change marks at 0 indexing
#print(r['marks'])   # will print only marks column
r.to_csv('test.csv', index=False)