import pandas as pd
from scipy import stats

dados = pd.read_csv('HousingData.csv', sep=',')
alpha = 0.05

### 1- HIPÓTESE 0: não há relação entre o número de quartos e o valor do imóvel.
print("\n1- HIPÓTESE 0: não há relação entre o número de quartos e o valor do imóvel:")
rm = dados['RM']
medv = dados['MEDV']

correlacao, p_value = stats.pearsonr(rm, medv)

print("Correlação de Pearson (RM x MEDV):", correlacao)
print("p-valor:", p_value)

if p_value < alpha:
    print('Rejeita-se H0. Ou seja, existe uma relação significativa entre número de quartos e valor do imóvel a uma significância de 5%')
else:
    print('Não é possível rejeitar H0. Não há evidência de relação significativa entre número de quartos e valor do imóvel a uma significância de 5%')



### 2- HIPÓTESE 0: não há relação entre o indice de poluição e o valor do imóvel. 
print("\n2- HIPÓTESE 0: não há relação entre o indice de poluição e o valor do imóvel:")
nox = dados['NOX']
medv = dados['MEDV']

correlacao, p_value = stats.pearsonr(nox, medv)

print("Correlação de Pearson (NOX x MEDV):", correlacao)
print("p-valor:", p_value)

if p_value < alpha:
    print('Rejeita-se H0. Ou seja, existe uma relação significativa entre NOX e valor do imóvel a uma significância de 5%')
else:
    print('Não é possível rejeitar H0. Não há evidência de relação significativa entre NOX e valor do imóvel a uma significância de 5%')



### 3- HIPÓTESE 0: não há relação entre a idade da casa e o valor do imóvel.
print("\n3- HIPÓTESE 0: não há relação entre a idade da casa e o valor do imóvel:")
age = pd.to_numeric(dados['AGE'], errors='coerce')
medv = pd.to_numeric(dados['MEDV'], errors='coerce')

# Removendo linhas com NaN
age_clean = age.dropna()
medv_clean = medv[age_clean.index]  # garante que os índices coincidam

correlacao, p_value = stats.pearsonr(age_clean, medv_clean)

print("Correlação de Pearson (AGE x MEDV):", correlacao)
print("p-valor:", p_value)

if p_value < alpha:
    print('Rejeita-se H0. Ou seja, existe uma relação significativa entre AGE e valor do imóvel a uma significância de 5%')
else:
    print('Não é possível rejeitar H0. Não há evidência de relação significativa entre AGE e valor do imóvel a uma significância de 5%')


### 4- HIPÓTESE 0: a casa estar próximo ao rio não influencia o valor do imóvel.
print("\n4- HIPÓTESE 0: a casa estar próximo ao rio não influencia o valor do imóvel:")
chas = pd.to_numeric(dados['CHAS'], errors='coerce')
medv = pd.to_numeric(dados['MEDV'], errors='coerce')

# Removendo linhas com NaN
chas_clean = chas.dropna()
medv_clean = medv[chas_clean.index]  # garante que os índices coincidam

correlacao, p_value = stats.pearsonr(chas_clean, medv_clean)

print("Correlação de Pearson (CHAS x MEDV):", correlacao)
print("p-valor:", p_value)

if p_value < alpha:
    print('Rejeita-se H0. Ou seja, estar próximo ao rio influencia o valor do imóvel a uma significância de 5%')
else:
    print('Não é possível rejeitar H0. Ou seja, não há evidência de que estar próximo ao rio influencie o valor do imóvel a uma significância de 5%')