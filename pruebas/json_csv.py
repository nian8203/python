import pandas as pd
df = pd.read_json (r'/home/nian/Documentos/minTIC/prueba.json')
export_csv = df.to_csv (r'/home/nian/Documentos/minTIC/prueba.csv', index = None, header=True)


