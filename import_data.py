import pandas as pd
# Creata my own header
headers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Get the data from URL and assign it to variable called url
url = "https://archive.ics.uci.edu/mc/machine-learning-databases/autos/imports-85.names"

# Assign the data we downloaded above to a variable called df 
df = pd.read_csv(url)

# Add the header we created for this data. 
df.columns=headers

# Returns more data above the objects
print(df)
