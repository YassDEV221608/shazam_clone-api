from shazamio import Shazam


class Search:
    #max search track is 10
    async def searchTrack(self,query):
        D = []
        shazam = Shazam()
        try:
            tracks = await shazam.search_track(query=query,limit=10)
            for track in tracks['tracks']['hits']:
                if 'avatar' in track['share'] and 'previewurl' in track['stores']['apple'] and 'avatar' in track['share']:
                    D.append({'key':track['key'],'title':track['heading']['title'],'artist':track['heading']['subtitle'],'url':track['stores']['apple']['previewurl'],'cover':track['share']['avatar'],'artistid':track['artists'][0]['adamid']})
            return {'tracks':D}
        except Exception:
            return {}
        
    #max search tracks is 10
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
                    D.append({'key':artist['artist']['adamid'],'name':artist['artist']['name'],'weburl':artist['artist']['weburl'],'avatar':"https://i.ibb.co/26SJKDp/not-found.png"})
            return {'artists':D}
        except Exception:
            return {}



