#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import mlflow
import torch
import torch.nn as nn


x_train = pd.read_csv(r'train_set_features.csv')
print(x_train.head())
# %%
