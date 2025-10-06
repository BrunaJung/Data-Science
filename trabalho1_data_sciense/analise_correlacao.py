import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

dados = pd.read_csv('HousingData.csv', sep=',')
alpha = 0.05

# 1 - CRIM x MEDV
print("\n=== Correlação entre CRIM e MEDV ===")
x = pd.to_numeric(dados['CRIM'], errors='coerce')
y = pd.to_numeric(dados['MEDV'], errors='coerce')

mask = x.notna() & y.notna()
x = x[mask]; y = y[mask]
corr, p_value = stats.pearsonr(x, y)

direcao = "positiva" if corr > 0 else "negativa"
forca = "fraca" if abs(corr) < 0.3 else ("moderada" if abs(corr) < 0.7 else "forte")

print(f"Coeficiente de Pearson: {corr:.4f}")
print(f"Valor-p: {p_value:.10f}")
print(f"A correlação é {direcao} e {forca}.")
print("Rejeita-se H0 → relação significativa." if p_value < alpha else "Não é possível rejeitar H0 → sem relação significativa.")
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.scatter(x, y, alpha=0.7, color='blue')
plt.xlabel('CRIM'); plt.ylabel('MEDV')
plt.title(f'Dispersão: r = {corr:.3f}')
plt.subplot(1,2,2)
sns.regplot(x=x, y=y, ci=None, color='blue')
plt.title('Reta de Regressão')
plt.tight_layout()
plt.show()



# 2 - ZN x MEDV
print("\n=== Correlação entre ZN e MEDV ===")
x = pd.to_numeric(dados['ZN'], errors='coerce'); y = pd.to_numeric(dados['MEDV'], errors='coerce')
mask = x.notna() & y.notna(); x = x[mask]; y = y[mask]
corr, p_value = stats.pearsonr(x, y)
direcao = "positiva" if corr > 0 else "negativa"
forca = "fraca" if abs(corr) < 0.3 else ("moderada" if abs(corr) < 0.7 else "forte")
print(f"Coeficiente de Pearson: {corr:.4f}")
print(f"Valor-p: {p_value:.10f}")
print(f"A correlação é {direcao} e {forca}.")
print("Rejeita-se H0 → relação significativa." if p_value < alpha else "Não é possível rejeitar H0 → sem relação significativa.")
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.scatter(x, y, alpha=0.7, color='green')
plt.xlabel('ZN'); plt.ylabel('MEDV')
plt.title(f'Dispersão: r = {corr:.3f}')
plt.subplot(1,2,2)
sns.regplot(x=x, y=y, ci=None, color='green')
plt.title('Reta de Regressão')
plt.tight_layout()
plt.show()



# 3 - INDUS x MEDV
print("\n=== Correlação entre INDUS e MEDV ===")
x = pd.to_numeric(dados['INDUS'], errors='coerce'); y = pd.to_numeric(dados['MEDV'], errors='coerce')
mask = x.notna() & y.notna(); x = x[mask]; y = y[mask]
corr, p_value = stats.pearsonr(x, y)
direcao = "positiva" if corr > 0 else "negativa"
forca = "fraca" if abs(corr) < 0.3 else ("moderada" if abs(corr) < 0.7 else "forte")
print(f"Coeficiente de Pearson: {corr:.4f}")
print(f"Valor-p: {p_value:.10f}")
print(f"A correlação é {direcao} e {forca}.")
print("Rejeita-se H0 → relação significativa." if p_value < alpha else "Não é possível rejeitar H0 → sem relação significativa.")
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.scatter(x, y, alpha=0.7, color='orange')
plt.xlabel('INDUS'); plt.ylabel('MEDV')
plt.title(f'Dispersão: r = {corr:.3f}')
plt.subplot(1,2,2)
sns.regplot(x=x, y=y, ci=None, color='orange')
plt.title('Reta de Regressão')
plt.tight_layout()
plt.show()



# 4 - CHAS x MEDV
print("\n=== Correlação entre CHAS e MEDV ===")
x = pd.to_numeric(dados['CHAS'], errors='coerce'); y = pd.to_numeric(dados['MEDV'], errors='coerce')
mask = x.notna() & y.notna(); x = x[mask]; y = y[mask]
corr, p_value = stats.pearsonr(x, y)
direcao = "positiva" if corr > 0 else "negativa"
forca = "fraca" if abs(corr) < 0.3 else ("moderada" if abs(corr) < 0.7 else "forte")
print(f"Coeficiente de Pearson: {corr:.4f}")
print(f"Valor-p: {p_value:.10f}")
print(f"A correlação é {direcao} e {forca}.")
print("Rejeita-se H0 → relação significativa." if p_value < alpha else "Não é possível rejeitar H0 → sem relação significativa.")
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.scatter(x, y, alpha=0.7, color='purple')
plt.xlabel('CHAS'); plt.ylabel('MEDV')
plt.title(f'Dispersão: r = {corr:.3f}')
plt.subplot(1,2,2)
sns.regplot(x=x, y=y, ci=None, color='purple')
plt.title('Reta de Regressão')
plt.tight_layout()
plt.show()



# 5 - NOX x MEDV
print("\n=== Correlação entre NOX e MEDV ===")
x = pd.to_numeric(dados['NOX'], errors='coerce'); y = pd.to_numeric(dados['MEDV'], errors='coerce')
mask = x.notna() & y.notna(); x = x[mask]; y = y[mask]
corr, p_value = stats.pearsonr(x, y)
direcao = "positiva" if corr > 0 else "negativa"
forca = "fraca" if abs(corr) < 0.3 else ("moderada" if abs(corr) < 0.7 else "forte")
print(f"Coeficiente de Pearson: {corr:.4f}")
print(f"Valor-p: {p_value:.10f}")
print(f"A correlação é {direcao} e {forca}.")
print("Rejeita-se H0 → relação significativa." if p_value < alpha else "Não é possível rejeitar H0 → sem relação significativa.")
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.scatter(x, y, alpha=0.7, color='red')
plt.xlabel('NOX'); plt.ylabel('MEDV')
plt.title(f'Dispersão: r = {corr:.3f}')
plt.subplot(1,2,2)
sns.regplot(x=x, y=y, ci=None, color='red')
plt.title('Reta de Regressão')
plt.tight_layout()
plt.show()



# 6 - RM x MEDV
print("\n=== Correlação entre RM e MEDV ===")
x = pd.to_numeric(dados['RM'], errors='coerce'); y = pd.to_numeric(dados['MEDV'], errors='coerce')
mask = x.notna() & y.notna(); x = x[mask]; y = y[mask]
corr, p_value = stats.pearsonr(x, y)
direcao = "positiva" if corr > 0 else "negativa"
forca = "fraca" if abs(corr) < 0.3 else ("moderada" if abs(corr) < 0.7 else "forte")
print(f"Coeficiente de Pearson: {corr:.4f}")
print(f"Valor-p: {p_value:.10f}")
print(f"A correlação é {direcao} e {forca}.")
print("Rejeita-se H0 → relação significativa." if p_value < alpha else "Não é possível rejeitar H0 → sem relação significativa.")
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.scatter(x, y, alpha=0.7, color='blue')
plt.xlabel('RM'); plt.ylabel('MEDV')
plt.title(f'Dispersão: r = {corr:.3f}')
plt.subplot(1,2,2)
sns.regplot(x=x, y=y, ci=None, color='blue')
plt.title('Reta de Regressão')
plt.tight_layout()
plt.show()



# 7 - AGE x MEDV
print("\n=== Correlação entre AGE e MEDV ===")
x = pd.to_numeric(dados['AGE'], errors='coerce'); y = pd.to_numeric(dados['MEDV'], errors='coerce')
mask = x.notna() & y.notna(); x = x[mask]; y = y[mask]
corr, p_value = stats.pearsonr(x, y)
direcao = "positiva" if corr > 0 else "negativa"
forca = "fraca" if abs(corr) < 0.3 else ("moderada" if abs(corr) < 0.7 else "forte")
print(f"Coeficiente de Pearson: {corr:.4f}")
print(f"Valor-p: {p_value:.10f}")
print(f"A correlação é {direcao} e {forca}.")
print("Rejeita-se H0 → relação significativa." if p_value < alpha else "Não é possível rejeitar H0 → sem relação significativa.")
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.scatter(x, y, alpha=0.7, color='gray')
plt.xlabel('AGE'); plt.ylabel('MEDV')
plt.title(f'Dispersão: r = {corr:.3f}')
plt.subplot(1,2,2)
sns.regplot(x=x, y=y, ci=None, color='gray')
plt.title('Reta de Regressão')
plt.tight_layout()
plt.show()



# 8 - DIS x MEDV
print("\n=== Correlação entre DIS e MEDV ===")
x = pd.to_numeric(dados['DIS'], errors='coerce'); y = pd.to_numeric(dados['MEDV'], errors='coerce')
mask = x.notna() & y.notna(); x = x[mask]; y = y[mask]
corr, p_value = stats.pearsonr(x, y)
direcao = "positiva" if corr > 0 else "negativa"
forca = "fraca" if abs(corr) < 0.3 else ("moderada" if abs(corr) < 0.7 else "forte")
print(f"Coeficiente de Pearson: {corr:.4f}")
print(f"Valor-p: {p_value:.10f}")
print(f"A correlação é {direcao} e {forca}.")
print("Rejeita-se H0 → relação significativa." if p_value < alpha else "Não é possível rejeitar H0 → sem relação significativa.")
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.scatter(x, y, alpha=0.7, color='pink')
plt.xlabel('DIS'); plt.ylabel('MEDV')
plt.title(f'Dispersão: r = {corr:.3f}')
plt.subplot(1,2,2)
sns.regplot(x=x, y=y, ci=None, color='pink')
plt.title('Reta de Regressão')
plt.tight_layout()
plt.show()



# 9 - RAD x MEDV
print("\n=== Correlação entre RAD e MEDV ===")
x = pd.to_numeric(dados['RAD'], errors='coerce'); y = pd.to_numeric(dados['MEDV'], errors='coerce')
mask = x.notna() & y.notna(); x = x[mask]; y = y[mask]
corr, p_value = stats.pearsonr(x, y)
direcao = "positiva" if corr > 0 else "negativa"
forca = "fraca" if abs(corr) < 0.3 else ("moderada" if abs(corr) < 0.7 else "forte")
print(f"Coeficiente de Pearson: {corr:.4f}")
print(f"Valor-p: {p_value:.10f}")
print(f"A correlação é {direcao} e {forca}.")
print("Rejeita-se H0 → relação significativa." if p_value < alpha else "Não é possível rejeitar H0 → sem relação significativa.")
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.scatter(x, y, alpha=0.7, color='teal')
plt.xlabel('RAD'); plt.ylabel('MEDV')
plt.title(f'Dispersão: r = {corr:.3f}')
plt.subplot(1,2,2)
sns.regplot(x=x, y=y, ci=None, color='teal')
plt.title('Reta de Regressão')
plt.tight_layout()
plt.show()



# 10 - TAX x MEDV
print("\n=== Correlação entre TAX e MEDV ===")
x = pd.to_numeric(dados['TAX'], errors='coerce'); y = pd.to_numeric(dados['MEDV'], errors='coerce')
mask = x.notna() & y.notna(); x = x[mask]; y = y[mask]
corr, p_value = stats.pearsonr(x, y)
direcao = "positiva" if corr > 0 else "negativa"
forca = "fraca" if abs(corr) < 0.3 else ("moderada" if abs(corr) < 0.7 else "forte")
print(f"Coeficiente de Pearson: {corr:.4f}")
print(f"Valor-p: {p_value:.10f}")
print(f"A correlação é {direcao} e {forca}.")
print("Rejeita-se H0 → relação significativa." if p_value < alpha else "Não é possível rejeitar H0 → sem relação significativa.")
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.scatter(x, y, alpha=0.7, color='olive')
plt.xlabel('TAX'); plt.ylabel('MEDV')
plt.title(f'Dispersão: r = {corr:.3f}')
plt.subplot(1,2,2)
sns.regplot(x=x, y=y, ci=None, color='olive')
plt.title('Reta de Regressão')
plt.tight_layout()
plt.show()



# 11 - PTRATIO x MEDV
print("\n=== Correlação entre PTRATIO e MEDV ===")
x = pd.to_numeric(dados['PTRATIO'], errors='coerce'); y = pd.to_numeric(dados['MEDV'], errors='coerce')
mask = x.notna() & y.notna(); x = x[mask]; y = y[mask]
corr, p_value = stats.pearsonr(x, y)
direcao = "positiva" if corr > 0 else "negativa"
forca = "fraca" if abs(corr) < 0.3 else ("moderada" if abs(corr) < 0.7 else "forte")
print(f"Coeficiente de Pearson: {corr:.4f}")
print(f"Valor-p: {p_value:.10f}")
print(f"A correlação é {direcao} e {forca}.")
print("Rejeita-se H0 → relação significativa." if p_value < alpha else "Não é possível rejeitar H0 → sem relação significativa.")
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.scatter(x, y, alpha=0.7, color='brown')
plt.xlabel('PTRATIO'); plt.ylabel('MEDV')
plt.title(f'Dispersão: r = {corr:.3f}')
plt.subplot(1,2,2)
sns.regplot(x=x, y=y, ci=None, color='brown')
plt.title('Reta de Regressão')
plt.tight_layout()
plt.show()



# 12 - B x MEDV
print("\n=== Correlação entre B e MEDV ===")
x = pd.to_numeric(dados['B'], errors='coerce'); y = pd.to_numeric(dados['MEDV'], errors='coerce')
mask = x.notna() & y.notna(); x = x[mask]; y = y[mask]
corr, p_value = stats.pearsonr(x, y)
direcao = "positiva" if corr > 0 else "negativa"
forca = "fraca" if abs(corr) < 0.3 else ("moderada" if abs(corr) < 0.7 else "forte")
print(f"Coeficiente de Pearson: {corr:.4f}")
print(f"Valor-p: {p_value:.10f}")
print(f"A correlação é {direcao} e {forca}.")
print("Rejeita-se H0 → relação significativa." if p_value < alpha else "Não é possível rejeitar H0 → sem relação significativa.")
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.scatter(x, y, alpha=0.7, color='navy')
plt.xlabel('B'); plt.ylabel('MEDV')
plt.title(f'Dispersão: r = {corr:.3f}')
plt.subplot(1,2,2)
sns.regplot(x=x, y=y, ci=None, color='navy')
plt.title('Reta de Regressão')
plt.tight_layout()
plt.show()



# 13 - LSTAT x MEDV
print("\n=== Correlação entre LSTAT e MEDV ===")
x = pd.to_numeric(dados['LSTAT'], errors='coerce'); y = pd.to_numeric(dados['MEDV'], errors='coerce')
mask = x.notna() & y.notna(); x = x[mask]; y = y[mask]
corr, p_value = stats.pearsonr(x, y)
direcao = "positiva" if corr > 0 else "negativa"
forca = "fraca" if abs(corr) < 0.3 else ("moderada" if abs(corr) < 0.7 else "forte")
print(f"Coeficiente de Pearson: {corr:.4f}")
print(f"Valor-p: {p_value:.10f}")
print(f"A correlação é {direcao} e {forca}.")
print("Rejeita-se H0 → relação significativa." if p_value < alpha else "Não é possível rejeitar H0 → sem relação significativa.")
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.scatter(x, y, alpha=0.7, color='red')
plt.xlabel('LSTAT'); plt.ylabel('MEDV')
plt.title(f'Dispersão: r = {corr:.3f}')
plt.subplot(1,2,2)
sns.regplot(x=x, y=y, ci=None, color='red')
plt.title('Reta de Regressão')
plt.tight_layout()
plt.show()
