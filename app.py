from flask import Flask, request
from parser.netflix import Netflix

app = Flask(__name__)
app.debug = True
services = ['Netflix',
            'Amazon',
            'Hulu',
            'Youtube',
            'GooglePlay',
            'Redbox',
            'iTunes',
            'Vudu',
            'ePix',
            'xfinity'
            ]

netflix = Netflix()

@app.route('/')
def search():
    searchword = request.args.get('title', 'Argo')
    
    movie = netflix.get_movie_by_title(searchword)
    return '{0}\n'.format(movie)

if __name__ == '__main__':
    app.run()
