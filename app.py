from flask import Flask, request
from parser.netflix import Netflix
from parser.youtube import Youtube
from parser.apple import Apple

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


@app.route('/')
def search():
    searchword = request.args.get('title', 'Argo')

    netflix = Netflix()
    youtube = Youtube()
    itunes = Apple()

    #movie = youtube.get_movie_by_title(searchword)
    #movie = netflix.get_movie_by_title(searchword)
    movie = itunes.get_movie_by_title(searchword)

    return '{0}\n'.format(movie)

if __name__ == '__main__':
    app.run()
