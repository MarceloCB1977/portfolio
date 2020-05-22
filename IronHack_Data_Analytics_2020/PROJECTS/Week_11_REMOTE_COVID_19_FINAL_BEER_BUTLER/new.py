import streamlit as st
import pandas as pd
import numpy as np
import sqlalchemy as db
from secret import engine


conn = engine.connect()
metadata = db.MetaData()
beer = db.Table('beer', metadata)


age = st.sidebar.selectbox('Selecione a sua idade',
                          ('18 - 24', '25 - 29', '30 - 34', '35 - 39', '40 - 49', '50 - 59', '60 - 69', '70 +' ))

gender = st.sidebar.selectbox('Selecione seu gênero',
                             ('Masculino', 'Feminino', 'Outros'))

st.title('The Beer Butler')

text = 'Para sua referência, Uma SKOL tem Teor Alcóolico de 4.6, Amargor de 8.'

st.sidebar.markdown(f"<span style='color: green;font-size: 15px; font-weight:bold'>{text}</span>", unsafe_allow_html=True)

st.sidebar.title("Encontre a sua cerveja artesanal")


abv = st.sidebar.selectbox("Escolha o nível de Teor Alcóolico",
                          ('3.6 - 4.8', '4.9 - 6.0', '6.1 - 7.2', '7.3 - 9.6', '9.7 - 14.4'))

ibu = st.sidebar.selectbox("Escolha o nível de Amargor",
                          ('12 - 28', '29 - 44', '45 - 60', '61 - 100'))

srm = st.sidebar.selectbox("Escolha a Claridade",
                          ('Cerveja Clara - 1 - 14', 'Cerveja Escura - 15 - 100'))


if st.sidebar.button('Enviar'):
    abv_res = float(abv.split('-')[0].strip()), float(abv.split('-')[1].strip())
    ibu_res = int(ibu.split('-')[0].strip()), int(ibu.split('-')[1].strip())
    srm_res = int(srm.split('-')[1].strip()), int(srm.split('-')[2].strip())

    beer = pd.read_csv('data/beer_final.csv')
    result = beer[(beer['ABV_max'] >= abv_res[0]) & (beer['ABV_max'] <= abv_res[1]) &
                  (beer['IBU_max'] >= ibu_res[0]) & (beer['IBU_max'] <= ibu_res[1]) &
                  (beer['SRM_max'] >= srm_res[0]) & (beer['SRM_max'] <= srm_res[1])]
    final = pd.DataFrame(columns=['style_name', 'recommend', 'gender', 'age'])
    final[['style_name', 'recommend']] = result[['style_name', 'recommend']]
    final[['gender', 'age']] = gender, age
    final.to_sql('beer', conn, if_exists='append')
    styles = [x for x in result['style_name']]
    imgs = [x for x in result['images']]
    caps = [x for x in result['recommend']]
    st.subheader('Cervejas recomendadas para você, por estilo')
    st.image(imgs, caption=caps, width=200)

    #if st.button('Onde comprar'):
        #pass
    #else:
        #pass
else:
    st.subheader('Se você nunca experimentou Cervejas Artesanais, por não saber "qual é boa", e pelo investimento ser alto, para comprar e depois não gostar.')
    st.subheader('Este sistema foi criado pensando em você!')
    st.subheader('Bem vindo ao Sistema de Recomendação de Cervejas Artesanais')
    st.title('Selecione das listas ao lado e clique em "Enviar"')
