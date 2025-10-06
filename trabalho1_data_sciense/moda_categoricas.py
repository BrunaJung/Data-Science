import pandas as pd

dados = pd.read_csv('HousingData.csv',sep=',')

### MODA DA COLUNA CATEGÓRICA CHAS ###
print("\n----COLUNA CHAS----")
print('Moda da coluna CHAS:', dados['CHAS'].mode().values[0])