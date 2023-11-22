_until_complete(Tracks().getTopTracksInWorldByGenre(genre))
    return jsonify(result)