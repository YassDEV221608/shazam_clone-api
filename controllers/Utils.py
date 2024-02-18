from shazamio import Shazam

class Utils:
    async def getCities(self,code):
        try:
            shzam = Shazam()
            cities = await shzam.all_cities_from_country(code)
            D = []
            for city in cities:
                D.append(city)
            return {"cities":D}
        except Exception:
            return {}
        
