import fastf1
import pandas as pd
from sqlalchemy import create_engine

fastf1.Cache.enable_cache('C:/Users/samee/Desktop/Python/f1_cache')#enable caching

session=fastf1.get_session(2024,8,'R')#2024,8 is the race number and R is the race session
session.load()#load the session data

laps=session.laps[["Driver","LapNumber","LapTime","Sector1Time","Sector2Time","Sector3Time"]].copy()#copy the data
laps.dropna(inplace=True)#drop the na values
laps.reset_index(drop=True, inplace=True)#reset the index

laps["LapNumber"]=laps["LapNumber"].astype(int)
for col in ["LapTime","Sector1Time","Sector2Time","Sector3Time"]:
    laps[f"{col}"]=laps[col].dt.total_seconds()

print(laps.head())


db_url = f"postgresql+psycopg2://aiuser:aipassword@localhost:5432/analytics_db"
engine = create_engine(db_url)

laps.to_sql('f1_monaco_laps', con=engine, if_exists='replace', index=False)
print("Data saved to database")

