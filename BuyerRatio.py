from scipy import stats as stats
import pandas as pd
df = pd.read_csv("D:\\DS\\books\\ASSIGNMENTS\\Hypothesis testing\\BuyerRatio.csv")
df
df.shape
df.head()

df1 = df.iloc[:,1:6]
df1

df1.values

# pip install researchpy
import researchpy as rp

val = stats.chi2_contingency(df1)
val

rows = len(df1.iloc[0:2,0])
columns = len(df1.iloc[0,0:4])
dff=(rows-1)*(columns-1)
print('Degree of Freedom=',dff)

Expected_value = val[dff]

from scipy.stats import chi2

chi_square = sum([(o-e)**2/e for o,e in zip(df1.values,Expected_value)])
chi_square_statestic = chi_square[0]+chi_square[1]
chi_square_statestic

chi_ = chi2.ppf(q = 0.95, df = 3)
chi_.round(4)

pvalue=1-chi2.cdf(chi_square_statestic,3)
pvalue

alpha = 0.05

if 0.6787 < alpha:
    print("Ho is Rejected and H1 is Accepted")
else:
    print("Ho is Accepted and H1 is Rejected")

# CONCLUSION
"""
There for the All proportions are equal and they are independent.
"""







