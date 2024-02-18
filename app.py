import asyncio
from flask import Flask, jsonify,request
from flask_cors import CORS
from controllers.Tracks import Tracks
from controllers.Artists import Artists
from controllers.Search import Search
from controllers.Utils import Utils






app = Flask(__name__)
CORS(app)



@app.route('/get_top_artists/<path:max>',methods=['GET'])
def get_top_artists(max):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(Artists().getTopArtists(max))
    return jsonify(result)




@app.route('/top_world_tracks/<path:max>',methods=['GET'])
def get_top_world_tracks(max):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(Tracks().getTopTracks(max))
    return jsonify(result)



@app.route('/top_country_tracks/<path:iso>',methods=['GET'])
def get_top_country_tracks(iso):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(Tracks().getTopTracksByCountry(iso))
    return jsonify(result)

    
@app.route('/top_world_tracks_by_genre/<path:genre>',methods=['GET'])
def get_top_world_tracks_by_genre(genre):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(Tracks().getTopTracksInWorldByGenre(genre))
    return jsonify(result)

@app.route('/top_country_tracks_by_genre/<path:code>/<path:genre>',methods=['GET'])
def get_top_country_tracks_by_genre(code,genre):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(Tracks().getTopTracksInCountryByGenre(code,genre))
    return jsonify(result)

@app.route('/top_city_tracks/<path:code>/<path:city>')
def get_to_tracks_by_city(code,city):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(Tracks().getTopTracksByCity(code,city))
    return jsonify(result)


@app.route("/search_artists/<path:query>",methods=['GET'])
def search_artists(query):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(Search().searchArtists(query))
    return jsonify(result)


@app.route("/search_tracks/<path:query>",methods=['GET'])
def search_tracks(query):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(Search().searchTrack(query))
    return jsonify(result)

@app.route("/get_similar_tracks/<path:id>",methods=['GET'])
def get_similar_tracks(id):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(Tracks().getSimilarTracks(id))
    return jsonify(result)

@app.route("/about_track/<path:id>",methods=['GET'])
def about_track(id):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(Tracks().aboutTrack(id))
    return jsonify(result)

@app.route("/about_artist/<path:id>",methods=['GET'])
def about_artist(id):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(Artists().aboutArtist(id))
    return jsonify(result)

@app.route("/country_cities/<path:code>",methods=['GET'])
def country_cities(code):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(Utils().getCities(code))
    return jsonify(result)

@app.route("/recognize_track",methods=['POST'])
def recognize_track():
    data = request.get_json()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(Tracks().recognizeTrack(data))
    return jsonify(result)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)
