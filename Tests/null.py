from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from candis import spell
from DPP import DetectClean

df = pd.read_csv('Data/train.csv')

b = DetectClean()
b.find_to_clean(df=df, unique='PassengerId')

# return_dict = dict()
# return_dict['intiger_columns'] = ['PassengerId',
#                                   'Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
# return_dict['category_columns'] = [
#     'Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']
# return_dict['missing_value_columns'] = ['Age']
# return_dict['outlier_list'] = [631, 852, 60, 72, 160, 181, 202, 325, 387, 481, 684, 793, 847, 864, 14, 26, 168, 361, 439,
#                                568, 611, 639, 679, 886, 28, 89, 119, 259, 300, 312, 342, 378, 381, 439, 528, 558, 690, 701, 717, 731, 738, 743, 780],
# return_dict['low_info_columns'] = ['Age']
# return_dict['drop_list'] = ['Age']

# for i in return_dict:
#     print(i)

# unique = 'PassengerId'
# drop_list = []
# for col in df.columns:
#     if col = unique:
#         print(df[col].head(5))
#         chs = input("Do you want to keep this column "+col+" :")
#         if chs == 'Y' or chs == 'y':
#             continue
#         else:
#             drop_list.append(col)

# print(drop_list)

# return_dict = dict()
# return_dict['intiger_columns'] = ['PassengerId',
#                                   'Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
# return_dict['category_columns'] = [
#     'Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']
# return_dict['missing_value_columns'] = ['Age']
# return_dict['outlier_list'] = [631, 852, 60, 72, 160, 181, 202, 325, 387, 481, 684, 793, 847, 864, 14, 26, 168, 361, 439,
#                                568, 611, 639, 679, 886, 28, 89, 119, 259, 300, 312, 342, 378, 381, 439, 528, 558, 690, 701, 717, 731, 738, 743, 780],
# return_dict['low_info_columns'] = ['Age']
# return_dict['drop_list'] = ['Age']

# for i in return_dict['drop_list']:
#     if i == 'Age':
#         return_dict[i].remove(i)


# {
#  'intiger_columns': ['PassengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare'],
#  'category_columns': ['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'],
#  'missing_value_columns': ['Age'],
#  'outlier_list': [631, 852, 60, 72, 160, 181, 202, 325, 387, 481, 684, 793, 847, 864, 14, 26, 168, 361, 439, 568, 611, 639, 679, 886, 28, 89, 119, 259, 300, 312, 342, 378, 381, 439, 528, 558, 690, 701, 717, 731, 738, 743, 780],
#  'low_info_columns': []
# }

# num_rows = len(df.index)
# low_information_cols = []

# for col in df.columns:
#     cnts = df[col].value_counts(dropna=False)
#     top_pct = (cnts/num_rows).iloc[0]

#     if top_pct > 0.65:
#         low_information_cols.append(col)
#         print('{0}: {1:.5f}%'.format(col, top_pct*100))
#         print(cnts)
#         keep = input("Do you want to keep this feature Y/N :")
#         if keep == 'Y' or keep == 'y':
#             low_information_cols.remove(col)

# print(low_information_cols)
# print(df['Age'].mean())
# lower_lim = round(df['Age'].mean()-3*df['Age'].std())
# upper_lim = round(df['Age'].mean()+3*df['Age'].std())

# del_dict = dict(df[(df['Age'] > upper_lim) | (
#     df['Age'] < lower_lim)]['PassengerId'])
# mango = []
# for i in del_dict:
#     if i not in mango:
#         mango.append(del_dict[i])
# print(mango)

# int_col = []
# cate_col = []
# datatypes = dict(df.dtypes)
# for col in df.columns:
#     if datatypes[col] == 'O':
#         cate_col.append(col)
#     else:
#         int_col.append(col)

# print(int_col)
# print(cate_col)

# a = []
# for col in df.columns:
#     pct_missing = np.mean(df[col].isnull())
#     if round(pct_missing*100) > 0:
#         a.append(col)

# print(a)
