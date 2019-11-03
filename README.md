# Search Engine Demo

### Scope:
This project is aimed towards showcasing a quick demo of implementing a Search Engine powered by Elasticsearch in the backend. The project performs 2 major functionalities:  
   1. Insert JSON files to Elasticsearch and index them
   2. Build a web page using Flask to retrieve search queries from the already inserted JSON files. 
   
### Pre-requisites
1. IDE - PyCharm, intellij, Eclipse etc.
2. Python - install [elasticsearch](https://pypi.org/project/elasticsearch/), flask, flask-wtf
3. [Elasticsearch](https://www.elastic.co/)
4. Sample Data set from [here](https://webhose.io/free-datasets/news-articles-by-topics/)

### Run and Execute
#### Start Elasticsearch engine 
1. Download [elasticsearch](https://www.elastic.co/)
2. Add entries to your `~/.bash_profile` (if using Mac)

    ```
    export ES_HOME=/Users/pavanpkulkarni/Documents/ELK/elasticsearch-7.4.2
    export PATH=$PATH:$ES_HOME/bin
    ```
  
3. Open terminal and run `source ~/.bash_profile`
4. Open another terminal and run `elasticsearch`
5. Verify if elasticsearch has started using - [http://localhost:9200/](http://localhost:9200/)
 
#### Load and Index JSON files in Elasticsearch 
1. Clone this git repo in your local.
2. Make sure you have you all the JSON files downloaded in your local.
3. Change the `iinputPath` variable in the file [InsertDataToElasticSearch.py](https://github.com/pavanpkulkarni/SearchEngine_ES_Flask/blob/master/com/pavanpkulkarni/es/InsertDataToElasticSearch.py) to point to the directory where you've downloaded all the sample dataset.
4. Run the script  [InsertDataToElasticSearch.py](https://github.com/pavanpkulkarni/SearchEngine_ES_Flask/blob/master/com/pavanpkulkarni/es/InsertDataToElasticSearch.py)
5. [http://localhost:9200/_search](http://localhost:9200/_search) should yield all results now. You can narrow the search using the query 
    http://localhost:9200/travelagent/_search?q=mexico

#### Start Search Engine
1. Run the script [SearchEngine_FlaskApp.py](https://github.com/pavanpkulkarni/SearchEngine_ES_Flask/blob/master/com/pavanpkulkarni/flask/SearchEngine_FlaskApp.py)
2. Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to view the search engine.
3. Search for any "Keyword" and click on "Search Keyword"
4. Retrieve all results by clicking on "Search All".
 
***P.S:*** This module is developed on Mac+intellij. Please customize as per your OS, IDE, local paths, port #, etc.