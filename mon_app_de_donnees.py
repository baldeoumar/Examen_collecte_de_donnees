
import streamlit as st
import pandas as pd

#st.write(st.session_state["browser_language"])

st.markdown("<h2 style='text-align: center; color: black;'>MY DATA SHARING APP</h2>", unsafe_allow_html=True)

st.markdown("""
This app allows you to download scraped data car and moto from Dakar-auto
* **Python libraries:** base64, pandas, streamlit
* **Data source:** [Dakar-auto](https://dakar-auto.com/).
""")


# Fonction de loading des données
def load_(dataframe, title, key) :
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)

    if st.button(title,key):
      
        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
        st.dataframe(dataframe)

# définir quelques styles liés aux box
st.markdown('''<style> .stButton>button {
    font-size: 12px;
    height: 3em;
    width: 25em;
}</style>''', unsafe_allow_html=True)

st.markdown( """
                    Scraped Prores Data with BeautifulSoup 
                    * ** Link:* [Codes de scrapping](https://drive.google.com/drive/folders/1lrntuYJAXEOBt6SnTWzWRe_iBt47uOR6?usp=sharing)
                    
                     """)
# Charger les données 
load_(pd.read_csv('data/bs_dakar_voitures_data.csv'), 'Car BeautifulSoup data', '1')
load_(pd.read_csv('data/bs_moto-data.csv'), 'motorcycle Beautiful data', '2')
load_(pd.read_csv('data/bs_location_voiture_data.csv'), 'Car rental BeautifulSoup data', '3')

st.markdown( """
            
            Improres data scraped with Web Scraper
            
            """)
load_(pd.read_csv('data/web_dakar_voitures_data.csv'), 'Car Web Scraper data', '4')
load_(pd.read_csv('data/web_dakar_moto_data.csv'), 'motorcycle Web Scraper data', '5')
load_(pd.read_csv('data/web_dakar_location_data.csv'), 'Car rental Web Scraper data', '6')



 


