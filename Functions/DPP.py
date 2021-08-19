import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer


class DetectClean:
    def __init__(self):
        print("placeholder")

    def find_to_clean(self, df, unique):
        int_col = []  # Contains integer data type columns
        cate_col = []  # Contains object data type columns
        int_missing = []  # Contains columns with missing data
        outliers = []  # Contains outlier unique keys
        low_information_cols = []  # Contains a list of all the columns with >95% of same data
        datatypes = dict(df.dtypes)
        num_rows = len(df.index)

        # This for-loop separates the columns into object and not object list for better manipulation
        for col in df.columns:
            if datatypes[col] == 'O':
                cate_col.append(col)
            else:
                int_col.append(col)

        # This for loop finds the int type columns with missing values
        for col in int_col:
            pct_missing = np.mean(df[col].isnull())
            if round(pct_missing*100) > 0:
                int_missing.append(col)

        # This loop is to finds all the outlier unique keys so we can delete them later
        for col in int_col:
            lower_lim = round(df[col].mean()-3*df[col].std())
            upper_lim = round(df[col].mean()+3*df[col].std())

            del_dict = dict(df[(df[col] > upper_lim) | (
                df[col] < lower_lim)][unique])

            for i in del_dict:
                if i not in outliers:
                    outliers.append(del_dict[i])

        # This loop finds all the columns with a lot of same type of data and if it more than 95% gives option to remove it
        for col in df.columns:
            cnts = df[col].value_counts(dropna=False)
            top_pct = (cnts/num_rows).iloc[0]

            if top_pct > 0.95:
                low_information_cols.append(col)
                print('{0}: {1:.5f}%'.format(col, top_pct*100))
                print(cnts)
                keep = input("Do you want to keep this feature Y/N :")
                if keep == 'Y' | keep == 'y':
                    low_information_cols.remove(col)

    def to_clean():
        if missing == True:
            for i in missing_lables:
                if:
        if categorical == True:
            for i in categorical_lables:
                if:
        if irregular == True:
            for i in irregularl_lables:
                if:
        if unnecessary == True:
            for i in unnecessary_lables:
                if:
