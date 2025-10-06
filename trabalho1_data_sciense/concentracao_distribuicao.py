import pandas as pd

dados = pd.read_csv('HousingData.csv',sep=',')

### CONCENTRAÇÃO E DISTRIBUIÇÃO DA COLUNA CRIM ###
print("\n----COLUNA CRIM----")
print('Média da coluna CRIM:', dados['CRIM'].mean())

print('Mediana da coluna CRIM:', dados['CRIM'].median())

print('Desvio Padrão da coluna CRIM:', dados['CRIM'].std())

print('Valor Máximo da coluna CRIM:', dados['CRIM'].max())
print('Valor Minímo da coluna CRIM:', dados['CRIM'].min())

print('Variância da coluna CRIM:', dados['CRIM'].var())

print('Coef de variaçao da coluna CRIM:', (dados['CRIM'].std()/dados['CRIM'].mean()))

print('Amplitude da coluna CRIM:', dados['CRIM'].max() - dados['CRIM'].min())



### CONCENTRAÇÃO E DISTRIBUIÇÃO DA COLUNA ZN ###
print("\n----COLUNA ZN----")
print('Média da coluna ZN:', dados['ZN'].mean())

print('Mediana da coluna ZN:', dados['ZN'].median())

print('Desvio Padrão da coluna ZN:', dados['ZN'].std())

print('Valor Máximo da coluna ZN:', dados['ZN'].max())
print('Valor Minímo da coluna ZN:', dados['ZN'].min())

print('Variância da coluna ZN:', dados['ZN'].var())

print('Coef de variaçao da coluna ZN:', (dados['ZN'].std()/dados['ZN'].mean()))

print('Amplitude da coluna ZN:', dados['ZN'].max() - dados['ZN'].min())



### CONCENTRAÇÃO E DISTRIBUIÇÃO DA COLUNA INDUS ###
print("\n----COLUNA INDUS----")
print('Média da coluna INDUS:', dados['INDUS'].mean())

print('Mediana da coluna INDUS:', dados['INDUS'].median())

print('Desvio Padrão da coluna INDUS:', dados['INDUS'].std())

print('Valor Máximo da coluna INDUS:', dados['INDUS'].max())
print('Valor Minímo da coluna INDUS:', dados['INDUS'].min())

print('Variância da coluna INDUS:', dados['INDUS'].var())

print('Coef de variaçao da coluna INDUS:', (dados['INDUS'].std()/dados['INDUS'].mean()))

print('Amplitude da coluna INDUS:', dados['INDUS'].max() - dados['INDUS'].min())



### CONCENTRAÇÃO E DISTRIBUIÇÃO DA COLUNA NOX ###
print("\n----COLUNA NOX----")
print('Média da coluna NOX:', dados['NOX'].mean())

print('Mediana da coluna NOX:', dados['NOX'].median())

print('Desvio Padrão da coluna NOX:', dados['NOX'].std())

print('Valor Máximo da coluna NOX:', dados['NOX'].max())
print('Valor Minímo da coluna NOX:', dados['NOX'].min())

print('Variância da coluna NOX:', dados['NOX'].var())

print('Coef de variaçao da coluna NOX:', (dados['NOX'].std()/dados['NOX'].mean()))

print('Amplitude da coluna NOX:', dados['NOX'].max() - dados['NOX'].min())



### CONCENTRAÇÃO E DISTRIBUIÇÃO DA COLUNA RM ###
print("\n----COLUNA RM----")
print('Média da coluna RM:', dados['RM'].mean())

print('Mediana da coluna RM:', dados['RM'].median())

print('Desvio Padrão da coluna RM:', dados['RM'].std())

print('Valor Máximo da coluna RM:', dados['RM'].max())
print('Valor Minímo da coluna RM:', dados['RM'].min())

print('Variância da coluna RM:', dados['RM'].var())

print('Coef de variaçao da coluna RM:', (dados['RM'].std()/dados['RM'].mean()))

print('Amplitude da coluna RM:', dados['RM'].max() - dados['RM'].min())



### CONCENTRAÇÃO E DISTRIBUIÇÃO DA COLUNA AGE ###
print("\n----COLUNA AGE----")
print('Média da coluna AGE:', dados['AGE'].mean())

print('Mediana da coluna AGE:', dados['AGE'].median())

print('Desvio Padrão da coluna AGE:', dados['AGE'].std())

print('Valor Máximo da coluna AGE:', dados['AGE'].max())
print('Valor Minímo da coluna AGE:', dados['AGE'].min())

print('Variância da coluna AGE:', dados['AGE'].var())

print('Coef de variaçao da coluna AGE:', (dados['AGE'].std()/dados['AGE'].mean()))

print('Amplitude da coluna AGE:', dados['AGE'].max() - dados['AGE'].min())


### CONCENTRAÇÃO E DISTRIBUIÇÃO DA COLUNA DIS ###
print("\n----COLUNA DIS----")
print('Média da coluna DIS:', dados['DIS'].mean())

print('Mediana da coluna DIS:', dados['DIS'].median())

print('Desvio Padrão da coluna DIS:', dados['DIS'].std())

print('Valor Máximo da coluna DIS:', dados['DIS'].max())
print('Valor Minímo da coluna DIS:', dados['DIS'].min())

print('Variância da coluna DIS:', dados['DIS'].var())

print('Coef de variação da coluna DIS:', (dados['DIS'].std()/dados['DIS'].mean()))

print('Amplitude da coluna DIS:', dados['DIS'].max() - dados['DIS'].min())


### CONCENTRAÇÃO E DISTRIBUIÇÃO DA COLUNA RAD ###
print("\n----COLUNA RAD----")
print('Média da coluna RAD:', dados['RAD'].mean())

print('Mediana da coluna RAD:', dados['RAD'].median())

print('Desvio Padrão da coluna RAD:', dados['RAD'].std())

print('Valor Máximo da coluna RAD:', dados['RAD'].max())
print('Valor Minímo da coluna RAD:', dados['RAD'].min())

print('Variância da coluna RAD:', dados['RAD'].var())

print('Coef de variação da coluna RAD:', (dados['RAD'].std()/dados['RAD'].mean()))

print('Amplitude da coluna RAD:', dados['RAD'].max() - dados['RAD'].min())


### CONCENTRAÇÃO E DISTRIBUIÇÃO DA COLUNA TAX ###
print("\n----COLUNA TAX----")
print('Média da coluna TAX:', dados['TAX'].mean())

print('Mediana da coluna TAX:', dados['TAX'].median())

print('Desvio Padrão da coluna TAX:', dados['TAX'].std())

print('Valor Máximo da coluna TAX:', dados['TAX'].max())
print('Valor Minímo da coluna TAX:', dados['TAX'].min())

print('Variância da coluna TAX:', dados['TAX'].var())

print('Coef de variação da coluna TAX:', (dados['TAX'].std()/dados['TAX'].mean()))

print('Amplitude da coluna TAX:', dados['TAX'].max() - dados['TAX'].min())


### CONCENTRAÇÃO E DISTRIBUIÇÃO DA COLUNA PTRATIO ###
print("\n----COLUNA PTRATIO----")
print('Média da coluna PTRATIO:', dados['PTRATIO'].mean())

print('Mediana da coluna PTRATIO:', dados['PTRATIO'].median())

print('Desvio Padrão da coluna PTRATIO:', dados['PTRATIO'].std())

print('Valor Máximo da coluna PTRATIO:', dados['PTRATIO'].max())
print('Valor Minímo da coluna PTRATIO:', dados['PTRATIO'].min())

print('Variância da coluna PTRATIO:', dados['PTRATIO'].var())

print('Coef de variação da coluna PTRATIO:', (dados['PTRATIO'].std()/dados['PTRATIO'].mean()))

print('Amplitude da coluna PTRATIO:', dados['PTRATIO'].max() - dados['PTRATIO'].min())


### CONCENTRAÇÃO E DISTRIBUIÇÃO DA COLUNA B ###
print("\n----COLUNA B----")
print('Média da coluna B:', dados['B'].mean())

print('Mediana da coluna B:', dados['B'].median())

print('Desvio Padrão da coluna B:', dados['B'].std())

print('Valor Máximo da coluna B:', dados['B'].max())
print('Valor Minímo da coluna B:', dados['B'].min())

print('Variância da coluna B:', dados['B'].var())

print('Coef de variação da coluna B:', (dados['B'].std()/dados['B'].mean()))

print('Amplitude da coluna B:', dados['B'].max() - dados['B'].min())


### CONCENTRAÇÃO E DISTRIBUIÇÃO DA COLUNA LSTAT ###
print("\n----COLUNA LSTAT----")
print('Média da coluna LSTAT:', dados['LSTAT'].mean())

print('Mediana da coluna LSTAT:', dados['LSTAT'].median())

print('Desvio Padrão da coluna LSTAT:', dados['LSTAT'].std())

print('Valor Máximo da coluna LSTAT:', dados['LSTAT'].max())
print('Valor Minímo da coluna LSTAT:', dados['LSTAT'].min())

print('Variância da coluna LSTAT:', dados['LSTAT'].var())

print('Coef de variação da coluna LSTAT:', (dados['LSTAT'].std()/dados['LSTAT'].mean()))

print('Amplitude da coluna LSTAT:', dados['LSTAT'].max() - dados['LSTAT'].min())


### CONCENTRAÇÃO E DISTRIBUIÇÃO DA COLUNA MEDV ###
print("\n----COLUNA MEDV----")
print('Média da coluna MEDV:', dados['MEDV'].mean())

print('Mediana da coluna MEDV:', dados['MEDV'].median())

print('Desvio Padrão da coluna MEDV:', dados['MEDV'].std())

print('Valor Máximo da coluna MEDV:', dados['MEDV'].max())
print('Valor Minímo da coluna MEDV:', dados['MEDV'].min())

print('Variância da coluna MEDV:', dados['MEDV'].var())

print('Coef de variação da coluna MEDV:', (dados['MEDV'].std()/dados['MEDV'].mean()))

print('Amplitude da coluna MEDV:', dados['MEDV'].max() - dados['MEDV'].min())
