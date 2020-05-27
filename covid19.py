# Import libraries
import numpy as np
import pandas as pd
import datetime
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
# Read Data
df = pd.read_csv("new-covid-cases-per-million.csv")
# Rename columns
df = df.rename(columns={'Entity':'Pais','Date':'Fecha','Daily new confirmed cases of COVID-19 per million people (cases)':'Casos'})
# Select columns to keep
columns_to_keep = ['Pais','Fecha','Casos']
df = df[columns_to_keep].dropna() ## Eliminate the cells with NaN
#print(df.head())
# We create a new column with the cumulative number of cases per day
df['Acum'] = df.groupby(by=['Pais'])['Casos'].agg({'acum':np.cumsum})
print(df.head())
df = df.set_index('Pais')

# Select data per country beloging to OCDE
Chile = df.loc['Chile']
EEUU = df.loc['United States']
Brasil = df.loc['Brazil']
Argentina = df.loc['Argentina']
Peru = df.loc['Peru']

## Plot: Casos diarios de contagio por millon de habitantes ##
fig,ax= plt.subplots(figsize=(10,8))
plt.title('Algunos paises de America', fontsize=20)
plt.xlabel(" Fecha ",fontsize=20)
plt.ylabel("Número de contagios por \n millon de habitantes",fontsize=20)
ax.xaxis.set_major_locator(tck.MultipleLocator(base=5))
#plt.yscale('log')

plt.plot(EEUU['Fecha'], EEUU['Casos'], color='b', label='EEUU')
plt.plot(Chile['Fecha'], Chile['Casos'], color='r', label='Chile')
plt.plot(Brasil['Fecha'],Brasil['Casos'], color='g', label='Brasil')
plt.plot(Argentina['Fecha'],Argentina['Casos'], color='k', label='Argentina')

plt.legend(loc='upper left', fontsize = 15)
plt.gcf().autofmt_xdate()
plt.savefig('Casos_diarios.pdf')

# EN chile se comenzaron a tomar datos desde el 4 de Marzo de 2020
# En EEUU se comenzaron a tomar datos desde el 31 de Diciembre de 2019

## Plot: Casos Acumulados por millon de habitantes ##
fig,ax= plt.subplots(figsize=(10,8))
plt.title('Algunos paises de America', fontsize=20)
plt.xlabel(" Fecha ",fontsize=20)
plt.ylabel("Número de contagios acumulados \n millon de habitantes",fontsize=20)
ax.xaxis.set_major_locator(tck.MultipleLocator(base=5))
#plt.yscale('log')

plt.plot(EEUU['Fecha'], EEUU['Acum'], color='b', label='EEUU')
plt.plot(Chile['Fecha'], Chile['Acum'], color='r', label='Chile')
plt.plot(Brasil['Fecha'],Brasil['Acum'], color='g', label='Brasil')
plt.plot(Argentina['Fecha'],Argentina['Acum'], color='k', label='Argentina')

plt.legend(loc='upper left', fontsize = 15)
plt.gcf().autofmt_xdate()
plt.savefig('Casos_Acumulados.pdf')
