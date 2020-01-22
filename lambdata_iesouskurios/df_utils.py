"""
Utility functions for working with dataframes

"""

import pandas as pd

# change the path to df to where your datafile is stored

df = pd.read_excel('~/unit3/repos/iesous-kurios/lambdata/90Day.xlsx')

NO_NULL_DF = df.isna()