import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
import plotly.express as px


base_credit = pd.read_csv('/credit_data.csv')

#Exibir os 10 primeiros valores da base_credit.
base_credit.head(10) 

#Exibir os 10 ultimos valores da base_credit.
base_credit.tail(8)

base_credit[base_credit['income'] > = 69995.685578

#Agrupamento de valores nulos
base_credit.isnull().sum()


#Identificando os valores nulos em 'age'
base_credit.loc[pd.isnull(base_credit['age'])]


#Implementando em valores em locais nulos
base_credit['age'].fillna(base_credit['age'].mean(), inplace = True)


#fitrando por valores.
base_credit.loc(base_credit['clientid']).isin(29,31,32)


#Rows and Columns of the array:

x_census.shape()
