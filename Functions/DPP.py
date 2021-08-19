import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer


class Clean:
    def __init__(self, *, data=True, normalize=False, copy_X=True,
                 n_jobs=None, positive=False):
        self.data = data
        self.normalize = normalize
        self.copy_X = copy_X
        self.n_jobs = n_jobs
        self.positive = positive

    def heat(self):
        for col in self.columns:
            pct_missing = np.mean(self[col].isnull())
            null_val = '{} - {}%'.format(col, round(pct_missing*100))
            print(null_val)
