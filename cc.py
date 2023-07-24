import pandas as pd
import requests
from bs4 import BeautifulSoup
Product_name=[]
Prices=[]
Description=[]
Review=[]
url="https://www.amazon.in/s?k=laptops+under+50000&crid=B1HBK4HP9F9N&sprefix=laptops+under%2Caps%2C569&ref=nb_sb_ss_ts-doa-p_5_13="+str(1)

r=requests.get(url)
#print(r)
s=BeautifulSoup(r.text,"html.parser")
#parsing:means convert standard in easily way to unstandard.

names=s.find_all("span",class_="a-size-medium a-color-base a-text-normal")
#parsing karne k baad  beautiful soup librabrary ki help  class k ander walo ko find karra.
 
 

#
for i in names:
    name=i.text
    Product_name.append(name)
print(len(Product_name))

prices=s.find_all("span",class_="a-price-whole")
for i in prices:
    name=i.text
    Prices.append(name)
print(len(Prices))


desc=s.find_all("div",class_="a-section a-spacing-none a-spacing-top-micro")

for i in desc:
    name=i.text
    Description.append(name)
    
#dataframe:tabular from m data ko show karta hai.
#productname!=price  to data frame banegaaa 

df=pd.DataFrame({"Product Name":Product_name,"Prices":Prices})

print(df)