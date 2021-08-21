import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer


class DetectClean:
    def __init__(self):
        print("placeholder")

    def find_to_clean(df, unique):
        int_col = []  # Contains integer data type columns
        cate_col = []  # Contains object data type columns
        int_missing = []  # Contains columns with missing data
        outliers = []  # Contains outlier unique keys
        low_information_cols = []  # Contains a list of all the columns with >95% of same data
        drop_list = []  # Contains list of all the columns that need to be dropped form the database
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
        return_dict = dict()
        return_dict['intiger_columns'] = int_col
        return_dict['category_columns'] = cate_col
        return_dict['missing_value_columns'] = int_missing
        return_dict['outlier_list'] = outliers
        return_dict['low_info_columns'] = low_information_cols
        return return_dict

    def now_clean(df, Drop_data=False, drop_list=None, int_columns=None, cat_columns=None):
        if Drop_data:
            for i in drop_list:
                df.drop(i)
                if i in int_columns:
                    int_columns.remove(i)
                else:
                    cat_columns.remove(i)
