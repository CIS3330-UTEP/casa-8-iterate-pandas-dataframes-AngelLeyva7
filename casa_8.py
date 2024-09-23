import pandas as pd 

file = pd.read_csv('big-mac-full-index.csv')

# 1. Method 4: Using iterrows() method
for i,r in file.iterrows():
    print(r['name'], r['iso_a3'], r['currency_code']) 
    
    
# 2. Method 6: Using apply() method    
print(file.apply(lambda row:  row['dollar_price'], axis = 1))    