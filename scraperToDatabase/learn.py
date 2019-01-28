from sqlalchemy import create_engine
import pandas as pd

# Read file into a DataFrame and print its head
df = pd.read_csv('khaadi.csv')
print(df.head())
