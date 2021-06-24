# READING A CSV FILE
"""Read a comma separated value (csv) file"""
import pandas as pd

CSVFILE = "thefile.csv"
df = pd.read_csv((CSVFILE), sep=";")
df.head()
