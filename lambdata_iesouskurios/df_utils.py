"""
Utility functions for working with dataframes

"""

import pandas as pd

# Check a dataframe for nulls, print/report them in a nice "pretty" format


def get_info(dataframe):
    print(dataframe.shape)
    print (dataframe.isna().sum())

#searches for text all throughout data frame and returns row index
def find_text(string, dataframe):
    for col in dataframe:
        for row in dataframe:
            for value in row:
                if value == string:
                    return value.iloc