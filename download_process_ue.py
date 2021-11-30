import pandas as pd

# by using RemoteZip (pip install remotezip) this speeds
# up downloads by only downloading the files in the zip file
# that we actually need from DOL
from remotezip import RemoteZip

dolzip='https://dol.ny.gov/statistics-lauszip'

# download & load only cities and counties 
with RemoteZip(dolzip) as zip:
    df=pd.read_csv(zip.extract('laus_counties.txt'))
    df=df.append(pd.read_csv(zip.extract('laus_cities.txt')))

# get rid of double quotes in column names
df.columns = df.columns.str.replace('\"','')

# get rid of spaces in column names
df.columns=df.columns.str.replace(' ','')

# convert year and month field to datetime, coerce makes the column NaN for yearly averages
df['DATETIME']=pd.to_datetime({'year': df['YEAR'], 'month': df['MONTH'],'day': 1}, errors='coerce')

# drop yearly averages, as they are NaN
df=df.dropna(subset=['DATETIME'])

# Convert City/Town to Census Style
df['AREA']=df['AREA'].str.replace('City','city')
df['AREA']=df['AREA'].str.replace('Town','town')
df['AREA']=df['AREA'].str.replace('Village','village')
df['AREA']=df['AREA'].str.replace(' Ny','')

df
