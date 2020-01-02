import pandas as pd
# Creata my own header
headers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Get the data from URL and assign it to variable called url
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

# Assign the data we downloaded above to a variable called df 
df = pd.read_csv(url)

# Add the header we created for this data. 
df.columns=headers

# Print out  the data
print(df.tail(10))

# Export too "/tmp/somefile"
df.to_csv("/tmp/somefile")

# Gives data type for columns
print(df.dtypes)

# Returns more data above the objects
print(df.describe())

# Full summary statistics including Data for objects
print(df.describe(include="all"))


# Gives memory related information
print(df.info())

print(df['a'])