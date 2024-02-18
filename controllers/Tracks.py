from shazamio import Shazam, GenreMusic, Serialize
import base64
from io import BytesIO



"""
class GenreMusic(IntEnum):
    POP = 1
    HIP_HOP_RAP = 2
    DANCE = 3
    ELECTRONIC = 4
    RNB_SOUL = 5
    ALTERNATIVE = 6
    ROCK = 7
    LATIN = 8
    FILM_TV_STAGE = 9
    COUNTRY = 10
    AFRO_BEATS = 11
    WORLDWIDE = 12
    REGGAE_DANCE_HALL = 13
    HOUSE = 14
    K_POP = 15
    FRENCH_POP = 16
    SINGER_SONGWRITER = 17
    REGIONAL_MEXICANO = 18
"""

class Tracks:
    #max top tracks in the world is 200
    async def getTopTracks(self,max:int):
        D = []
        shazam = Shazam()
        try:
            top_world_tracks = await shazam.top_world_tracks(limit=max)
            for track in top_world_tracks['tracks']:
                serialized = Serialize.track(track)   
                cover = "https://i.ibb.co/26SJKDp/not-found.png"
                if "avatar" in track["share"]:
                    cover = track["share"]["avatar"]
                D.append({'key':str(serialized.key),'title':serialized.title,'artist':serialized.subtitle,'url':serialized.ringtone,'cover':cover})
            return {'tracks':D}
        except Exception:
            return {}
    
    #max top tracks by country is 200
    async def getTopTracksByCountry(self,iso):
        D = []
        shazam = Shazam()
        try:
            top_world_tracks = await shazam.top_country_tracks(country_code=iso,limit=200)
            for track in top_world_tracks['tracks']:
                serialized = Serialize.track(track)   
                cover = "https://i.ibb.co/26SJKDp/not-found.png"
                if "avatar" in track["share"]:
                    cover = track["share"]["avatar"]
                D.append({'key':str(serialized.key),'title':serialized.title,'artist':serialized.subtitle,'url':serialized.ringtone,'cover':cover})
            return {'tracks':D}
        except Exception:
            return {}

    #max top tracks by genre in world is 200
    async def getTopTracksInWorldByGenre(self,genre):
        D = []
        shazam = Shazam()
        try:
            top_tracks_in_the_world = await shazam.top_world_genre_tracks(genre=GenreMusic[genre], limit=200)
            for track in top_tracks_in_the_world['tracks']:
                serialized = Serialize.track(track)   
                cover = "https://i.ibb.co/26SJKDp/not-found.png"
                if "avatar" in track["share"]:
                    cover = track["share"]["avatar"]
                D.append({'key':str(serialized.key),'title':serialized.title,'artist':serialized.subtitle,'url':serialized.ringtone,'cover':cover})
            return {'tracks':D}
        except Exception:
            return {}
    
    #max top tracks by genre in country is 200
    async def getTopTracksInCountryByGenre(self,code,genre):
        D = []
        shazam = Shazam()
        try:
            top_tracks = await shazam.top_country_genre_tracks(
                country_code=code,
                genre=GenreMusic[genre],
                limit=200)
            for track in top_tracks['tracks']:
                serialized = Serialize.track(track)   
                cover = "https://i.ibb.co/26SJKDp/not-found.png"
                if "avatar" in track["share"]:
                    cover = track["share"]["avatar"]
                D.append({'key':str(serialized.key),'title':serialized.title,'artist':serialized.subtitle,'url':serialized.ringtone,'cover':cover})
            return {'tracks':D}
        except Exception:
            return {}
        
    #max tracks in city is 200
    async def getTopTracksByCity(self,code,city:str):
        D = []
        shazam = Shazam()
        try:
            top_tracks = await shazam.top_city_tracks(country_code=code, city_name=city, limit=200)
            for track in top_tracks['tracks']:
                serialized = Serialize.track(track)   
                cover = "https://i.ibb.co/26SJKDp/not-found.png"
                if "avatar" in track["share"]:
                    cover = track["share"]["avatar"]
                D.append({'key':str(serialized.key),'title':serialized.title,'artist':serialized.subtitle,'url':serialized.ringtone,'cover':cover})
            return {'tracks':D}
        except Exception:
            return {}
        
    
    #max similar tracks is 20
    async def getSimilarTracks(self,id):
        D = []
        shazam = Shazam()
        try:
            related = await shazam.related_tracks(track_id=id, limit=20, offset=0)
            for track in related['tracks']:
                serialized = Serialize.track(track)   
                cover = "https://i.ibb.co/26SJKDp/not-found.png"
                if "avatar" in track["share"]:
                    cover = track["share"]["avatar"]
                D.append({'key':str(serialized.key),'title':serialized.title,'artist':serialized.subtitle,'url':serialized.ringtone,'cover':cover})
            return {'tracks':D}
        except Exception as err:
            print(err)
            return {}
        
    #about track
    async def aboutTrack(self,id):
        shazam = Shazam()
        try:
            D = {}
            about_track = await shazam.track_about(id)
            serialized = Serialize.track(about_track)
            cover = "https://i.ibb.co/26SJKDp/not-found.png"
            if "avatar" in about_track["share"]:
                cover = about_track["share"]["avatar"]
            D["track"] = {'key':str(serialized.key),'title':serialized.title,'artist':serialized.subtitle,'url':serialized.ringtone,'cover':cover}
            return D
        except Exception as err:
            print(err)
            return {}
        
    async def recognizeTrack(self,audio):
        base64audio = base64.b64decode(audio)
        #file = BytesIO(base64audio)
        output_file_path = "sample.ogg"
        with open(output_file_path, 'wb') as file:
            file.write(base64audio)
        shazam = Shazam()
        out = await shazam.recognize_song("sample.ogg")
        tracks = []
        for track in out["matches"]:
            about_track = await self.aboutTrack(track["id"]);
            tracks.append(about_track["track"])
        return {"matches":tracks}


        
    
        

    