import pandas as pd

# Cargar el dataset
df = pd.read_csv('data/metadata.csv')

# Mostrar las primeras filas para tener una idea general del dataset
print(df.head())

# Ver información sobre el dataset (columnas, tipos de datos, valores nulos, etc.)
print(df.info())

# Estadísticas descriptivas
print(df.describe())

# Análisis de estadística descriptiva de la población y otros atributos
print(df[['Population2007', 'Population2008', 'Population2009', 'Population2010']].describe())

# Revisar valores faltantes
print(df.isnull().sum())

# Eliminar filas con valores nulos
df.dropna(inplace=True)

# Eliminar duplicados
df.drop_duplicates(inplace=True)

# Convertir variables categóricas en numéricas (ejemplo: municipio)
df_municipalities = pd.get_dummies(df, columns=['Municipality'])

print("TIPOS: ")
# Verificar el tipo de datos de cada columna
print(df.dtypes)

# Verificar el tipo de la columna '2019/w48'
print(df['2019/w48'].dtype)




