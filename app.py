import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
from Functions.DPP import DetectClean

dc = DetectClean()

data = pd.read_csv("./Data/AviationData.csv")


dc.find_to_clean(df=data, unique="Accident.Number")
