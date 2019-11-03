from flask_wtf import Form
from wtforms import SubmitField, StringField


class SearchTitleForms(Form):
    q = StringField("Keyword")
    submit = SubmitField("Search Keyword")
    search_all = SubmitField("Search All")
