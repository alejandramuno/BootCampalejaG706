import pandas as pd
# crear datos (simulacion estudiantes)
datos={
    "nombre":["ana","luis","carlos","sofia","pedro"],
    "edad":[30,70,18,21,22],
    "nota":[3.5,4.2,2.8,4.8,3.0]
}

df =pd.DataFrame(datos)
print(df)

#Promedio de notas 
print("promedio:",df["nota"].mean())

#Promedio de edad
print("promedio:",df["edad"].mean())