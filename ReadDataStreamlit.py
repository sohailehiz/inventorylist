import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
# importing module for regex
import re


def convert(row):
    #print(row)
    return '<a href="{}">{}</a>'.format(row['ProductLink'],  row.name)

def convertInv(row):
    #print(row)
    return '<a href="{}">{}</a>'.format(row['SearchOnLine'],  row.name)

def convertImg(row):
    #print(row)
    return '<img src="{}">'.format(row['ProductImage'],  row.name)

def convertImgInv(row):
    #print(row)
    return '<img src="{}">'.format(row['img'],  row.name)

pd.set_option('display.max_colwidth', -1)

sizes = {'h=831':'h=200', 'w=615':'w=115'}
webfileurl = "https://docs.google.com/viewer?url=https%3A%2F%2Fgithub.com%2Fsohailehiz%2Finventorylist%2Fblob%2Fmain%2FInventoryData1.xlsx"
invfileurl = "https://docs.google.com/viewer?url=https%3A%2F%2Fgithub.com%2Fsohailehiz%2Finventorylist%2Fblob%2Fmain%2FInventoryData1.xlsx"

st.title('Life Style')
df  = pd.read_excel('F:\Development\DressIT\Brands\LIFESTYLE\Files\WebsiteData.xlsx', index_col=0)
df2 = pd.read_excel(invfileurl, index_col=0)      

#user_input = 'White graphic print'
#ui = user_input.split(" ")
df['SearchColumn'] = df['SearchColumn'].str.upper()
df2['SearchColumn'] = df2['SearchColumn'].str.upper()
user_input = st.text_input("Search Product", "red top")
ui = user_input.split(" ")
for i in range(len(ui)):
    def matcher(x):
        z= "-"+ui[i]+"-"
        if z.upper() in x.upper():
            return z
        else:
            return np.nan
    df['Match'] = df['SearchColumn'].apply(matcher)
    df2['Match'] = df2['SearchColumn'].apply(matcher)
    if i == 0:
        df = df[(df.Match.notnull())]
        df2 = df2[(df2.Match.notnull())]
    else:
        df = df#df[(df.Match.notnull())]
        df2 = df2#df[(df.Match.notnull())]
    res = df
    res2 = df2
    temp = res
    temp2 = res2
    df = temp
    df2 = temp2

empty = pd.DataFrame(columns=['lookupvalue','ProductLink','ProductTitle','ProductColor','ProductPrice','ProductImage','ProductGender','ProductType','SearchColumn','Match'],index=['Empty'])
empty2 = pd.DataFrame(columns=['ITEM_PARENT_OPTION','COLOR','SIZE_DESC','BRAND_NAME','MRP','SOH_QTY','SearchColumn','Stock','img','Match','SearchOnLine'],index=['Empty'])

df = pd.concat([df,empty])
df2 = pd.concat([df2, empty2])

print(df)
print(df2)
webempty = empty[["ProductLink", "ProductTitle","ProductImage"]]
invempty = empty2[["BRAND_NAME", "ITEM_PARENT_OPTION","SIZE_DESC","Stock","img","SearchOnLine"]]

df['ProductLink']  = df.apply(convert, axis=1)
df['ProductImage'] = df['ProductImage'].str.replace('h=831','h=250')
df['ProductImage'] = df['ProductImage'].str.replace('w=615','w=115')
df['ProductImage'] = df.apply(convertImg, axis=1)

df2['SearchOnLine'] = df2.apply(convertInv, axis=1)
df2['img'] = df2['img'].str.replace('h=345','h=200')
df2['img'] = df2['img'].str.replace('w=345','w=115')
df2['img'] = df2.apply(convertImgInv, axis=1)

web = df[["ProductLink", "ProductTitle","ProductImage"]]
inv = df2[["BRAND_NAME", "ITEM_PARENT_OPTION","SIZE_DESC","Stock","img","SearchOnLine"]]

print(inv)

if st.button('Check On Website'):
    if st.button('Check On In Store Inventory'):
        st.title('Inventory')
        st.markdown(inv.to_html(escape=False, index=False), unsafe_allow_html=True)
    else:
        st.title('Website Products')
        st.markdown(web.to_html(escape=False, index=False), unsafe_allow_html=True)
else:
    st.title('Inventory')
    st.markdown(inv.to_html(escape=False, index=False), unsafe_allow_html=True)


