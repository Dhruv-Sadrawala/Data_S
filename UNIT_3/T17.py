import numpy as np
import pandas as pd

# 7. Data:
# Product=['Pen','Notebook','Pencil']
# Price=[10,50,5]
# Export DataFrame to Excel 'sales.xlsx'.
#incomplete
#incomplete

data = {
		'Product':['Pen','Notebook','Pencil'],
		'Price':[10,50,5]
}

df = pd.DataFrame(data)

print(df)

with open("sales.xlsx","w") as file:
	file.write(df)

print("File Saved.")