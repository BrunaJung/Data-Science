import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('HousingData.csv', sep=',')

### QUARTIS DE CRIM ###
print("\nValores Quartis de CRIM:")
dados['CRIM'] = pd.to_numeric(dados['CRIM'], errors='coerce')

q1 = dados['CRIM'].quantile(0.25)
q2 = dados['CRIM'].quantile(0.50)
q3 = dados['CRIM'].quantile(0.75)

print("Primeiro Quartil (Q1):", q1)
print("Segundo Quartil (Q2 - mediana):", q2)
print("Terceiro Quartil (Q3):", q3)

plt.boxplot(dados['CRIM'].dropna(), showfliers=False)
plt.title("Boxplot da Coluna CRIM")
plt.ylabel("Valores de CRIM")
plt.show()


### QUARTIS DE ZN ###
print("\nValores Quartis de ZN:")
dados['ZN'] = pd.to_numeric(dados['ZN'], errors='coerce')

q1 = dados['ZN'].quantile(0.25)
q2 = dados['ZN'].quantile(0.50)
q3 = dados['ZN'].quantile(0.75)

print("Primeiro Quartil (Q1):", q1)
print("Segundo Quartil (Q2 - mediana):", q2)
print("Terceiro Quartil (Q3):", q3)

plt.boxplot(dados['ZN'].dropna(), showfliers=False)
plt.title("Boxplot da Coluna ZN")
plt.ylabel("Valores de ZN")
plt.show()


### QUARTIS DE INDUS ###
print("\nValores Quartis de INDUS:")
dados['INDUS'] = pd.to_numeric(dados['INDUS'], errors='coerce')

q1 = dados['INDUS'].quantile(0.25)
q2 = dados['INDUS'].quantile(0.50)
q3 = dados['INDUS'].quantile(0.75)

print("Primeiro Quartil (Q1):", q1)
print("Segundo Quartil (Q2 - mediana):", q2)
print("Terceiro Quartil (Q3):", q3)

plt.boxplot(dados['INDUS'].dropna(), showfliers=False)
plt.title("Boxplot da Coluna INDUS")
plt.ylabel("Valores de INDUS")
plt.show()



### QUARTIS DE NOX ###
print("\nValores Quartis de NOX:")
dados['NOX'] = pd.to_numeric(dados['NOX'], errors='coerce')

q1 = dados['NOX'].quantile(0.25)
q2 = dados['NOX'].quantile(0.50)
q3 = dados['NOX'].quantile(0.75)

print("Primeiro Quartil (Q1):", q1)
print("Segundo Quartil (Q2 - mediana):", q2)
print("Terceiro Quartil (Q3):", q3)

plt.boxplot(dados['NOX'].dropna(), showfliers=False)
plt.title("Boxplot da Coluna NOX")
plt.ylabel("Valores de NOX")
plt.show()



### QUARTIS DE RM ###
print("\nValores Quartis de RM:")
dados['RM'] = pd.to_numeric(dados['RM'], errors='coerce')

q1 = dados['RM'].quantile(0.25)
q2 = dados['RM'].quantile(0.50)
q3 = dados['RM'].quantile(0.75)

print("Primeiro Quartil (Q1):", q1)
print("Segundo Quartil (Q2 - mediana):", q2)
print("Terceiro Quartil (Q3):", q3)

plt.boxplot(dados['RM'].dropna(), showfliers=False)
plt.title("Boxplot da Coluna RM")
plt.ylabel("Valores de RM")
plt.show()



### QUARTIS DE AGE ###
print("Valores Quartis de AGE:")
dados['AGE'] = pd.to_numeric(dados['AGE'], errors='coerce')

q1 = dados['AGE'].quantile(0.25)
q2 = dados['AGE'].quantile(0.50)
q3 = dados['AGE'].quantile(0.75)

print("Primeiro Quartil (Q1):", q1)
print("Segundo Quartil (Q2 - mediana):", q2)
print("Terceiro Quartil (Q3):", q3)

plt.boxplot(dados['AGE'].dropna(), showfliers=False)
plt.title("Boxplot da Coluna AGE")
plt.ylabel("Valores de AGE")
plt.show()



### QUARTIS DE DIS ###
print("\nValores Quartis de DIS:")
dados['DIS'] = pd.to_numeric(dados['DIS'], errors='coerce')

q1 = dados['DIS'].quantile(0.25)
q2 = dados['DIS'].quantile(0.50)
q3 = dados['DIS'].quantile(0.75)

print("Primeiro Quartil (Q1):", q1)
print("Segundo Quartil (Q2 - mediana):", q2)
print("Terceiro Quartil (Q3):", q3)

plt.boxplot(dados['DIS'].dropna(), showfliers=False)
plt.title("Boxplot da Coluna DIS")
plt.ylabel("Valores de DIS")
plt.show()


### QUARTIS DE RAD ###
print("\nValores Quartis de RAD:")
dados['RAD'] = pd.to_numeric(dados['RAD'], errors='coerce')

q1 = dados['RAD'].quantile(0.25)
q2 = dados['RAD'].quantile(0.50)
q3 = dados['RAD'].quantile(0.75)

print("Primeiro Quartil (Q1):", q1)
print("Segundo Quartil (Q2 - mediana):", q2)
print("Terceiro Quartil (Q3):", q3)

plt.boxplot(dados['RAD'].dropna(), showfliers=False)
plt.title("Boxplot da Coluna RAD")
plt.ylabel("Valores de RAD")
plt.show()


### QUARTIS DE TAX ###
print("\nValores Quartis de TAX:")
dados['TAX'] = pd.to_numeric(dados['TAX'], errors='coerce')

q1 = dados['TAX'].quantile(0.25)
q2 = dados['TAX'].quantile(0.50)
q3 = dados['TAX'].quantile(0.75)

print("Primeiro Quartil (Q1):", q1)
print("Segundo Quartil (Q2 - mediana):", q2)
print("Terceiro Quartil (Q3):", q3)

plt.boxplot(dados['TAX'].dropna(), showfliers=False)
plt.title("Boxplot da Coluna TAX")
plt.ylabel("Valores de TAX")
plt.show()



### QUARTIS DE PTRATIO ###
print("\nValores Quartis de PTRATIO:")
dados['PTRATIO'] = pd.to_numeric(dados['PTRATIO'], errors='coerce')

q1 = dados['PTRATIO'].quantile(0.25)
q2 = dados['PTRATIO'].quantile(0.50)
q3 = dados['PTRATIO'].quantile(0.75)

print("Primeiro Quartil (Q1):", q1)
print("Segundo Quartil (Q2 - mediana):", q2)
print("Terceiro Quartil (Q3):", q3)

plt.boxplot(dados['PTRATIO'].dropna(), showfliers=False)
plt.title("Boxplot da Coluna PTRATIO")
plt.ylabel("Valores de PTRATIO")
plt.show()



### QUARTIS DE B ###
print("\nValores Quartis de B:")
dados['B'] = pd.to_numeric(dados['B'], errors='coerce')

q1 = dados['B'].quantile(0.25)
q2 = dados['B'].quantile(0.50)
q3 = dados['B'].quantile(0.75)

print("Primeiro Quartil (Q1):", q1)
print("Segundo Quartil (Q2 - mediana):", q2)
print("Terceiro Quartil (Q3):", q3)

plt.boxplot(dados['B'].dropna(), showfliers=False)
plt.title("Boxplot da Coluna B")
plt.ylabel("Valores de B")
plt.show()



### QUARTIS DE LSTAT ###
print("\nValores Quartis de LSTAT:")
dados['LSTAT'] = pd.to_numeric(dados['LSTAT'], errors='coerce')

q1 = dados['LSTAT'].quantile(0.25)
q2 = dados['LSTAT'].quantile(0.50)
q3 = dados['LSTAT'].quantile(0.75)

print("Primeiro Quartil (Q1):", q1)
print("Segundo Quartil (Q2 - mediana):", q2)
print("Terceiro Quartil (Q3):", q3)

plt.boxplot(dados['LSTAT'].dropna(), showfliers=False)
plt.title("Boxplot da Coluna LSTAT")
plt.ylabel("Valores de LSTAT")
plt.show()



### QUARTIS DE MEDV ###
print("\nValores Quartis de MEDV:")
dados['MEDV'] = pd.to_numeric(dados['MEDV'], errors='coerce')

q1 = dados['MEDV'].quantile(0.25)
q2 = dados['MEDV'].quantile(0.50)
q3 = dados['MEDV'].quantile(0.75)

print("Primeiro Quartil (Q1):", q1)
print("Segundo Quartil (Q2 - mediana):", q2)
print("Terceiro Quartil (Q3):", q3)

plt.boxplot(dados['MEDV'].dropna(), showfliers=False)
plt.title("Boxplot da Coluna MEDV")
plt.ylabel("Valores de MEDV")
plt.show()

