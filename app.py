from pandas.io.parsers import read_csv
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

plt.style.use('seaborn')

@st.cache
def load_data():
    df = read_csv("video_games.csv",index_col=0)
    return df

st.title("Heading of Mini Project")
st.sidebar.header("Project Options")

options = [
    'About Project',
    'Game Genre Analysis',
    'Game Score vs Duration']

choice = st.sidebar.selectbox("select an option",options)

df = load_data()

if choice == options[0]:
    st.image("image.png")
    st.header("This is About the project")
    st.info('''Blah blah blah, Blah blah blah Blah blah blah Blah blah blah
    Blah blah blah Blah blah blah Blah blah blah Blah blah blah
    Blah blah blahBlah blah blahBlah blah blahBlah blah blahBlah blah blahBlah blah blah
    Blah blah blahBlah blah blah
    ''')
elif choice == options[1]:
    color = st.sidebar.color_picker("select graph color")
    genre_limit = st.sidebar.number_input("How many top genres",3,25,10)
    fig,ax = plt.subplots()
    df['Metadata.Genres'].value_counts().head(genre_limit).plot(
                    kind='barh', 
                    figsize=(7,10),
                    ax=ax,
                    color=color)
    st.pyplot(fig)

elif choice == options[2]:
    fig,ax = plt.subplots(figsize=(10,5))
    df.plot.scatter(x='Metrics.Review Score',y='Length.All PlayStyles.Polled',title='Game Length vs Game Duration',s='Metrics.Review Score',c='Length.All PlayStyles.Polled',cmap='rainbow',ax=ax)
    st.pyplot(fig)