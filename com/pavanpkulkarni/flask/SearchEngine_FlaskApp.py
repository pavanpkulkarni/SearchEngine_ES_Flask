from elasticsearch import Elasticsearch
from flask import Flask, render_template, request
from SearchForm import SearchTitleForms

es = Elasticsearch('http://localhost:9200')
app = Flask(__name__)
app.secret_key = 'my secret key'


@app.route('/', methods=['GET'])
@app.route('/search', methods=['POST', 'GET'])
def search():
    form = SearchTitleForms()

    if request.method == 'POST':
        if form.submit.data:
            q = request.form['q']
            print("We are looking for : ", q, " In elastic search ")

            body = {
                "query": {
                    "multi_match": {
                        "query": q
                    }
                }
            }

            results = es.search(index='travelagent', body=body, sort="_score")
            return render_template('es_searchengine.html', form=form, response=results)

        elif form.search_all.data:
            body = {"query": {"match_all": {}}}
            results = es.search(index='travelagent', body=body, sort="_score")
            return render_template('es_searchengine.html', form=form, response=results)

    elif request.method == 'GET':
        return render_template('es_searchengine.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
