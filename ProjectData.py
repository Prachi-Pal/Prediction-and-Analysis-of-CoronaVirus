# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

### Libraries Required
import re
import requests
import pandas as pd
import numpy as np
import os.path

### Step - 1:  Data Collection

html_source = requests.get("https://www.worldometers.info/coronavirus/").text
html_source = re.sub(r'<.*?>', lambda g: g.group(0).upper(), html_source)
df=pd.read_html(html_source)[0]




### Step - 2: Data Cleaning

#removing extra columns
df.drop(df.columns[[10, 11,13,15,16,17,18,19,20,21]], axis = 1, inplace = True)

#removing extra rows
df = df.drop(labels = range(0,8),axis = 0 )
df = df.drop(labels = range(237,245) , axis = 0)
df = df[:-1]

#replacing Nan values with zero
df= df.replace(np.nan,0)

# Renaming Columns
df.columns=['Index','Country','Total-Cases','New-Cases','Total-Deaths','New-Deaths','Total-Recovered','New-Recovered','Active-Cases',
            'Serious-Critical','Total-Test','Population']

# Indexing the Dataframe
df.set_index("Index", inplace=True)
df.index = df.index.astype(int)
 
### Step - 3: Exporting Live Data
df.to_excel(r'covid19_dataset.xlsx')
