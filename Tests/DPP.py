import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer


class DetectClean:

    def __init__(self, df=None, int_col=[], cate_col=[], int_missing=[], outliers=[], low_information_cols=[], drop_list=[]):

        self.df = df

        self.int_col = int_col  # Contains integer data type columns

        self.cate_col = cate_col  # Contains object data type columns

        self.int_missing = int_missing  # Contains columns with missing data

        self.outliers = outliers  # Contains outlier unique keys

        # Contains a list of all the columns with >95% of same data
        self.low_information_cols = low_information_cols

        # Contains list of all the columns that need to be dropped form the database
        self.drop_list = drop_list

    def find_to_clean(self, df, unique):
        self.df = df
        datatypes = dict(df.dtypes)
        num_rows = len(df.index)

        # This for-loop separates the columns into object and not object list for better manipulation
        for col in self.df.columns:
            if datatypes[col] == 'O':
                self.cate_col.append(col)
            else:
                self.int_col.append(col)

        # This for loop finds the int type columns with missing values
        for col in self.int_col:
            pct_missing = np.mean(self.df[col].isnull())
            if round(pct_missing*100) > 0:
                self.int_missing.append(col)

        # This loop is to finds all the outlier unique keys so we can delete them later
        for col in self.int_col:
            lower_lim = round(self.df[col].mean()-3*self.df[col].std())
            upper_lim = round(self.df[col].mean()+3*self.df[col].std())

            del_dict = dict(self.df[(self.df[col] > upper_lim) | (
                self.df[col] < lower_lim)][unique])

            for i in del_dict:
                if i not in self.outliers:
                    self.outliers.append(del_dict[i])

        # This loop finds all the columns with a lot of same type of data and if it more than 95% gives option to remove it
        for col in self.df.columns:
            cnts = self.df[col].value_counts(dropna=False)
            top_pct = (cnts/num_rows).iloc[0]

            if top_pct > 0.95:
                self.low_information_cols.append(col)
                print('{0}: {1:.5f}%'.format(col, top_pct*100))
                print(cnts)
                keep = input("Do you want to keep this feature Y/N :")
                if keep == 'Y' | keep == 'y':
                    self.low_information_cols.remove(col)

        # This loop is to go through all the columns and drop make a list of all the to be dropped once
        for col in self.df.columns:
            if col != unique:
                print(self.df[col].head(5))
                chs = input("Do you want to keep this column "+col+" :")
                if chs == 'Y' or chs == 'y':
                    continue
                else:
                    self.drop_list.append(col)

        # return_dict = dict()
        # return_dict['intiger_columns'] = int_col
        # return_dict['category_columns'] = cate_col
        # return_dict['missing_value_columns'] = int_missing
        # return_dict['outlier_list'] = outliers
        # return_dict['low_info_columns'] = low_information_cols
        # return_dict['drop_list'] = drop_list
        # return return_dict

    def now_clean(self):

        # Here we remove the columns that are not required
        if self.Drop_data:
            self.df = self.df.drop(columns=self.drop_list)
            for i in self.drop_status:
                if i in self.int_col:
                    self.int_col.remove(i)
                if i in self.cate_col:
                    self.cate_col.remove(i)
                if i in self.int_missing:
                    self.int_missing.remove(i)
                if i in self.low_information_cols:
                    self.low_information_cols.remove(i)
        if self.outlier_status:
            self.df = self.df.drop(self.outlier_list, axis=0)
