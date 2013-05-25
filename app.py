from flask import Flask, request
from parser.netflix import Netflix
from parser.youtube import Youtube
from parser.apple import Apple
import json

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
youtube = Youtube()
itunes = Apple()

@app.route('/')
def home():
    searchword = request.args.get('title', 'Argo')

    #movie = youtube.get_movie_by_title(searchword)
    #movie = netflix.get_movie_by_title(searchword)
    movie = itunes.get_movie_by_title(searchword)

    return '{0}\n'.format(movie)



information = {
              }
"""
api definition
 /api/search.json?title=title

 Parameters
 title: title of the movie to search

 Returns
 [list of movies] on success
 {"error":error} on error

"""

@app.route('/api/search.json')
def search():
    title = 'Argo'
    orderby = 'stream'
    search_term = request.args.get('title', title)
    ret = [
           {
            'title': search_term,
            'availability':[],
            'orderby': orderby
           }
          ]

    yt = youtube.get_movie_by_title(search_term)
    nf = netflix.get_movie_by_title(search_term)
    it = itunes.get_movie_by_title(search_term)

    if yt:
        ytd = {'YouTube':{}}
        if yt.dvd:
            ytd['YouTube']['dvd'] = yt.price_dvd
        if yt.stream:
            ytd['YouTube']['stream'] = yt.price_stream

        ret[0]['availability'].append(ytd)

    if nf:
        nfd = {'Netflix':{}}
        if nf.dvd:
            nfd['Netflix']['dvd'] = nf.price_dvd
        if nf.stream:
            nfd['Netflix']['stream'] = nf.price_stream

        ret[0]['availability'].append(nfd)

    if it:
        itd = {'iTunes':{}}
        if it.dvd:
            itd['iTunes']['dvd'] = it.price_dvd
        if it.stream:
            itd['iTunes']['stream'] = it.price_stream

        ret[0]['availability'].append(itd)

    print ret
    return json.dumps(ret)




if __name__ == '__main__':
    app.run()
