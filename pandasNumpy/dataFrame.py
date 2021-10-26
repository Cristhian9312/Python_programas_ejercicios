import pandas as pd 

# DIFERENTES FORMAS DE MOSTRAR LA TABLA CON DATAFRAME

persnas = {
    "peso": pd.Series([54,58,65,25,30],["santiago","cristhian","julian","juan","luis"]),
    "altura": pd.Series({"luis":165,"santiago":170,"cristhian":178,"julian":173,"juan":160}),
    "hijos": pd.Series([2,5],["pedro","luis"])
}

df = pd.DataFrame(persnas)
print(df,"\n") # muestra como tabla los datos ingresados en el diccionaro sin importar el orden ingresado, lo ordena 
df = pd.DataFrame(persnas, columns=["peso","altura"], index=["cristhian","santiago"])
print(df,"\n") # filtra como una consulta 

valores = [
    [185,654,789],
    [456,789,123],
    [987,654,321]
    ]

de = pd.DataFrame(valores, columns=["altura","hijos","peso"], index=["pedro","ana","juan"])
print(de,"\n")

personas = {
    "altura": {"santiago":458,"laura":56,"juan":45},
    "peso" : {"santiago": 45, "laura":52, "juan":45}
}
pe = pd.DataFrame(personas)
print(pe,"\n")

# ACCESO A LOS ELEMENTOS DEL DATAFRAME

persnas = {
    "peso": pd.Series([54,58,65,25,30],["santiago","cristhian","julian","juan","luis"]),
    "altura": pd.Series({"luis":165,"santiago":170,"cristhian":178,"julian":173,"juan":160}),
    "hijos": pd.Series([2,5],["pedro","luis"])
}
df = pd.DataFrame(persnas)
print(df["peso"],"\n")# solo regresa un valor de la tabla
print(df[["peso","altura"]],"\n")# solo regresa los filtros 
print(df[df["peso"] > 50]) # calculos, filtro de consultas
print(df[(df["peso"]>50) & (df["altura"]>=170)])

print(df.loc["santiago"])
print(df.iloc[2])# me arroja solo la fila de datos del posicion 2


# cosulta avanzada de dataframe

df.query("altura > 170 and peso > 60") #se puede hacer consultas con solo palabras con query
print(df)

# copiar un dataframe 

persnas = {
    "peso": pd.Series([54,58,65,25,30],["santiago","cristhian","julian","juan","luis"]),
    "altura": pd.Series({"luis":165,"santiago":170,"cristhian":178,"julian":173,"juan":160}),
    "hijos": pd.Series([2,5],["pedro","luis"])
}
df = pd.DataFrame(persnas)
df_copy = df.copy()

# Modificacion de dataframe 

persnas = {
    "peso": pd.Series([54,58,65,25,30],["santiago","cristhian","julian","juan","luis"]),
    "altura": pd.Series({"luis":165,"santiago":170,"cristhian":178,"julian":173,"juan":160}),
    "hijos": pd.Series([2,5],["pedro","luis"])
}
df = pd.DataFrame(persnas)
df["cumpleaños"]=[1990,1998,1993,2000,2021,1999]# se tienen que asignar la misma cantidad con la cantidad de filas
print(df)

df["años"]= 2021 - df["cumpleaños"]# calcula la edad que tiene la persona agregando una culumna
print(df)

# añadir una nueva culumna creando un dataframe nuevo

persnas = {
    "peso": pd.Series([54,58,65,25,30],["santiago","cristhian","julian","juan","luis"]),
    "altura": pd.Series({"luis":165,"santiago":170,"cristhian":178,"julian":173,"juan":160}),
    "hijos": pd.Series([2,5],["pedro","luis"])
}
df = pd.DataFrame(persnas)
df_nuv = df.assign(mascotas =[1,2,3,4,5,7])
print(df_nuv)

# Eliminar una columna del dataframe 

persnas = {
    "peso": pd.Series([54,58,65,25,30],["santiago","cristhian","julian","juan","luis"]),
    "altura": pd.Series({"luis":165,"santiago":170,"cristhian":178,"julian":173,"juan":160}),
    "hijos": pd.Series([2,5],["pedro","luis"])
}
df = pd.DataFrame(persnas)
del df["hijos"]
print(df)

# evaluar una funcion sobre una columna 

persnas = {
    "peso": pd.Series([54,58,65,25,30],["santiago","cristhian","julian","juan","luis"]),
    "altura": pd.Series({"luis":165,"santiago":170,"cristhian":178,"julian":173,"juan":160}),
    "hijos": pd.Series([2,5],["pedro","luis"])
}
df = pd.DataFrame(persnas)
print(df.eval("altura / 2")) # divide la columna altura entre dos

# Asignar el valor resultante 

persnas = {
    "peso": pd.Series([54,58,65,25,30],["santiago","cristhian","julian","juan","luis"]),
    "altura": pd.Series({"luis":165,"santiago":170,"cristhian":178,"julian":173,"juan":160}),
    "hijos": pd.Series([2,5],["pedro","luis"])
}
df = pd.DataFrame(persnas)
df.eval("media_altura = altura / 2", inplace=True)# agrega una columna con la funcion implementada
print(df)

# evaluar una funcion evaluando una variable local 

persnas = {
    "peso": pd.Series([54,58,65,25,30],["santiago","cristhian","julian","juan","luis"]),
    "altura": pd.Series({"luis":165,"santiago":170,"cristhian":178,"julian":173,"juan":160}),
    "hijos": pd.Series([2,5],["pedro","luis"])
}
df = pd.DataFrame(persnas)
max_altura = 180
print(df.eval("altura > @max_altura"))# me dice si cumple o no la condicion con la variable local

# aplicar una funcion externa 

persnas = {
    "peso": pd.Series([54,58,65,25,30],["santiago","cristhian","julian","juan","luis"]),
    "altura": pd.Series({"luis":165,"santiago":170,"cristhian":178,"julian":173,"juan":160}),
    "hijos": pd.Series([2,5],["pedro","luis"])
}
df = pd.DataFrame(persnas)

def func(x):
    return x+2

print(df["peso"].apply(func))

# Guardar y cargar un dataframe en disco 

persnas = {
    "peso": pd.Series([54,58,65,25,30],["santiago","cristhian","julian","juan","luis"]),
    "altura": pd.Series({"luis":165,"santiago":170,"cristhian":178,"julian":173,"juan":160}),
    "hijos": pd.Series([2,5],["pedro","luis"])
}
df = pd.DataFrame(persnas)
df.to_csv("df_personas.csv")
df.to_html("de_personas.html")
df.to_json("df_personas.json")  
