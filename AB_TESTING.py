

import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro, levene, ttest_ind
import seaborn as sns



pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

dataframe_control = pd.read_excel("hafta3(Measurement Problems)/ABTesti/ab_testing.xlsx", sheet_name="Control Group")
dataframe_test = pd.read_excel("hafta3(Measurement Problems)/ABTesti/ab_testing.xlsx", sheet_name="Test Group")

df_control = dataframe_control.copy()
df_test = dataframe_test.copy()



def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head())
    print("##################### Tail #####################")
    print(dataframe.tail())
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

check_df(df_control)

check_df(df_test)


df_control["group"] = "control"
df_test["group"] = "test"


df = pd.concat([df_control,df_test], axis=0,ignore_index=False)
df.head()
df.shape

df.groupby("group").agg({"Purchase": "mean"})




df.groupby("group").agg({"Purchase": "mean"})





test_stat, pvalue = shapiro(df.loc[df["group"] == "control", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))



test_stat, pvalue = shapiro(df.loc[df["group"] == "test", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))


def create_displot(dataframe, col):
    sns.displot(data=dataframe, x=col, kde=True)
    plt.show()

create_displot(df_control, "Purchase")

df_control["Purchase"].mean()


test_stat, pvalue = shapiro(df.loc[df["group"] == "test", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))


# To observe the distribution of both:

for group in list(df["group"].unique()):
    pvalue = shapiro(df.loc[df["group"] == group, "Purchase"])[1] #shapironun 1. indexteki degeri
    print(group,'p-value = %.4f' % pvalue)


# Variance Homogeneity :
test_stat, pvalue = levene(df.loc[df["group"] == "control", "Purchase"],
                           df.loc[df["group"] == "test", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))





test_stat, pvalue = ttest_ind(df.loc[df["group"] == "control", "Purchase"],
                              df.loc[df["group"] == "test", "Purchase"],
                              equal_var=True)

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

