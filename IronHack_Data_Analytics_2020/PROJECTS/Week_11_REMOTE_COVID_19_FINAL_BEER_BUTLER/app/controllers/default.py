from app import app, db
from flask import render_template, url_for, request, redirect
from app.models.forms import BeerForm, age_choices
from app.models.tables import Beer_Table
import pandas as pd
import numpy as np
from secret import engine

conn = engine.connect()
metadata = db.MetaData()
beer = db.Table('beer', metadata)


@app.route('/index')
@app.route('/', methods=['GET','POST'])
def index():
    beer_form = BeerForm()
    if request.method == 'POST':
        age_res = str(beer_form.age.data.split('-')[0].strip()), str(beer_form.age.data.split('-')[1].strip())
        abv_res = float(beer_form.abv.data.split('-')[0].strip()), float(beer_form.abv.data.split('-')[1].strip())
        ibu_res = int(beer_form.ibu.data.split('-')[0].strip()), int(beer_form.ibu.data.split('-')[1].strip())
        srm_res = int(beer_form.srm.data.split('-')[0].strip()), int(beer_form.srm.data.split('-')[1].strip())

        beer_df = pd.read_csv('data/beer_final.csv')
        result = beer_df[(beer_df['ABV_max'] >= abv_res[0]) & (beer_df['ABV_max'] <= abv_res[1]) &
                      (beer_df['IBU_max'] >= ibu_res[0]) & (beer_df['IBU_max'] <= ibu_res[1]) &
                      (beer_df['SRM_max'] >= srm_res[0]) & (beer_df['SRM_max'] <= srm_res[1])]
        final = pd.DataFrame(columns=['style_name', 'recommend', 'gender', 'age'])
        final[['style_name', 'recommend']] = result[['style_name', 'recommend']]
        final[['gender', 'age']] = beer_form.gender.data, age_res
        final.to_sql('beer', conn, if_exists='append')
        styles = [x for x in result['style_name']]
        imgs = [x for x in result['images']]
        caps = [x for x in result['recommend']]
        return render_template('index.html', beer_form=beer_form, zipped_results=zip(styles, imgs, caps), reco=caps)
    return render_template('index.html', beer_form=beer_form)


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')
