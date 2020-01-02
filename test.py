import pandas as pd

df = pd.DataFrame({'values_1': ['700','ABC','500','XYZ','1200'],
                   'values_2': ['DDD','150','350','400','5000'] 
                   })

print (df)


df = df.apply(pd.to_numeric, errors='coerce')
print(df)