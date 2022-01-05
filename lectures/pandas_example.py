import pandas as pd

stores = pd.read_excel('nov29_groceries.xlsx', 1)

RI_stores = stores[stores['State'] == 'RI']

many_stores = stores[stores['Num_Grocery_Stores'] + stores['Num_Convenience_Stores'] > 500]

RI_stores_sorted = RI_stores.sort_values(by = 'Num_Grocery_Stores', ascending = False)

RI_stores['Num_Total_Stores'] = RI_stores['Num_Grocery_Stores'] + \
                                RI_stores['Num_Convenience_Stores']

RI_stores.plot.bar('County', 'Num_Total_Stores')
