import pandas as pd

# Create a dataframe
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [25, 32, 18, 47],
        'country': ['USA', 'Canada', 'Australia', 'UK']}
df = pd.DataFrame(data)

new_data = {'name': 'Emma', 'age': '23', 'country': 'France'}


df["some"] = [3, 2, 5, 5]

# Print the dataframe
print(df)