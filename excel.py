import pandas as pd
import numpy as np
d={"name" :['harry', 'rohan', 'skillf', 'shubh'],
   "marks":[92, 34, 24, 17],
   "city":['rampur', 'kolkata', 'bariely', 'antartica']}
df=pd.DataFrame(d)
df.to_csv('test.csv',index=False)  #if index not needed index is serial numbers