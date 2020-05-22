from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

age_choices = []

class BeerForm(FlaskForm):
    age = SelectField(u'age_test', choices=[('18 - 24', '18 - 24'), ('25 - 29', '25 - 29'),
                                           ('30 - 34', '30 - 34'), ('35 - 39', '35 - 39'),
                                           ('40 - 49', '40 - 49'), ('50 - 59', '50 - 59'),
                                           ('60 - 69', '60 - 69'), ('70 - 100', '70 - 100')])

    gender = SelectField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Outros', 'Outros')])

    abv = SelectField(choices=[('3.6 - 4.8', '3.6 - 4.8'),('4.9 - 6.0', '4.9 - 6.0'),
                               ('6.1 - 7.2', '6.1 - 7.2'), ('7.3 - 9.6', '7.3 - 9.6'),
                               ('9.7 - 14.4', '9.7 - 14.4')])

    ibu = SelectField(choices=[('12 - 28', '12 - 28'), ('29 - 44', '29 - 44'),
                               ('45 - 60', '45 - 60'), ('61 - 100', '61 - 100')])

    srm = SelectField(choices=[('1 - 14 - Cerveja Clara', '1 - 14 - Cerveja Clara'),
                               ('15 - 100 - Cerveja Escura', '15 - 100 - Cerveja Escura')])
