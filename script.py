import pandas as pd

# Dataset URL
url = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"

# Read the dataset from the url
df = pd.read_csv(url)

# Print random sample of 5
print(df.sample(5))
