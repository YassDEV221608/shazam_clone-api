from shazamio import Shazam

class Artists:
    #max top artists is 200


    async def getTopArtists(self,max):
        D = []
        shazam = Shazam()
        try:
            top_world_tracks = await shazam.top_world_tracks(limit=max)
            for track in top_world_tracks['tracks']:
                if 'avatar' in track['share']:
                    if 'artists' in track : D.append({'key':track['artists'][0]['adamid'],'name':track['artists'][0]['alias'],'avatar':track['share']['avatar']})
                else:
                    if 'artists' in track : D.append({'key':track['artists'][0]['adamid'],'name':track['artists'][0]['alias'],'avatar':"https://i.ibb.co/26SJKDp/not-found.png"})
            return {'artists':D}
        except Exception:
            return {}
        
    #max search tracks is 200
    async def searchArtists(self,query):
        D = []
        shazam = Shazam()
        try:
            shazam = Shazam()
            artists = await shazam.search_artist(query=query, limit=10)
            for artist in artists['artists']['hits']:
                if 'avatar' in artist['artist']:
                    D.append({'key':artist['artist']['adamid'],'avatar':artist['artist']['avatar'],'name':artist['artist']['name'],'weburl':artist['artist']['weburl']})
                else:
                    D.append({'key':artist['artist']['adamid'],'name':artist['artist']['name'],'weburl':artist['artist']['weburl'],'webuel':"https://i.ibb.co/26SJKDp/not-found.png"})
            return {'artists':D}
        except Exception:
            return {}
        
    #about artist
    async def aboutArtist(self,id):
        D = []
        shazam = Shazam()
        try:
            shazam = Shazam()
            artist = await shazam.artist_about(artist_id=id,query="")
            D.append({"name":artist['data'][0]['attributes']['name'],"id":artist['data'][0]['id'],"bgColor":artist['data'][0]['attributes']['artwork']['bgColor'],"cover":artist['data'][0]['attributes']['artwork']['url'].format(w=800,h=800)})
            return {"artist":D}
        except Exception as e:
            print(e)
            return {}


    

    