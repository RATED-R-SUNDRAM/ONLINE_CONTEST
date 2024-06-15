#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import mlflow
import torch
import torch.nn as nn

#%%
print(os.getcwd())
x_train = pd.read_csv(r'training_set_features.csv')
y_train = pd.read_csv(r'training_set_labels.csv')
# %%
print(y_train.head())
print(x_train.head())
# %%
