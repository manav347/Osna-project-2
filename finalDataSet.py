import pandas as pd

# Read the Excel file
df = pd.read_excel("original dataset.xlsx")

# Create a dictionary mapping new_id to a list of names
id_to_names = df.groupby('new_id')['name'].apply(list).to_dict()

# Replace new_id with name(s) in the Source column
df["Source"] = df["Source"].map(lambda x: ', '.join(id_to_names.get(x, [])))

# Replace new_id with name(s) in the Target column
df["Target"] = df["Target"].map(lambda x: ', '.join(id_to_names.get(x, [])))

# Save the updated DataFrame to a new Excel file
df.to_excel("final.xlsx", index=False)