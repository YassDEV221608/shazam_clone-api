import asyncio
from shazamio import Shazam, Serialize

import asyncio
from shazamio import Shazam, Serialize


async def getTopArtists(max):
    D = []
    #dict_keys(['layout', 'type', 'key', 'title', 'subtitle', 'share', 'images', 'hub', 'artists', 'url', 'highlightsurls', 'properties']) 
    shazam = Shazam()
    top_world_tracks = await shazam.top_world_tracks(limit=max)
    for track in top_world_tracks['tracks']:
        if 'avatar' in track['share'].keys():
            D.append({'key':track['artists'][0]['adamid'],'name':track['artists'][0]['alias'],'avatar':track['share']['avatar']})
        else:
            D.append({'key':track['artists'][0]['adamid'],'name':track['artists'][0]['alias'],'avatar':None})
    return {'artists':D}
        

async def getTopTracksByCountry(iso):
    D = []
    shazam = Shazam()
    top_world_tracks = await shazam.top_country_tracks(country_code=iso,limit=200)
    for track in top_world_tracks['tracks']:
        serialized = Serialize.track(track)    
        D.append({'key':serialized.key,'title':serialized.title,'subtitle':serialized.subtitle,'url':serialized.ringtone,'cover':serialized.photo_url})
    return {'tracks':D}