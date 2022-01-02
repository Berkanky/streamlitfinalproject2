import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)
@st.cache
def countryfilter(countryname):
    countryfind=dosya[dosya["country"].str.contains(countryname)]
    return countryfind

@st.cache
def filterofcountry(countryofname):
    countryoffind=dosya4[dosya4["country"].str.contains(countryofname)]
    return countryoffind

@st.cache
def countryfilternew(nameofcountry):
    countryfound=dosya5[dosya5["country"].str.contains(nameofcountry)]
    return countryfound

dosya=pd.read_csv("uni2022.csv")
st.title("University Scores(Only 2022)")
dosya=dosya.drop(columns=["link","logo"])
dosya.columns=["year","rank","university","score","country","city","region"]
dosya["score"]=dosya["score"].fillna(0)
region=dosya.set_index("region")
regions=region.index
regions=list(regions.unique())
score=dosya["score"]
minscore=int(min(score))
maxscore=int(max(score))

listofcountries=list(dosya["country"].unique())
listofcountries.insert(0,"All Countries")
col1,col2=st.columns(2)
with col2:
    regionst = st.multiselect("Choose Region", regions,default=regions)
    #countryst=st.text_input("Enter Country Name")
    scorest=st.slider("Min Score",minscore,maxscore)
    selectcountriesst=st.selectbox("Choose Country",listofcountries)
    if regionst:
        dosya=region.loc[regionst]
        dosya=dosya.reset_index()
    if scorest:
        dosya=dosya[dosya["score"]>=scorest]
    #if countryst:
        #dosya = countryfilter(countryst)
    if selectcountriesst!="All Countries":
        dosya=dosya[dosya["country"]==selectcountriesst]
with col1:
    st.dataframe(dosya)
st.title("Number of Universities (Only 2022) ")
dosya2=pd.read_csv("uni2022.csv")
dosya2=dosya2.drop(columns=["link","logo"])
dosya2.columns=["year","rank","university","score","country","city","region"]
dosya2=dosya2.drop(columns=["year","rank","score","university"])
columns=list(dosya2.columns)
columnst = st.selectbox("Choose Column", columns)
if columnst:
    dosya2=dosya2[columnst]
    datas=dosya2.value_counts()
    x=datas.index
    y=datas.values
    fig=px.bar(dosya2,x,y)
    st.plotly_chart(fig,use_container_width=True)
st.title("Number Of Universities For All Years(2017-2022)")
df2=pd.read_csv("all.csv")
df2=df2.drop(columns=["link","logo","rank_display","university","score"])
df2.columns=["year","country","city","region"]
allcolumns=list(df2.columns)
defaultx=allcolumns.index("country")
col1,col2=st.columns(2)
with col1:
    firstst=st.selectbox("Select Column",allcolumns,index=defaultx)
    allrows=list(df2[firstst].unique())
with col2:
    secondst=st.selectbox("Select Row",allrows)

df2=df2[df2[firstst]==secondst]

secondvalues=df2["year"].value_counts()
x2=secondvalues.index
y2=secondvalues.values
radiobt=st.radio("Select Option",["Graph Pie","DataFrame"])
if radiobt=="Graph Pie":
    fig=px.pie(df2,values=y2,names=x2)
    st.plotly_chart(fig,use_container_width=True)
if radiobt=="DataFrame":
    yearslist = list(df2["year"].unique())
    yearslist.insert(0, "All Years")
    yearselectbox = st.selectbox("Select Year", yearslist)
    if yearselectbox != "All Years":
        df2 = df2[df2["year"] == yearselectbox]
    col1,col2=st.columns(2)
    with col1:
        st.dataframe(df2)
    with col2:
        st.write(df2["city"].value_counts())



















