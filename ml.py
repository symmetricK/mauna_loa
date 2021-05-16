##This file contains functions that plots mauna_loa carbon dioxide data

import pandas as pd
import matplotlib.pyplot as plt
def get_df(filename):
    '''
    INPUT:filename e.g. mauna_loa.csv
    OUTPUT: Pandas Dataframe
    '''
    dataframe = pd.read_csv(filename)
    return dataframe

def plot_df(df):
    '''
    INPUT: Pandas DataFrame
    OUTPUT: handle to plot axis
    '''
    df_plot=plt.plot(df[0],df[1])
    return df_plot
    