import streamlit as st
import pickle as pkl
import pandas as pd

st.title('Anime Recommender System')
recommended= pd.read_csv('recommend.csv')
print(recommended)
anime_dict = pkl.load(open('anime_dict.pkl', 'rb'))
anime = pd.DataFrame(anime_dict)

selected_anime = st.selectbox(
    'Selected one of your favourite anime from these:',
    anime['Anime_Name'].values)


def recommend(selected_anime):
    anime_idx = anime[anime['Anime_Name'] == selected_anime].index[0]
    #select_prod = df.loc[df['Type'] == 'Electronic']
    return recommended.iloc[anime_idx]


# def set_bg_hack_url():
#     '''
#      A function to unpack an image from url and set as bg.
#      Returns
#      -------
#      The background.
#      '''
#
#     st.markdown(
#         f"""
#          <style>
#          .stApp {{
#              background: url("https://wallpaperaccess.com/full/2661458.jpg");
#              background-size: cover
#
#          }}
#          </style>
#          """,
#         unsafe_allow_html=True
#     )
#
# set_bg_hack_url()
if st.button('Recommend'):
    print('Check out these: ')
    for s in recommend(selected_anime):
        name= s.replace(' ', '')
        link= 'https://www.google.com/search?q='+name
        st.write("["+str(s)+"]("+str(link)+")")
st.header("HAPPY WATCHING!!")