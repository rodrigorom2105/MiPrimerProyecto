import pandas as pd

# Carga los datos
FILEPATH = "C:/Users/rocob/OneDrive/Documentos/Tec/3er Semestre/AnalisisPython/spotify.csv"
df = pd.read_csv(FILEPATH)
print(df.head())
print("\n")
print(df.info())

print("\nCantidad de filas y columnas:")
print(df.shape)
print("\nNombres de las columnas:")
print(df.columns.tolist())

# Valores nulos por columna
print("\nValores nulos por columna:")
valores_nulos = df.isnull().sum()
print(valores_nulos)

print("\nTipos de datos de cada variable:")
print(df.dtypes)

print("\nEstadísticas descriptivas:")
print(df.describe())

print("\nRangos (mínimo y máximo) de cada variable numérica:")
for col in df.select_dtypes(include='number').columns:
    print(f"{col}: min = {df[col].min()}, max = {df[col].max()}")
    
stats = pd.DataFrame({
"Media": df.mean(numeric_only=True),
"Mediana": df.median(numeric_only=True),
"Desviación estándar": df.std(numeric_only=True)
})
print("\nMedias, medianas y desviaciones estándar:")
print(stats)
