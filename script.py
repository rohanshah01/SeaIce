import pandas as pd
import numpy as np
import matplotlib as plt
from os import *

df = pd.read_csv("data.csv")
print df.boxplot(column="Y1996")