import pandas as pd
import numpy as np
d={"name" :['harry', 'rohan', 'skillf', 'shubh'],
   "marks":[92, 34, 24, 17],
   "city":['rampur', 'kolkata', 'bariely', 'antartica']}
df=pd.DataFrame(d)
#df.head(2)  # will show top 2 rows
#df.tail(2)  # will show bottom 2 rows
df.describe()  # some normal statistical functions only inculdes numeric values
#print(df)
#print(df.head())
#print(df.tail())
print(df.describe())
