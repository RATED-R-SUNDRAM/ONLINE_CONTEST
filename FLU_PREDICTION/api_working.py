#%%
import requests 
import json  

response = requests.get('https://api.stackexchange.com/2.3/comments?order=desc&sort=creation&site=stackoverflow')
print(type(response)) 
data = response.json()
print(type(data))
print(data.keys())
# %%
