import pandas as pd 

file = '/workspaces/api-geo/code/dados_ibge_part1.json'

df = pd.read_json(file)
print(df)