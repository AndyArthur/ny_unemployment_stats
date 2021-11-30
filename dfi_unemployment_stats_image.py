# create dataframe image of unemployment statistics for sharing on social media
# requires download_process_ue.py also in this directory 
import download_process_ue

# also uses seaborn for color ramps and dataframe image libraries
import seaborn as sns

# create county tables
cm = sns.light_palette("green", as_cmap=True)
ctbl=df[((df['AREA'].str.contains('County')) & (df['YEAR'] > 2019))].pivot(index='DATETIME',columns='AREA',values='UNEMPRATE')
ctbl.index = ctbl.index.strftime("%b %Y")
ctbl.style.background_gradient(cmap=cm).format('{:.1f}')

for i in range(0, 70, 10):
    dfi.export(ctbl.iloc[:,i:i+10].style.background_gradient(cmap=cm).format('{:.1f}'), '/tmp/county_uerate'+str(i)+'.png')
    
# create city tables
cm = sns.light_palette("purple", as_cmap=True)
ctbl=df[((df['AREA'].str.contains('city')) & (df['YEAR'] > 2019))].pivot(index='DATETIME',columns='AREA',values='UNEMPRATE')
ctbl.index = ctbl.index.strftime("%b %Y")
ctbl.style.background_gradient(cmap=cm).format('{:.1f}')

for i in range(0, 70, 10):
    dfi.export(ctbl.iloc[:,i:i+10].style.background_gradient(cmap=cm).format('{:.1f}'), '/tmp/city_uerate'+str(i)+'.png')
