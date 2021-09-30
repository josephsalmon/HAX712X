import  pandas as pd
import numpy as np


def get_accident(df_bikes, log_scale=True):
  gd = df_bikes.groupby(['departement']).size()
  if log_scale:
    gd = np.log(gd)
  return gd
