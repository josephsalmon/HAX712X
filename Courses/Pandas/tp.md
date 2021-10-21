
# Pandas
This lecture is extracted and adapted from the work by Joris Van den Bossche
<https://github.com/jorisvandenbossche/pandas-tutorial/blob/master/01-pandas_introduction.ipynb>

For R users, you might also want to read <https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_r.html> for a smooth start.

## Introduction

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ipywidgets import interact  # widget manipulation
from ipywidgets import widgets, interact, interactive, fixed, interact_manual

from download import download  # download data / avoid re-downloading
from IPython import get_ipython

pd.options.display.max_rows = 8
```

### Dataset 1: Titanic dataset

First, it is important to download automatically remote files for reproducibility (and avoiding typing manually names, )
```python
url = "http://josephsalmon.eu/enseignement/datasets/titanic.csv"
path_target = "./titanic.csv"
download(url, path_target, replace=False)  # if needed `pip install download`
```

Reading the file as a `pandas` dataframe:

```python
df_titanic_raw = pd.read_csv("titanic.csv")
```

Visualize the end of the dataset:
```python
df_titanic_raw.tail(n=3)
```

Visualize the beginning of the dataset:

```python
df_titanic_raw.head(n=5)
```



## Missing values
It is common to encounter features/covariates with missing values.
In `pandas` they were mostly handled as `np.nan` (not a number).
In the future, they will be treated as `NA` (note available), in a similar way as in R; see for standard behavior and details <https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html>.

Note that the main difference between `pd.NA` and `np.nan` is that `pd.NA` propagates even for comparisons:

```python
pd.NA == 1
>>><A>
```
whereas
```python
np.nan == 1
>>>False
```

Testing the presence of missing values
```python
pd.isna(pd.NA)
>>> True
pd.isna(np.nan)
>>> True
```

The simplest strategy (when you can / when you have enough samples) consists in removing all nans/NAs.


```python
df_titanic = df_titanic_raw.dropna()
df_titanic.tail(3)
```

```python
# Useful info on the dataset (especially missing values!)
df_titanic.info()
```

```python
# Check that cabin is mostly missing, also the age
df_titanic_raw.info()
```

### Description of the `titanic.csv` dataset
More details can be found here: <https://biostat.app.vumc.org/wiki/pub/Main/DataSets/titanic3info.txt>

- `Survived`: 	 Survival 	0 = No, 1 = Yes
- `Pclass`: 	 Ticket class 	1 = 1st, 2 = 2nd, 3 = 3rd
- `Sex`: 	     Sex male/female
- `Age`: 	     Age in years
- `Sibsp`: 	     # of siblings / spouses aboard the Titanic
- `Parch`: 	     # of parents / children aboard the Titanic
- `Ticket`: 	 Ticket number
- `Fare`: 	     Passenger fare
- `Cabin`: 	     Cabin number
- `Embarked`:    Port of Embarkation C = Cherbourg, Q = Queenstown, S = Southampton
- `Name`:        Name of the passenger
- `PassengerId`: Number to identify passenger

Note: an extended version of the dataset is available here for those interested <https://biostat.app.vumc.org/wiki/pub/Main/DataSets/titanic.txt>.


## Simple descriptive statistics
```python
df_titanic.describe()
```

## Visualization

- Histograms (please avoid...often useless)
    ```python
    plt.figure(figsize=(5, 5))
    plt.hist(df_titanic['Age'], density=True, bins=25)
    plt.xlabel('Age')
    plt.ylabel('Proportion')
    plt.title("Passager age histogram")
    ```

- Kernel Density Estimate (KDE):  :

    ```python
    plt.figure(figsize=(5, 5), num='jfpwje')
    # KDE: kernel density estimate
    ax = sns.kdeplot(df_titanic['Age'], shade=True, cut=0, bw=0.1)  # bw: bandwith
    plt.xlabel('Proportion')
    plt.ylabel('Age')
    ax.legend().set_visible(False)
    plt.title("Passager age kernel density estimate")
    plt.tight_layout()
    ```

- Swarmplot:
    ```python
    plt.figure(figsize=(10, 5), num='jfpwje')
    # Swarmplot from seaborn package
    ax = sns.swarmplot(data=df_titanic_raw, x='Sex', y='Age', hue='Survived',
                    palette={0: 'r', 1: 'k'}, order=['female', 'male'])
    plt.title("Passager age by gender/survival")
    plt.legend()
    plt.tight_layout()
    ```


## <font color='red'> EXERCISE : density over histogram </font>.
Plot the density estimate over the histogram


## Widgets
Interactive interaction with codes and output is nowdays easier and easier (see also Shiny app in R-software).
In python one can use for that `widgets` and the `interact` package.
We are going to visualize that on the simple KDE and histograms examples.


```python
def hist_explore(
    dataset=df_titanic,
    variable=df_titanic.columns,
    n_bins=24,
    alpha=0.25,
    density=False,
):
    fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    ax.hist(
        dataset[variable], density=density, bins=n_bins, alpha=alpha
    )  # standardization
    plt.ylabel("Density level")
    plt.title(f"Dataset {dataset.attrs['name']}:\n Histogram for passengers' age")
    plt.tight_layout()
    plt.show()


interact(
    hist_explore,
    dataset=fixed(df_titanic),
    n_bins=(1, 50, 1),
    alpha=(0, 1, 0.1),
    density=False,
)
```


```python
def kde_explore(dataset=df_titanic, variable=df_titanic.columns, bw=5):
    fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    sns.kdeplot(dataset[variable], bw_adjust=bw, shade=True, cut=0, ax=ax)
    plt.ylabel("Density level")
    plt.title(f"Dataset {dataset.attrs['name']}:\n KDE for passengers'  {variable}")
    plt.tight_layout()
    plt.show()

interact(kde_explore, dataset=fixed(df_titanic), bw=(0.001, 2, 0.01))

```

## `Groupby` function
How does the survival rate change w.r.t. to sex?

```python
df_titanic_raw.groupby('Sex')[['Survived']].aggregate(lambda x: x.mean())
```

How does the survival rate change w.r.t. the class?


```python
df_titanic.columns
```


```python
plt.figure()
df_titanic.groupby('Pclass')['Survived'].aggregate(lambda x:
                                                   x.mean()).plot(kind='bar')
plt.xlabel('Classe')
plt.ylabel('Taux de survie')
plt.title('Taux de survie par classe')
plt.show()
```



## <font color='red'> EXERCISE : median by class </font>
# Perform a similar analysis with the median for the price per class in pounds.

```python

```

## Catplot: a visual groupby

```python
sns.catplot(x='Pclass', y="Age",
            hue="Sex", data=df_titanic_raw, kind="swarm", legend=False)
plt.title("Age par classe")
plt.legend(loc=1)
plt.tight_layout()
```

Beware: large difference in sex ratio by class

```python
df_titanic_raw.groupby(['Sex', 'Pclass'])[['Sex']].count()
df_titanic_raw.groupby(['Sex'])[['Sex']].count()
```

More on groupby pandas-kungfu: cf. also pd.crosstab, etc. <https://pbpython.com/groupby-agg.html>

### pd.crosstab?

```python
pd.crosstab(df_titanic_raw['Sex'],
            df_titanic_raw['Pclass'],
            values=df_titanic_raw['Sex'],
            aggfunc='count',
            normalize=False)
```


```python
df_titanic
```

```python
df_titanic.index
```

```python
df_titanic.columns
```

```python
pd.options.display.max_rows = 12
df_titanic.dtypes

df_titanic['Name'].astype(str)
```


# Extract numpy array from dataframe
useful for using packages on top of `pandas` (e.g., sklearn, though nowadays it works out of the box with `pandas`)

```python
array_titanic = df_titanic.values  # associated numpy array
array_titanic
```

### <font color='red'> EXERCISE : dropna</font>
Perform the following operation: remove the columns Cabin from the raw
dataset, and then remove the rows with missing age.
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html


```python
# XXX TODO
```


# 1D dataset : Series (a column of a DataFrame)

A Series is a labelled 1D column of a kind.

```python
fare = df_titanic['Fare']
fare
```


## Attributes *Series*: indices and values

```python
fare.values[:10]
```

Contrarily to *numpy* arrays, you can index with other thing that integers:

```python
df_titanic_raw = df_titanic_raw.set_index('Name')  # you can only do it once !!
df_titanic_raw
```

```python
age = df_titanic_raw['Age']
age['Behr, Mr. Karl Howell']
```

```python
age.mean()
```

```python
df_titanic_raw[age < 2]
```

```
df_titanic_raw = df_titanic_raw.reset_index()  # come back to original index
```


# Counting values for categorical variables

```python
df_titanic_raw['Embarked'].value_counts(normalize=False, sort=True,
                                        ascending=False)
```

```python
pd.options.display.max_rows = 70
df_titanic[df_titanic['Embarked'] == 'C']
```
Comments: not all passagers from Cherbourg are  Gallic...


```python
pd.options.display.max_rows = 8
df_titanic_raw['Survived'].sum() / df_titanic_raw['Survived'].count()
```


```python
df_titanic['Survived'].mean()
```

**Q:What was the proportion of women on the boat?**


# See also the command:
```python
df_titanic_raw.groupby(['Sex']).mean()
```

# Data import et export

 Pandas supports many formats:
 - CSV, text
 - SQL database
 - Excel
 - HDF5
 - json
 - html
 - pickle
 - sas, stata
 - ...

```python
pd.read_csv?
# http://josephsalmon.eu/enseignement/datasets/babies23.data
pd.read_csv('babies23.data', skiprows=38, sep='\s+')
# pd.read_csv?
```
# Exploration

```python
df_titanic_raw.tail()
```

```python
df_titanic_raw.head()
```

# Pandas pairs well with seaborn:
```python
sns.set_palette("colorblind")
sns.catplot(x='Pclass', y='Age', hue='Survived', data=df_titanic_raw,
            kind="violin")
```


# Access values by line/columns etc.

- `iloc`
df_titanic_raw.iloc[0:2, 1:8]

- `loc`

```python
# with original index:
# df_titanic_raw.loc[128]

# with naming indexing
df_titanic_raw.loc['Bonnell, Miss. Elizabeth', 'Fare']


```python
df_titanic_raw.loc['Bonnell, Miss. Elizabeth']
```

```python
df_titanic_raw.loc['Bonnell, Miss. Elizabeth', 'Survived']
df_titanic_raw.loc['Bonnell, Miss. Elizabeth', 'Survived'] = 0
```

```python
df_titanic_raw.loc['Bonnell, Miss. Elizabeth']
```

```python
# set back the original value
df_titanic_raw.loc['Bonnell, Miss. Elizabeth', 'Survived'] = 1
```

## `groupby`

```python
df_titanic.groupby('Sex').mean()
```

```python
df_titanic_raw.groupby('Sex').mean()['Pclass']
```

## Create binned values

```python
df_titanic['AgeClass'] = pd.cut(df_titanic['Age'], bins=np.arange(0, 90, 10))
df_titanic['AgeClass']


###############################################################################

# # Second Case study: air quality in Paris.
# (Source: Airparif)

```python


url = "http://josephsalmon.eu/enseignement/datasets/20080421_20160927-PA13_auto.csv"
path_target = "./20080421_20160927-PA13_auto.csv"
download(url, path_target, replace=False)


```python


!head -26 ./20080421_20160927-PA13_auto.csv

# Alternatively :
# get_ipython().system('head -26 ./20080421_20160927-PA13_auto.csv')


# # Times series help:
# https://jakevdp.github.io/PythonDataScienceHandbook/03.11-working-with-time-series.html

```python


polution_df = pd.read_csv('20080421_20160927-PA13_auto.csv', sep=';',
                          comment='#',
                          na_values="n/d",
                          converters={'heure': str})


```python

pd.options.display.max_rows = 30
polution_df.head(25)


# ## Preprocess the data

# ### <font color='red'> EXERCISE : handling missing values </font>
#
# What is the meaning of "na_values="n/d" above?
#
# Note that an alternative can be obtained with the command
# `polution_df.replace('n/d', np.nan, inplace=True)`
#

```python


# check types
polution_df.dtypes

# check all
polution_df.info()

# For more info on the object nature (inherited from numpy), see
# https://stackoverflow.com/questions/21018654/strings-in-a-dataframe-but-dtype-is-object

# ### First issue non conventional hours

```python

# start by changing to integer type (e.g. int8)
polution_df['heure'] = polution_df['heure'].astype(np.int8)
polution_df['heure']

```python

# no data is from 1 to 24... not conventional so let's make it from 0 to 23
polution_df['heure'] = polution_df['heure'] - 1
polution_df['heure']


```python

# and back to strings:
polution_df['heure'] = polution_df['heure'].astype('str')
polution_df['heure']


# ### Time processing
#

```python


# https://www.tutorialspoint.com/python/time_strptime.htm

time_improved = pd.to_datetime(polution_df['date'] +
                               ' ' + polution_df['heure'] + ':00',
                               format='%d/%m/%Y %H:%M')

# Where d = day, m=month, Y=year, H=hour, M=minutes
time_improved


```python


polution_df['date'] + ' ' + polution_df['heure'] + ':00'


```python


# create correct timing format in the dataframe
polution_df['DateTime'] = time_improved

# remove useles columns
del polution_df['heure']
del polution_df['date']


```python


polution_df


```python


# visualize the data set now that the time is well formated:
polution_ts = polution_df.set_index(['DateTime'])
polution_ts = polution_ts.sort_index(ascending=True)
polution_ts.head(12)


```python


polution_ts.describe()


```python

# raw version
# sns.color_palette("colorblind")
# cmap = sns.light_palette("Navy", as_cmap=True)

fig, axes = plt.subplots(2, 1, figsize=(6, 6), sharex=True)

axes[0].plot(polution_ts['O3'])
axes[0].set_title("Ozone polution: daily average in Paris")
axes[0].set_ylabel("Concentration (µg/m³)")

axes[1].plot(polution_ts['NO2'])
axes[1].set_title("Nitrogen polution: daily average in Paris")
axes[1].set_ylabel("Concentration (µg/m³)")

plt.show()

```python

fig, axes = plt.subplots(2, 1, figsize=(10, 5), sharex=True)

# axes[0].plot(polution_ts['O3'].resample('d').mean(), '-')
axes[0].plot(polution_ts['O3'].resample('d').max(), '--')
axes[0].plot(polution_ts['O3'].resample('d').min(),'-.')


axes[0].set_title("Ozone polution: daily average in Paris")
axes[0].set_ylabel("Concentration (µg/m³)")

# axes[1].plot(polution_ts['NO2'].resample('d').mean())
# axes[1].plot(polution_ts['NO2'].resample('d').mean())
axes[1].plot(polution_ts['NO2'].resample('d').max(),  '--')
axes[1].plot(polution_ts['NO2'].resample('d').min(),  '-.')

axes[1].set_title("Nitrogen polution: daily average in Paris")
axes[1].set_ylabel("Concentration (µg/m³)")

plt.show()


# ### <font color='red'> EXERCISE : worst of the day  </font>
# Provide the same plots as before, but with dayly best and worst on the same
# figures (and use different color and/or style)

```python


# ### Is the polution getting better along the years or not?

ax = polution_ts['2008':].resample('Y').mean().plot(figsize=(4, 4))
# Sample by year (A pour Annual) or Y for Year
plt.ylim(0, 50)
plt.title("Pollution evolution: \n yearly average in Paris")
plt.ylabel("Concentration (µg/m³)")
plt.xlabel("Year")


```python


# Load colors
sns.set_palette("GnBu_d", n_colors=7)
polution_ts['weekday'] = polution_ts.index.weekday  # Monday=0, Sunday=6
polution_ts['weekend'] = polution_ts['weekday'].isin([5, 6])

# days = ['Lundi', 'Mardi', 'Mercredi',
#         'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']


polution_week_no2 = polution_ts.groupby(['weekday', polution_ts.index.hour])[
    'NO2'].mean().unstack(level=0)
polution_week_03 = polution_ts.groupby(['weekday', polution_ts.index.hour])[
    'O3'].mean().unstack(level=0)
plt.show()


```python


fig, axes = plt.subplots(2, 1, figsize=(7, 7), sharex=True)

polution_week_no2.plot(ax=axes[0])
axes[0].set_ylabel("Concentration (µg/m³)")
axes[0].set_xlabel("Heure de la journée")
axes[0].set_title(
    "Profil journalier de la pollution au NO2: effet du weekend?")
axes[0].set_xticks(np.arange(0, 24))
axes[0].set_xticklabels(np.arange(0, 24), rotation=45)
axes[0].set_ylim(0, 60)

polution_week_03.plot(ax=axes[1])
axes[1].set_ylabel("Concentration (µg/m³)")
axes[1].set_xlabel("Heure de la journée")
axes[1].set_title("Profil journalier de la pollution au O3: effet du weekend?")
axes[1].set_xticks(np.arange(0, 24))
axes[1].set_xticklabels(np.arange(0, 24), rotation=45)
axes[1].set_ylim(0, 70)
axes[0].legend().set_visible(False)
# ax.legend()
axes[1].legend(labels=days, loc='lower left', bbox_to_anchor=(1, 0.1))

plt.tight_layout()



```python


import calendar
polution_ts['month'] = polution_ts.index.month  # Janvier=0, .... Decembre=11
polution_ts['month'] = polution_ts['month'].apply(lambda x:
                                                  calendar.month_abbr[x])
polution_ts.head()


```python


# days = []

polution_month_no2 = polution_ts.groupby(['month', polution_ts.index.hour])[
    'NO2'].mean().unstack(level=0)
polution_month_03 = polution_ts.groupby(['month', polution_ts.index.hour])[
    'O3'].mean().unstack(level=0)


```python

sns.set_palette("Paired", n_colors=12)

fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

polution_month_no2.plot(ax=axes[0])
axes[0].set_ylabel("Concentration (µg/m³)")
axes[0].set_xlabel("Heure de la journée")
axes[0].set_title(
    "Profil journalier de la pollution au NO2: effet du weekend?")
axes[0].set_xticks(np.arange(0, 24))
axes[0].set_xticklabels(np.arange(0, 24), rotation=45)
axes[0].set_ylim(0, 90)

polution_month_03.plot(ax=axes[1])
axes[1].set_ylabel("Concentration (µg/m³)")
axes[1].set_xlabel("Heure de la journée")
axes[1].set_title("Profil journalier de la pollution au O3: effet du weekend?")
axes[1].set_xticks(np.arange(0, 24))
axes[1].set_xticklabels(np.arange(0, 24), rotation=45)
axes[1].set_ylim(0, 90)
axes[0].legend().set_visible(False)
# ax.legend()
axes[1].legend(labels=calendar.month_name[1:], loc='lower left',
               bbox_to_anchor=(1, 0.1))

plt.tight_layout()


# # Third example (your turn: explore the bike accident dataset on you own)
# https://www.data.gouv.fr/fr/datasets/accidents-de-velo-en-france/
#
# Possible visualization
# https://koumoul.com/en/datasets/accidents-velos

```python


url = "https://koumoul.com/s/data-fair/api/v1/datasets/accidents-velos/raw"
path_target = "./bicycle_db.csv"
download(url, path_target, replace=True)


```python


# df: data frame
df_bikes = pd.read_csv("bicycle_db.csv", na_values="",
                       converters={'data': str, 'heure': str})


```python


get_ipython().system('head -5 ./bicycle_db.csv')


```python


pd.options.display.max_columns = 40
df_bikes.head()


```python


df_bikes['existence securite'].unique()


```python


df_bikes['gravite accident'].unique()


# ### Handle missing values in `heure`

```python


df_bikes['date'].hasnans


```python


df_bikes['heure'].hasnans


```python


pd.options.display.max_rows = 20
df_bikes.iloc[400:402]


```python


# remove missing hours cases by np.nan
df_bikes['heure'] = df_bikes['heure'].replace('', np.nan)
df_bikes.iloc[400:402]


```python


df_bikes.dropna(subset=['heure'], inplace=True)
df_bikes.iloc[399:402]


# ### <font color='red'> EXERCISE : Dates?  </font>
# Can you find the starting day and the ending day of the study automatically?
# hint sort the data.
# You can sort the data by time, , say with df.sort('Time') )

```python


df_bikes['date'] + ' ' + df_bikes['heure'] + ':00'


```python


# ADAPT OLD to create the df_bikes['Time']

time_improved = pd.to_datetime(df_bikes['date'] +
                               ' ' + df_bikes['heure'] + ':00',
                               format='%Y-%m-%d %H:%M')

# Where d = day, m=month, Y=year, H=hour, M=minutes
# create correct timing format in the dataframe


```python


df_bikes['Time'] = time_improved
df_bikes.set_index('Time', inplace=True)
# remove useles columns
del df_bikes['heure']
del df_bikes['date']


```python


df_bikes.info()


```python


df_bike2 = df_bikes[['gravite accident', 'existence securite',
                             'age', 'sexe']]
df_bike2['existence securite'] = df_bike2['existence securite'].replace(np.nan, "Inconnu")
df_bike2.dropna(inplace=True)


# ### <font color='red'> EXERCISE : Is the helmet saving your life?  </font>
# Peform an analysis so that you can check the benefit or not of wearing
# helmet to save your life.
# Beware preprocessing needed to use `pd.crosstab`,  `pivot_table` to avoid
# issues.

```python


group = df_bike2.pivot_table(columns='existence securite',
                             index=['gravite accident', 'sexe'],
                             aggfunc={'age': 'count'}, margins=True)
group


```python


# pd.crosstab?
pd.crosstab(df_bike2['existence securite'],
            df_bike2['gravite accident'], normalize='index') * 100


```python


pd.crosstab(df_bike2['existence securite'],
            df_bike2['gravite accident'], values=df_bike2['age'],
            aggfunc='count', normalize='index') * 100


# ### <font color='red'> EXERCISE :
# Are men and women dying equally on a bike?  </font>
# Peform an analysis to check differences between men and woman survival ?

```python


idx_dead = df_bikes['gravite accident'] == '3 - Tué'
df_deads = df_bikes[idx_dead]
df_gravite = df_deads.groupby('sexe').size() / idx_dead.sum()
df_gravite


```python


df_bikes.groupby('sexe').size()  / df_bikes.shape[0]


```python


pd.crosstab(df_bike2['sexe'],
            df_bike2['gravite accident'],
            values=df_bike2['age'], aggfunc='count',
            normalize='columns', margins=True) * 100


# ### To conclude:
# Note: information on the level of bike practice by men/women is missing...

# ### <font color='red'> EXERCISE : Accident during the week?  </font>
# Peform an analysis to check when the accidents are occuring during the week.

```python


df_bikes


```python


# Chargement des couleurs
sns.set_palette("GnBu_d", n_colors=7)

df_bikes['weekday'] = df_bikes.index.weekday  # Monday=0, Sunday=6

accidents_week = df_bikes.groupby(['weekday', df_bikes.index.hour])[
    'sexe'].count().unstack(level=0)

fig, axes = plt.subplots(1, 1, figsize=(7, 7))


accidents_week.plot(ax=axes)
axes.set_ylabel("Accidents")
axes.set_xlabel("Heure de la journée")
axes.set_title(
    "Profil journalier des accidents: effet du weekend?")
axes.set_xticks(np.arange(0, 24))
axes.set_xticklabels(np.arange(0, 24), rotation=45)
# axes.set_ylim(0, 6)
axes.legend(labels=days, loc='lower left', bbox_to_anchor=(1, 0.1))
plt.legend()
plt.tight_layout()


```python


df_bikes.groupby(['weekday', df_bikes.index.hour])[
    'sexe'].count()


# ### <font color='red'> EXERCISE : Accident during the year?  </font>
# Peform an analysis to check when the accidents are occuring during the week.

```python


df_bikes['month'] = df_bikes.index.month  # Janvier=0, .... Decembre=11
df_bikes['month'] = df_bikes['month'].apply(lambda x: calendar.month_abbr[x])
df_bikes.head()

sns.set_palette("GnBu_d", n_colors=12)
# sns.set_palette("colorblind", n_colors=12)

df_bikes_month = df_bikes.groupby(['month', df_bikes.index.hour])[
    'age'].count().unstack(level=0)

fig, axes = plt.subplots(1, 1, figsize=(7, 7), sharex=True)

df_bikes_month.plot(ax=axes)
axes.set_ylabel("Concentration (µg/m³)")
axes.set_xlabel("Heure de la journée")
axes.set_title(
    "Profil journalier de la pollution au NO2: effet du weekend?")
axes.set_xticks(np.arange(0, 24))
axes.set_xticklabels(np.arange(0, 24), rotation=45)
# axes.set_ylim(0, 90)
axes.legend(labels=calendar.month_name[1:], loc='lower left',
            bbox_to_anchor=(1, 0.1))

plt.tight_layout()


# ### <font color='red'> EXERCISE : Accidents by departement  </font>
# Peform an analysis to check when the accidents are occuring by departement.

```python


import pygal
# First install if needed for maps:
# pip install pygal
# andpip install pygal_maps_frpip install pygal_maps_fr
# pip install pygal_maps_fr

# Departement population: https://public.opendatasoft.com/explore/dataset/population-francaise-par-departement-2018/table/?disjunctive.departement&location=7,47.12995,3.41125&basemap=jawg.streets
path_target = "./dpt_population.csv"
url = "https://public.opendatasoft.com/explore/dataset/population-francaise-par-departement-2018/download/?format=csv&timezone=Europe/Berlin&lang=en&use_labels_for_header=true&csv_separator=%3B"
download(url, path_target, replace=False)

```python

# Departement area: https://www.regions-et-departements.fr/departements-francais#departements_fichiers
path_target = "./dpt_area.csv"
url = "https://www.regions-et-departements.fr/fichiers/departements-francais.csv"
download(url, path_target, replace=False)

df_dtp_pop = pd.read_csv("dpt_population.csv", sep=";", low_memory=False)
df_dtp_area = pd.read_csv("dpt_area.csv", sep="\t", low_memory=False, skiprows=[102, 103, 104])
df_dtp_area['NUMÉRO']


df_dtp_area.set_index('NUMÉRO', inplace=True)

df_dtp_pop.set_index('Code Département', inplace=True)
df_dtp_pop.sort_index(inplace=True)


fr_chart = pygal.maps.fr.Departments(human_readable=True)

# display = "ration_tue"
display = "ratio_accident"


if display is "ratio_accident":
    fr_chart.title = 'Accidents by departement'
    gd = df_bikes.groupby(['departement']).size()
    gd = (gd / df_dtp_pop['Population'])  # mean accident per habitant
else:
    fr_chart.title = 'Deaths by departement'
    df_deads = df_bikes[df_bikes['gravite accident']=='3 - Tué']
    df_gravite = df_deads.groupby('departement').size()
    # gd = df_bikes.groupby(['departement']).aggregate(lambda: x->sum(x))
    gd = (df_gravite / df_dtp_pop['Population'])  # mean deaths per habitant

# Area normalization
normalization = True
if normalization is True:
    gd = (gd / df_dtp_area['SUPERFICIE (km²)'])
gd.dropna(inplace=True)   # anoying NA due to 1 vs 01 in datasets
fr_chart.add('Accidents', gd.to_dict())
fr_chart.render_in_browser()
# fr_chart.render_to_file('./chatr.svg')  # Write the chart in a specified file

```python

